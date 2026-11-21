export const meta = {
  name: 'setu-assemble',
  description: 'Film-level checks on the assembled SETU Food film (cuts, cross-scene consistency, captions vs picture), then per-scene fixes',
  phases: [
    { title: 'Inspect', detail: 'cut reviewers, consistency lead, caption/picture reviewer' },
    { title: 'Fix', detail: 'one fixer per scene with all of its findings' },
    { title: 'Recheck', detail: 'confirm the fixes on the assembled film' },
  ],
}

const A = args // { hf, vp, total, scenes: [{n,id,title,start,end,dur,prev,next}], cutGroups: [[cutIndex...]...], boundariesDir, montageDir, round }

const ISSUES = {
  type: 'object',
  properties: {
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          scene: { type: 'string', description: 'the scene id that must change, e.g. s05-delivery-spot' },
          severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
          filmTime: { type: 'string', description: 'film seconds or range' },
          category: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['scene', 'severity', 'filmTime', 'category', 'problem', 'evidence', 'fix'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['issues', 'summary'],
}
const REPORT = {
  type: 'object',
  properties: {
    scene: { type: 'string' },
    fixed: { type: 'array', items: { type: 'string' } },
    disputed: { type: 'array', items: { type: 'string' } },
    lintErrors: { type: 'integer' },
    summary: { type: 'string' },
  },
  required: ['scene', 'fixed', 'disputed', 'lintErrors', 'summary'],
}

const FILM = `FILM: "SETU Food — customer walkthrough" (${A.total} s, 1920x1080, 60 fps, silent master with burned-in captions), built in HyperFrames 0.8.143 as 12 scene sub-compositions (hard cuts between them) plus a shared caption track, assembled by ${A.hf}/index.html. Storyboard (source of truth): ${A.vp}/storyboard/scene-timing.json; per-scene packets: ${A.hf}/.packets/<sceneId>.json; build guide: ${A.hf}/STYLE.md; motion kit: ${A.hf}/assets/js/kit.js + assets/css/kit.css. Scenes: ${A.scenes.map((s) => `${s.id} ${s.start}-${s.end}`).join('; ')}.
Tools (run from ${A.hf}; every Chrome command goes through tools/hf-lock.sh — shared machine, little free memory):
- Full-film frames at any film time: tools/hf-lock.sh hyperframes snapshot . --at <t1,t2,...> --no-end -o <dir>   (add --zoom x,y,w,h for crops)
- One scene alone: node tools/preview-scene.mjs <sNN>, then snapshot .preview/<sceneId> (scene-local times)
- Cut pairs already rendered: ${A.boundariesDir}/cut-NN-<from>-to-<to>.png (left = last frame of the scene before, right = first frame after)
- Representative frames of every scene: ${A.montageDir}/`

const cutPrompt = (cuts) => `You are the continuity editor checking the hard cuts between scenes of a product film.
${FILM}
YOUR CUTS: ${cuts.map((c) => `#${c.k} ${c.from} -> ${c.to} at film ${c.t} s`).join('; ')}.
For each cut: open the cut pair image; read both scenes' handoffOut / handoffIn in their packets; take extra full-film snapshots at t-0.25, t-0.1, t-1/60, t, t+0.1, t+0.25 (and zoom crops where needed) to judge motion continuity across the cut (an element still moving at the end of one scene and frozen at the start of the next reads as a jump; a phone at a slightly different position/scale reads as a jolt; text or a badge popping on/off at the cut reads as a glitch). An invisible cut, or a clearly designed transition the storyboard asks for, is a pass. For every problem name the scene that must change (prefer the scene whose frame deviates from the shared handoff contract) and the exact fix. Do not edit files.`

const consistencyPrompt = `You are the art director doing a cross-scene consistency pass on a product film assembled from 12 scenes built by different designers.
${FILM}
Look at every frame in ${A.montageDir}/ (and take any extra full-film snapshots you need). Compare scenes against each other and against STYLE.md: kicker position, size and format ("NN · Name"); headline/subline sizes, weights, colours and positions; callout/label/chip styles; ring colours and meaning (orange = look here, blue = next tap, green = confirmations only); tap cue look; DEMO / tag-row badge style and position (140,112); phone position at rest (default spec) and push-in feel; margins and the caption zone kept clear; overall rhythm and polish. Flag only real inconsistencies a viewer would notice or that break the guide, naming the scene that should change (match the majority / the guide). Do not edit files.`

const captionsPrompt = `You are the story editor checking captions against picture across the whole film.
${FILM}
For every caption in the storyboard (global times), take full-film snapshots at caption start + 0.3 s and at its middle (batch many --at times in one snapshot run). Check: the caption plate never covers anything important (phone UI being highlighted, labels, the DEMO badge), the picture shows what the caption says at that moment (e.g. "Tap ADD" while ADD is being tapped), no caption collides with on-screen headlines or labels, nothing important happens in the caption zone, captions read naturally in sequence for a silent viewer, and nothing on screen is misleading (SETU never delivers/collects payments; demo data is labelled; the QR side branch is the stall's own QR after acceptance; no pickup, rider map, time promise or "free"). Name the scene that must change for each problem. Do not edit files.`

const fixPrompt = (sc, issues) => `You are a senior motion designer fixing ONE scene after film-level review of the assembled film.
${FILM}
YOUR SCENE: ${sc.id} (film ${sc.start}-${sc.end} s, local 0-${sc.dur} s). The ONLY file you may edit is ${A.hf}/compositions/${sc.id}.html.
FINDINGS FOR YOUR SCENE (film times; local = film - ${sc.start}):
${JSON.stringify(issues, null, 1)}
Reproduce each finding (preview your scene and/or snapshot the full film), fix it without regressions, keep frame 0 == handoffIn and the last frame == handoffOut (unless a finding says the contract itself must be realigned with the neighbour — then match the neighbour's actual frame and say so), re-run lint on .preview/${sc.id} (0 errors, 0 warnings) and re-snapshot the affected beats and both boundaries. If a finding is wrong, explain under disputed with evidence.`

const cuts = A.scenes.slice(0, -1).map((s, i) => ({ k: i + 1, from: s.id, to: A.scenes[i + 1].id, t: s.end }))
const groups = (A.cutGroups || [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]).map((g) => g.map((k) => cuts[k - 1]).filter(Boolean))

phase('Inspect')
const inspections = await parallel([
  ...groups.map((g, i) => () => agent(cutPrompt(g), { label: `cuts:${g.map((c) => c.k).join(',')}`, phase: 'Inspect', schema: ISSUES })),
  () => agent(consistencyPrompt, { label: 'consistency', phase: 'Inspect', schema: ISSUES }),
  () => agent(captionsPrompt, { label: 'captions-vs-picture', phase: 'Inspect', schema: ISSUES }),
])
const all = inspections.filter(Boolean).flatMap((r) => r.issues)
const byScene = new Map()
for (const i of all) {
  const sc = A.scenes.find((s) => i.scene && (i.scene === s.id || i.scene.startsWith(`${s.n}-`) || i.scene === s.n))
  if (!sc) { log(`unassigned finding: ${i.problem.slice(0, 80)}`); continue }
  if (!byScene.has(sc.id)) byScene.set(sc.id, [])
  byScene.get(sc.id).push(i)
}
log(`${all.length} findings across ${byScene.size} scenes (${all.filter((i) => i.severity !== 'minor').length} blocker/major)`)

phase('Fix')
const fixes = await parallel([...byScene.entries()].map(([id, issues]) => () => {
  const sc = A.scenes.find((s) => s.id === id)
  return agent(fixPrompt(sc, issues), { label: `fix:${sc.n}`, phase: 'Fix', schema: REPORT })
}))

return { findings: all, byScene: Object.fromEntries(byScene), fixes: fixes.filter(Boolean), summaries: inspections.filter(Boolean).map((r) => r.summary) }
