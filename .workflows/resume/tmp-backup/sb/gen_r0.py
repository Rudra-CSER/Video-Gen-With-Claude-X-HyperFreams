# Generator for video-production/storyboard/scene-timing.json + layout.json.
# Scenes are authored in SCENE-LOCAL seconds; everything except `animation` is converted to GLOBAL seconds here.
import json, re, sys
from geom import toC, under, box, FOC, F, rig

OUT = '/home/rudra-cser/Setu-Food-PWA/video-production/storyboard'

def n(v, d=2):
    s = f'{v:.{d}f}'.rstrip('0').rstrip('.')
    return s if s != '-0' else '0'

def _f(f):
    return FOC[f] if isinstance(f, str) else f

def bx(f, b):
    x0, y0, x1, y1 = box(_f(f), b)
    return f'({n(x0,1)},{n(y0,1)})–({n(x1,1)},{n(y1,1)})'

def pt(f, x, y):
    cx, cy = under(_f(f), x, y)
    return f'({n(cx,1)},{n(cy,1)})'

def frame(name):
    f = FOC[name]
    return f"{{s {n(f['s'])}, P [{n(f['P'][0])},{n(f['P'][1])}], T [{n(f['T'][0])},{n(f['T'][1])}]}}"

def rigobj(name):
    f = FOC[name]
    return {'s': f['s'], 'P': list(f['P']), 'T': list(f['T'])}

ID = 'identity'
def handoff(phone='default', screen=None, rig_=ID, left='empty', overlays='none', notes=''):
    return {'phone': phone, 'screen': screen, 'rig': rig_, 'leftColumn': left, 'overlays': overlays, 'notes': notes}

SCENES = []
def scene(**kw):
    SCENES.append(kw)

FSPLIT = F(0.7407, [195, 422], [346.4, 497.9])

# ---------------------------------------------------------------- s01
scene(
 id='s01', compositionName='hook', title='Hook — your campus, your food', chapter=None, dur=5.4,
 captions=[(0.20, 3.70, 'Your campus. Your food.\nA simpler way to order.'),
           (3.80, 5.35, 'Meet Aarav, Nehru Hall.')],
 onScreenText=[
  ('SETU Food', 2.60, 5.35, 'title (Sora 800, 84 px, white, centred under the lockup tile; no rupee sign)'),
  ('ON SETU SERVICES · IIT KHARAGPUR', 3.00, 5.35, 'subline (Space Mono 700, 18 px caps, #B8C7FF, centred)'),
  ('Aarav · Room B-212', 3.85, 5.35, 'persona chip beside the Nehru Hall pin (Space Mono 700, 20 px)'),
 ],
 shots=[
  ('graphic:real campus boundary outline (assets/data/campus-boundary.json) with the Nehru Hall pin', 0.0, 5.4,
   'Motion graphic from real data: the 78-point Main Campus Boundary path drawn 1000×516.4 at canvas (460,150); orange outline map-pin on the file\'s nehruHall point.'),
  ('graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)', 2.2, 5.4,
   'Tile 260×206 centred at (960,360); lockup 216 px wide, downscaled only, never recoloured.'),
  ('graphic:hook type (SETU Food title, subline, persona chip)', 2.6, 5.4, 'Kinetic type only.'),
 ],
 uiState='No app UI: motion graphics built from real data (campus boundary polygon and its Nehru Hall point) plus the official SETU lockup.',
 animation=f"""Local times. Full-screen motion graphic, no phone. Captions are CENTRED in this scene (layout.json), so keep y 880–1050 empty across the width.
Outline group (#s01-map): the real 'Main Campus Boundary' path from assets/data/campus-boundary.json (viewBox 0 0 1000 516.4) as an inline SVG 1000×516.4 at left 460, top 150 (x 460–1460, y 150–666). Stroke #B8C7FF 3 px, round joins, filter drop-shadow(0 0 10px rgba(130,160,255,.55)); fill rgba(46,91,238,.06) (starts at fill-opacity 0).
0.10–2.10 K.drawPath on the outline (2.0 s, power2.inOut). 1.60–2.30 the fill fades in.
1.70 Nehru Hall marker at the file's nehruHall point (114.2, 98.8) → canvas (574.2, 248.8): a Lucide map-pin (OUTLINE, stroke 2.5 px #EC5A2A, 40 px tall, tip on the point) fromTo y −60/opacity 0 → 0/1 (expo.out 0.45 s), plus an 8 px orange dot exactly on the point; 1.95–2.65 one 2 px orange ripple ring grows 0→80 px and fades.
2.20–2.90 the outline group tweens to opacity 0.30 (power2.out); the pin and dot stay at 100%.
2.20 white tile (kit .white-tile, 260×206, radius 32) centred at (960,360) → x 830–1090, y 257–463, holding assets/brand/setu-logo.png at 216 px wide (≈170 px tall), centred: fromTo scale 0.94/opacity 0 → 1/1 (expo.out 0.7 s).
2.60 title 'SETU Food' (Sora 800, 84 px, white, letter-spacing −.03em, centred, top 492) K.revealWords (stagger 0.08).
3.00 subline 'ON SETU SERVICES · IIT KHARAGPUR' (Space Mono 700 18 px caps, letter-spacing .2em, #B8C7FF, centred, top 600) K.fadeUp.
3.85 persona chip 'Aarav · Room B-212' (Space Mono 700 20 px, white on rgba(12,18,51,.88), 1 px rgba(255,255,255,.18) border, radius 12, padding 10/16; ≈300×42) at left 604, top 196 (right of the pin head, clear of the tile): fromTo x −16/opacity 0 → 0/1 (expo.out 0.5 s).
4.95–5.35 exit: tile, title, subline and chip rise −16 px and fade (power2.in 0.4 s); outline, pin and dot fade (0.4 s). The frame at 5.35–5.40 is the empty shared background.""",
 transitionIn='Cold open on the shared indigo background; the outline starts drawing at 0.10 s.',
 transitionOut='Every hook element exits 4.95–5.35; the last frame is the empty background (hard cut; s02 starts empty).',
 handoffIn=handoff(phone='none', notes='Cold open: only the shared background (index.html) is visible.'),
 handoffOut=handoff(phone='none', notes='All hook graphics are gone by 5.35; empty background at the cut.'),
 demoBadge=[],
 soundCues=[(0.0, 'Placeholder bed: low warm pad fades in (owner replaces)'), (0.10, 'Fine line-draw shimmer following the outline (2.0 s)'),
            (1.70, 'Pin drop: short wooden tick'), (2.20, 'Soft paper tick as the white logo tile lands'),
            (3.85, 'Two-note soft chime for the Aarav chip'), (4.95, 'Air whoosh out')],
 accuracyNotes="""- The outline is the real 78-point 'Main Campus Boundary' (server campus-zone config, via assets/data/campus-boundary.json) and its nehruHall point; it is a motion graphic, never presented as a map screenshot.
- The lockup is the official raster on a WHITE rounded tile, downscaled only, never recoloured; the 75-years mark is not used.
- 'SETU Food' is the walkthrough's name for the Food service of SETU Services (the app's on-screen brand is 'SETU Services'; 'SETU Food' is the email brand and the CTA). It is set as plain title type under the tile, never fused into a logo, and the subline says 'on SETU Services'.
- No app UI is recreated (the Food / Commute / Utilities pills are not redrawn).
- The opening line is the owner's. 'Room B-212' is the demo persona's room (it appears later in the Home header).""",
)

