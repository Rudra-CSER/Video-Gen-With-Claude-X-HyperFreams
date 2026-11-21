# ---------------------------------------------------------------- s04
scene(
 id='s04', compositionName='new-here', title='New here? Create a customer account', chapter='02 · New here?', dur=10.0,
 captions=[(0.10, 2.80, "New here? Rewind to Aarav's day one."),
           (2.90, 6.85, 'Tap “Create a Customer account”:\nname, institute email, phone, password.'),
           (7.60, 9.55, 'Then four quick steps.')],
 onScreenText=[
  ('DAY ONE', 0.40, 2.90, 'tag (tag row at (140,112): Lucide rotate-ccw + Space Mono 700 18 px caps)'),
  ('02 · New here?', 0.45, 9.90, 'kicker (kit .kicker)'),
 ],
 shots=[
  ('signin/07-home.png', 0.0, 0.41, 'Frame 0 (from s03), covered by the rewind band at 0.41.'),
  ('graphic:editorial rewind band (full-height indigo band, orange leading edge)', 0.0, 0.70, 'Sweeps left → right; the screen changes under it.'),
  ('onboarding/01-signin.png', 0.41, 2.20, "Swapped in under the band; ring--blue + tap 'Create a Customer account' (1.30) at identity."),
  ('onboarding/02-signup-empty.png', 1.65, 3.15, "swapPush in ('Create your Customer account') while the camera moves to Fcreate; tap Name (2.80)."),
  ('onboarding/03-type-name/', 3.15, 3.77, "Typing clip, clipSeconds 0.62: 'Aarav Mehta'.", 0.62),
  ('onboarding/04-type-email/', 3.77, 5.33, "Typing clip, clipSeconds 1.56: 'aarav.demo@kgpian.iitkgp.ac.in'.", 1.56),
  ('onboarding/05-type-phone/', 5.33, 5.89, "Typing clip, clipSeconds 0.56: '9000012345'; ring on the helper line.", 0.56),
  ('onboarding/06-type-password/', 5.89, 6.60, 'Typing clip, clipSeconds 0.71: masked dots.', 0.71),
  ('onboarding/07-signup-filled.png', 6.60, 8.10, "Still under the clips ('Strong enough.'); ring--blue + tap 'Create account' (7.20)."),
  ('onboarding/10-step1-identity.png', 7.55, 9.95, "swapPush in (Step 1 of 4 'Confirm your campus identity'); ring the app's stepper; tap 'Continue' (9.05)."),
  ('onboarding/21-step2-prompt.png', 9.40, 10.00, "swapPush in (Step 2 of 4 'Where should orders arrive?') and settle."),
 ],
 uiState="Rewind to day one: sign-in page with the card 'New here? Create a customer account — it takes a moment…' → 'Create your Customer account' (empty → filled: Aarav Mehta, aarav.demo@kgpian.iitkgp.ac.in, 9000012345, masked password, 'Strong enough.') → onboarding Step 1 of 4 'Confirm your campus identity' → Step 2 of 4 'Where should orders arrive?'.",
 animation=f"""Local times. Frame 0 = s03's last frame (signin/07-home.png at identity). Camera framing Fcreate = {frame('Fcreate')}: canvas of a screen point = (1125.16 + 1.512·x, −409.8 + 1.512·y); the header logos stay off-frame.
0.00–0.70 rewind band: a full-height band 760 px wide (linear-gradient(90deg,#151E4D,#22307A)) with a 3 px #EC5A2A leading edge on its right side, x −760 → 1920 (power2.inOut 0.7 s), above the phone and the left column (the caption track stays on top). It fully covers the phone between ≈0.39 and 0.43 s.
0.41 instant swap under the band: signin/07-home.png → onboarding/01-signin.png (set the new layer visible, hide the old one; verify the frame in a snapshot).
0.40–0.70 tag 'DAY ONE' (Lucide rotate-ccw 20 px + Space Mono 700 18 px caps, #B8C7FF, pill padding 10/16) fades in at the tag row (140,112); 2.60–2.90 it fades out. 0.45 kicker '02 · New here?' K.fadeUp at (140,200).
1.05 ring--blue on onboarding/01-signin.createAccount (at identity, canvas {bx(None, (30,709.8,330,48))}) — the band has cleared at 0.70, so the sign-in page reads for 0.6 s first. 1.30 K.tap createAccount ('Create a Customer account') → 1.65 K.swapPush → onboarding/02-signup-empty.png (0.55 s).
1.65–2.65 K.focus Fcreate (1.0 s), moving with the page push; the form fills the frame (name {bx('Fcreate', (16,333.5,358,48))}, submit {bx('Fcreate', (16,677.5,358,48))}).
2.80 K.tap onboarding/02-signup-empty.name → 3.15 the typing clips play back-to-back in one non-timed layer stack, each starting on the frame where the previous one ends (the field-to-field focus changes are in the captures, so no extra taps are drawn): onboarding/03-type-name/ 3.15–3.77 (0.62), 04-type-email/ 3.77–5.33 (1.56), 05-type-phone/ 5.33–5.89 (0.56), 06-type-password/ 5.89–6.60 (0.71); onboarding/07-signup-filled.png holds underneath from 6.60.
5.35–6.55 orange ring on the phone helper line, measured box {{x:16,y:546,w:234,h:17}} 'The seller calls this number at handover.' (canvas {bx('Fcreate', (16,546,234,17))}).
6.95 ring--blue on onboarding/07-signup-filled.submit. 7.20 K.tap submit ('Create account') → 7.55 K.swapPush → onboarding/10-step1-identity.png (0.55 s). 7.55–8.45 K.unfocus (0.9 s).
8.10–9.30 orange ring (radius 15) on the app's own stepper, measured box {{x:16,y:58,w:358,h:30}} (canvas at identity {bx(None, (16,58,358,30))}).
8.80 ring--blue on onboarding/10-step1-identity.cont. 9.05 K.tap cont ('Continue') → 9.40 K.swapPush → onboarding/21-step2-prompt.png (0.55 s), settled at 9.95.
9.50–9.90 the kicker fades out. 9.95–10.00 hold.""",
 transitionIn='Editorial rewind band (left → right) wipes from tonight\'s Home to the sign-in page of day one — a chapter wipe, not in-app navigation.',
 transitionOut="Tap 'Continue' on Step 1; Step 2 pushes in and settles at identity before the cut.",
 handoffIn=handoff(screen='signin/07-home.png', notes='Same frame as s03 ends.'),
 handoffOut=handoff(screen='onboarding/21-step2-prompt.png', notes='Step 2 fully settled at identity; tag, kicker and rings gone.'),
 demoBadge=[],
 soundCues=[(0.0, 'Band wipe whoosh (rewind)'), (1.30, 'UI tap'), (1.65, 'Page push'), (3.15, 'Fast keyboard ticks through 6.6 s'),
            (7.20, 'UI tap (Create account)'), (7.55, 'Page push + soft step chime'), (9.05, 'UI tap (Continue)'), (9.40, 'Page push')],
 accuracyNotes="""- The band is an editorial 'rewind' to the day Aarav set up his account (it makes the second path explicit), not an in-app back navigation.
- The fields are exactly Name / Institute email / Phone / Password; the helper 'The seller calls this number at handover.' is the form's own copy. 'Create a Customer account' is the card's exact button text.
- Onboarding has four steps ('Step N of 4'); the ring is on the app's own stepper.
- Typing is real (four clips at ≈0.76× of their base length; no keyboard is added); the password shows masked dots only.
- Step 1's line about what stakeholders see is visible but not featured (not in the verified facts).
- Demo persona data only (Aarav Mehta, aarav.demo@kgpian.iitkgp.ac.in, 9000012345).""",
)

