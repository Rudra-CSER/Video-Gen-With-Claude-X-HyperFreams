export const meta = {
  name: 'setu-storyboard-final',
  description: 'Synthesize the final SETU Food storyboard from the winning draft + judge fixes, adversarially verify it on three lenses, and revise',
  phases: [
    { title: 'Synthesize', detail: 'one director agent writes storyboard/scene-timing.json' },
    { title: 'Verify', detail: 'truth, mechanics and craft lenses check it independently' },
    { title: 'Revise', detail: 'apply verified fixes, re-check' },
  ],
}

const A = args
const ISSUES = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['pass', 'needs-fixes'] },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          sceneId: { type: 'string' },
          severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
          field: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['sceneId', 'severity', 'field', 'problem', 'evidence', 'fix'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['verdict', 'issues', 'summary'],
}

const CONTEXT = `
PROJECT
- Repo: ${A.repo} (React/Vite PWA "SETU Services"; food is its live service). NEVER modify anything outside ${A.vp}. Do not commit.
- Video project: ${A.vp}. HyperFrames project: ${A.hf}. Brief (long; the binding spec is its final "MASTER PROMPT" section near the end, lines ~1273-1612): ${A.brief}.
- Build guide every scene builder follows: ${A.hf}/STYLE.md (canvas grid, type, colours, phone, motion vocabulary, HyperFrames rules, honesty rules). Motion helpers: ${A.hf}/assets/js/kit.js. Styles: ${A.hf}/assets/css/kit.css.
- Verified product facts and the MAY / MUST-NOT-SAY lists: ${A.vp}/research/codebase-flow.md (section 3 is binding; sections 2.x hold exact UI copy).
- Real captures (the only app screens allowed): ${A.hf}/assets/ui/<group>/<shot>.png (1170x2532 = 390x844 CSS px at 3x). Element boxes (CSS px of the 390x844 screen) per shot: ${A.hf}/assets/data/marks.json (keys "<group>/<shot>"; clip lengths under "clip:<group>/<seq>"). Source frame sequences for typing/scroll clips: ${A.vp}/assets/screens/<group>/<seq>/*.png, encoded at ${A.hf}/assets/clips/<group>-<seq>.mp4. Inventory: ${A.vp}/research/shot-inventory.md (also location/30-home-unset, 31-picker-saved, 32-confirm-saved, 33-home-set exist with marks). Desktop captures are 1440x900 CSS at 2x. Brand: ${A.hf}/assets/brand/setu-logo.png (always on a white rounded tile), setu-mark.svg. Campus boundary polygon: ${A.hf}/assets/data/campus-boundary.json. Demo QR: ${A.vp}/assets/demo/demo-payment-qr.png (also visible inside the order-qr captures).
- Data in the captures is an isolated DEMO stack: 13 fictional seeded stalls, demo persona "Aarav Mehta" (Nehru Hall of Residence, Room B-212), clock shifted to ~7 pm campus time, a labelled demo payment QR, codes caught by a local test inbox. The cash order ran with realistic gaps (placed 7:02 pm ... delivered 7:25 pm).

PREVIOUS STORYBOARD ROUND (already done; do not redo it)
- Three full drafts were written and judged by three independent judges. All three judges chose B-story.
  - Winner: ${A.draftB}
  - Runners-up to graft from: ${A.draftA} (A-tutorial), ${A.draftC} (C-value)
  - Judge verdicts with concrete fix lists: ${A.judges.join(', ')}
  - A first synthesis attempt was cut off just before writing its result; its caption timeline (12 scenes, 112 s, fixes applied) is in ${A.capcheck}. Treat it as a strong reference, not a requirement.

OUTPUT CONTRACT (the build tools read this file; keep every field)
File: ${A.vp}/storyboard/scene-timing.json  (UTF-8, ensure_ascii false, pretty-printed). Root object:
{
  "title": str, "angle": str (the film's one-paragraph idea + the GLOBAL SYSTEM notes builders must share),
  "totalSeconds": number, "wordCount": int (narration words),
  "phoneSpec": { "left": 1150, "top": 70, "k": 1.08 },
  "scenes": [ {
    "id": "s01".."s12" (zero-padded, contiguous),
    "compositionName": short kebab slug (<= 24 chars; composition id becomes "<id>-<compositionName>"),
    "title": str, "chapter": str|null (the kicker label for the scene, e.g. "Step 2 · Location"),
    "start": num, "end": num   (GLOBAL seconds; scenes tile 0..totalSeconds with no gaps/overlaps),
    "narration": str (the spoken-style script for this scene; captions carry it, there is no voice-over),
    "captions": [ { "start": num, "end": num, "text": str } ]   (GLOBAL seconds; "\\n" = the intended line break, honoured by the caption renderer),
    "onScreenText": [ { "text": str, "start": num, "end": num, "role": str } ]   (GLOBAL seconds; every visible word that is not a caption),
    "shots": [ { "file": str, "start": num, "end": num, "treatment": str, "clipSeconds"?: num } ]   (GLOBAL seconds).
        file forms: "<group>/<shot>.png" (real capture), "<group>/<seq>/" (typing/scroll clip; "clipSeconds" optional = the playback length you want, allowed 0.75x..2.5x of the base length in marks.json "clip:<group>/<seq>".seconds; a speed variant will be pre-rendered), "desktop/<shot>.png" (laptop frame), or "graphic:<short description>" for motion graphics (brand tile, campus outline, end-card type, demo QR art is NOT allowed outside the captures).
    "uiState": str,
    "animation": str — the precise build spec, in SCENE-LOCAL seconds (t=0 at scene start; say "Local times." first). Time-code every entrance, tap (tap BEFORE the screen change it causes), ring, swap, camera move, callout and exit. Name marks by key (e.g. cart/01-cart.payable) and give any box not in marks.json as explicit CSS-px {x,y,w,h} measured on the PNG. Give camera moves as kit focus() arguments: scale s, screen point P (CSS px), target canvas point T.
    "transitionIn": str, "transitionOut": str,
    "handoffIn": HANDOFF, "handoffOut": HANDOFF,
    "demoBadge": [ { "start": num, "end": num } ]  (GLOBAL seconds; when the "Demo environment" badge must be visible; [] if none),
    "soundCues": [ { "at": num, "cue": str } ]   (GLOBAL seconds; placeholders for the owner's soundtrack),
    "accuracyNotes": str
  } ]
}
HANDOFF = { "phone": "default" | "none" | "custom", "phoneSpec"?: {left,top,k} (only if custom), "screen": "<group>/<shot>.png" | null (the capture fully visible in the phone at the boundary frame), "rig": "identity" | { "s": num, "P": [screenX, screenY], "T": [canvasX, canvasY] }, "leftColumn": "empty" | exact text that is fully visible at the boundary, "overlays": "none" | exact description (badges, chips, laptop, brand tile...), "notes": str }.
Rule: scene N handoffOut must equal scene N+1 handoffIn field-for-field, because the two halves are built by different people and the cut must be invisible (or deliberately designed). Prefer simple boundaries: rig identity, left column empty, no overlays; use a non-identity rig or carried text only where the drafted continuous move is worth it, and specify it numerically.
Also write ${A.vp}/storyboard/layout.json: { "captionCenter": [scene ids whose captions are centred because the scene is full-screen], "notes": str }.
`

