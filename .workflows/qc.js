export const meta = {
  name: 'setu-qc',
  description: 'Quality control of the rendered SETU Food master: segment reviewers, a first-time viewer, a compliance auditor; then per-scene fixes',
  phases: [
    { title: 'Review', detail: 'segment reviewers + holistic viewer + compliance auditor on the rendered MP4' },
    { title: 'Fix', detail: 'one fixer per scene with all its findings' },
  ],
}

const A = args // { hf, vp, video, framesDir, sheetsDir, qcDir, total, scenes:[{n,id,title,start,end,dur}], windows:[[a,b],...], round, fix }

const ISSUES = {
  type: 'object',
  properties: {
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          scene: { type: 'string', description: 'scene id that must change, e.g. s05-delivery-spot (or "film" for global)' },
          severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
          filmTime: { type: 'string' },
          category: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['scene', 'severity', 'filmTime', 'category', 'problem', 'evidence', 'fix'],
      },
    },
    scorecard: { type: 'string', description: 'short quality assessment of what you reviewed' },
  },
  required: ['issues', 'scorecard'],
}
const REPORT = {
  type: 'object',
  properties: { scene: { type: 'string' }, fixed: { type: 'array', items: { type: 'string' } }, disputed: { type: 'array', items: { type: 'string' } }, lintErrors: { type: 'integer' }, summary: { type: 'string' } },
  required: ['scene', 'fixed', 'disputed', 'lintErrors', 'summary'],
}

const FILM = `FILM UNDER REVIEW: ${A.video} — "SETU Food — customer walkthrough", rendered master (expected 1920x1080, 60 fps, H.264 yuv420p, ~${A.total} s, no audio by design; burned-in captions carry the narration). Built in HyperFrames from 12 scene compositions ${A.hf}/compositions/sNN-*.html with hard cuts; source of truth ${A.vp}/storyboard/scene-timing.json (per scene: narration, captions, on-screen text, animation spec, accuracy notes); build guide ${A.hf}/STYLE.md; product truth ${A.vp}/research/codebase-flow.md §2-3. Scenes: ${A.scenes.map((s) => `${s.id} ${s.start}-${s.end}`).join('; ')}.
Material: frames every 0.25 s at ${A.framesDir}/ (f_<seconds>.jpg, e.g. f_012.25.jpg); 10-second contact sheets at ${A.sheetsDir}/ (sheet_<start>.jpg, 8 columns x 5 rows, left-to-right, 0.25 s apart); technical QC (probe, black/freeze detection) in ${A.qcDir}/. Pull any exact frame yourself: ~/.local/bin/ffmpeg -v error -ss <t> -i ${A.video} -frames:v 1 <out.png> (and crop/zoom with python3 PIL). Never edit project files.`

const SEV = `SEVERITY: blocker = misleading/dishonest content, broken or missing picture, unreadable key text, technical spec failure; major = a visible flaw a normal viewer would notice (glitch, pop, jump cut, overlap, caption covering important UI, mistimed caption vs picture, clipped text, wrong copy, confusing step); minor = polish. Every issue needs film time, the scene id that must change, evidence (frame file + what is visible) and a concrete fix.`

const segPrompt = ([a, b]) => `You are a finishing editor doing frame-level QC on film time ${a}-${b} s of a rendered product film.
${FILM}
Go through every 0.25 s frame in your window (sheets for overview, single frames to inspect), and extract extra exact frames around every cut, swap, tap and camera move (e.g. 1/60 s apart) to catch one-frame glitches, pops, flicker, jumps, misaligned overlays, rings not matching the UI under them, half-faded elements at cuts, text clipping, labels overlapping the phone/each other/captions, captions covering the highlighted UI, and anything unpolished. Compare with the storyboard for these scenes: is every planned beat there and readable, in order, with the caption matching the picture? Also judge legibility at 1080p of every text you see (UI text under a highlight must be readable when the film wants it read).
${SEV}`

const viewerPrompt = `You are a first-time viewer and a creative director at once: an IIT Kharagpur student who has never used SETU Food, and a professor who will order dinner for the first time. Watch the whole film through the contact sheets (in order) and selected frames.
${FILM}
Answer as issues where something fails: Is it clear within 5 s what SETU Food is? Can you follow sign-in (existing customer) and the new-customer path? Do you understand how to choose a delivery spot and that it must be on campus? How to find food, add it, check the total, and that you pay the stall directly (cash, or the stall's own QR after it accepts) with no platform commission? How tracking and the handover code work? That SETU does not cook, deliver, collect payment or guarantee hygiene? Is the pacing comfortable (nothing rushed, nothing dead), the tone right for Gen Z without excluding faculty, the motion premium and consistent, the brand (SETU blue/indigo/orange, the logo tile) respected, the ending clear with a legible disclaimer? Report concrete problems with times and fixes; put your overall judgement in the scorecard.
${SEV}`

