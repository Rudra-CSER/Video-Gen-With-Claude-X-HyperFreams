export const meta = {
  name: 'setu-build-scenes',
  description: 'Build every SETU Food scene in parallel; each is reviewed by an independent critic and fixed until clean',
  phases: [
    { title: 'Build', detail: 'one motion designer per scene writes compositions/<sceneId>.html' },
    { title: 'Review', detail: 'independent critic snapshots the scene densely and checks it against the packet' },
    { title: 'Fix', detail: 'a fresh designer applies the verified review issues' },
  ],
}

const A = args
const MAX_FIX_ROUNDS = A.maxFixRounds ?? 3

const REPORT = {
  type: 'object',
  properties: {
    sceneId: { type: 'string' },
    file: { type: 'string' },
    lintErrors: { type: 'integer' },
    lintWarnings: { type: 'integer' },
    framesInspected: { type: 'integer' },
    handoffInMatches: { type: 'boolean' },
    handoffOutMatches: { type: 'boolean' },
    deviations: { type: 'array', items: { type: 'string' } },
    fixed: { type: 'array', items: { type: 'string' } },
    disputed: { type: 'array', items: { type: 'string' } },
    kitRequests: { type: 'array', items: { type: 'string' } },
    openIssues: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['sceneId', 'file', 'lintErrors', 'lintWarnings', 'framesInspected', 'handoffInMatches', 'handoffOutMatches', 'deviations', 'openIssues', 'summary'],
}

const REVIEW = {
  type: 'object',
  properties: {
    sceneId: { type: 'string' },
    verdict: { type: 'string', enum: ['pass', 'needs-fixes'] },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
          time: { type: 'string', description: 'scene-local seconds or range, e.g. "3.40" or "3.4-4.1"' },
          category: { type: 'string', description: 'timing | layout | legibility | continuity | honesty | copy | motion | structure | spec' },
          problem: { type: 'string' },
          evidence: { type: 'string', description: 'snapshot file + what is visible, or file:line' },
          fix: { type: 'string' },
        },
        required: ['severity', 'time', 'category', 'problem', 'evidence', 'fix'],
      },
    },
    strengths: { type: 'string' },
    summary: { type: 'string' },
  },
  required: ['sceneId', 'verdict', 'issues', 'summary'],
}

const FILM = `FILM: "SETU Food — customer walkthrough": a ${A.total} s, 1920x1080, 60 fps product film for IIT Kharagpur campus customers (students, faculty, staff) — modern and confident for Gen Z without being childish, clear for professors. It teaches the real customer journey (sign in, onboarding, delivery location, finding food, cart, paying the stall directly, tracking, handover code, review) through ONE story: Aarav (Nehru Hall of Residence, Room B-212) orders dinner. Silent master (the owner adds sound later); burned-in captions carry the narration and are drawn by a shared caption track, never by a scene. It is built with HyperFrames 0.8.143: HTML + GSAP, seeked frame by frame in headless Chrome, so every frame must be a pure function of time. Only real captures of the app appear as app screens; overlays may point, highlight and zoom, never change what the app says. Quality bar: polished after-effects-style motion graphics (camera push-ins, layered UI, typographic reveals, tap cues), not a slideshow.`

const where = (sc) => `YOUR SCENE: ${sc.id} — "${sc.title}". Local time 0 -> ${sc.dur} s (film ${sc.start} -> ${sc.end} s). Previous scene: ${sc.prev || 'none (film start)'}. Next scene: ${sc.next || 'none (film end)'}.${sc.note ? `\nDIRECTOR NOTE: ${sc.note}` : ''}
PATHS (run every command from the project root ${A.hf}):
- Your spec packet: ${A.hf}/.packets/${sc.id}.json  (animationLocal = the time-coded build spec in scene-local seconds; captionsLocal = when the shared captions occupy the caption zone; onScreenText; shots with exact asset srcs, marks and clip lengths; handoffIn/handoffOut; demoBadgeLocal; accuracyNotes; globalSystem).
- Neighbour packets (read-only, to understand the cuts): ${sc.prev ? `${A.hf}/.packets/${sc.prev}.json` : '-'} and ${sc.next ? `${A.hf}/.packets/${sc.next}.json` : '-'}.
- Build guide (binding): ${A.hf}/STYLE.md. Motion kit API: ${A.hf}/assets/js/kit.js (window.SetuKit). Styles/classes: ${A.hf}/assets/css/kit.css.
- Lint-clean starter: ${A.hf}/tests/scene-template.html. Prototype idioms and quality bar: ${A.hf}/tests/golden.html, ${A.hf}/tests/opener.html (root-level prototypes; yours is a sub-composition).
- Real captures: ${A.hf}/assets/ui/<group>/<shot>.png (1170x2532 = 390x844 CSS px at 3x; desktop ones 1440x900 CSS at 2x). Element boxes: ${A.hf}/assets/data/marks.json. Open every PNG you use (Read tool); measure anything not in marks.json with python3/PIL crops.
- Product truth for anything you write on screen: ${A.vp}/research/codebase-flow.md (sections 2 and 3).
- The ONLY project file you may create or edit: ${A.hf}/compositions/${sc.id}.html. Scratch: ${A.hf}/.preview/${sc.id}/ (snapshots, notes as .md/.txt, never extra .html there). Never edit kit.js, kit.css, STYLE.md, tools/, index.html, captions, packets, the storyboard or another scene: report needed shared changes as kitRequests.`