const RULES = `
DIRECTOR'S DECISIONS (binding)
1. Base the film on B-story ("Dinner at B-212"): 12 scenes, story of Aarav (Nehru Hall of Residence, Room B-212) ordering 1 x Masala Dosa + 2 x Filter Coffee from Southside Tiffins; items Rs140 + the stall's own delivery charge Rs10 = Rs150 payable to the seller; cash at the door; six-digit handover code completes it; 5-star review; report path mentioned. Total 110-114 s (acceptable 105-120). Keep B's story beats and best motion ideas unless a fix below changes them.
2. Apply every judge fix, specifically: never set the rupee sign in Sora (use Plus Jakarta Sans or Space Mono for any text containing it); stagger chip flights (never fly several objects into the phone at once) and remove the left-column stepper vs parked-chip clash; taps always land 0.25-0.45 s BEFORE the screen change they cause (C's tap order: return to location/13-confirm-search and tap Home before cutting on; coffee ADD, then +, then the 2 appears); a TIME-LAPSE tag over the order status run; end card starts ~1.5 s earlier than B so the disclaimer is fully legible for >= 6 s; frame every location-picker/map shot so the app's subtitle "SETU delivers inside the IIT Kharagpur campus boundary" is never magnified or lingered on (A's framing: map push-in s 1.8 focused near screen y 575; keep that subtitle off-frame or tiny); DEMO badge across the whole OTP portion (from the moment the code is requested until the app reaches Home); numbered chapter kickers (A) and the exact button name in key captions where it helps a first-timer; short caps labels instead of long quote callouts (C); the simpler hook naming SETU Food; "Have an account? / New here?" phrasing.
3. Canonical layout is STYLE.md's: phone default spec {left:1150, top:70, k:1.08}; text column x140-820 (kicker, headline, subline); callout lane x840-1130; right margin x1620-1880 for secondary labels only; caption zone reserved (left captions x120-1140, y880-1050; centred captions y900-1050 on full-screen scenes). Drafts used other phone positions: convert every canvas coordinate. Max 4 floating labels at once, none overlapping the phone, each other, the text column or the caption zone, all fully on canvas (right edge <= 1880; a 28 px chip ~ 17 px per character + 70 px).
4. Captions: <= 42 characters per line, <= 2 lines, each >= 1.3 s, <= 2.6 words/s, no overlaps, inside their scene, readable by a silent viewer. Narration total about 200-240 words (B has 223). Plain, warm, confident; Gen Z-friendly without being childish; professors must feel welcome too. "For IIT Kharagpur campus accounts: students, faculty, staff." is approved wording.
5. Honesty (non-negotiable, see codebase-flow.md section 3.2 and STYLE.md): only real captures for app screens; overlays may point, highlight, zoom, never alter app text; the OTP portion carries the DEMO badge and must not imply a real inbox received it; label sample data once when stalls first appear ("Demo environment · sample stalls") and in the end-card fine print; the demo QR is labelled in its capture and nothing may imply real money moved; QR flow = the stall accepts first, then the QR appears, you pay, the stall confirms before cooking (never "pay first" or "QR at checkout"); no pickup choice; no rider/GPS/map tracking; no delivery-time promise; no "free", "zero cost", "minimal delivery charge"; "no commission"/"no platform fee" are fine; never "SETU delivers" (the stall delivers); no competitor names (real or disguised); never claim SETU guarantees hygiene; the closing disclaimer is verbatim: "SETU connects customers with approved campus food providers. Food preparation, delivery and payment are handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene." End-card tagline "Your campus. Your food. Your SETU." and CTA "Explore SETU Food".
6. Rhythm (STYLE.md): one idea at a time; tap, result, a beat >= 0.6 s; hold any screen whose text matters >= 1.2 s; camera moves 0.8-1.2 s (scale 1.4-2.2 typical, never > 2.5); no constant drifting, spinning, particles or glitch; exits 0.3-0.5 s; elements that enter later are fully hidden until their entrance.
7. Every scene must be buildable with kit.js helpers + plain GSAP inside one HyperFrames sub-composition; videos (clips) play inside a non-timed layer in the phone screen and are never animated directly; captions are drawn by the shared caption track, never inside scenes.
8. Exact copy: every quoted UI string and every dish name/price must match the captures (open the PNGs to check). Seeded prices: Masala Dosa Rs80, Ghee Roast Dosa Rs110, Filter Coffee Rs30 (2 x = Rs60). Order numbers/codes must match the final captures (the cash order's handover code is visible in order-cash/07 and 08; do not invent others).
`


