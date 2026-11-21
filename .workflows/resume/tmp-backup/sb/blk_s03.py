# ---------------------------------------------------------------- s03
code_x = (45.2, 105.1, 165.1, 225.0, 285.0, 344.9)
card_dx = (727.3, 765.7, 804.2, 842.2, 881.2, 919.6)
CLIP0 = 7.60            # code clip start (local)
FR = 1.2 / 7            # seconds per captured frame of signin/05-type-code at clipSeconds 1.2
f1_boxes = [under(FOC['F1'], x, 304) for x in code_x]
digit_t = [CLIP0 + FR * (k + 1) for k in range(6)]
trail_lines = '; '.join(f'{k+1}: ({n(card_dx[k],1)},541.8)→({n(f1_boxes[k][0],1)},{n(f1_boxes[k][1],1)}) draws {n(digit_t[k]-0.16,3)}–{n(digit_t[k],3)}'
                        for k in range(6))
scene(
 id='s03', compositionName='sign-in', title='Have an account? Sign in — password, or an emailed code', chapter='01 · Sign in', dur=10.6,
 captions=[(0.10, 3.40, 'For IIT Kharagpur campus accounts:\nstudents, faculty, staff.'),
           (3.50, 8.15, 'Have an account? Sign in with\nyour password, or an emailed code.'),
           (8.25, 10.25, "Six digits, and Aarav's in.")],
 onScreenText=[
  ('01 · Sign in', 0.10, 10.30, 'kicker (kit .kicker)'),
  ('Password, or a code.', 0.30, 6.10, "headline (.headline--md, Sora 800 68 px, two lines 'Password,' / 'or a code.' with 'or a code.' in #B8C7FF; no rupee sign)"),
  ('MAIN WAY IN', 3.35, 5.00, 'label (short caps, Space Mono 700 20 px, callout lane)'),
  ('OR EMAIL A CODE', 4.55, 6.20, 'label (short caps, Space Mono 700 20 px, callout lane)'),
  ('Demo environment', 5.55, 10.20, 'DEMO badge (kit .demo-badge, tag row at (140,112))'),
  ('DEMO · Local test inbox', 6.40, 9.65, 'mail-card head strip (orange-outline DEMO tag + Space Mono 700 16 px)'),
 ],
 shots=[
  ('signin/01-signin.png', 0.0, 1.55, 'Phone at the default spec; camera F1 from 0.30; ring on the campus pill; tap id at 1.20.'),
  ('signin/02-type-email/', 1.55, 3.11, "Typing clip, clipSeconds 1.56: 'aarav.demo@kgpian.iitkgp.ac.in' into the id field.", 1.56),
  ('signin/03-email-typed.png', 3.11, 6.50, 'Still under the clip, then held: ring password + MAIN WAY IN; ring--blue + tap otpLink (5.60); pushes out 5.95–6.50.'),
  ('signin/04-enter-code.png', 5.95, 7.60, "swapPush in; ring sentTo ('We emailed a six-digit code to aa***@kgpian.iitkgp.ac.in. It expires in 10 minutes.')."),
  ('signin/email-otp.png', 6.40, 9.65, 'DEMO mail card in the left column: the real email render cropped to email CSS x12–378, y24–420 inside a white card under a DEMO head strip; code-box glow; light trails to the phone.'),
  ('signin/05-type-code/', 7.60, 8.80, 'Typing clip, clipSeconds 1.2 (7 frames × 0.1714 s): the six digits, synced to the light trails.', 1.2),
  ('signin/06-code-entered.png', 8.80, 9.90, "Still under the clip, then held; ring--blue + tap 'Verify and continue' (9.25)."),
  ('signin/07-home.png', 9.60, 10.60, "swapFade in ('Good evening, Aarav', 'Set your delivery location'); camera back to identity."),
 ],
 uiState="Signed-out phone sign-in (Customer selected, 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY') → email typed → 'Enter the code' (sent to aa***@kgpian.iitkgp.ac.in, 'It expires in 10 minutes.') → six digits entered → Home on a fresh device ('Set your delivery location · Tap to pick it on the map', 'Good evening, Aarav').",
 animation=f"""Local times. Phone at the default spec from frame 0 (handoffIn). Camera framing F1 = {frame('F1')}: header logos (screen y<100) stay off-frame, so the crest and the 75-years mark are never magnified; visible screen y≈104–818; canvas of a screen point = (1125.16 + 1.512·x, −156.86 + 1.512·y).
0.10 kicker '01 · Sign in' K.fadeUp at (140,200). 0.30 headline 'Password,' / 'or a code.' (.headline--md, top 250, width 680; 'or a code.' in #B8C7FF) K.revealWords.
0.30–1.30 K.focus F1 (1.0 s).
0.60–2.20 orange ring (radius 14) on the campus pill, measured box {{x:52,y:164,w:286,h:27}} 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY' → canvas {bx('F1', (52,164,286,27))}.
1.20 K.tap signin/01-signin.id → 1.55 clip layer signin/02-type-email/ (clipSeconds 1.56) plays 1.55–3.11; signin/03-email-typed.png sits underneath and holds from 3.11.
3.30–4.60 orange ring on signin/01-signin.password (same layout in 03; canvas {bx('F1', (16,472.6,358,48))}) + label 'MAIN WAY IN' (≈206×40) at x 910–1116, y 574–614 from 3.35; 2 px leader (1116,594)→(1149,594); 4.70–5.00 the label fades.
4.45 ring--blue on signin/03-email-typed.otpLink (canvas {bx('F1', (75.7,578.6,238.6,40))}) until 5.60. 4.55 label 'OR EMAIL A CODE' (≈260×40) at x 856–1116, y 728–768; leader (1116,748)→(1239,748); 5.85–6.20 it fades.
5.55–5.80 DEMO badge (kit .demo-badge 'Demo environment') fades up at the tag row (140,112) — on from the code request until Home is reached.
5.60 K.tap signin/03-email-typed.otpLink ('Email me a one-time code instead') → 5.95 K.swapPush → signin/04-enter-code.png (0.55 s). 5.70–6.10 the headline fades out.
6.50–7.80 orange ring on signin/04-enter-code.sentTo (canvas {bx('F1', (16,206.1,358,40))}).
6.40–7.00 DEMO mail card (kit .mailcard, width 480) at left 590, top 200: head strip 52 px = orange-outline 'DEMO' tag + 'Local test inbox' (Space Mono 700 16 px; no sender, no time, no OS or mail-app chrome); body = signin/email-otp.png cropped to email CSS x12–378, y24–420 at 1.3115× (480×519; card bottom ≈771). Entrance fromTo x −40/opacity 0/rotate 1.5° → 0/1/0 (expo.out 0.6 s). Email CSS → canvas: X = 590 + (x−12)·1.3115, Y = 252 + (y−24)·1.3115.
7.00–7.60 pale-blue glow ring around the email's code box (canvas x 621.5–1038.5, y 495.9–587.7).
{n(CLIP0)} clip layer signin/05-type-code/ (clipSeconds 1.2; 7 frames × 0.1714 s; f0000 = the empty boxes of 04). Digits appear at {', '.join(n(t,3) for t in digit_t)}; the clip ends at 8.80 and signin/06-code-entered.png holds underneath.
Light trails: one per digit, a 1.5 px pale-blue line drawn with K.drawPath (0.16 s, power2.out) from the card digit to its phone box (F1 canvas), finishing exactly as that digit appears, then fading in 0.2 s; never two drawing at once. From → to and timing: {trail_lines}. As each trail leaves, that digit on the card brightens.
8.90 ring--blue on signin/06-code-entered.verify. 9.25 K.tap verify ('Verify and continue') → 9.60 K.swapFade → signin/07-home.png (0.3 s). 9.25–9.65 the mail card exits left (x −60, fade, power2.in 0.4 s).
9.60–10.50 K.unfocus (0.9 s): the camera returns to identity as Home settles (the header 'Set your delivery location' comes into frame).
9.90–10.20 the DEMO badge fades out (Home is fully shown at 9.90). 10.00–10.30 the kicker fades out. 10.50–10.60 hold.""",
 transitionIn='Continuous from the web → phone match cut: the phone is already at its default spec on the sign-in screen.',
 transitionOut="Settles on fresh-device Home at identity with the left column empty; s04's rewind band opens on this frame.",
 handoffIn=handoff(screen='signin/01-signin.png', notes='Same frame as s02 ends: phone at the default spec, nothing else.'),
 handoffOut=handoff(screen='signin/07-home.png', notes="Camera back at identity; DEMO badge, mail card, kicker and labels gone. Home reads 'Set your delivery location' (fresh device)."),
 demoBadge=[(5.80, 9.90)],
 soundCues=[(0.60, 'Ring swish (campus accounts)'), (1.55, 'Quiet keyboard ticks for 1.5 s'), (5.60, 'UI tap'), (5.95, 'Page push swish'),
            (6.40, 'Gentle chime: DEMO mail card (not an OS notification sound)'), (7.77, 'Six soft digit ticks, 0.17 s apart'),
            (9.25, 'UI tap (Verify and continue)'), (9.60, 'Success: soft two-note rise')],
 accuracyNotes="""- Password sign-in is the main method; the emailed one-time code is the alternative ('Email me a one-time code instead'). The caption names both and the labels say exactly that.
- The code really was emailed, by the isolated demo stack to a local test inbox (Mailpit). The DEMO badge is on from the code request (5.55–5.80 fade-in, with the 5.60 tap) until Home is shown (9.90), and the card's head strip says 'Local test inbox'. Nothing implies a real inbox received it: no sender, timestamp, app icon or OS notification styling.
- The card shows the real email render (header 'SETU Food', 'Your sign-in code', the code, 'It expires in 10 minutes … and works once.', 'Never share this code. SETU staff will never ask you for it.'). Digits 686713 match in signin/email-otp.png and signin/06-code-entered.png; never retype or invent digits; keep the masked address as captured.
- 'For IIT Kharagpur campus accounts: students, faculty, staff.' is the approved audience line; the UI pill reads 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY' (no UI string names faculty or staff, so the line is anchored to campus accounts).
- F1 keeps the crest row off-frame; the 75-years mark is never enlarged.
- signin/07-home.png ('Set your delivery location') is the real fresh-device state; it sets up the flashback.""",
)