const CHECKS = `ACCEPTANCE CHECKS (verify each against real snapshots, not by reading code):
1. Structure: everything inside <template>; <div id="root" data-composition-id="${'${sceneId}'}" data-width="1920" data-height="1080">; kit.css linked inside the template; exactly one paused GSAP timeline registered last as window.__timelines['<sceneId>']; script wrapped in an IIFE; every id prefixed with the scene number (e.g. s05-); every custom CSS rule scoped to your prefixed ids/classes; no Date.now/Math.random/network/getBoundingClientRect at tween time; no repeat:-1; fromTo for entrances; nothing tweens visibility/display on a .clip; no CSS transform plus GSAP transform on the same element; videos sit directly inside a non-timed .layer, carry data-start (local) + data-duration (= the asset's real seconds) + data-hf-media-start-basis="local" + muted playsinline + class="clip", are never animated themselves (animate their layer), and have the matching still underneath so the last frame holds. Lint: 0 errors, 0 warnings.
2. Timing: every beat lands within ±0.1 s of animationLocal; a tap (K.tap) starts 0.25-0.45 s BEFORE the screen change it causes; results get a readable beat (>= 0.6 s) and text-heavy screens hold >= 1.2 s; camera moves 0.8-1.2 s; exits 0.3-0.5 s and complete before the scene end.
3. Boundaries: the frame at t=0 equals handoffIn exactly (phone spec, visible capture, rig transform, left column, overlays) and the frame at t=duration-1/60 equals handoffOut exactly — the neighbouring builder matches the same contract, so the hard cut must be invisible. Nothing "enters" at t=0 that the contract says is already there; nothing still animating at the last frame unless the contract says so.
4. Layout: text column x140-820; callouts in the lane x840-1130 or the right margin x1620-1880; max 4 floating labels; nothing overlaps the phone (including the phone enlarged by a camera push-in), the text column, other labels or the caption zone while a caption is on screen (left captions: x120-1140, y880-1050; centred: y900-1050 full width); everything fully on canvas (right edge <= 1880).
5. Legibility & polish: no clipped or overflowing words; headlines max two lines; the rupee sign renders in Plus Jakarta Sans or Space Mono, never a fallback box; entrances fully hidden before they start (no peeking); easing per STYLE.md (expo.out entrances, expo.inOut camera/navigation, back.out only on small pops); no jitter, no constant drift, no particles/glitch/spin; composition feels balanced and premium.
6. Honesty & copy: app screens are untouched captures; every quoted UI string, dish, price, code and order number matches the capture exactly; the DEMO badge ("Demo environment") is fully visible exactly during demoBadgeLocal; never "SETU delivers", pickup, rider/GPS/map tracking, delivery-time promises, "free"/"zero cost", competitor names; the end-card disclaimer (if yours) is verbatim and legible for >= 6 s.`

const VERIFY_LOOP = (sc) => `VERIFY LOOP (repeat until every acceptance check passes):
  cd ${A.hf}
  node tools/preview-scene.mjs ${sc.n}                       # writes .preview/${sc.id}/ (your scene at t=0 + the film background + your captions)
  tools/hf-lock.sh hyperframes lint .preview/${sc.id}
  tools/hf-lock.sh hyperframes snapshot .preview/${sc.id} --at <times> --no-end -o .preview/${sc.id}/snaps-<name>
- Snapshot t=0, t=${sc.dur}-0.017, and the frames just before and just after every tap, swap, camera move, callout and caption change, plus a sweep every ~0.5 s; use --zoom x,y,w,h for small text. Look at the PNGs yourself (Read). Each snapshot run takes ~5-20 s; the lock wrapper may queue you behind other builders (this is a shared machine with little free memory — never start Chrome outside tools/hf-lock.sh).
- Optionally run once near the end: tools/hf-lock.sh hyperframes check .preview/${sc.id} --at-transitions (ignore contrast findings that are inside the captured app screenshots).`

const buildPrompt = (sc) => `You are a senior motion designer building ONE scene of a product film. Other designers build the other scenes in parallel; the director assembles them by hard cuts.
${FILM}
${where(sc)}${FLUX}
TASK
1. Read the packet completely, STYLE.md, kit.js, kit.css and the starter. Open every capture you use. Plan every beat on a local timeline from animationLocal (write the plan to .preview/${sc.id}/plan.md).
2. Write ${A.hf}/compositions/${sc.id}.html (start from tests/scene-template.html). Use kit helpers where they fit; write small local helpers inside your IIFE for anything else (number rolls, wipes, masks, slips). Prefer exact numbers from the packet (marks, framings, positions) over eyeballing.
3. Run the verify loop until every acceptance check passes.
${VERIFY_LOOP(sc)}
${CHECKS.replace('${sceneId}', sc.id)}
If the spec is physically impossible or contradicts the captures or STYLE.md, build the closest faithful version, keep the boundary contracts and the caption-zone rule intact, and list it under deviations with the reason. Return the report.`