const ADDENDUM = `
DIRECTOR'S ADDENDUM (added after the synthesis; binding from now on, verifiers must check it)
A. SAVED-ADDRESS SELECTION MUST BE SHOWN. The brief lists it, and the story needs it: tonight, on his new phone, Home first reads "Set your delivery location" (signin/07-home.png; location/30-home-unset.png), yet after the DAY ONE flashback the film shows Home · B-212 without him choosing it. At the start of s07 ("TONIGHT"), show Aarav picking his saved Home with real taps placed before each change: tap the Deliver-to row on Home -> the picker sheet opens with "Saved locations" (location/31-picker-saved.png) -> tap the Home row -> the confirm step (location/32-confirm-saved.png) -> tap "Confirm location" -> Home now reads Home · Room B-212 (location/33-home-set.png); then continue to search "dosa". Check every mark you use in marks.json (keys location/30-home-unset, 31-picker-saved, 32-confirm-saved, 33-home-set) and open the PNGs. Make the s07 frame-0 state and the s06/s07 handoff consistent with this (e.g. s06 may end on the day-one Home, then the TONIGHT band returns to tonight's unset Home). Keep it brisk (about 3.5 s) but within the rhythm minimums. A caption such as "Back to tonight: his saved Home\nis one tap away." (<= 42 chars per line) can carry it.
B. KEEP THE TOTAL <= 119.5 s (QC fails above 120 s). Recover the time from the least valuable holds: shorten (do not remove) the s05 map round trip, take the end card to 8.0 s with the disclaimer still fully legible >= 6 s, small trims in s06 and s09; never break the rhythm minimums or caption rules.
C. The synthesis generated the JSON with ${A.gen}; prefer editing that generator and re-running it so every global time stays consistent, then re-run the validator.
`