const auditPrompt = `You are the compliance and accuracy auditor for a product film.
${FILM}
1. Technical: read ${A.qcDir}/probe.json and the black/freeze reports; confirm 1920x1080, 60 fps, H.264, yuv420p, 16:9, duration within 105-120 s, no audio stream; investigate any black segment or long still (intended holds like the end card are fine).
2. Words: list every caption and every on-screen text in the film (frames + storyboard) and check each against product truth: SETU lists/approves stalls and does not cook, deliver, collect or process payments, or guarantee hygiene; no platform commission; delivery charge set by the stall and shown; pay the stall directly (cash at the door, or the stall's own UPI QR only after the stall accepts, then the stall confirms before cooking); order status separate from payment; no pickup choice, no rider/GPS/map tracking, no delivery-time promise, no "free"/"zero cost"/"minimal", no competitor names (real or disguised); exact app copy when quoted; the closing disclaimer verbatim ("SETU connects customers with approved campus food providers. Food preparation, delivery and payment are handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene.") and fully legible for >= 6 s.
3. Demo honesty: the one-time-code section carries a visible "Demo environment" badge the whole time and never implies a real inbox; sample stalls/data are labelled; the demo QR is labelled and nothing implies money moved; no private data (real emails, phone numbers, real codes outside the demo, tokens, real customers) is visible in any frame (check zoomed frames of every screen).
${SEV}`

const fixPrompt = (sc, issues) => `You are a senior motion designer fixing ONE scene after QC of the rendered master.
${FILM}
YOUR SCENE: ${sc.id} (film ${sc.start}-${sc.end} s = local 0-${sc.dur} s). The ONLY file you may edit is ${A.hf}/compositions/${sc.id}.html.
FINDINGS (film times; local = film - ${sc.start}):
${JSON.stringify(issues, null, 1)}
Reproduce each finding in your scene preview (cd ${A.hf}; node tools/preview-scene.mjs ${sc.n}; tools/hf-lock.sh hyperframes snapshot .preview/${sc.id} --at <local times> --no-end -o .preview/${sc.id}/qc-r${A.round}), fix it without regressions, keep frame 0 == handoffIn and the last frame == handoffOut from the packet ${A.hf}/.packets/${sc.id}.json, re-run lint (tools/hf-lock.sh hyperframes lint .preview/${sc.id}: 0 errors, 0 warnings) and re-snapshot the affected beats and both boundaries. Explain any finding you dispute (with evidence).`

phase('Review')
const reviews = await parallel([
  ...A.windows.map((w) => () => agent(segPrompt(w), { label: `seg:${w[0]}-${w[1]}`, phase: 'Review', schema: ISSUES })),
  () => agent(viewerPrompt, { label: 'first-time-viewer', phase: 'Review', schema: ISSUES }),
  () => agent(auditPrompt, { label: 'compliance-audit', phase: 'Review', schema: ISSUES }),
])
const all = reviews.filter(Boolean).flatMap((r) => r.issues)
const byScene = new Map(); const unassigned = []
for (const i of all) {
  const sc = A.scenes.find((s) => i.scene && (i.scene === s.id || i.scene.startsWith(`${s.n}-`) || i.scene === s.n))
  if (!sc) { unassigned.push(i); continue }
  if (!byScene.has(sc.id)) byScene.set(sc.id, [])
  byScene.get(sc.id).push(i)
}
log(`${all.length} findings (${all.filter((i) => i.severity !== 'minor').length} blocker/major) across ${byScene.size} scenes; ${unassigned.length} film-level`)

let fixes = []
if (A.fix !== false) {
  phase('Fix')
  fixes = await parallel([...byScene.entries()].map(([id, issues]) => () => {
    const sc = A.scenes.find((s) => s.id === id)
    return agent(fixPrompt(sc, issues), { label: `fix:${sc.n}`, phase: 'Fix', schema: REPORT })
  }))
}
return { scorecards: reviews.filter(Boolean).map((r) => r.scorecard), findings: all, unassigned, byScene: Object.fromEntries(byScene), fixes: fixes.filter(Boolean) }