# ---------------------------------------------------------------- s02
scene(
 id='s02', compositionName='what-setu-does', title='What SETU does', chapter='What SETU does', dur=6.6,
 captions=[(0.15, 3.65, 'SETU Food lists approved stalls.\nThey cook and deliver.'),
           (3.75, 6.50, 'You pay the stall directly.\nNo commission.')],
 onScreenText=[('What SETU does', 0.15, 5.40, 'kicker (kit .kicker)')],
 shots=[
  ('desktop/01-signin-wide.png', 0.0, 6.2,
   "Kit .laptop frame (--lk .7, no browser/OS chrome) at left 760, top 150. Camera on the laptop rig: lede, then the stats row; rings; then a match move that lays the desktop sign-in form over the phone's screen rectangle."),
  ('signin/01-signin.png', 5.75, 6.6, 'Phone at the default spec fades in over the matched desktop form (web → phone match cut) and holds.'),
 ],
 uiState="Signed-out web sign-in page (desktop wide layout, Customer selected): art panel 'The campus, and only the campus.', the lede 'Approved local stakeholders, delivered to your hall. …' and the stats DELIVERY Campus only · COMMISSION None · PAYMENT Direct; then the phone's own sign-in screen ('SIGNING IN AS Customer', 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY').",
 animation="""Local times. Two layers: #s02-rig-desk (a full-canvas .rig) holds the laptop; the phone is OUTSIDE it at the default spec and only appears at the end.
Laptop at rest: kit .laptop with --lk .7 showing desktop/01-signin-wide.png (an <img> filling .lscreen) at left 760, top 150 → lid x 760–1804, y 150–824; screen x 778–1786, y 168–798; base y 824–846. Desktop CSS (1440×900) → canvas at rest: X = 778 + 0.7·x, Y = 168 + 0.7·y. Rings below are drawn inside the laptop screen in desktop CSS px, so they scale with the camera.
0.00–0.80 the laptop fromTo y +90/opacity 0 → 0/1 (expo.out 0.8 s). 0.15 kicker 'What SETU does' K.fadeUp at (140,200).
0.70–1.70 camera: K.focus(desk rig, P=(1052.4,497) [desktop (392,470)], s 1.3, 0.70, 1.0, {to:{x:1110,y:420}}) — headline and lede fill the frame; the lid's bottom edge lands at y≈845, above the caption zone.
0.90–2.30 pale-indigo ring (2.5 px #B8C7FF, radius 10, no fill) around the first sentence only: desktop box {x:60,y:500,w:464,h:34} 'Approved local stakeholders, delivered to your hall.'
2.10–3.10 camera: K.focus(desk rig, P=(1026.5,736.4) [desktop (355,812)], s 1.35, 2.10, 1.0, {to:{x:1080,y:520}}) — the stats row lands at y≈495–546.
2.60–3.80 orange ring (kit .ring look, inside the laptop screen) on 'DELIVERY · Campus only' desktop {x:58,y:778,w:216,h:68}; one ring scale pulse 1→1.04→1 (the UI is never recoloured).
3.80–5.00 orange ring on 'COMMISSION · None' desktop {x:318,y:778,w:110,h:68}.
4.10–5.20 orange ring on 'PAYMENT · Direct' desktop {x:543,y:778,w:110,h:68}.
5.10–5.90 match move: K.focus(desk rig, P=(1405.2,240.8) [desktop (896,104), the form's 'SIGNING IN AS' line], s 1.0, 5.10, 0.8, {to:{x:1181.3,y:206}}) — the desktop form's left edge and its 'SIGNING IN AS' line now sit on the phone screen's left edge and heading line (lid x 536–1580, y 115–789; an approximate overlay, the dissolve does the rest). 5.10–5.40 the kicker fades out.
5.75–6.15 the phone (default spec {left:1150,top:70,k:1.08}, outside the desk rig) fromTo scale 0.97/opacity 0 → 1/1 (transform-origin centre, expo.out 0.4 s) showing signin/01-signin.png; 5.85–6.20 the laptop fades out (power1.in 0.35 s). The shared 'SIGNING IN AS · Customer' heading and form make the web → phone match cut.
6.20–6.60 hold: phone at the default spec on signin/01-signin.png; the laptop is invisible (reset the desk rig to identity once it is at opacity 0); left column empty.""",
 transitionIn='Starts on the empty background; the laptop rises 0.00–0.80.',
 transitionOut='Web → phone match cut on the shared sign-in form (5.10–6.20), then a 0.4 s settled hold on the phone.',
 handoffIn=handoff(phone='none', notes='Empty shared background (s01 has fully exited).'),
 handoffOut=handoff(screen='signin/01-signin.png', notes='Laptop fully gone; phone at the default spec, no camera move, nothing else on canvas.'),
 demoBadge=[],
 soundCues=[(0.0, 'Card settle: soft low thud as the laptop rises'), (0.90, 'Highlight swish (lede ring)'), (2.60, 'Tiny tick (Campus only)'),
            (3.80, 'Tiny tick (None)'), (4.10, 'Tiny tick (Direct)'), (5.10, 'Glassy whoosh on the web → phone match cut')],
 accuracyNotes="""- desktop/01-signin-wide.png is real UI shown in the kit's neutral laptop frame: no browser chrome, URL bar or OS UI.
- Ring only 'Approved local stakeholders, delivered to your hall.' and the three stats. Never ring, zoom on or caption 'SETU checks the licence and holds the record.' (it reads as 'every stall is licence-checked').
- desktop/02-home-web.png is not used ('Every stall is licence-checked by SETU').
- 'They cook and deliver' = the stalls (app: 'The seller brings the order themselves'); never 'SETU delivers'. 'No commission' = the stat 'COMMISSION None'.
- The panel's crest / 75-years row is never featured: both push-ins centre below it.""",
)

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
  ('MAIN WAY IN', 3.35, 5.00, 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('OR EMAIL A CODE', 4.55, 6.20, 'label (short caps, Space Mono 700 18 px, callout lane)'),
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
3.30–4.60 orange ring on signin/01-signin.password (same layout in 03; canvas {bx('F1', (16,472.6,358,48))}) + label 'MAIN WAY IN' (≈187×38) at x 905–1092, y 575–613 from 3.35; 2 px leader (1092,594)→(1149,594); 4.70–5.00 the label fades.
4.45 ring--blue on signin/03-email-typed.otpLink (canvas {bx('F1', (75.7,578.6,238.6,40))}) until 5.60. 4.55 label 'OR EMAIL A CODE' (≈236×38) at x 856–1092, y 729–767; leader (1092,748)→(1239,748); 5.85–6.20 it fades.
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
2.80 K.tap onboarding/02-signup-empty.name → 3.15 the typing clips play back-to-back in one non-timed layer stack, each starting on the frame where the previous one ends (the field-to-field focus changes are in the captures, so no extra taps are drawn): onboarding/03-type-name/ 3.15–3.77 (0.62), onboarding/04-type-email/ 3.77–5.33 (1.56), onboarding/05-type-phone/ 5.33–5.89 (0.56), onboarding/06-type-password/ 5.89–6.60 (0.71); onboarding/07-signup-filled.png holds underneath from 6.60.
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

# ---------------------------------------------------------------- s05
FC = 'Fconf'
def T5(x):
    """s05 local time: beats from the first-result tap on sit 0.2 s later than the first plan (longer hold on the result)."""
    return round(x + (0.2 if x >= 5.40 else 0.0), 3)
def t5(x):
    return f'{T5(x):.2f}'
scene(
 id='s05', compositionName='delivery-spot', title='Where should orders arrive?', chapter='03 · Delivery spot', dur=T5(16.2),
 captions=[(0.10, 3.60, 'Next: where should orders arrive?\nLocation access is optional.'),
           (3.70, 5.00, 'Search works too.'),
           (T5(6.10), T5(8.50), 'Nehru Hall: inside the delivery area.'),
           (T5(8.60), T5(11.00), 'Check the pin on the map.'),
           (T5(11.10), T5(13.50), 'Save it as Home, add B-212.')],
 onScreenText=[
  ('03 · Delivery spot', 0.10, T5(16.05), 'kicker (kit .kicker)'),
  ('OPTIONAL', 0.60, 2.20, 'label chip on the explainer inset (Space Mono 700 18 px caps, orange outline)'),
  ('CAMPUS ONLY', T5(6.55), T5(7.85), 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('CAMPUS BOUNDARY', T5(8.60), T5(9.95), 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('Home · B-212', T5(14.55), T5(16.05), 'address card title (Plus Jakarta Sans 700 32 px)'),
  ('Nehru Hall of Residence', T5(14.55), T5(16.05), 'address card subline (Plus Jakarta Sans 500 22 px, #B8C7FF)'),
 ],
 shots=[
  ('onboarding/21-step2-prompt.png', 0.0, 2.90, 'Identity; ring on the Delivery location box; ring--blue on "Use my current location" (no tap) beside the explainer inset; tap the box (2.05).'),
  ('location/01-allow-dialog.png', 0.60, 2.20, "INSET outside the phone: crop CSS {x:20,y:276,w:350,h:293} (SETU's own 'Allow location for SETU?' explainer) at 1.15× in a white card at x 420–823, y 300–637; labelled OPTIONAL; no tap; dashed leader to the GPS row."),
  ('location/10-picker-select.png', 2.40, 3.85, "swapSheet (sheetTop 537) — 'Select a location'; identity framing keeps the sheet subtitle tiny; tap search (3.50)."),
  ('location/11-type-search/', 3.85, 4.65, "Typing clip, clipSeconds 0.8: the expanded sheet, 'Nehru Hall' typed.", 0.8),
  ('location/12-search-results.png', 4.65, T5(6.05), f"Ring + tap the first result 'Nehru Hall of Residence · Pan Loop, IIT Kharagpur…' ({t5(5.40)})."),
  ('location/13-confirm-search.png', T5(5.75), T5(8.45), f"'Confirm delivery location'; camera Fconf; green ring on 'Location is within the IIT Kharagpur delivery area.'; tap 'Adjust on the map' ({t5(7.75)})."),
  ('location/20-map.png', T5(8.10), T5(10.75), f"'Select delivery location' map at Fconf (s 1.8 at screen y 575): the sheet subtitle is off-frame; pin halo; boundary label; tap 'Use this location' ({t5(10.05)})."),
  ('location/13-confirm-search.png', T5(10.40), T5(11.70), f"Back on Confirm (the map hands the same pin back); tap the 'Home' chip ({t5(11.35)})."),
  ('location/14-type-room/', T5(11.70), T5(12.50), "Typing clip, clipSeconds 0.8: f0000 has Home selected (sheet 25 px lower), then 'B-212' into Address details.", 0.8),
  ('location/15-confirm-home.png', T5(12.50), T5(14.20), f"Still under the clip (identical to its last frame); rings; tap 'Confirm location' ({t5(13.40)}); the sheet closes."),
  ('onboarding/23-step2-done.png', T5(13.75), T5(16.20), 'Revealed as the sheet closes; pin → address card; rings on the filled box and room; camera back to identity.'),
  ('graphic:pin → address card (Lucide outline map-pin, dotted path, glass card)', T5(14.25), T5(16.05), "Action → result: the field's pin flies out and unfolds into the saved-address card."),
 ],
 uiState="Onboarding Step 2 of 4 'Where should orders arrive?' (inset: SETU's own explainer 'Allow location for SETU?' … 'It is only read when you ask for it.') → 'Select a location' picker → search 'Nehru Hall' → 'Confirm delivery location' ('Location is within the IIT Kharagpur delivery area.') → map 'Select delivery location' (red pin, faint blue campus-boundary line, Google attribution) → back to Confirm → SAVE AS Home + ADDRESS DETAILS 'B-212' → 'Confirm location' → Step 2 filled ('Nehru Hall of Residence, Cricket Groun…', 22.319759, 87.298041, Room B-212, Home).",
 animation=f"""Local times. Frame 0 = onboarding/21-step2-prompt.png at identity. Camera framing Fconf = {frame(FC)} (A's map framing): visible screen y≈287–842; canvas of a screen point = (1120.92 + 1.944·x, −557.8 + 1.944·y). It keeps every 'SETU delivers inside the IIT Kharagpur campus boundary' subtitle (map: screen y 226–258) and the Confirm sheet title off-frame. The picker and search shots stay at identity, where their subtitle is tiny.
0.10 kicker '03 · Delivery spot' K.fadeUp at (140,200).
0.30–1.10 orange ring on onboarding/21-step2-prompt.box.
0.50–1.95 ring--blue on onboarding/21-step2-prompt.gps ('Use my current location') — NOT tapped.
0.60–1.00 explainer inset: a white card (radius 24, shadow 0 30px 80px rgba(0,0,0,.45)) holding location/01-allow-dialog.png cropped to CSS {{x:20,y:276,w:350,h:293}} at 1.15× (402.5×337) at left 420, top 300: fromTo scale 0.94/opacity 0 → 1/1 (back.out(1.4) 0.4 s). Label chip 'OPTIONAL' (orange 2 px outline, Space Mono 700 18 px caps, ≈148×38) at (420,250). Dashed leader (2 px rgba(184,199,255,.7), 6/6 dash) from (822.5,468) to the GPS row's left edge (1181.3,596.7).
1.10–1.80 a 3 px orange underline sweeps left → right under 'It is only read when you ask for it.' inside the inset (canvas x 473–717, y 504).
1.90–2.20 inset, label and leader fade out (0.3 s).
1.85 ring--blue on onboarding/21-step2-prompt.box. 2.05 K.tap box (centre (195,361.7)) → 2.40 K.swapSheet → location/10-picker-select.png (sheetTop 537, 0.5 s).
3.30 ring--blue on location/10-picker-select.search (pad 12). 3.50 K.tap search → 3.85 K.swapFade (0.2 s) → clip layer location/11-type-search/ (clipSeconds 0.8; f0000 = the sheet expanded to the top with the field focused) 3.85–4.65; 4.65 the clip ends: cut to location/12-search-results.png (set it visible under the clip layer at 4.65; its results list differs from the clip's last frame).
4.80–{t5(5.75)} orange ring on location/12-search-results.first. {t5(5.40)} K.tap first → {t5(5.75)} K.swapFade (0.3 s) → location/13-confirm-search.png (the sheet shrinks to 'Confirm delivery location').
{t5(5.80)}–{t5(6.80)} K.focus Fconf (1.0 s).
{t5(6.45)}–{t5(7.75)} green ring (border #19B36B + green glow) on location/13-confirm-search.zoneOk (canvas {bx(FC, (55,469,292,17))}) + label 'CAMPUS ONLY' (≈185×38) at x 900–1085, y 351–389 from {t5(6.55)} to {t5(7.85)}; leader (1085,370)→(1227.8,370).
{t5(7.55)} ring--blue on the 'Adjust on the map' row, measured box {{x:18,y:684,w:354,h:66}}. {t5(7.75)} K.tap location/13-confirm-search.adjust (centre (205.5,708)) → {t5(8.10)} K.swapFade (0.35 s) → location/20-map.png (no layer movement: at Fconf both sheet tops are off-frame and the blurred page behind them is the same).
{t5(8.50)}–{t5(9.70)} pin halo: two 2 px orange rings grow from the map pin's tip (screen (195,456); pin head (195,433); canvas tip {pt(FC,195,456)}) to r 36 CSS px, 0.6 s each, 0.3 s apart.
{t5(8.60)}–{t5(9.95)} label 'CAMPUS BOUNDARY' (≈234×38) at x 852–1086, y 279–317; leader (1086,298)→{pt(FC,91.3,440)} — the faint blue boundary line on the map passes through screen (91.3,440) (it runs ≈(164.7,330)→(18.6,549)). The Google logo and 'Map data ©2026' strip (screen y 566–588) stay unobstructed.
{t5(9.85)} ring--blue on location/20-map.useThis (canvas {bx(FC, (183.5,782,188.5,48))}). {t5(10.05)} K.tap useThis ('Use this location') → {t5(10.40)} K.swapFade (0.35 s) → location/13-confirm-search.png.
{t5(11.35)} K.tap location/13-confirm-search.home (the 'Home' chip, centre (63,538)) → {t5(11.70)} K.swapFade (0.2 s) → clip layer location/14-type-room/ (clipSeconds 0.8: f0000 Home selected and the sheet 25 px lower because the 'Choose one…' line disappears; then 'B-212' typed) {t5(11.70)}–{t5(12.50)}; location/15-confirm-home.png holds underneath from {t5(12.50)} (identical to the clip's last frame).
{t5(12.55)}–{t5(13.35)} orange rings on location/15-confirm-home.home and location/15-confirm-home.details.
{t5(13.20)} ring--blue on location/15-confirm-home.confirm. {t5(13.40)} K.tap confirm ('Confirm location') → {t5(13.75)} the sheet closes: onboarding/23-step2-done.png sits underneath; the 15 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 576px 0)) fades out (0.35 s) while its sheet part (clip-path inset(268px 0 0 0)) slides y 0 → +576 (expo.in 0.45 s).
{t5(14.25)}–{t5(14.95)} pin → address card: a Lucide map-pin (OUTLINE, stroke 2.5 px #EC5A2A, 36 px) pops (scale 0→1, back.out(2) 0.25 s) at the Delivery-location field's pin icon — 23's screen (346,363) → canvas {pt(FC,346,363)} under Fconf — then travels left along a 2 px dotted pale path (K.drawPath) to (300,470) and unfolds into a glass card (kit .glass-card, left 140, top 420, 420×110): Lucide house icon + 'Home · B-212' (Plus Jakarta Sans 700 32 px, white) over 'Nehru Hall of Residence' (Plus Jakarta Sans 500 22 px, #B8C7FF) (expo.out 0.7 s). The card is canvas-level (outside the rig).
{t5(14.40)}–{t5(15.40)} orange rings on onboarding/23-step2-done.box (canvas {bx(FC, (16,309.7,358,104))}) and onboarding/23-step2-done.room.
{t5(14.95)}–{t5(15.85)} K.unfocus (0.9 s).
{t5(15.70)}–{t5(16.05)} card, dotted path and kicker fade out. {t5(16.05)}–{t5(16.20)} hold at identity.""",
 transitionIn='Continuous: Step 2 is already on screen at identity.',
 transitionOut='The saved address becomes a card in the left column, then everything clears; Step 2 (filled) holds at identity for the cut.',
 handoffIn=handoff(screen='onboarding/21-step2-prompt.png', notes='Same frame as s04 ends.'),
 handoffOut=handoff(screen='onboarding/23-step2-done.png', notes='Step 2 filled (Nehru Hall of Residence, Room B-212, Home) at identity; card, path, rings and kicker gone.'),
 demoBadge=[],
 soundCues=[(0.60, 'Soft card pop (explainer inset)'), (2.05, 'UI tap'), (2.40, 'Sheet slide up'), (3.50, 'UI tap'), (3.85, 'Keyboard ticks (10)'),
            (T5(5.40), 'UI tap'), (T5(6.45), 'Positive ping (inside the delivery area)'), (T5(7.75), 'UI tap'), (T5(8.10), 'Map slide + soft pin settle'),
            (T5(10.05), 'UI tap'), (T5(11.35), 'UI tap (Home chip)'), (T5(11.70), 'Keyboard ticks (5)'), (T5(13.40), 'UI tap (Confirm location)'),
            (T5(14.25), 'Card lock-in: soft click + shimmer')],
 accuracyNotes="""- Location access is optional: SETU's own explainer ('Allow location for SETU?' … 'It is only read when you ask for it.') is shown as a labelled inset beside the phone; 'Use my current location' is ringed but never tapped and no detection result is claimed. Search is the path demonstrated. Do not push in on location/10-picker-select.png: its dimmed background carries a blurred GPS reading from the capture run, an unreadable smudge at identity.
- Search result and zone check are the app's own: 'Nehru Hall of Residence · Pan Loop, IIT Kharagpur…' and 'Location is within the IIT Kharagpur delivery area.' The off-campus refusal is not shown or faked.
- The map shows the real red pin, the faint blue campus-boundary polygon (#0033DA at 0.5 opacity) and the Google attribution; nothing covers them. 'Check the pin' = viewing it; no pin move is claimed or shown.
- Never ring, zoom on or caption 'SETU delivers inside the IIT Kharagpur campus boundary' (picker and map subtitles) or Step 2's lede '…SETU delivers inside the campus area only.' Fconf keeps the map subtitle off-frame; the picker shots stay at identity.
- 'Use this location' returns the unchanged pin to Confirm, so location/13-confirm-search.png is reused honestly. 'Home' is tapped on 13 before the cut to 14-type-room/f0000.
- 'Nehru Hall of Residence, Cricket Ground', 22.319759, 87.298041 and 'B-212' are the real saved values.""",
)

# ---------------------------------------------------------------- s06
scene(
 id='s06', compositionName='your-picks', title='Your picks — and three things SETU does not do', chapter='04 · Your picks', dur=9.85,
 captions=[(0.45, 3.55, 'Pick cuisines you like.\nThey show up first.'),
           (4.40, 7.20, 'Then three things SETU does not do.'),
           (7.30, 9.10, 'Confirm, then “Start ordering”.')],
 onScreenText=[
  ('04 · Your picks', 0.10, 9.70, 'kicker (kit .kicker)'),
  ('SETU never takes your money', 5.10, 7.65, 'kinetic list line (Sora 700 40 px; exact app title; no rupee sign)'),
  ('SETU does not deliver', 5.60, 7.65, 'kinetic list line (Sora 700 40 px; exact app title)'),
  ('SETU approves and records', 6.10, 7.65, 'kinetic list line (Sora 700 40 px; exact app title)'),
 ],
 shots=[
  ('onboarding/23-step2-done.png', 0.0, 1.30, "Frame 0; ring--blue + tap 'Continue' (0.40)."),
  ('onboarding/30-step3.png', 0.75, 2.25, "swapPush in: Step 3 of 4 'What should we show first?'."),
  ('onboarding/31-step3-picked.png', 2.25, 4.95, 'Pixel-aligned; revealed through circular masks at each tapped chip (only those chip rows differ from 30).'),
  ('onboarding/40-step4.png', 4.40, 8.00, "swapPush in (no tap: Step 3's Continue sits below the captured viewport); focus mask on the three titles; rings; kinetic list."),
  ('onboarding/41-step4-ack.png', 7.65, 9.40, "Circular reveal from the tapped switch (toggle on, 'Start ordering' enabled); ring--blue + tap 'Start ordering' (8.60)."),
  ('home/01-first-home.png', 9.40, 9.85, "Revealed by the 'Start ordering' commit wipe: Home with 'Home · Room B-212 · Nehru Hall of Residence'."),
  ('graphic:commit wipe (#0033DA circle from the Start ordering button)', 8.95, 9.70, 'Action → result transition.'),
 ],
 uiState="Onboarding Step 3 of 4 'What should we show first?' (South Indian, Street Food, Chinese selected) → Step 4 of 4 'Three things SETU does not do' → switch 'I understand SETU is a directory and approval gate' on → 'Start ordering' → Home ('Home · Room B-212 · Nehru Hall of Residence', 'Good evening, Aarav').",
 animation="""Local times. Frame 0 = onboarding/23-step2-done.png at identity; the whole scene stays at identity.
0.10 kicker '04 · Your picks' K.fadeUp at (140,200).
0.15 ring--blue on onboarding/23-step2-done.cont. 0.40 K.tap cont ('Continue') → 0.75 K.swapPush → onboarding/30-step3.png (0.55 s).
Chip taps in the capture's order; each 'result' is a layer of onboarding/31-step3-picked.png revealed by clip-path circle(r at x y) growing 0 → 70 px (0.25 s, power2.out) around the tapped chip:
- 1.90 K.tap onboarding/31-step3-picked.southIndian (centre (148.4,584.7)) → 2.25 reveal (Step 3 has read for 0.6 s since its push ended at 1.30).
- 2.55 K.tap 'Street Food', measured box {x:209,y:568,w:100,h:34} (centre (259,585)) → 2.90 reveal.
- 3.20 K.tap 'Chinese', measured box {x:90,y:396,w:77,h:34} (centre (128.5,413)) → 3.55 reveal.
3.80 set the 31 layer fully visible (no visible change: only those chip rows differ).
4.40 K.swapPush → onboarding/40-step4.png (0.55 s; no tap is drawn because Step 3's Continue is below the captured viewport).
5.00–5.35 focus mask fades in: an SVG (390×844, inside the screen) filled rgba(8,12,32,.55) with three feathered rounded holes around onboarding/40-step4.fact1, .fact2 and .fact3 (each padded 8 px). It keeps every card's sub-line — including fact 3's licence sentence — and the switch's 'Required. Recorded…' line dim. 7.65–8.00 it fades out.
Kinetic list in the left column (Sora 700 40 px white, each line led by a Lucide icon 34 px stroke 2 #B8C7FF: wallet / bike / shield-check; fromTo y 24/opacity 0 → 0/1, expo.out 0.5 s), each with an orange ring on its title in the phone:
- 5.10 'SETU never takes your money' at (140,330); ring onboarding/40-step4.fact1 5.10–7.30.
- 5.60 'SETU does not deliver' at (140,400); ring .fact2 5.60–7.30.
- 6.10 'SETU approves and records' at (140,470); ring .fact3 6.10–7.30.
7.30–7.65 the three lines fade out (each held ≥1.2 s).
7.10 ring--blue on the switch, measured box {x:313,y:622,w:46,h:27}. 7.30 K.tap the switch (centre (336,635)) → 7.65 circular reveal of onboarding/41-step4-ack.png from (336,635), r 0 → 280 (0.35 s): the switch turns on and 'Start ordering' becomes active.
8.05 ring--blue on onboarding/41-step4-ack.start. 8.60 K.tap start ('Start ordering') → 8.95 commit wipe: a #0033DA circle (inside the screen) grows from the button centre (255.8,742.7) to cover the whole screen (0.45 s, power2.in); 9.40 home/01-first-home.png is set underneath and the circle fades (0.3 s, done 9.70).
9.35–9.70 the kicker fades out. 9.70–9.85 hold on Home.""",
 transitionIn='Continuous: Step 2 (filled) is on screen at identity.',
 transitionOut="'Start ordering' → blue commit wipe → Home, settled at identity.",
 handoffIn=handoff(screen='onboarding/23-step2-done.png', notes='Same frame as s05 ends.'),
 handoffOut=handoff(screen='home/01-first-home.png', notes='Home (day one, address set) at identity; wipe circle, mask, list and kicker gone.'),
 demoBadge=[],
 soundCues=[(0.40, 'UI tap'), (0.75, 'Page push'), (1.90, 'Chip tap (pitch 1)'), (2.55, 'Chip tap (pitch 2)'), (3.20, 'Chip tap (pitch 3)'),
            (4.40, 'Page push'), (5.10, 'Low tick'), (5.60, 'Low tick'), (6.10, 'Low tick'), (7.30, 'Toggle click'),
            (8.60, 'UI tap (Start ordering)'), (8.95, 'Blue wipe swoosh into Home')],
 accuracyNotes="""- Chips are tapped in the capture's order (South Indian, Street Food, Chinese); 30-step3 and 31-step3-picked differ only in those chip rows, so the circular reveals composite two real captures. The taps are a quick multi-select (0.65 s apart); the beat after the last chip is 0.6 s.
- Step 4's three titles are quoted exactly. The focus mask keeps 'Every seller listed here cleared a licence check…' and 'Required. Recorded against your account with today's date.' dim; never ring, zoom on or caption them (the acknowledgement is not stored; not every stall is licence-gated). Fact 1's body ('no checkout … UPI to the seller's own handle') is likewise never featured.
- 'They show up first' = 'Stalls serving these move to the top of the home page'; the liked cuisines also lead the Home tabs (s07).
- No tap is drawn on Step 3's Continue: it is below the captured viewport.""",
)

# ---------------------------------------------------------------- s07
scene(
 id='s07', compositionName='find-and-add', title='Back to tonight — dosa from Southside Tiffins', chapter='05 · Find & add', dur=10.25,
 captions=[(0.20, 2.60, 'Good evening, Aarav.\nTonight: dosa.'),
           (4.00, 6.30, 'Southside Tiffins: approved by SETU.'),
           (6.40, 9.50, 'Tap ADD: one Masala Dosa,\ntwo filter coffees.')],
 onScreenText=[
  ('TONIGHT', 0.40, 2.00, 'tag (tag row at (140,112): Lucide moon + Space Mono 700 18 px caps)'),
  ('05 · Find & add', 0.45, 10.10, 'kicker (kit .kicker)'),
  ('YOUR PICKS FIRST', 0.85, 2.15, 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('Demo environment · sample stalls', 2.00, 7.30, 'honesty note (tag row; Space Mono 700 18 px caps, shown once in the body)'),
  ('Masala Dosa ₹80', 3.75, 7.65, 'dish chip (kit .dish-chip: name Plus Jakarta Sans 700 28 px, price Space Mono 700 26 px #B8C7FF; exact menu line)'),
  ('Ghee Roast Dosa ₹110', 3.90, 6.30, 'dish chip (kit .dish-chip: Plus Jakarta Sans name, Space Mono price; exact menu line)'),
  ('1 × Masala Dosa ₹80', 7.65, 10.25, "order-slip row (kit .dish-chip; '1 ×' Space Mono 700 26 px #EC5A2A, name Plus Jakarta Sans, price Space Mono; exact cart line)"),
  ('2 × Filter Coffee ₹60', 9.45, 10.25, "order-slip row (kit .dish-chip; '2 ×' Space Mono, name Plus Jakarta Sans, price Space Mono; exact cart line)"),
 ],
 shots=[
  ('home/01-first-home.png', 0.0, 2.30, "Frame 0; 'back to tonight' band; ring on the cuisine tabs + YOUR PICKS FIRST; ring--blue + tap search (1.95)."),
  ('graphic:editorial return band (right → left)', 0.0, 0.70, 'Marks the jump back to tonight (no screen change under it).'),
  ('search/01-search-empty.png', 2.30, 2.95, 'swapPush in; the box is auto-focused.'),
  ('search/02-type-dosa/', 2.95, 3.45, "Typing clip, clipSeconds 0.5: 'dosa'.", 0.5),
  ('search/03-results.png', 3.45, 5.35, "Southside Tiffins with 'Masala Dosa ₹80' / 'Ghee Roast Dosa ₹110'; dish chips rise out; tap the stall card (5.00)."),
  ('stall/01-stall.png', 5.35, 7.60, "swapPush in; ring on 'Approved by SETU · you pay the seller directly'; tap Masala Dosa ADD (7.25)."),
  ('stall/02-dosa-added.png', 7.60, 9.15, "Circular reveal at the ADD button (ADD → '− 1 +') + bottom wipe revealing 'View cart'."),
  ('stall/04-coffee.png', 7.60, 9.15, "Pixel-identical to 02 (no swap needed): Filter Coffee ADD (8.45) then '+' (8.80) are tapped on this state."),
  ('stall/05-coffee-two.png', 9.15, 10.25, "Circular reveal at the coffee stepper: '− 2 +'."),
 ],
 uiState="Back to tonight: Home ('Home · Room B-212 · Nehru Hall of Residence', 'Good evening, Aarav', tabs All · Chinese · South Indian · Street Food · Amer…, 'Approved sellers · 13 open now') → Search 'dosa' → Southside Tiffins ('Masala Dosa ₹80', 'Ghee Roast Dosa ₹110') → stall page ('Approved by SETU · you pay the seller directly') → Masala Dosa 1, Filter Coffee 2, 'View cart'.",
 animation=f"""Local times. Frame 0 = home/01-first-home.png at identity; the whole scene stays at identity.
0.00–0.70 return band: the s04 band style (760 px, linear-gradient(270deg,#151E4D,#22307A), 3 px orange leading edge on its LEFT side) sweeps right → left, x 1920 → −760 (power2.inOut 0.7 s); nothing changes under it.
0.40–0.70 tag 'TONIGHT' (Lucide moon 20 px + Space Mono 700 18 px caps) fades in at the tag row (140,112); 1.70–2.00 it fades out. 0.45 kicker '05 · Find & add' K.fadeUp at (140,200).
0.80–2.10 orange ring on the cuisine tabs, measured box {{x:6,y:233,w:378,h:40}} (canvas {bx(None,(6,233,378,40))}) + label 'YOUR PICKS FIRST' (≈246×38) at x 874–1120, y 338–376 from 0.85 to 2.15; leader (1120,357)→(1170,357).
2.00–2.30 note 'Demo environment · sample stalls' (Space Mono 700 18 px caps, #B8C7FF at 80%, a 6 px orange dot first) fades in at the tag row; 7.00–7.30 it fades out.
1.70 ring--blue on home/01-first-home.search. 1.95 K.tap search → 2.30 K.swapPush → search/01-search-empty.png (0.55 s; the box is auto-focused, no tap needed).
2.95 clip layer search/02-type-dosa/ (clipSeconds 0.5; f0000 = 01-search-empty) types 'dosa' 2.95–3.45; 3.45 the clip ends: cut to search/03-results.png (set it visible under the clip layer at 3.45; the filtered results replace the clip's last frame).
3.65–4.85 orange ring on the Southside Tiffins dish lines, measured box {{x:128,y:256,w:236,h:46}} ('Masala Dosa ₹80' / 'Ghee Roast Dosa ₹110').
3.75 dish chip 'Masala Dosa ₹80' (kit .dish-chip with .veg mark; name Plus Jakarta Sans 700 28 px, price in <b> Space Mono 700 26 px #B8C7FF) rises at left 140, top 340: fromTo y +30/opacity 0 → 0/1 (expo.out 0.5 s). 3.90 'Ghee Roast Dosa ₹110' the same at left 140, top 412. They move OUT of the phone; nothing flies in.
4.80 ring--blue on search/03-results.stall. 5.00 K.tap the stall card (centre (195,220.5)) → 5.35 K.swapPush → stall/01-stall.png (0.55 s).
5.95–7.15 orange ring on stall/01-stall.trust ('Approved by SETU · you pay the seller directly'). 6.00–6.30 the 'Ghee Roast Dosa ₹110' chip fades out.
7.00 ring--blue on stall/01-stall.dosaAdd. 7.25 K.tap dosaAdd ('ADD') → 7.60 circular reveal of a stall/02-dosa-added.png layer from (299,611), r 0 → 90 (0.25 s): ADD becomes '− 1 +' (stall/02-dosa-added.stepper); 7.60–7.90 a second 02 layer clipped to the bottom strip (screen y ≥ 790) wipes up from the bottom, revealing 'View cart'; 7.95 set one full 02 layer visible (stall/04-coffee.png is pixel-identical, so it stands for both).
7.65 the Masala Dosa chip gains an orange '1 ×' prefix (Space Mono 700 26 px #EC5A2A, slides in from the left 0.25 s): it now reads '1 × Masala Dosa ₹80', the cart's line.
8.45 K.tap stall/04-coffee.coffeeAdd (Filter Coffee 'ADD', centre (299,362); 0.6 s after the dosa stepper settled); 8.80 K.tap stall/05-coffee-two.plus ('+', centre (327,362)); nothing changes between the two taps (there is no capture of the '1' state). 9.15 circular reveal of stall/05-coffee-two.png from (299,362), r 0 → 80 (0.25 s): '− 2 +'.
9.45 slip row 2 '2 × Filter Coffee ₹60' (same chip style) fromTo y +20/opacity 0 → 0/1 at left 140, top 412 (expo.out 0.4 s). The two chips now form the order slip: wrap them in one element #s07-slip (left 140, top 340, 600×132) so s08 can move them as ONE object.
9.75–10.10 the kicker fades out. 10.10–10.25 hold (slip visible, phone on 05-coffee-two at identity).""",
 transitionIn="Editorial return band (right → left) from day one back to tonight; Home looks the same because Aarav's saved Home is set.",
 transitionOut='Holds on the stall with both items added and the order slip (two cart lines) in the left column — carried into s08.',
 handoffIn=handoff(screen='home/01-first-home.png', notes='Same frame as s06 ends.'),
 handoffOut=handoff(screen='stall/05-coffee-two.png', left='1 × Masala Dosa ₹80 / 2 × Filter Coffee ₹60 (order slip; no kicker, no tag)',
                    overlays="Order slip #sNN-slip: two kit .dish-chip rows in one wrapper at left 140, top 340 (600×132), fully opaque, at rest: row 1 at top 340 '[veg] 1 × Masala Dosa ₹80', row 2 at top 412 '[veg] 2 × Filter Coffee ₹60' ('1 ×'/'2 ×' Space Mono 700 26 px #EC5A2A; names Plus Jakarta Sans 700 28 px white; prices Space Mono 700 26 px #B8C7FF; kit .dish-chip padding 16/24, radius 22).",
                    notes='Phone at identity on stall/05-coffee-two.png; the only canvas element is the order slip.'),
 demoBadge=[],
 soundCues=[(0.0, 'Band whoosh (back to tonight) + light evening swell'), (1.95, 'UI tap'), (2.30, 'Page push'), (2.95, 'Four keyboard ticks'),
            (3.75, 'Two soft pops (dish chips)'), (5.00, 'UI tap'), (5.35, 'Page push'), (7.25, 'ADD tap + soft pop'),
            (8.45, 'UI tap'), (8.80, 'UI tap + tick (× 2)')],
 accuracyNotes="""- Home's header shows the address saved on day one ('Home · Room B-212 · Nehru Hall of Residence'); the liked cuisines lead the tabs (capture order: All, Chinese, South Indian, Street Food…).
- 'Demo environment · sample stalls' appears here once, at the first sight of stalls (repeated only in the end-card fine print).
- Search 'dosa' → Southside Tiffins with 'Masala Dosa ₹80' and 'Ghee Roast Dosa ₹110' (exact). Never ring or zoom on the result rows' '20–20 min' or the stall's '20 min'; no delivery-time claim.
- The stall line is quoted: 'Approved by SETU · you pay the seller directly'. The stall shows 'New' (fresh demo data).
- Coffee: ADD, then '+', then the 2 appears (no capture of the '1' state). stall/04-coffee.png is pixel-identical to 02-dosa-added. stall/03-scroll-menu/ is not used (it snaps back).
- Dish chips and slip rows quote the real menu and cart lines; prices are never set in Sora.""",
)

# ---------------------------------------------------------------- s08
FT, FK = 'Ftotals', 'Fcard'
scene(
 id='s08', compositionName='cart', title='Cart — ₹150, payable to the seller', chapter='06 · Cart', dur=9.3,
 captions=[(0.10, 3.20, 'One stall per order.\nThen tap “View cart”.'),
           (3.30, 6.40, "Items ₹140, plus the stall's\ndelivery charge: ₹10."),
           (6.50, 9.20, '₹150 to the seller.\nNo platform fee.')],
 onScreenText=[
  ('1 × Masala Dosa ₹80', 0.0, 1.90, 'order-slip row carried from s07 (Space Mono count/price, Plus Jakarta Sans name); flies into the cart as one object'),
  ('2 × Filter Coffee ₹60', 0.0, 1.90, 'order-slip row carried from s07 (Space Mono count/price, Plus Jakarta Sans name)'),
  ('06 · Cart', 0.10, 9.15, 'kicker (kit .kicker)'),
  ('ITEM TOTAL ₹140', 3.40, 7.65, "math row: label Space Mono 700 18 px caps + value '₹140' Plus Jakarta Sans 800 64 px"),
  ('+ SELLER DELIVERY CHARGE ₹10', 4.60, 7.65, "math row: label Space Mono 700 18 px caps + value '₹10' Plus Jakarta Sans 800 64 px"),
  ('SET BY THE STALL', 4.70, 5.90, 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('= PAYABLE TO SELLER ₹150', 5.85, 7.65, "math result: label Space Mono 700 18 px caps + value '₹150' Plus Jakarta Sans 800 64 px white"),
  ('₹150', 7.80, 8.85, 'number flight (Plus Jakarta Sans 800, white) from the cart total onto the Confirm card amount'),
 ],
 shots=[
  ('stall/05-coffee-two.png', 0.0, 1.60, "Frame 0 with the order slip; ring--blue + tap 'View cart' (0.70)."),
  ('cart/01-cart.png', 1.05, 8.30, "swapPush in; the slip flies into the item block and dissolves; camera Ftotals; rings on the three total rows; tap 'Review order' (7.40)."),
  ('checkout/01-confirm-cash.png', 7.75, 9.30, "swapPush in ('Confirm order'); camera Ftotals → Fcard; the ₹150 number flight lands on 'AMOUNT PAYABLE TO THE SELLER ₹150'."),
 ],
 uiState="Stall with both items → cart 'Your order · Southside Tiffins' (Masala Dosa ₹80 each × 1 = ₹80; Filter Coffee ₹30 each × 2 = ₹60; DELIVER TO Home · Room B-212 · Aarav Mehta; Item total ₹140; Seller delivery charge ₹10 'Set by the seller, collected by the seller'; Payable to seller ₹150) → 'Confirm order' with 'AMOUNT PAYABLE TO THE SELLER ₹150' and Cash on delivery selected.",
 animation=f"""Local times. Frame 0 = stall/05-coffee-two.png at identity with the order slip from s07 (handoffIn). Framings: Ftotals = {frame(FT)} (canvas of a screen point = (1124.1 + 1.62·x, −387.2 + 1.62·y)); Fcard = {frame(FK)} (canvas = (1125.16 + 1.512·x, 85.24 + 1.512·y)).
0.10 kicker '06 · Cart' K.fadeUp at (140,200).
0.40 ring--blue on stall/05-coffee-two.viewCart. 0.70 K.tap viewCart ('View cart') → 1.05 K.swapPush → cart/01-cart.png (0.55 s).
1.10–1.70 the order slip flies as ONE object (the #sNN-slip wrapper) into the cart's item block cart/01-cart.lines (canvas at identity {bx(None,(18,66.3,354,240))}): translate + scale to ≈0.64 along a gentle arc (expo.inOut 0.6 s), then 1.70–1.90 it dissolves (opacity → 0) as it lands.
1.80–2.70 orange ring on cart/01-cart.lines.
2.40–3.40 K.focus Ftotals (1.0 s).
Left-column math (canvas-level, x 140–700; labels Space Mono 700 18 px caps #B8C7FF; values Plus Jakarta Sans 800 64 px white — never Sora; each value fromTo y 18/opacity 0 → 0/1, expo.out 0.4 s):
- 3.40 'ITEM TOTAL' (top 300) + '₹140' (top 322); orange ring on the Item total row, measured box {{x:26,y:462,w:338,h:30}} (canvas {bx(FT,(26,462,338,30))}) 3.40–4.60.
- 4.60 '+ SELLER DELIVERY CHARGE' (top 410) + '₹10' (top 432); orange ring on the fee row, measured box {{x:26,y:518,w:338,h:56}} (label, sub-label and ₹10; canvas {bx(FT,(26,518,338,56))}) 4.60–5.80; label 'SET BY THE STALL' (≈246×38) at x 846–1092, y 478–516 from 4.70 to 5.90; leader (1092,497)→(1166.2,497).
- 5.70 a 2 px rule draws (x 140–600, y 524, 0.25 s). 5.85 '= PAYABLE TO SELLER' (top 540) + '₹150' (top 562; the two rows above dim to 70%); orange ring on the payable row, measured box {{x:26,y:603,w:338,h:32}} (canvas {bx(FT,(26,603,338,32))}) 5.85–7.15.
7.15 ring--blue on cart/01-cart.review (canvas {bx(FT,(143.8,782,228.2,48))}). 7.40 K.tap review ('Review order') → 7.75 K.swapPush → checkout/01-confirm-cash.png (0.55 s). 7.30–7.65 the math fades out.
7.75–8.65 K.focus Fcard (0.9 s).
7.80–8.65 number flight (canvas-level): a '₹150' (Plus Jakarta Sans 800, white) lifts from the cart's payable value — canvas box (1637.6,601.0)–(1702.4,630.2) under Ftotals — and arcs onto the Confirm card's big amount, landing exactly over its box under Fcard, measured screen {{x:33,y:105,w:108,h:40}} → canvas (1175.1,244.1)–(1338.4,304.5), at 8.65 (font size grows ≈30 → 60 px; expo.inOut, timed with the camera); 8.65–8.85 it dissolves into the real UI.
8.80–9.15 the kicker fades out. 8.85–9.30 hold on checkout/01-confirm-cash.png at Fcard.""",
 transitionIn="Continuous from s07: the order slip is on canvas; the 'View cart' tap starts the chapter.",
 transitionOut='The ₹150 lands on the Confirm card; the camera holds at Fcard for s09.',
 handoffIn=handoff(screen='stall/05-coffee-two.png', left='1 × Masala Dosa ₹80 / 2 × Filter Coffee ₹60 (order slip; no kicker, no tag)',
                   overlays="Order slip #sNN-slip: two kit .dish-chip rows in one wrapper at left 140, top 340 (600×132), fully opaque, at rest: row 1 at top 340 '[veg] 1 × Masala Dosa ₹80', row 2 at top 412 '[veg] 2 × Filter Coffee ₹60' ('1 ×'/'2 ×' Space Mono 700 26 px #EC5A2A; names Plus Jakarta Sans 700 28 px white; prices Space Mono 700 26 px #B8C7FF; kit .dish-chip padding 16/24, radius 22).",
                   notes='Phone at identity on stall/05-coffee-two.png; the only canvas element is the order slip.'),
 handoffOut=handoff(screen='checkout/01-confirm-cash.png', rig_=rigobj(FK), notes='Camera held at Fcard (dark amount card, HOW WILL YOU PAY?, Cash on delivery and Pay by QR in frame); number flight dissolved; math and kicker gone.'),
 demoBadge=[],
 soundCues=[(0.70, 'UI tap (View cart)'), (1.05, 'Page push + soft whoosh (slip into the cart)'), (3.40, 'Number tick'), (4.60, 'Number tick'),
            (5.85, 'Soft resolve tone (= ₹150)'), (7.40, 'UI tap (Review order)'), (7.80, 'Number-flight swish'), (8.65, 'Soft lock-in')],
 accuracyNotes="""- Cart values are exact: items ₹140, 'Seller delivery charge' ₹10 'Set by the seller, collected by the seller', 'Payable to seller' ₹150.
- Each stall sets its own delivery charge (₹0–₹500; the row is hidden at ₹0) — 'the stall's delivery charge' and the label 'SET BY THE STALL' cover that. Never 'free', 'zero cost' or 'minimal'.
- No platform fee or commission exists: payable = items + the stall's own charge.
- One order goes to one stall (adding from another stall replaces the cart).
- The slip and the ₹150 flight link real values and land exactly on the real UI; they never cover app text after landing.
- checkout/03-scroll-summary/ and checkout/04-summary.png are not used (captured with Pay by QR selected; Aarav pays cash).""",
)

# ---------------------------------------------------------------- s09
scene(
 id='s09', compositionName='pay', title='Pay the stall directly — cash, or the stall\'s QR', chapter='07 · Pay', dur=11.95,
 captions=[(0.10, 4.00, "Pay cash at your door,\nor scan the stall's QR."),
           (4.10, 7.60, 'With QR, the stall accepts first,\nthen you pay.'),
           (9.85, 11.85, 'Aarav picks cash: “Place order”.')],
 onScreenText=[
  ('07 · Pay', 0.10, 11.80, 'kicker (kit .kicker; hidden 3.10–9.60 while the QR branch is up)'),
  ('IF YOU PICK QR', 3.30, 9.65, 'kicker-style heading for the side branch (Space Mono 700 22 px caps)'),
  ('DEMO QR · NOT A REAL PAYMENT CODE', 3.40, 9.65, 'demo tag (orange outline pill, Space Mono 700 18 px caps)'),
  ('1 · Stall accepts', 3.90, 9.65, 'step list (Space Mono 700 22 px)'),
  ('2 · You pay · five minutes', 4.80, 9.65, 'step list (Space Mono 700 22 px)'),
  ('3 · Stall confirms', 7.95, 9.65, 'step list (Space Mono 700 22 px)'),
 ],
 shots=[
  ('checkout/01-confirm-cash.png', 0.0, 9.20, "Main phone at Fcard: rings on 'SETU does not collect this…', Cash on delivery and Pay by QR; then shrinks left and dims for the QR branch."),
  ('order-qr/02-pay-qr.png', 2.95, 6.85, "Second phone (default spec, slides in from the right): a separate demo QR order after the stall accepted — 'Pay to continue', countdown, the stall's labelled DEMO QR; tap 'I've paid' (6.25)."),
  ('order-qr/04-payment-review.png', 6.60, 8.10, "swapFade: 'Seller is checking your payment' (held 1.25 s)."),
  ('order-qr/05-payment-confirmed.png', 7.85, 9.65, "swapFade (the stall's confirmation): 'Order confirmed', 'The stall confirmed your payment.'; the second phone exits right."),
  ('order-cash/00-confirm.png', 9.20, 11.60, "Main phone back at the default spec (identical to checkout/01 except the button shade); ring Cash; tap 'Place order · ₹150' (10.80)."),
  ('order-cash/01-placed.png', 11.60, 11.95, "Revealed by the 'Place order' commit wipe: 'Waiting for the seller'."),
  ('graphic:commit wipe (#0033DA circle from the Place order button)', 11.15, 11.90, 'Action → result transition.'),
 ],
 uiState="'Confirm order': AMOUNT PAYABLE TO THE SELLER ₹150 · 'SETU does not collect this. Southside Tiffins receives it directly.'; HOW WILL YOU PAY? Cash on delivery 'Hand ₹150 to the seller at your door.' / Pay by QR 'Southside Tiffins's QR appears here once they accept. You will have five minutes to pay…'. Side branch on a second phone (separate demo QR order CE1013-VGKQ): accepted → 'Pay to continue' with the stall's DEMO QR and countdown → 'Seller is checking your payment' → 'Order confirmed' / 'The stall confirmed your payment.'. Back on Aarav's phone: Cash on delivery → 'Place order · ₹150' → 'Waiting for the seller'.",
 animation=f"""Local times. Frame 0 = checkout/01-confirm-cash.png with the main rig at Fcard = {frame(FK)} (canvas of a screen point = (1125.16 + 1.512·x, 85.24 + 1.512·y)). Fsplit = {{s 0.7407, P [195,422], T [346.4,497.9]}} puts the main phone at x 180–513, y 150–846 (= spec {{left:180, top:150, k:0.8}}).
0.10 kicker '07 · Pay' K.fadeUp at (140,200).
0.20–1.20 orange ring on 'SETU does not collect this. Southside Tiffins receives it directly.', measured box {{x:33,y:162,w:270,h:36}} (canvas {bx(FK,(33,162,270,36))}).
1.00–2.10 orange ring on checkout/01-confirm-cash.cash (canvas {bx(FK,(18,260,354,70))}).
1.90–3.00 orange ring on checkout/01-confirm-cash.qr (canvas {bx(FK,(18,340,354,102))}).
2.90–3.70 split: K.focus main rig Fcard → Fsplit (0.8 s, expo.inOut); a kit .dim layer inside the main screen fades to opacity 1 (rgba(8,12,32,.55)). 3.10–3.40 the kicker fades out.
2.95–3.65 the QR phone — a second kit .phone at the default spec {{left:1150,top:70,k:1.08}} with its own screen, outside the main rig — fromTo x +800 → 0 (opacity 1 throughout; expo.out 0.7 s) showing order-qr/02-pay-qr.png.
Branch type in the middle column (x 560–1110, canvas-level): 3.30 'IF YOU PICK QR' (kit .kicker) at (560,250); 3.40 tag 'DEMO QR · NOT A REAL PAYMENT CODE' (orange 2 px outline pill, Space Mono 700 18 px caps, ≈450×38) at (560,296).
Step list (Space Mono 700 22 px white, numerals #EC5A2A; a Lucide check (#19B36B, 22 px) appears at a row's left when it is reached):
- 3.90 '1 · Stall accepts' at (560,390), checked at once; orange ring on the QR phone's thread line 'Order confirmed by Southside Tiffins', measured box {{x:40,y:74,w:310,h:22}}, 3.90–5.10.
- 4.80 '2 · You pay · five minutes' at (560,450); orange rings on order-qr/02-pay-qr.timer 4.80–5.80 and order-qr/02-pay-qr.qrImg 5.10–6.10 (its own 'DEMO QR · Not a real payment code' label stays legible).
6.00 ring--blue on order-qr/02-pay-qr.paid. 6.25 K.tap paid ('I've paid') → 6.60 K.swapFade → order-qr/04-payment-review.png (0.25 s); row 2 gets its check; 6.90–7.95 orange ring on order-qr/04-payment-review.headline ('Seller is checking your payment'; the screen holds 1.25 s).
7.85 K.swapFade → order-qr/05-payment-confirmed.png (0.25 s; the stall's confirmation, no customer tap). 7.95 '3 · Stall confirms' at (560,510) with its check; 8.15–9.15 green ring on order-qr/05-payment-confirmed.qrCard ('The stall confirmed your payment.').
9.15–9.65 the QR phone exits right (x → +800, expo.in 0.5 s); 9.25–9.65 heading, tag and step list fade out.
9.20–10.00 K.focus main rig Fsplit → identity (0.8 s, expo.inOut); the dim fades out; at 9.20 the main screen's still is swapped to order-cash/00-confirm.png under the dim (identical layout; only the button shade differs). 9.60 the kicker fades back in.
10.05–10.85 orange ring on the Cash on delivery card (same box as checkout/01-confirm-cash.cash; canvas at identity {bx(None,(18,260,354,70))}).
10.55 ring--blue on order-cash/00-confirm.place (canvas {bx(None,(18,782,354,48))}). 10.80 K.tap place ('Place order · ₹150') → 11.15 commit wipe: a #0033DA circle grows from the button centre (195,806) to cover the screen (0.45 s, power2.in); 11.60 order-cash/01-placed.png is set underneath and the circle fades (0.3 s, done 11.90).
11.50–11.80 the kicker fades out. 11.90–11.95 hold.""",
 transitionIn='Continuous from s08: the camera is already framing the amount card and the payment options (Fcard).',
 transitionOut="'Place order · ₹150' → blue commit wipe → 'Waiting for the seller', settled at identity.",
 handoffIn=handoff(screen='checkout/01-confirm-cash.png', rig_=rigobj(FK), notes='Same frame as s08 ends: camera at Fcard, nothing on canvas.'),
 handoffOut=handoff(screen='order-cash/01-placed.png', notes="Order thread 'Waiting for the seller' at identity; the second phone, branch type, wipe and kicker are gone."),
 demoBadge=[],
 soundCues=[(1.00, 'Ring swish (cash)'), (1.90, 'Ring swish (QR)'), (2.90, 'Dual-phone slide whoosh'), (4.80, 'Soft timer tick'),
            (6.25, "UI tap (I've paid)"), (7.85, 'Soft confirm ping (stall confirms)'), (9.15, 'Whoosh out'), (10.80, 'UI tap (Place order)'),
            (11.15, 'Warm confirm swell into the order')],
 accuracyNotes="""- Cash copy is quoted ('Hand ₹150 to the seller at your door.'); the dark card line 'SETU does not collect this. Southside Tiffins receives it directly.' is the app's.
- QR order of events: the stall accepts first, then its own QR appears in the order thread with a five-minute window; 'I've paid' → 'Seller is checking your payment' → the stall confirms ('The stall confirmed your payment.'). Never 'pay first' or 'QR at checkout'. Order status and payment status stay separate in copy.
- The QR is the labelled demo QR (it encodes a plain sentence, not a UPI address); its in-capture 'DEMO QR · Not a real payment code' stays legible and our tag repeats it; nothing implies money moved.
- The QR phone is a separate demo order (CE1013-VGKQ), framed as 'if you pick QR'; Aarav's order (CE1013-BCQK) continues with cash.
- No pickup option exists and nothing suggests one.""",
)

# ---------------------------------------------------------------- s10
FH = 'Fhand'
scene(
 id='s10', compositionName='track-handover', title='Track it, then hand over cash and the code', chapter='08 · Track & hand over', dur=12.0,
 captions=[(0.20, 3.40, 'Now follow along:\nconfirmed, cooking, on the way.'),
           (5.40, 8.60, 'At the door, Aarav pays ₹150 in cash.'),
           (8.70, 11.80, 'Then he tells them his code.\nOrder complete.')],
 onScreenText=[
  ('08 · Track & hand over', 0.10, 11.90, 'kicker (kit .kicker)'),
  ('TIME-LAPSE', 0.20, 5.40, 'tag (tag row at (140,112): Lucide fast-forward + Space Mono 700 18 px caps)'),
  ('STATUS TIMELINE · NOT A MAP', 0.20, 11.90, 'rail header (Space Mono 700 18 px caps, #B8C7FF)'),
  ('Placed · Confirmed · Preparing · Ready · Out for delivery · Delivered', 0.20, 11.90, "status rail rows (Plus Jakarta Sans 600 28 px; the progress view's exact labels)"),
  ('HANDOVER CODE', 6.90, 8.10, 'label (short caps, Space Mono 700 18 px, callout lane)'),
 ],
 shots=[
  ('order-cash/01-placed.png', 0.0, 1.45, "Frame 0 ('Waiting for the seller')."),
  ('order-cash/02-accepted.png', 1.20, 2.65, "swapFade: 'Order confirmed' (the prep time is not featured)."),
  ('order-cash/04-preparing.png', 2.40, 3.85, "swapFade: 'Being cooked now'."),
  ('order-cash/06-ready.png', 3.60, 5.05, "swapFade: 'Ready'."),
  ('order-cash/07-on-the-way-code.png', 4.80, 8.55, "swapFade: 'On the way' + handover panel; camera Fhand; rings on 'Please pay ₹150 in cash' and the six-digit code."),
  ('order-cash/08-cash-confirmed.png', 8.30, 11.85, "swapFade (the stall confirmed the cash): green 'The stall has confirmed your ₹150 cash payment'; code + 'Now tell them this code — that completes your order.'"),
  ('order-cash/09-delivered-review.png', 11.30, 12.00, "swapSheet (sheetTop 412): 'Delivered' with the review sheet rising; camera back to identity."),
  ('graphic:status rail (the app\'s six progress labels)', 0.20, 11.90, 'Left-column motion graphic lit in sync with each status change.'),
 ],
 uiState="Aarav's cash order thread: 'Waiting for the seller' → 'Order confirmed' ('Being prepared · usually ready by 7:24 pm') → 'Being cooked now' → 'Ready' → 'On the way' with the handover panel ('Please pay ₹150 in cash', six-digit code, 'Then tell this code to the stall owner or the delivery partner — that completes your order. SETU staff will never ask for it.') → 'The stall has confirmed your ₹150 cash payment' / 'Now tell them this code — that completes your order.' → 'Delivered' (review sheet rises).",
 animation=f"""Local times. Frame 0 = order-cash/01-placed.png at identity. Camera framing Fhand = {frame(FH)} (canvas of a screen point = (1121.98 + 1.836·x, −476.75 + 1.836·y)).
0.10 kicker '08 · Track & hand over' K.fadeUp at (140,200).
0.20–0.50 tag 'TIME-LAPSE' (Lucide fast-forward 20 px + Space Mono 700 18 px caps, #B8C7FF pill) fades in at the tag row (140,112); 5.10–5.40 it fades out. It covers the whole status run (the real order spanned 7:02 → 7:25 pm).
0.20–0.80 status rail (canvas-level, left column): header 'STATUS TIMELINE · NOT A MAP' (Space Mono 700 18 px caps, #B8C7FF) at (150,290); a 2 px rgba(255,255,255,.35) line from (162,352) to (162,667) drawn top → bottom (K.drawPath 0.6 s); six rows, 14 px dots at x 162 and labels (Plus Jakarta Sans 600 28 px) at x 192: Placed (y 352), Confirmed (415), Preparing (478), Ready (541), Out for delivery (604), Delivered (667). Future rows 35% white; the current row has an orange dot and a white label; done rows white with a filled pale dot.
Status run (in-place K.swapFade 0.25 s; each change is the stall's action, so no taps; every state is held 1.2 s), with a 0.6 s orange ring flash on that capture's .headline and the matching rail row lighting:
- 0.40 'Placed' current (01-placed).
- 1.20 → order-cash/02-accepted.png, 'Confirmed'.
- 2.40 → order-cash/04-preparing.png, 'Preparing'.
- 3.60 → order-cash/06-ready.png, 'Ready'.
- 4.80 → order-cash/07-on-the-way-code.png, 'Out for delivery'.
5.10–6.10 K.focus Fhand (1.0 s): the handover panel fills the frame.
6.10–7.30 orange ring on 'Please pay ₹150 in cash', measured box {{x:25,y:455,w:340,h:34}} (canvas {bx(FH,(25,455,340,34))}).
6.80–8.00 ring--blue on order-cash/07-on-the-way-code.code (canvas {bx(FH,(25,498.8,340,48))}) + label 'HANDOVER CODE' (≈209×38) at x 880–1089, y 464–502 from 6.90 to 8.10 (both gone before the 8.30 swap moves the code 18 px down); leader (1089,483)→(1167.9,483).
8.30 K.swapFade → order-cash/08-cash-confirmed.png (0.25 s; the stall tapped 'Yes, cash received'; its panel sits 18 px lower, the camera stays).
8.60–9.80 green ring on 'The stall has confirmed your ₹150 cash payment', measured box {{x:25,y:473,w:340,h:34}} (canvas {bx(FH,(25,473,340,34))}).
9.60–11.10 orange ring on order-cash/08-cash-confirmed.code (canvas {bx(FH,(25,517,340,48))}) and on 'Now tell them this code — that completes your order.', measured box {{x:25,y:576,w:310,h:18}}. 9.80–11.10 three concentric 2 px pale arcs (radii 20/34/48 px, opening left, centred at canvas (1080,516) in the callout lane, clear of the bezel) ripple once each, 0.35 s apart: the code is said out loud.
11.10–11.90 K.unfocus (0.8 s).
11.30 K.swapSheet → order-cash/09-delivered-review.png (sheetTop 412, 0.55 s; the stall entered the right code — no customer tap); the rail's 'Delivered' row lights with a soft orange flash.
11.55–11.90 the rail and the kicker fade out. 11.90–12.00 hold at identity.""",
 transitionIn="Continuous from s09's commit wipe: 'Waiting for the seller' at identity.",
 transitionOut="The review sheet rises over 'Delivered'; settled at identity for the cut.",
 handoffIn=handoff(screen='order-cash/01-placed.png', notes='Same frame as s09 ends.'),
 handoffOut=handoff(screen='order-cash/09-delivered-review.png', notes="'Delivered' with the review sheet up ('How was Southside Tiffins?') at identity; rail, tag, label and kicker gone."),
 demoBadge=[],
 soundCues=[(0.40, 'Status tick (Placed)'), (1.20, 'Tick + soft chime (Confirmed)'), (2.40, 'Tick (Preparing)'), (3.60, 'Tick (Ready)'),
            (4.80, 'Tick (Out for delivery) + light whoosh'), (6.80, 'Code shimmer'), (8.30, 'Soft ping (cash confirmed)'),
            (9.80, 'Two soft voice-arc pulses'), (11.30, 'Sheet slide + gentle success chord (Delivered)')],
 accuracyNotes="""- Status headlines are the app's own ('Waiting for the seller', 'Order confirmed', 'Being cooked now', 'Ready', 'On the way'); the rail uses the progress view's labels (Placed, Confirmed, Preparing, Ready, Out for delivery, Delivered).
- The TIME-LAPSE tag is on for the whole status run: the real order took 7:02 → 7:25 pm. 'Being prepared · usually ready by 7:24 pm' is a prep target — shown in the capture, never featured or narrated; no delivery-time promise.
- Tracking is a status timeline in the order thread, not a map ('STATUS TIMELINE · NOT A MAP' paraphrases Step 4's 'You will see a status timeline, not a rider on a map.'). No live map or location tracking anywhere.
- Handover order is real: cash first ('Please pay ₹150 in cash' → 'The stall has confirmed your ₹150 cash payment'), then the code completes it ('Now tell them this code — that completes your order.'). 'Them' = the stall owner or the delivery partner, as the app says.
- The handover code in 07/08 is 806688 as captured; never type it into captions or overlays; don't alter the captured times.""",
)

# ---------------------------------------------------------------- s11
scene(
 id='s11', compositionName='rate-report', title='Delivered, rated — and reportable', chapter='09 · Rate & report', dur=7.1,
 captions=[(0.10, 2.50, 'Delivered. Five stars\nfor Southside Tiffins.'),
           (2.60, 5.40, 'Something off? Report it\nfrom the order.'),
           (5.60, 6.95, 'Dinner, sorted.')],
 onScreenText=[
  ('09 · Rate & report', 0.10, 7.05, 'kicker (kit .kicker)'),
  ('TO CAMPUS STAFF', 4.30, 5.50, 'label (short caps, Space Mono 700 18 px, callout lane)'),
 ],
 shots=[
  ('order-cash/09-delivered-review.png', 0.0, 1.30, "Frame 0: 'How was Southside Tiffins?'; tap the 5th star (0.60)."),
  ('order-cash/10-review-5.png', 0.95, 3.25, "Circular reveal from the 5th star: five stars, 'Excellent'; tap 'Submit review' (2.45)."),
  ('order-cash/12-review-sent.png', 2.80, 6.20, "The sheet slides down: thread ends 'Delivered · handover code verified · ₹150 paid in cash'; ring 'Report'; tap the progress icon (5.55)."),
  ('order-cash/13-progress-delivered.png', 5.90, 7.10, 'swapFade: the progress view with all six steps and their real times; green ring.'),
 ],
 uiState="Delivered order: review sheet 'How was Southside Tiffins?' (1 × Masala Dosa · 2 × Filter Coffee) → 5 stars 'Excellent' → 'Submit review' → thread ends 'Delivered · handover code verified · ₹150 paid in cash' with 'Report' / 'Order again' → progress view (Placed 7:02 pm … Delivered 7:25 pm).",
 animation=f"""Local times. Frame 0 = order-cash/09-delivered-review.png at identity; the scene stays at identity (no push on the review sheet, so its note placeholder is never featured).
0.10 kicker '09 · Rate & report' K.fadeUp at (140,200).
0.35 ring--blue on the 5th star, measured box {{x:292,y:514,w:36,h:36}} (inside order-cash/09-delivered-review.stars). 0.60 K.tap the 5th star (centre (310,532)) → 0.95 circular reveal of order-cash/10-review-5.png from (310,532), r 0 → 330 (0.35 s): five stars fill and 'Excellent' appears.
1.35–2.35 orange ring on order-cash/10-review-5.word ('Excellent').
2.20 ring--blue on order-cash/09-delivered-review.submit. 2.45 K.tap submit ('Submit review') → 2.80 the sheet closes: order-cash/12-review-sent.png sits underneath; the 10 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 432px 0)) fades out (0.35 s) while its sheet part (clip-path inset(412px 0 0 0)) slides y 0 → +432 (expo.in 0.45 s).
3.30–4.40 orange ring on 'Delivered · handover code verified · ₹150 paid in cash', measured box {{x:14,y:484,w:362,h:32}}.
4.20–5.40 orange ring on the 'Report' button, measured box {{x:18,y:720,w:170,h:48}} (canvas {bx(None,(18,720,170,48))}) + label 'TO CAMPUS STAFF' (≈234×38) at x 886–1120, y 795–833 from 4.30 to 5.50; leader (1120,814)→(1183.4,880) — the label stays above the caption zone.
5.35 ring--blue on order-cash/12-review-sent.progress (the clipboard icon). 5.55 K.tap progress → 5.90 K.swapFade → order-cash/13-progress-delivered.png (0.3 s).
6.25–6.70 green ring on order-cash/13-progress-delivered.card (fades by 7.05).
6.75–7.05 the kicker fades out. 7.05–7.10 hold.""",
 transitionIn='Continuous: the review sheet is already up.',
 transitionOut='The completed progress view holds at identity; s12 opens by pulling the phone back.',
 handoffIn=handoff(screen='order-cash/09-delivered-review.png', notes='Same frame as s10 ends.'),
 handoffOut=handoff(screen='order-cash/13-progress-delivered.png', notes='Progress view (six steps with real times) at identity; rings, label and kicker gone.'),
 demoBadge=[],
 soundCues=[(0.60, 'Star tap: rising five-note arpeggio'), (2.45, 'UI tap (Submit review)'), (2.80, 'Sheet slides down'),
            (3.30, 'Soft confirm ping'), (4.20, 'Ring swish (Report)'), (5.55, 'UI tap'), (5.90, 'Page fade')],
 accuracyNotes="""- Review copy: 'How was Southside Tiffins?'; five stars → 'Excellent'; 'Submit review'. The note is optional, 'Don't ask again' exists, and a rating can be given later from Orders.
- 11-review-note.png is not used (its note says 'On time.'); the camera never features the note placeholder ('Hot, on time…'): the scene stays at identity.
- 'Delivered · handover code verified · ₹150 paid in cash' is the app's own line.
- 'Report' exists on ended orders; reports go to SETU campus staff as a record against the stall (not a refund claim against SETU) — the label says only 'TO CAMPUS STAFF'.
- The progress view's 'Delivered' row shows a clock icon in the app; nothing redraws it.
- 'Dinner, sorted.' is story copy, not a product claim.""",
)

# ---------------------------------------------------------------- s12
DISCLAIMER = ('SETU connects customers with approved campus food providers. Food preparation, delivery and payment are handled by the '
              'respective provider. SETU does not collect payments or independently guarantee food hygiene.')
scene(
 id='s12', compositionName='end-card', title='End card', chapter=None, dur=8.2,
 captions=[],
 onScreenText=[
  ('Your campus. Your food. Your SETU.', 0.80, 8.20, "tagline (Sora 800 64 px, centred; 'Your SETU.' in #B8C7FF; no rupee sign)"),
  ('Explore SETU Food', 1.20, 8.20, 'CTA pill (Plus Jakarta Sans 700 30 px #0033DA on white, Lucide arrow-right)'),
  (DISCLAIMER, 1.50, 8.20, 'disclaimer (verbatim; Plus Jakarta Sans 500 26 px; fully legible 1.95–8.20 = 6.25 s)'),
  ('Demo environment · sample stalls · demo QR, not a real payment code', 1.70, 8.20, 'fine print (Space Mono 400 18 px, 60% white)'),
 ],
 shots=[
  ('order-cash/13-progress-delivered.png', 0.0, 0.80, 'The phone pulls back (scale 1 → 0.72, sinks 60 px) and fades out.'),
  ('graphic:real campus boundary outline, faint (assets/data/campus-boundary.json)', 0.20, 8.20, 'Redraws at 18% opacity behind the type; the Nehru Hall point glows once.'),
  ('graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)', 0.40, 8.20, 'Tile 240×190 centred at (960,215); lockup 200 px wide, never recoloured.'),
  ('graphic:end-card type (tagline, CTA, disclaimer, fine print)', 0.80, 8.20, 'Kinetic type only.'),
 ],
 uiState='No app UI after 0.80 s: end-card motion graphics.',
 animation="""Local times. Frame 0 = order-cash/13-progress-delivered.png at identity. No captions in this scene (layout.json lists it as centred anyway); keep y 880–1050 empty.
0.00–0.80 the phone recedes: fromTo scale 1 → 0.72 (transform-origin its centre, canvas (1374.6,539.8)), y 0 → +60, opacity 1 → 0 (expo.in 0.8 s).
0.20–1.20 the real campus outline (assets/data/campus-boundary.json path) redraws centred, 960 px wide: x 480–1440, y 260–756; stroke #B8C7FF 2 px at 18% opacity (K.drawPath 1.0 s). 1.00–1.60 the Nehru Hall point (canvas (589.6,354.8)) glows once (8 px orange dot, opacity 0 → 1 → 0.6).
0.40–1.00 white tile (kit .white-tile, 240×190, radius 32) centred at (960,215) → x 840–1080, y 120–310, with assets/brand/setu-logo.png at 200 px wide, centred: fromTo scale 0.94/opacity 0 → 1/1 (expo.out 0.6 s).
0.80 tagline 'Your campus. Your food. Your SETU.' (Sora 800 64 px, white, centred, top 350; 'Your SETU.' in #B8C7FF) K.revealWords (stagger 0.06).
1.20 CTA pill 'Explore SETU Food' (white, radius 999, padding 16/30, Plus Jakarta Sans 700 30 px #0033DA, Lucide arrow-right 26 px) centred, top 460: fromTo scale 0.9/opacity 0 → 1/1 (back.out(1.6) 0.5 s).
1.50–1.95 the disclaimer (verbatim) fades up: Plus Jakarta Sans 500 26 px / 1.45, rgba(255,255,255,.88), centred, max-width 1200 px (3 lines), top 580 (≈ y 580–693).
1.70–2.00 fine print 'Demo environment · sample stalls · demo QR, not a real payment code' (Space Mono 400 18 px, rgba(255,255,255,.6), centred, top 760) fades in.
After 2.00 nothing moves. Hold the complete card to 8.20 (no fade to black).""",
 transitionIn='The phone recedes into the indigo as the campus outline redraws faintly.',
 transitionOut='Hold to the last frame (no fade) so the owner can add sound or an outro.',
 handoffIn=handoff(screen='order-cash/13-progress-delivered.png', notes='Same frame as s11 ends.'),
 handoffOut=handoff(phone='none', overlays='End card (final frame): faint campus outline with the Nehru Hall dot, lockup tile, tagline, CTA pill, disclaimer and fine print.',
                    notes='Last frame of the film.'),
 demoBadge=[],
 soundCues=[(0.0, 'Pad swell resolves'), (0.40, 'Brand sting placeholder (owner\'s choice)'), (1.20, 'Soft pop (CTA)'), (8.0, 'Pad tail out')],
 accuracyNotes=f"""- The disclaimer is verbatim: '{DISCLAIMER}' It is fully legible from 1.95 s to the end (6.25 s), with no caption competing.
- Tagline 'Your campus. Your food. Your SETU.' and CTA 'Explore SETU Food' are exactly as briefed; the CTA is type in a pill, not a store badge or link.
- The lockup is the official raster on a white rounded tile, downscaled only, never recoloured; the 75-years mark is not used.
- The fine print repeats the demo-environment note (shown once in the body, s07) and the demo-QR note.
- No 'free', no claims about other platforms.""",
)

# ---------------------------------------------------------------- assemble
def words(t):
    return len(t.split())

scenes_out = []
t0 = 0.0
for s in SCENES:
    start = round(t0, 3); end = round(t0 + s['dur'], 3)
    g = lambda v: round(start + v, 3)
    caps = [{'start': g(a), 'end': g(b), 'text': txt} for a, b, txt in s['captions']]
    narration = ' '.join(c['text'].replace('\n', ' ') for c in caps)
    shots = []
    for sh in s['shots']:
        d = {'file': sh[0], 'start': g(sh[1]), 'end': g(sh[2]), 'treatment': sh[3]}
        if len(sh) > 4: d['clipSeconds'] = sh[4]
        shots.append(d)
    scenes_out.append({
        'id': s['id'], 'compositionName': s['compositionName'], 'title': s['title'], 'chapter': s['chapter'],
        'start': start, 'end': end, 'narration': narration, 'captions': caps,
        'onScreenText': [{'text': a, 'start': g(b), 'end': g(c), 'role': r} for a, b, c, r in s['onScreenText']],
        'shots': shots, 'uiState': s['uiState'], 'animation': s['animation'],
        'transitionIn': s['transitionIn'], 'transitionOut': s['transitionOut'],
        'handoffIn': s['handoffIn'], 'handoffOut': s['handoffOut'],
        'demoBadge': [{'start': g(a), 'end': g(b)} for a, b in s['demoBadge']],
        'soundCues': [{'at': g(a), 'cue': c} for a, c in s['soundCues']],
        'accuracyNotes': s['accuracyNotes'],
    })
    t0 += s['dur']
# One shared object per boundary: scene N+1's handoffIn IS scene N's handoffOut (all fields but notes were authored on both sides; check them).
for a_, b_ in zip(scenes_out, scenes_out[1:]):
    ho, hi = a_['handoffOut'], b_['handoffIn']
    diff = [k for k in set(ho) | set(hi) if k != 'notes' and ho.get(k) != hi.get(k)]
    assert not diff, (a_['id'], b_['id'], diff)
    b_['handoffIn'] = json.loads(json.dumps(ho))
total = round(t0, 3)
wc = sum(words(x['narration']) for x in scenes_out)
print('total', total, 'words', wc)
ANGLE = """STORY-FIRST ('Dinner at B-212'): one evening with Aarav (Nehru Hall of Residence, Room B-212). Tonight he signs in on a new phone with an emailed one-time code (DEMO-labelled; the password stays the main way in). A band wipe rewinds to his day one to show how a first-timer creates an account and runs the four onboarding steps — that is how 'Home · B-212' was saved inside the campus boundary. A second band wipe returns to tonight: 1 × Masala Dosa + 2 × Filter Coffee from Southside Tiffins; items ₹140 + the stall's own delivery charge ₹10 = ₹150 payable to the seller. The stall's QR route is a labelled side branch (the stall accepts first, then you pay, then it confirms). Aarav pays cash at the door, his six-digit handover code completes the order, he rates it five stars, and the Report path is pointed out. Nine numbered chapters (01 Sign in … 09 Rate & report) keep first-timers oriented, and captions name the exact button where it helps. Tone: warm, plain, lightly playful ('Tonight: dosa.', 'Dinner, sorted.'), never hype; 'students, faculty, staff' is said once. Motif: the real campus-boundary polygon opens the film, returns as the delivery-area check and closes the end card.
GLOBAL SYSTEM (every scene):
- Frame: 1920×1080, 60 fps, silent. One HyperFrames sub-composition per scene with one paused GSAP timeline; kit.js helpers plus plain GSAP only. Scene roots are transparent over the shared indigo background from index.html (it already carries a faint drifting campus outline; never paint a background).
- Boundaries are HARD CUTS: frame 0 must equal handoffIn and the last frame must equal handoffOut. Unless a handoff says otherwise: phone at the default spec, rig identity, left column empty, no overlays, the named capture fully visible and settled.
- Phone: kit .phone at phoneSpec {left:1150, top:70, k:1.08}; screen origin canvas (1164,84), 421.2×911.5. At identity a screen point (x,y) is canvas (1164 + 1.08·x, 84 + 1.08·y). The phone, its capture layers and every in-screen overlay (rings, taps, reveals, halos, masks) live inside the scene rig (.rig, transform-origin 0 0). Camera = K.focus(tl, rig, K.toCanvas(spec, P[0], P[1]), s, t, dur, {to:{x:T[0], y:T[1]}}), expo.inOut, 0.8–1.2 s; framings are given as {s, P (screen px), T (canvas px)} and K.unfocus returns to identity. Canvas-level type, labels, leader lines, chips and tags sit OUTSIDE the rig; every canvas position in a spec already accounts for the rig state at that moment.
- Grid: text column x140–820 (kicker at (140,200), headline top 250, nothing below y 860); callout lane x840–1130 (label right edge ≤1120); right margin x1620–1880 (unused); one tag row at (140,112) for ONE tag at a time (DEMO badge, DAY ONE, TONIGHT, the sample-stalls note, TIME-LAPSE); caption zone x120–1140, y880–1050 stays empty (captions centred only in s01; s12 has none). At most 4 floating labels/chips/tags at once, never overlapping the phone, each other, the text column or the caption zone.
- Type: kicker = kit .kicker showing the scene's `chapter`, K.fadeUp at 0.10 and faded out ≥0.3 s before the scene ends. Headline = .headline--md (Sora 800, 68 px), words only. Sora has no ₹ glyph: every string containing ₹ is set in Plus Jakarta Sans (names, amounts) or Space Mono (labels, prices, counts). Labels = short caps tags: .callout.callout--dark with font 700 18px/1 Space Mono, letter-spacing .08em, uppercase, padding 10px 16px (≈ 12.24 px × chars + 50 px wide, 38 px tall), plus a 2 px rgba(184,199,255,.7) straight leader from the label's right edge to the element; a label's right edge stays ≥8 px left of the phone's bezel for the framing in use (identity ≤1140; s 1.4 ≤1097; Ftotals ≤1095; Fhand ≤1090; Fconf ≤1087). Tag-row items: Space Mono 700 18 px caps, letter-spacing .16em, pill padding 10/16; the DEMO badge is kit .demo-badge with the text 'Demo environment'.
- Overlays on real UI: K.tap at the centre of the named box, always 0.35 s before the screen change it causes (inside the 0.25–0.45 s rule). K.ring orange = look here; {blue:true} = the next tap target (≥0.2 s before the tap); green = a kit ring with border-color #19B36B and a green glow, used only for 'inside the delivery area', 'cash confirmed', 'payment confirmed' and the final progress card. Boxes are CSS px of the 390×844 screen: named marks from marks.json written <group>/<shot>.<mark>, or explicit {x,y,w,h} measured on the final PNGs. Nothing opaque over app text; UI is never recoloured.
- Screen changes: K.swapPush = forward navigation (0.55 s); K.swapSheet = sheets (sheetTop given); K.swapFade = in-place state change (0.15–0.35 s); circular reveal = a local state change caused by a tap (the 'after' capture as a new layer whose clip-path circle(r at x y) grows from 0 at the tap point, 0.25–0.35 s, power2.out); commit wipe = for 'Start ordering' and 'Place order · ₹150' a #0033DA circle grows from the button centre to cover the screen (0.45 s, power2.in), the next capture is set underneath, then the circle fades (0.3 s).
- Clips: play inside a non-timed .layer in the screen (data-hf-media-start-basis="local"); never animate the <video>; the next still sits underneath to hold the last frame; chained clips start exactly where the previous ends. clipSeconds = the length used (a speed variant is pre-rendered; each captured frame gets clipSeconds / frames).
- Rhythm: tap → result → ≥0.6 s beat; text that matters is held ≥1.2 s; exits 0.3–0.5 s; nothing is visible before its entrance (fromTo with opacity 0); no drifting, spinning, particles or glitch.
- Icons: Lucide line icons only (stroke 1.85–2.5); no emoji, food photos, clip-art or filled pins.
- Honesty: only real captures for app screens; DEMO badge across the whole OTP portion (code request → Home); the sample-stalls note once (s07) plus the end-card fine print; the demo QR stays labelled; no 'SETU delivers', pickup, map or location tracking, delivery-time promise, free/zero-cost/minimal-charge wording or competitor names anywhere. Never ring, zoom on or caption the app's own 'SETU delivers inside…' lines, Step 4's licence and 'Recorded…' sub-lines, search rows' '20–20 min', the stall's '20 min', the prep time or the review note placeholder."""

final = {
    'title': 'Dinner at B-212 — a SETU Food walkthrough',
    'angle': ANGLE,
    'totalSeconds': total,
    'wordCount': wc,
    'phoneSpec': {'left': 1150, 'top': 70, 'k': 1.08},
    'scenes': scenes_out,
}
layout = {
    'captionCenter': ['s01', 's12'],
    'notes': ('Captions are drawn only by compositions/captions.html (generated from scene-timing.json). Default plate: bottom-left (kit .cap--left: x 140, bottom 74, width 880) — '
              'scene builders keep x 120–1140, y 880–1050 empty. Centred plate (kit .cap--center, bottom 64) in s01 (full-screen hook) and s12 (end card, which has no captions: '
              'the disclaimer must have the frame to itself); those scenes keep y 900–1050 empty across the whole width. Camera push-ins keep the phone at x ≥ ~1120, so a '
              'pushed phone never sits under a left caption plate. A "\\n" in a caption is the intended line break (one plate per line).'),
}
if '--write' in sys.argv:
    with open(OUT + '/scene-timing.json', 'w', encoding='utf-8') as fh:
        json.dump(final, fh, ensure_ascii=False, indent=2); fh.write('\n')
    with open(OUT + '/layout.json', 'w', encoding='utf-8') as fh:
        json.dump(layout, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print('wrote', OUT)