phase('Synthesize')
const synth = await agent(`You are the director finalising the storyboard for the SETU Food customer walkthrough video (1920x1080, 60 fps, silent master with burned-in captions).
${CONTEXT}
${RULES}
TASK
1. Read the winning draft, both runners-up and all three judge verdicts in full. Read STYLE.md, kit.js, the shot inventory, codebase-flow.md section 3 and the parts of section 2 you quote. Open the real capture PNGs you rely on (use the Read tool on images) to confirm copy, positions and which captures exist. Check marks.json for every mark you name.
2. Write the final storyboard to ${A.vp}/storyboard/scene-timing.json and ${A.vp}/storyboard/layout.json following the OUTPUT CONTRACT exactly. Graft runner-up ideas only where they improve clarity or honesty.
3. Write and run a Python validator (keep it at ${A.vp}/storyboard/validate_storyboard.py so others can re-run it) that checks: scene tiling and total; ids contiguous; caption rules (chars/line, lines, duration, words/s, overlaps, inside scene); word count; every shot file exists (pngs under ${A.hf}/assets/ui, clip dirs under ${A.vp}/assets/screens, desktop pngs), every "clip:" base length is known and clipSeconds within 0.75x-2.5x; handoffOut(N) == handoffIn(N+1); demoBadge windows inside their scenes; onScreenText strings containing the rupee sign flagged if their role says Sora/headline; forbidden phrases absent from narration/captions/onScreenText (SETU delivers, pickup, rider, GPS tracking, free, zero cost, minimal, guarantee hygiene, Swiggy/Zomato/Higi/Tomato, minutes delivery promises). Fix until it prints no problems.
4. Run: cd ${A.hf} && node tools/build-docs.mjs  — it must succeed (it writes the script/storyboard/subtitle docs from your JSON).
Return a concise summary: scene list with times and titles, word count, what you changed versus B and why, and any judgement calls the reviewers should double-check.`, { label: 'synthesize', phase: 'Synthesize' })
log('Synthesis done; starting three independent verifiers')