const reviewPrompt = (sc, round, prior) => `You are an independent motion-design critic and QA engineer. Review ONE scene of a product film with fresh eyes and real snapshots. You must NOT edit any project file (scratch only under ${A.hf}/.preview/${sc.id}/review-r${round}/).
${FILM}
${where(sc)}
${round > 1 ? `This is review round ${round}. The designer reports: ${JSON.stringify(prior || {}).slice(0, 4000)}\nCheck that every previously reported issue is really fixed, then scan the whole scene again for regressions and anything missed.` : 'This is the first review.'}
METHOD
- Build the preview yourself (node tools/preview-scene.mjs ${sc.n}) and take your OWN snapshots: a dense sweep (every 0.25 s; use the generated contact-sheet.jpg for the overview), full frames at every beat named in animationLocal (before/after each tap, swap, camera move, callout, caption change), t=0 and t=${sc.dur}-0.017, and --zoom crops for any small text. Run lint. Use tools/hf-lock.sh for every Chrome command.
- Compare against the packet's animationLocal, onScreenText, handoffIn/handoffOut, captionsLocal and demoBadgeLocal, STYLE.md and the acceptance checks below. Also judge it as a viewer: is each step understandable without sound, is anything rushed or static for no reason, does it look premium?
${CHECKS.replace('${sceneId}', sc.id)}
SEVERITY: blocker = broken, lint error, misleading/dishonest, unreadable, or a handoff mismatch; major = a visible flaw a viewer would notice (overlap, collision with captions, wrong/missing beat, mistimed tap, clipped text, wrong copy, popping element); minor = polish. Every issue needs evidence (the snapshot path and what is visible) and a concrete fix. Verdict "pass" only if there is no blocker or major issue.`

const fixPrompt = (sc, review, round) => `You are a senior motion designer fixing ONE scene of a product film after an independent review (fix round ${round}). The scene file already exists; read it fully before changing it.
${FILM}
${where(sc)}${FLUX}
REVIEW FINDINGS (JSON):
${JSON.stringify(review, null, 1)}
TASK
1. Reproduce each finding with your own snapshot first. Fix every blocker and major finding; fix minor ones when safe. If a finding is wrong, leave the code as is and explain why under disputed (with snapshot evidence).
2. Re-run the verify loop for the affected beats AND the boundaries (t=0 and t=${sc.dur}-0.017), and re-run lint. Make sure nothing regressed.
${VERIFY_LOOP(sc)}
${CHECKS.replace('${sceneId}', sc.id)}
Return the report (list what you fixed under fixed and what you disputed under disputed).`

const FLUX = A.specInFlux ? `\nNOTE: the storyboard is still under a final editorial review running in parallel, so your packet may be regenerated while you work (usually small timing or wording changes). The packet file is the source of truth: re-read ${A.hf}/.packets/<your sceneId>.json right before your final verification pass and adapt to any change (re-run node tools/preview-scene.mjs too, since captions come from the storyboard).` : ''

const serious = (rv) => rv && rv.issues.some((i) => i.severity !== 'minor')
const anyIssues = (rv) => rv && rv.issues.length > 0

async function sceneJob(sc) {
  const build = await agent(buildPrompt(sc), { label: `build:${sc.n}`, phase: 'Build', schema: REPORT })
  let last = build
  let rv = await agent(reviewPrompt(sc, 1, null), { label: `review:${sc.n}:r1`, phase: 'Review', schema: REVIEW })
  const rounds = [{ round: 1, verdict: rv?.verdict, issues: rv?.issues?.length ?? null }]
  for (let r = 1; r <= MAX_FIX_ROUNDS; r++) {
    if (!rv) break
    // Fix when anything serious remains; in the first round also polish minor-only findings.
    if (!(serious(rv) || (r === 1 && anyIssues(rv)))) break
    last = await agent(fixPrompt(sc, rv, r), { label: `fix:${sc.n}:r${r}`, phase: 'Fix', schema: REPORT })
    rv = await agent(reviewPrompt(sc, r + 1, last), { label: `review:${sc.n}:r${r + 1}`, phase: 'Review', schema: REVIEW })
    rounds.push({ round: r + 1, verdict: rv?.verdict, issues: rv?.issues?.length ?? null })
  }
  const open = rv ? rv.issues : [{ severity: 'major', problem: 'final review missing' }]
  log(`${sc.n}: ${rv?.verdict ?? 'no review'} after ${rounds.length} review round(s); open: ${open.filter((i) => i.severity !== 'minor').length} serious, ${open.filter((i) => i.severity === 'minor').length} minor`)
  return { scene: sc.id, verdict: rv?.verdict ?? 'unknown', rounds, openIssues: open, lastReport: last, firstBuild: { deviations: build?.deviations, kitRequests: build?.kitRequests } }
}

phase('Build')
const results = await parallel(A.scenes.map((sc) => () => sceneJob(sc)))
return results