phase('Verify')
const LENSES = [
  { key: 'truth', prompt: `LENS: PRODUCT TRUTH AND HONESTY. Check every narration line, caption, onScreenText item, uiState, animation note and accuracy note in ${A.vp}/storyboard/scene-timing.json against codebase-flow.md (sections 2 and 3) and the brief's product-truth list. Open the capture PNGs that are quoted and confirm every quoted UI string, dish, price, total, order number and code is exact and visible in the named capture. Check: DEMO badge covers the whole OTP portion and nothing implies a real inbox; sample data labelled once on first stalls and in end-card fine print; demo QR never implies real money; QR order sequence correct (accept -> QR -> pay -> stall confirms -> cooking); payment status vs order status not conflated; no pickup choice; no rider/GPS/map; no delivery-time promise; no free/zero-cost/minimal; never "SETU delivers"; hygiene not guaranteed; disclaimer verbatim; no competitor names; the audience line is fair; nothing contradicts the app. Flag also any magnified app copy that itself says "SETU delivers". Blocker = would mislead a viewer or breaks a hard rule; major = inaccurate detail; minor = wording polish.` },
  { key: 'mechanics', prompt: `LENS: MECHANICS, TIMING AND TOOLING. Re-run ${A.vp}/storyboard/validate_storyboard.py and also write your own independent checks (do not trust the author's validator). Verify: schema matches the OUTPUT CONTRACT exactly (field names, types, global vs scene-local times: captions/onScreenText/shots/soundCues/demoBadge GLOBAL, animation LOCAL); scenes tile 0..totalSeconds; total 105-120 s (target 110-114); caption rules (<=42 chars/line, <=2 lines, >=1.3 s, <=2.6 words/s, no overlap, inside scene, at least ~0.1 s gap); narration 200-240 words; every shot file exists; every mark named in animation text exists in marks.json for that shot or an explicit box is given; clipSeconds within 0.75x-2.5x of base; for every moment of every scene some visual is defined (no blank phone, no gap between shots unless intended); handoffOut(N) equals handoffIn(N+1) field-for-field and is physically consistent with the last/first shots; demoBadge windows inside scenes and covering the OTP portion; the animation text's local times stay inside 0..duration and agree with the GLOBAL shot/caption times (convert and compare). Then run: cd ${A.hf} && node tools/build-docs.mjs && node tools/make-packets.mjs  — both must succeed. Blocker = a tool fails or the file is unusable; major = a timing/schema/handoff error a builder would trip on; minor = cosmetic.` },
  { key: 'craft', prompt: `LENS: CRAFT, CLARITY AND BUILDABILITY. Judge whether a first-time silent viewer can follow every step, and whether each scene can be built exactly as written with kit.js + GSAP in a HyperFrames sub-composition. Check against STYLE.md: canvas grid zones (text column x140-820, callout lane x840-1130, phone default {left:1150, top:70, k:1.08} = outer box x1150-1599 y70-1010, right margin x1620-1880, caption zone reserved), max 4 floating labels, label widths fit on canvas (28 px chip ~ 17 px/char + 70 px), nothing overlaps phone/text column/caption zone; rhythm (tap BEFORE result by 0.25-0.45 s, >=0.6 s beat after results, >=1.2 s holds on text-heavy screens, camera moves 0.8-1.2 s, scale <= 2.5); every chip/number flight is staggered; entrances fully hidden beforehand; transitions motivated by the real interaction; scene boundaries designed to be seamless given the handoff contracts; the hook is clear in 3 s; the end card disclaimer legible >= 6 s at a readable size; typing/scroll clip speeds plausible. Spot-check at least 12 mark coordinates and explicit boxes against the PNGs (open them; marks are CSS px of a 390x844 screen, PNG is 3x). Blocker = cannot be built or confuses viewers; major = visible flaw (overlap, rushed, unreadable, wrong coordinates); minor = polish.` },
]
const verify = async (round) => (await parallel(LENSES.map((L) => () => agent(`You are an independent, skeptical reviewer of the final storyboard for the SETU Food walkthrough video. Default to reporting a problem when unsure, but every issue needs concrete evidence (file, field, time, quote, pixel box).
${CONTEXT}
${RULES}
${ADDENDUM}
${L.prompt}
Do not edit the storyboard yourself. Return verdict "pass" only if there are no blocker or major issues. Review round ${round}.`, { label: `verify:${L.key}:r${round}`, phase: 'Verify', schema: ISSUES })))).map((r, i) => ({ lens: LENSES[i].key, ...(r || { verdict: 'needs-fixes', issues: [{ sceneId: '*', severity: 'major', field: '*', problem: 'verifier failed to return', evidence: '', fix: 'rerun' }], summary: 'verifier died' }) }))

let results = await verify(1)
let rounds = []
for (let round = 1; round <= 3; round++) {
  const serious = results.flatMap((r) => r.issues.filter((i) => i.severity !== 'minor').map((i) => ({ lens: r.lens, ...i })))
  const minor = results.flatMap((r) => r.issues.filter((i) => i.severity === 'minor').map((i) => ({ lens: r.lens, ...i })))
  rounds.push({ round, serious: serious.length, minor: minor.length, verdicts: results.map((r) => `${r.lens}:${r.verdict}`) })
  log(`Round ${round}: ${serious.length} blocker/major, ${minor.length} minor issues`)
  if (!serious.length && round > 1) break
  if (!serious.length && !minor.length) break
  phase('Revise')
  await agent(`You are the director revising the final storyboard after independent review (round ${round}).
${CONTEXT}
${RULES}
${ADDENDUM}
The storyboard is at ${A.vp}/storyboard/scene-timing.json (validator: ${A.vp}/storyboard/validate_storyboard.py).
Reviewers reported these issues (JSON). Fix every blocker and major issue; fix minor ones when cheap and safe. If you believe an issue is wrong, verify against the captures/code and explain in your summary instead of changing it.
${JSON.stringify({ serious, minor }, null, 1)}
After editing: re-run the validator until clean, then run: cd ${A.hf} && node tools/build-docs.mjs && node tools/make-packets.mjs (both must succeed). Return a summary of each change (or rebuttal) keyed to the issue.`, { label: `revise:r${round}`, phase: 'Revise' })
  if (round === 3) break
  phase('Verify')
  results = await verify(round + 1)
}
return { synth, rounds, finalVerdicts: results.map((r) => ({ lens: r.lens, verdict: r.verdict, summary: r.summary, open: r.issues })) }
