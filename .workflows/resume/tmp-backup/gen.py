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
  ('SETU Food', 1.70, 5.35, 'title (Sora 800, 84 px, white, centred under the lockup tile; no rupee sign)'),
  ('ON SETU SERVICES · IIT KHARAGPUR', 2.10, 5.35, 'subline (Space Mono 700, 18 px caps, #B8C7FF, centred)'),
  ('Aarav · Room B-212', 3.85, 5.35, 'persona chip beside the Nehru Hall pin (Space Mono 700, 20 px)'),
 ],
 shots=[
  ('graphic:real campus boundary outline (assets/data/campus-boundary.json) with the Nehru Hall pin', 0.0, 5.4,
   'Motion graphic from real data: the 78-point Main Campus Boundary path drawn 1000×516.4 at canvas (460,150); orange outline map-pin on the file\'s nehruHall point.'),
  ('graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)', 1.4, 5.4,
   'Tile 260×206 centred at (960,360); lockup 216 px wide, downscaled only, never recoloured.'),
  ('graphic:hook type (SETU Food title, subline, persona chip)', 1.7, 5.4, 'Kinetic type only; the product is named by ≈2.6 s.'),
 ],
 uiState='No app UI: motion graphics built from real data (campus boundary polygon and its Nehru Hall point) plus the official SETU lockup.',
 animation=f"""Local times. Full-screen motion graphic, no phone. Captions are CENTRED in this scene (layout.json), so keep y 880–1050 empty across the width. The hook names the product early: 'SETU Food' is fully readable by ≈2.6 s.
Outline group (#s01-map): the real 'Main Campus Boundary' path from assets/data/campus-boundary.json (viewBox 0 0 1000 516.4) as an inline SVG 1000×516.4 at left 460, top 150 (x 460–1460, y 150–666). Stroke #B8C7FF 3 px, round joins, filter drop-shadow(0 0 10px rgba(130,160,255,.55)); fill rgba(46,91,238,.06) (starts at fill-opacity 0).
0.10–1.40 K.drawPath on the outline (1.3 s, power2.inOut). 0.90–1.50 the fill fades in.
1.00 Nehru Hall marker at the file's nehruHall point (114.2, 98.8) → canvas (574.2, 248.8): a Lucide map-pin (OUTLINE, stroke 2.5 px #EC5A2A, 40 px tall, tip on the point) fromTo y −60/opacity 0 → 0/1 (expo.out 0.45 s), plus an 8 px orange dot exactly on the point; 1.25–1.95 one 2 px orange ripple ring grows 0→80 px and fades.
1.40–2.10 the outline group tweens to opacity 0.30 (power2.out); the pin and dot stay at 100%.
1.40 white tile (kit .white-tile, 260×206, radius 32) centred at (960,360) → x 830–1090, y 257–463, holding assets/brand/setu-logo.png at 216 px wide (≈170 px tall), centred: fromTo scale 0.94/opacity 0 → 1/1 (expo.out 0.7 s).
1.70 title 'SETU Food' (Sora 800, 84 px, white, letter-spacing −.03em, centred, top 492) K.revealWords (stagger 0.08; 'Food' is fully in at ≈2.58).
2.10 subline 'ON SETU SERVICES · IIT KHARAGPUR' (Space Mono 700 18 px caps, letter-spacing .2em, #B8C7FF, centred, top 600) K.fadeUp.
3.85 persona chip 'Aarav · Room B-212' (Space Mono 700 20 px, white on rgba(12,18,51,.88), 1 px rgba(255,255,255,.18) border, radius 12, padding 10/16; ≈300×42) at left 604, top 196 (right of the pin head, clear of the tile): fromTo x −16/opacity 0 → 0/1 (expo.out 0.5 s).
4.95–5.35 exit: tile, title, subline and chip rise −16 px and fade (power2.in 0.4 s); outline, pin and dot fade (0.4 s). The frame at 5.35–5.40 is the empty shared background.""",
 transitionIn='Cold open on the shared indigo background; the outline starts drawing at 0.10 s.',
 transitionOut='Every hook element exits 4.95–5.35; the last frame is the empty background (hard cut; s02 starts empty).',
 handoffIn=handoff(phone='none', notes='Cold open: only the shared background (index.html) is visible.'),
 handoffOut=handoff(phone='none', notes='All hook graphics are gone by 5.35; empty background at the cut.'),
 demoBadge=[],
 soundCues=[(0.0, 'Placeholder bed: low warm pad fades in (owner replaces)'), (0.10, 'Fine line-draw shimmer following the outline (1.3 s)'),
            (1.00, 'Pin drop: short wooden tick'), (1.40, 'Soft paper tick as the white logo tile lands'),
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
   "Kit .laptop frame (--lk .7, no browser/OS chrome) at left 760, top 150. Camera on the laptop rig: lede, then the stats row; rings; then a move that centres the desktop's selected Customer card over the phone's Customer card for the dissolve."),
  ('signin/01-signin.png', 5.75, 6.6, 'Phone at the default spec fades in over the aligned desktop form (web → phone dissolve) and holds.'),
 ],
 uiState="Signed-out web sign-in page (desktop wide layout, Customer selected): art panel 'The campus, and only the campus.', the lede 'Approved local stakeholders, delivered to your hall. …' and the stats 'DELIVERY' over 'Campus only', 'COMMISSION' over 'None', 'PAYMENT' over 'Direct'; then the phone's own sign-in screen ('SIGNING IN AS' over 'Customer', 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY').",
 animation="""Local times. Two layers: #s02-rig-desk (a full-canvas .rig) holds the laptop; the phone is OUTSIDE it at the default spec and only appears at the end.
Laptop at rest: kit .laptop with --lk .7 showing desktop/01-signin-wide.png (an <img> filling .lscreen) at left 760, top 150 → lid x 760–1804, y 150–824; screen x 778–1786, y 168–798; base y 824–846. Desktop CSS (1440×900) → canvas at rest: X = 778 + 0.7·x, Y = 168 + 0.7·y. Rings below are drawn inside the laptop screen in desktop CSS px, so they scale with the camera.
0.00–0.80 the laptop fromTo y +90/opacity 0 → 0/1 (expo.out 0.8 s). 0.15 kicker 'What SETU does' K.fadeUp at (140,200).
0.70–1.70 camera: K.focus(desk rig, P=(1052.4,497) [desktop (392,470)], s 1.3, 0.70, 1.0, {to:{x:1110,y:420}}) — headline and lede fill the frame; the lid's bottom edge lands at y≈845, above the caption zone.
0.90–2.30 pale-indigo ring (2.5 px #B8C7FF, radius 10, no fill) around the first sentence only: desktop box {x:60,y:500,w:464,h:34} 'Approved local stakeholders, delivered to your hall.'
2.10–3.10 camera: K.focus(desk rig, P=(1026.5,736.4) [desktop (355,812)], s 1.35, 2.10, 1.0, {to:{x:1080,y:520}}) — the stats row lands at y≈495–546.
2.60–3.80 orange ring (kit .ring look, inside the laptop screen) on the stat 'DELIVERY' over 'Campus only', desktop {x:58,y:778,w:216,h:68}; one ring scale pulse 1→1.04→1 (the UI is never recoloured).
3.80–5.00 orange ring on the stat 'COMMISSION' over 'None', desktop {x:318,y:778,w:110,h:68}.
4.10–5.20 orange ring on the stat 'PAYMENT' over 'Direct', desktop {x:543,y:778,w:110,h:68}.
5.10–5.90 dissolve set-up: K.focus(desk rig, P=(1559.2,334.6) [desktop (1116,238): the top-centre of the selected Customer card, measured box {x:896,y:238,w:440,h:84}], s 1.1, 5.10, 0.8, {to:{x:1374.6,y:306.5}}) — the desktop Customer card now sits centred on the phone's Customer card (signin/01-signin.customer, top at screen y 206) with the top edges aligned and the same height (64.7 vs 64.8 px; widths 338.8 vs 386.6 px). Lid x 495.5–1643.7, y 103.4–844.8, base bottom y 869 (s 1.1 is the largest scale that keeps the laptop above the caption zone). 5.10–5.40 the kicker fades out.
5.75–6.15 the phone (default spec {left:1150,top:70,k:1.08}, outside the desk rig) fromTo scale 0.97/opacity 0 → 1/1 (transform-origin centre, expo.out 0.4 s) showing signin/01-signin.png; 5.85–6.20 the laptop fades out (power1.in 0.35 s). This is a near-size DISSOLVE, not a pixel match: the Customer cards coincide, while the headings differ (left-aligned on the web, centred on the phone).
6.20–6.60 hold: phone at the default spec on signin/01-signin.png; the laptop is invisible (reset the desk rig to identity once it is at opacity 0); left column empty.""",
 transitionIn='Starts on the empty background; the laptop rises 0.00–0.80.',
 transitionOut='Web → phone dissolve on the shared sign-in form (Customer cards centred and top-aligned, 5.10–6.20), then a 0.4 s settled hold on the phone.',
 handoffIn=handoff(phone='none', notes='Empty shared background (s01 has fully exited).'),
 handoffOut=handoff(screen='signin/01-signin.png', notes='Laptop fully gone; phone at the default spec, no camera move, nothing else on canvas.'),
 demoBadge=[],
 soundCues=[(0.0, 'Card settle: soft low thud as the laptop rises'), (0.90, 'Highlight swish (lede ring)'), (2.60, 'Tiny tick (Campus only)'),
            (3.80, 'Tiny tick (None)'), (4.10, 'Tiny tick (Direct)'), (5.10, 'Glassy whoosh on the web → phone dissolve')],
 accuracyNotes="""- desktop/01-signin-wide.png is real UI shown in the kit's neutral laptop frame: no browser chrome, URL bar or OS UI.
- Ring only 'Approved local stakeholders, delivered to your hall.' and the three stats. Never ring, zoom on or caption 'SETU checks the licence and holds the record.' (it reads as 'every stall is licence-checked').
- desktop/02-home-web.png is not used ('Every stall is licence-checked by SETU').
- 'They cook and deliver' = the stalls (app: 'The seller brings the order themselves'); never 'SETU delivers'. 'No commission' = the stat 'COMMISSION' over 'None'.
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
  ('Demo environment', 5.20, 10.20, 'DEMO badge (kit .demo-badge, tag row at (140,112))'),
  ('DEMO · Local test inbox', 6.40, 9.65, 'mail-card head strip (orange-outline DEMO tag + Space Mono 700 16 px)'),
 ],
 shots=[
  ('signin/01-signin.png', 0.0, 1.55, 'Phone at the default spec; camera F1 from 0.30; ring on the campus pill; tap id at 1.20.'),
  ('signin/02-type-email/', 1.55, 3.11, "Typing clip, clipSeconds 1.56: 'aarav.demo@kgpian.iitkgp.ac.in' into the id field.", 1.56),
  ('signin/03-email-typed.png', 3.11, 6.50, 'Still under the clip, then held (deliberate focus-loss cut at 3.11: the clip ends with the field focused, the still has it unfocused): ring password + MAIN WAY IN; ring--blue + tap otpLink (5.60); pushes out 5.95–6.50.'),
  ('signin/04-enter-code.png', 5.95, 7.60, "swapPush in; ring sentTo ('We emailed a six-digit code to aa***@kgpian.iitkgp.ac.in. It expires in 10 minutes.')."),
  ('signin/email-otp.png', 6.40, 9.65, 'DEMO mail card in the left column: the real email render cropped to email CSS x12–378, y24–420 inside a white card under a DEMO head strip; code-box glow; light trails to the phone.'),
  ('signin/05-type-code/', 7.60, 8.80, 'Typing clip, clipSeconds 1.2 (7 frames × 0.1714 s): the six digits, synced to the light trails.', 1.2),
  ('signin/06-code-entered.png', 8.80, 9.90, "Still under the clip, then held; ring--blue + tap 'Verify and continue' (9.25)."),
  ('signin/07-home.png', 9.60, 10.60, "swapFade in ('Good evening, Aarav', 'Set your delivery location'); camera back to identity."),
 ],
 uiState="Signed-out phone sign-in (Customer selected, 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY') → email typed → 'Enter the code' (sent to aa***@kgpian.iitkgp.ac.in, 'It expires in 10 minutes.') → six digits entered → Home on a fresh device ('Set your delivery location' over 'Tap to pick it on the map'; 'Good evening, Aarav').",
 animation=f"""Local times. Phone at the default spec from frame 0 (handoffIn). Camera framing F1 = {frame('F1')}: header logos (screen y<100) stay off-frame, so the crest and the 75-years mark are never magnified; visible screen y≈104–818; canvas of a screen point = (1125.16 + 1.512·x, −156.86 + 1.512·y).
0.10 kicker '01 · Sign in' K.fadeUp at (140,200). 0.30 headline 'Password,' / 'or a code.' (.headline--md, top 250, width 680; 'or a code.' in #B8C7FF) K.revealWords.
0.30–1.30 K.focus F1 (1.0 s).
0.60–2.20 orange ring (radius 14) on the campus pill, measured box {{x:52,y:164,w:286,h:27}} 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY' → canvas {bx('F1', (52,164,286,27))}.
1.20 K.tap signin/01-signin.id → 1.55 clip layer signin/02-type-email/ (clipSeconds 1.56) plays 1.55–3.11; signin/03-email-typed.png sits underneath and holds from 3.11 — a deliberate focus-loss cut (the clip's last frame has the id field focused with a blue border, the still has it unfocused; the next action, the password ring, follows at 3.30).
3.30–4.60 orange ring on signin/01-signin.password (same layout in 03; canvas {bx('F1', (16,472.6,358,48))}) + label 'MAIN WAY IN' (≈187×38) at x 905–1092, y 575–613 from 3.35; 2 px leader (1092,594)→(1149,594); 4.70–5.00 the label fades.
4.45 ring--blue on signin/03-email-typed.otpLink (canvas {bx('F1', (75.7,578.6,238.6,40))}) until 5.60. 4.55 label 'OR EMAIL A CODE' (≈236×38) at x 856–1092, y 729–767; leader (1092,748)→(1239,748); 5.85–6.20 it fades.
5.20–5.45 DEMO badge (kit .demo-badge 'Demo environment') fades up at the tag row (140,112) — fully visible before the code is requested (5.60) and until Home is reached.
5.60 K.tap signin/03-email-typed.otpLink ('Email me a one-time code instead') → 5.95 K.swapPush → signin/04-enter-code.png (0.55 s). 5.70–6.10 the headline fades out.
7.00–7.70 orange ring on signin/04-enter-code.sentTo (canvas {bx('F1', (16,206.1,358,40))}; fades 7.70–8.05) — it starts only once the 'DEMO · Local test inbox' card is fully in, so 'We emailed…' never reads without its DEMO context.
6.40–7.00 DEMO mail card (kit .mailcard, width 480) at left 590, top 200: head strip 52 px = orange-outline 'DEMO' tag + 'Local test inbox' (Space Mono 700 16 px; no sender, no time, no OS or mail-app chrome); body = signin/email-otp.png cropped to email CSS x12–378, y24–420 at 1.3115× (480×519; card bottom ≈771). Entrance fromTo x −40/opacity 0/rotate 1.5° → 0/1/0 (expo.out 0.6 s). Email CSS → canvas: X = 590 + (x−12)·1.3115, Y = 252 + (y−24)·1.3115.
7.20–7.80 pale-blue glow ring around the email's code box (signin/email-otp.codeBox {{x:36,y:210,w:318,h:70}} → canvas x 621.5–1038.5, y 495.9–587.7).
{n(CLIP0)} clip layer signin/05-type-code/ (clipSeconds 1.2; 7 frames × 0.1714 s; f0000 = the empty boxes of 04). Digits appear at {', '.join(n(t,3) for t in digit_t)}; the clip ends at 8.80 and signin/06-code-entered.png holds underneath.
Light trails: one per digit, a 1.5 px pale-blue line drawn with K.drawPath (0.16 s, power2.out) from the card digit to its phone box (F1 canvas), finishing exactly as that digit appears, then fading in 0.2 s; never two drawing at once. From → to and timing: {trail_lines}. As each trail leaves, that digit on the card brightens.
8.90 ring--blue on signin/06-code-entered.verify. 9.25 K.tap verify ('Verify and continue') → 9.60 K.swapFade → signin/07-home.png (0.3 s). 9.25–9.65 the mail card exits left (x −60, fade, power2.in 0.4 s).
9.60–10.50 K.unfocus (0.9 s): the camera returns to identity as Home settles (the header 'Set your delivery location' comes into frame).
9.90–10.20 the DEMO badge fades out (Home is fully shown at 9.90). 10.00–10.30 the kicker fades out. 10.50–10.60 hold.""",
 transitionIn='Continuous from the web → phone dissolve: the phone is already at its default spec on the sign-in screen.',
 transitionOut="Settles on fresh-device Home at identity with the left column empty; s04's rewind band opens on this frame.",
 handoffIn=handoff(screen='signin/01-signin.png', notes='Same frame as s02 ends: phone at the default spec, nothing else.'),
 handoffOut=handoff(screen='signin/07-home.png', notes="Camera back at identity; DEMO badge, mail card, kicker and labels gone. Home reads 'Set your delivery location' (fresh device)."),
 demoBadge=[(5.45, 9.90)],
 soundCues=[(0.60, 'Ring swish (campus accounts)'), (1.55, 'Quiet keyboard ticks for 1.5 s'), (5.60, 'UI tap'), (5.95, 'Page push swish'),
            (6.40, 'Gentle chime: DEMO mail card (not an OS notification sound)'), (7.77, 'Six soft digit ticks, 0.17 s apart'),
            (9.25, 'UI tap (Verify and continue)'), (9.60, 'Success: soft two-note rise')],
 accuracyNotes="""- Password sign-in is the main method; the emailed one-time code is the alternative ('Email me a one-time code instead'). The caption names both and the labels say exactly that.
- The code really was emailed, by the isolated demo stack to a local test inbox (Mailpit). The DEMO badge is fully visible from 5.45 — before the 5.60 tap that requests the code — until Home is shown (9.90), and the card's head strip says 'Local test inbox'. The sentTo ring waits until that card is fully in (7.00). Nothing implies a real inbox received it: no sender, timestamp, app icon or OS notification styling.
- The card shows the real email render (header 'SETU Food', 'Your sign-in code', the code, 'It expires in 10 minutes … and works once.', 'Never share this code. SETU staff will never ask you for it.'). Digits 686713 match in signin/email-otp.png and signin/06-code-entered.png; never retype or invent digits; keep the masked address as captured.
- 'For IIT Kharagpur campus accounts: students, faculty, staff.' is the approved audience line; the UI pill reads 'IIT KHARAGPUR CAMPUS ACCOUNTS ONLY' (no UI string names faculty or staff, so the line is anchored to campus accounts).
- F1 keeps the crest row off-frame; the 75-years mark is never enlarged.
- signin/07-home.png ('Set your delivery location') is the real fresh-device state; it sets up the flashback.""",
)

# ---------------------------------------------------------------- s04
scene(
 id='s04', compositionName='new-here', title='New here? Create a customer account', chapter='02 · New here?', dur=10.0,
 captions=[(0.10, 2.80, "New here? Rewind to Aarav's day one."),
           (2.90, 6.85, 'Create a Customer account:\nname, institute email, phone, password.'),
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
  ('onboarding/07-signup-filled.png', 6.60, 8.10, "Still under the clips ('Strong enough.'; deliberate focus-loss cut at 6.60); ring--blue + tap 'Create account' (7.20)."),
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
2.80 K.tap onboarding/02-signup-empty.name → 3.15 the typing clips play back-to-back in one non-timed layer stack, each starting on the frame where the previous one ends (the field-to-field focus changes are in the captures, so no extra taps are drawn): onboarding/03-type-name/ 3.15–3.77 (0.62), onboarding/04-type-email/ 3.77–5.33 (1.56), onboarding/05-type-phone/ 5.33–5.89 (0.56), onboarding/06-type-password/ 5.89–6.60 (0.71); onboarding/07-signup-filled.png holds underneath from 6.60 — a deliberate focus-loss cut (the clip ends with the password field focused, the still has it unfocused; the next action, the 'Create account' ring, follows at 6.95).
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
- The second caption describes the form ('Create a Customer account: name, institute email, phone, password.') rather than the tap, because the 'Create a Customer account' tap (1.30) happens under the first caption; the button itself is ringed blue before it is tapped.
- Typing is real (four clips at ≈0.76× of their base length; no keyboard is added); the password shows masked dots only.
- Step 1's line about what stakeholders see is visible but not featured (not in the verified facts).
- Demo persona data only (Aarav Mehta, aarav.demo@kgpian.iitkgp.ac.in, 9000012345).""",
)

# ---------------------------------------------------------------- s05
FC = 'Fconf'
_pin0 = under(FOC[FC], 346, 363)                     # the Delivery-location field's pin icon under Fconf
_card_pt = (300.0, 470.0)
_tt = (_pin0[0] - 1090) / (_pin0[0] - _card_pt[0])
_trail0 = (1090.0, _pin0[1] + _tt * (_card_pt[1] - _pin0[1]))   # where the straight flight crosses x 1090 (left of the bezel)
_zy = under(FOC[FC], 0, 469 + 17 / 2)[1]             # zoneOk centre line under Fconf
_zx = under(FOC[FC], 55, 0)[0]
_bpt = under(FOC[FC], 91.3, 440)                     # a point on the map's faint boundary line
INS = lambda x, y: (420 + (x - 20) * 1.08, 300 + (y - 276) * 1.08)   # allow-dialog crop → canvas (inset at 1.08×)
_nn0 = INS(42, 471.5); _nn1 = INS(42 + 147.8, 471.5 + 48)
scene(
 id='s05', compositionName='delivery-spot', title='Where should orders arrive?', chapter='03 · Delivery spot', dur=16.05,
 captions=[(0.10, 3.60, 'Next: where should orders arrive?\nLocation access is optional.'),
           (3.70, 5.30, 'Search works too.'),
           (5.40, 8.20, 'Nehru Hall: inside the delivery area.'),
           (8.30, 10.65, 'Check the pin on the map.'),
           (10.75, 13.40, 'Save it as Home, add B-212.')],
 onScreenText=[
  ('03 · Delivery spot', 0.10, 15.95, 'kicker (kit .kicker)'),
  ('OPTIONAL', 0.25, 2.20, 'label chip on the explainer inset (Space Mono 700 18 px caps, orange outline)'),
  ('CAMPUS ONLY', 6.75, 8.05, 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('CAMPUS BOUNDARY', 8.70, 10.00, 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('Home · B-212', 14.00, 15.95, 'address card title (Plus Jakarta Sans 700 32 px; our summary of two real values, not app copy)'),
  ('Nehru Hall of Residence', 14.00, 15.95, 'address card subline (Plus Jakarta Sans 500 22 px, #B8C7FF)'),
 ],
 shots=[
  ('onboarding/21-step2-prompt.png', 0.0, 2.90, "Identity; pale ring on 'Use my current location' (never tapped) beside the explainer inset; ring--blue + tap the Delivery location box (2.05); covered by the picker sheet 2.40–2.90."),
  ('location/01-allow-dialog.png', 0.25, 2.20, "INSET outside the phone: crop CSS {x:20,y:276,w:350,h:293} (SETU's own 'Allow location for SETU?' explainer) at the phone's own scale 1.08× (378×316) in a white card at x 420–798, y 300–616; labelled OPTIONAL; orange ring on 'Not now' only; no tap; dashed leader to the GPS row."),
  ('location/10-picker-select.png', 2.40, 4.05, "swapSheet (sheetTop 537) — 'Select a location'; identity framing keeps the sheet subtitle tiny; tap search (3.50); the clip layer fades in over it 3.85–4.05."),
  ('location/11-type-search/', 3.85, 4.65, "Typing clip, clipSeconds 0.8: the expanded sheet, 'Nehru Hall' typed.", 0.8),
  ('location/12-search-results.png', 4.65, 6.25, "Results ('Nehru Hall of Residence' over 'Pan Loop, IIT Kharagpur…' first); ring--blue + tap the first result (5.60); fades out 5.95–6.25."),
  ('location/13-confirm-search.png', 5.95, 8.65, "'Confirm delivery location'; camera Fconf; green ring on 'Location is within the IIT Kharagpur delivery area.'; tap 'Adjust on the map' (7.95); the map fades in over it 8.30–8.65."),
  ('location/20-map.png', 8.30, 10.05, "'Select delivery location' map at Fconf (s 1.8 at screen y 575, raised 32 px): the sheet subtitle is off-frame; pin halo; boundary label; tap 'Use this location' (9.35)."),
  ('location/13-confirm-search.png', 9.70, 11.20, "Back on Confirm (the map hands the same pin back); ring--blue + tap the 'Home' chip (10.65); the clip layer fades in over it 11.00–11.20."),
  ('location/14-type-room/', 11.00, 11.80, "Typing clip, clipSeconds 0.8: f0000 has Home selected (sheet 25 px lower), then 'B-212' into Address details.", 0.8),
  ('location/15-confirm-home.png', 11.80, 13.50, "Still under the clip (identical to its last frame); rings; tap 'Confirm location' (12.70); the sheet closes 13.05–13.50."),
  ('onboarding/23-step2-done.png', 13.05, 16.05, 'Revealed as the sheet closes; pin → address card; ring on the filled box; camera back to identity.'),
  ('graphic:pin → address card (Lucide outline map-pin, dotted trail left of the bezel, glass card)', 13.45, 15.95, "Action → result: the field's pin flies out and unfolds into the saved-address card; the trail is drawn only on the canvas left of the phone."),
 ],
 uiState="Onboarding Step 2 of 4 'Where should orders arrive?' (inset: SETU's own explainer 'Allow location for SETU?' with 'Not now' / 'Allow location') → 'Select a location' picker → search 'Nehru Hall' → 'Confirm delivery location' ('Location is within the IIT Kharagpur delivery area.') → map 'Select delivery location' (red pin, faint blue campus-boundary line, Google attribution) → back to Confirm → SAVE AS Home + ADDRESS DETAILS 'B-212' → 'Confirm location' → Step 2 filled ('Nehru Hall of Residence, Cricket Groun…', 22.319759, 87.298041, Room B-212, Home).",
 animation=f"""Local times. Frame 0 = onboarding/21-step2-prompt.png at identity. Camera framing Fconf = {frame(FC)} (A's map framing, raised 32 px): visible screen y≈303–844, and the phone's bottom bezel shows at canvas y≈1051–1076; canvas of a screen point = (1120.92 + 1.944·x, −589.8 + 1.944·y). It keeps every 'SETU delivers inside the IIT Kharagpur campus boundary' subtitle (map: screen y 226–258) and every Confirm sheet title (13: y≈259–277; 14-type-room and 15: y≈284–302) off-frame. The picker and search shots stay at identity, where their subtitle is tiny.
0.10 kicker '03 · Delivery spot' K.fadeUp at (140,200).
0.25–0.65 explainer inset: a white card (radius 24, shadow 0 30px 80px rgba(0,0,0,.45)) holding location/01-allow-dialog.png cropped to CSS {{x:20,y:276,w:350,h:293}} at the phone's own scale 1.08× (378×316.4, so nothing in it is magnified relative to the app) at left 420, top 300 (x 420–798, y 300–616.4): fromTo scale 0.94/opacity 0 → 1/1 (back.out(1.4) 0.4 s). Crop CSS → canvas: X = 420 + (x−20)·1.08, Y = 300 + (y−276)·1.08. With it, label chip 'OPTIONAL' (orange 2 px outline, Space Mono 700 18 px caps, ≈148×38) at (420,250) fades up, and a dashed leader (2 px rgba(184,199,255,.7), 6/6 dash) draws from the card's right edge (798,458) to the GPS row's left edge (1181.3,596.7) (K.drawPath 0.35–0.75).
0.35–1.75 pale ring (GLOBAL ring vocabulary: context, never a tap target) on onboarding/21-step2-prompt.gps ('Use my current location'), fading 1.75–2.10; it is never tapped.
0.75–1.80 orange ring (radius 30; drawn in the inset card, canvas-level) on location/01-allow-dialog.notNow ('Not now'): canvas x {n(_nn0[0],1)}–{n(_nn1[0],1)}, y {n(_nn0[1],1)}–{n(_nn1[1],1)} (pad 6): the choice is optional. Nothing marks the dialog's body text: never ring, underline, zoom or caption '…to find nearby stalls…' or 'It is only read when you ask for it.' (the code contradicts both).
1.90–2.20 inset, label, leader and ring fade out (0.3 s; the inset was settled 0.65–1.90 = 1.25 s).
1.85 ring--blue on onboarding/21-step2-prompt.box. 2.05 K.tap box (centre (195,361.7)) → 2.40 K.swapSheet → location/10-picker-select.png (sheetTop 537, 0.5 s).
3.30 ring--blue on location/10-picker-select.search (pad 12). 3.50 K.tap search → 3.85 K.swapFade (0.2 s) → clip layer location/11-type-search/ (clipSeconds 0.8; f0000 = the sheet expanded to the top with the field focused) 3.85–4.65; 4.65 the clip ends: cut to location/12-search-results.png (set it visible under the clip layer at 4.65; its results list differs from the clip's last frame).
4.85 ring--blue on location/12-search-results.first ('Nehru Hall of Residence' over 'Pan Loop, IIT Kharagpur, Kharagpur, West Be…'). 5.60 K.tap first → 5.95 K.swapFade (0.3 s) → location/13-confirm-search.png (the sheet shrinks to 'Confirm delivery location'). The results were readable 4.65–5.95 (1.3 s).
6.00–7.00 K.focus Fconf (1.0 s).
6.65–7.95 green ring on location/13-confirm-search.zoneOk (canvas {bx(FC, (55,469,292,17))}) + label 'CAMPUS ONLY' (≈185×38) at x 900–1085, y {n(_zy-19,1)}–{n(_zy+19,1)}, in 6.75 (0.3 s), out 7.75–8.05; leader (1085,{n(_zy,1)})→({n(_zx,1)},{n(_zy,1)}).
7.75 ring--blue on the 'Adjust on the map' row, measured box {{x:18,y:684,w:354,h:66}}. 7.95 K.tap location/13-confirm-search.adjust (centre (205.5,708)) → 8.30 K.swapFade (0.35 s) → location/20-map.png (no layer movement: at Fconf both sheet tops are off-frame and the blurred page behind them is the same).
8.65–9.45 pin halo: two 2 px orange rings grow from the map pin's tip (screen (195,456); pin head (195,433); canvas tip {pt(FC,195,456)}) to r 36 CSS px, 0.5 s each, 0.3 s apart.
8.70–10.00 label 'CAMPUS BOUNDARY' (≈234×38) at x 852–1086, y {n(_bpt[1]-19,1)}–{n(_bpt[1]+19,1)} (in 0.3 s; out 9.70–10.00); leader (1086,{n(_bpt[1],1)})→{pt(FC,91.3,440)} — the faint blue boundary line on the map passes through screen (91.3,440) (it runs ≈(164.7,330)→(18.6,549)). The Google logo and 'Map data ©2026' strip (screen y 566–588) stay unobstructed.
9.15 ring--blue on location/20-map.useThis (canvas {bx(FC, (183.5,782,188.5,48))}). 9.35 K.tap useThis ('Use this location') → 9.70 K.swapFade (0.35 s) → location/13-confirm-search.png. The map was fully visible 8.65–9.70 (the shortened round trip).
10.40 ring--blue on location/13-confirm-search.home (the 'Home' chip). 10.65 K.tap home (centre (63,538)) → 11.00 K.swapFade (0.2 s) → clip layer location/14-type-room/ (clipSeconds 0.8: f0000 Home selected and the sheet 25 px lower because the 'Choose one…' line disappears; then 'B-212' typed) 11.00–11.80; location/15-confirm-home.png holds underneath from 11.80 (identical to the clip's last frame).
11.85–12.65 orange rings on location/15-confirm-home.home and location/15-confirm-home.details.
12.50 ring--blue on location/15-confirm-home.confirm. 12.70 K.tap confirm ('Confirm location') → 13.05 the sheet closes: onboarding/23-step2-done.png sits underneath; the 15 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 576px 0)) fades out (0.35 s) while its sheet part (clip-path inset(268px 0 0 0)) slides y 0 → +576 (expo.in 0.45 s, done 13.50).
13.45 pin → address card: a Lucide map-pin (OUTLINE, stroke 2.5 px #EC5A2A, 36 px) pops (scale 0→1, back.out(2) 0.25 s) at the Delivery-location field's pin icon — 23's screen (346,363) → canvas {pt(FC,346,363)} under Fconf. 13.55–14.05 it flies in a straight line to (300,470) (expo.inOut 0.5 s); it crosses the screen only in flight. Its 2 px dotted pale trail is drawn ONLY on the canvas left of the phone, from ({n(_trail0[0],1)},{n(_trail0[1],1)}) to (300,470) (K.drawPath 13.80–14.05, in step with the pin), so no trail ever lies on app text. 14.00–14.45 the pin unfolds into a glass card (kit .glass-card, left 140, top 420, 420×110): Lucide house icon + 'Home · B-212' (Plus Jakarta Sans 700 32 px, white) over 'Nehru Hall of Residence' (Plus Jakarta Sans 500 22 px, #B8C7FF) (expo.out 0.45 s). Pin, trail and card are canvas-level (outside the rig). 14.20–14.50 the trail fades out, before any camera move.
13.55–14.55 orange ring on onboarding/23-step2-done.box (canvas {bx(FC, (16,309.7,358,104))}), fading 14.55–14.90.
14.65–15.55 K.unfocus (0.9 s); the card holds still (one movement at a time).
15.65–15.95 card and kicker fade out (the card was settled 14.45–15.65 = 1.2 s). 15.95–16.05 hold at identity.""",
 transitionIn='Continuous: Step 2 is already on screen at identity.',
 transitionOut='The saved address becomes a card in the left column, the camera returns to identity, then everything clears; Step 2 (filled) holds at identity for the cut.',
 handoffIn=handoff(screen='onboarding/21-step2-prompt.png', notes='Same frame as s04 ends.'),
 handoffOut=handoff(screen='onboarding/23-step2-done.png', notes='Step 2 filled (Nehru Hall of Residence, Room B-212, Home) at identity; card, trail, rings and kicker gone.'),
 demoBadge=[],
 soundCues=[(0.25, 'Soft card pop (explainer inset)'), (2.05, 'UI tap'), (2.40, 'Sheet slide up'), (3.50, 'UI tap'), (3.85, 'Keyboard ticks (10)'),
            (5.60, 'UI tap'), (6.65, 'Positive ping (inside the delivery area)'), (7.95, 'UI tap'), (8.30, 'Map slide + soft pin settle'),
            (9.35, 'UI tap'), (10.65, 'UI tap (Home chip)'), (11.00, 'Keyboard ticks (5)'), (12.70, 'UI tap (Confirm location)'),
            (13.45, 'Card lock-in: soft click + shimmer')],
 accuracyNotes="""- Location access is optional: SETU's own explainer ('Allow location for SETU?' with 'Not now' / 'Allow location') is shown as a labelled inset beside the phone at the phone's own scale; only 'Not now' is ringed. 'Use my current location' gets a pale context ring but is never tapped, and no detection result is claimed. Search is the path demonstrated.
- Never ring, underline, zoom or caption the dialog's body sentences 'SETU uses your location to find nearby stalls…' and 'It is only read when you ask for it.': on phones, auto-detect reads a fix each time the app opens and after a sign-in once permission is granted (client/src/state/useAutoLocation.js, client/src/layouts/ConsumerLayout.jsx), and no listing is sorted by distance. The caption says only 'Location access is optional.', which is true.
- Do not push in on location/10-picker-select.png: its dimmed background carries a blurred GPS reading from the capture run, an unreadable smudge at identity.
- Search result and zone check are the app's own: the first result reads 'Nehru Hall of Residence' over 'Pan Loop, IIT Kharagpur, Kharagpur, West Be…' (two lines), and Confirm says 'Location is within the IIT Kharagpur delivery area.' The off-campus refusal is not shown or faked.
- The map shows the real red pin, the faint blue campus-boundary polygon (#0033DA at 0.5 opacity) and the Google attribution; nothing covers them. 'Check the pin' = viewing it; no pin move is claimed or shown. The round trip is short (map fully visible 1.05 s, 1.75 s with its fades) but kept.
- Never ring, zoom on or caption 'SETU delivers inside the IIT Kharagpur campus boundary' (picker and map subtitles) or Step 2's lede '…SETU delivers inside the campus area only.' Fconf (T [1500,528]) shows screen y ≥ 303.4 only, so the map subtitle and every Confirm sheet title stay off-frame; the picker shots stay at identity.
- 'Use this location' returns the unchanged pin to Confirm, so location/13-confirm-search.png is reused honestly. 'Home' is tapped on 13 before the cut to 14-type-room/f0000.
- 'Nehru Hall of Residence, Cricket Ground', 22.319759, 87.298041 and 'B-212' are the real saved values. The card's 'Home · B-212' is the film's own summary label (saved name + room), not a quoted app string.""",
)

# ---------------------------------------------------------------- s06
scene(
 id='s06', compositionName='your-picks', title='Your picks — and three things SETU does not do', chapter='04 · Your picks', dur=9.55,
 captions=[(0.45, 3.55, 'Pick cuisines you like.\nThey show up first.'),
           (4.30, 7.00, 'Then three things SETU does not do.'),
           (7.10, 8.85, 'Confirm, then “Start ordering”.')],
 onScreenText=[
  ('04 · Your picks', 0.10, 9.45, 'kicker (kit .kicker)'),
  ('SETU never takes your money', 4.95, 7.25, 'kinetic list line (Sora 700 40 px; exact app title; no rupee sign)'),
  ('SETU does not deliver', 5.35, 7.25, 'kinetic list line (Sora 700 40 px; exact app title)'),
  ('SETU approves and records', 5.75, 7.25, 'kinetic list line (Sora 700 40 px; exact app title)'),
 ],
 shots=[
  ('onboarding/23-step2-done.png', 0.0, 1.30, "Frame 0; ring--blue + tap 'Continue' (0.40); pushed out 0.75–1.30."),
  ('onboarding/30-step3.png', 0.75, 3.70, "swapPush in: Step 3 of 4 'What should we show first?'; the base layer until the full 31 layer is set at 3.70."),
  ('onboarding/31-step3-picked.png', 2.25, 4.85, 'Pixel-aligned; revealed through a circle (r 0 → 56) at each tapped chip (only those three chips differ from 30); full layer from 3.70; pushed out 4.30–4.85.'),
  ('onboarding/40-step4.png', 4.30, 7.80, "swapPush in (no tap: Step 3's Continue sits below the captured viewport); focus mask on the three titles; rings; kinetic list; the base layer until the full 41 layer is set at 7.80."),
  ('onboarding/41-step4-ack.png', 7.45, 9.20, "Circular reveal from the tapped switch (r 0 → 340, then the full layer): toggle on, 'Start ordering' enabled; ring--blue + tap 'Start ordering' (8.40)."),
  ('home/01-first-home.png', 9.20, 9.55, "Revealed by the 'Start ordering' commit wipe: Home with 'Home' over 'Room B-212 · Nehru Hall of Residence'."),
  ('graphic:commit wipe (#0033DA circle from the Start ordering button)', 8.75, 9.50, 'Action → result transition.'),
 ],
 uiState="Onboarding Step 3 of 4 'What should we show first?' (South Indian, Street Food, Chinese selected) → Step 4 of 4 'Three things SETU does not do' → switch 'I understand SETU is a directory and approval gate' on → 'Start ordering' → Home ('Home' over 'Room B-212 · Nehru Hall of Residence'; 'Good evening, Aarav').",
 animation="""Local times. Frame 0 = onboarding/23-step2-done.png at identity; the whole scene stays at identity.
0.10 kicker '04 · Your picks' K.fadeUp at (140,200).
0.15 ring--blue on onboarding/23-step2-done.cont. 0.40 K.tap cont ('Continue') → 0.75 K.swapPush → onboarding/30-step3.png (0.55 s).
Chip taps in the capture's order; each 'result' is a layer of onboarding/31-step3-picked.png revealed by clip-path circle(r at x y) growing 0 → 56 px (0.25 s, power2.out) around the tapped chip. 56 px covers the tapped chip's far corners (≤54.3 px) and stops short of every other tapped chip (South Indian's circle ends at x 204.4; Street Food starts at x 209), so no chip looks selected before its own tap:
- 1.90 K.tap onboarding/31-step3-picked.southIndian (centre (148.4,584.7)) → 2.25 reveal (Step 3 has read for 0.6 s since its push ended at 1.30).
- 2.50 K.tap 'Street Food', measured box {x:209,y:568,w:100,h:34} (centre (259,585)) → 2.85 reveal.
- 3.10 K.tap 'Chinese', measured box {x:90,y:396,w:77,h:34} (centre (128.5,413)) → 3.45 reveal.
3.70 set the 31 layer fully visible (clip-path none; no visible change: only those three chips differ).
4.30 K.swapPush → onboarding/40-step4.png (0.55 s; no tap is drawn because Step 3's Continue is below the captured viewport; the last chip settled 0.6 s earlier).
4.90–5.25 focus mask fades in: an SVG (390×844, inside the screen) filled rgba(8,12,32,.55) with three feathered rounded holes around onboarding/40-step4.fact1, .fact2 and .fact3 (each padded 8 px). It keeps every card's sub-line — including fact 3's licence sentence — and the switch's 'Required. Recorded…' line dim. 6.60–6.90 it fades out, before the switch is ringed or tapped.
Kinetic list in the left column (Sora 700 40 px white, each line led by a Lucide icon 34 px stroke 2 #B8C7FF: wallet / bike / shield-check; fromTo y 24/opacity 0 → 0/1, expo.out 0.5 s), each with an orange ring on its title in the phone (all three rings start fading at 6.60, gone by 6.95):
- 4.95 'SETU never takes your money' at (140,330); ring onboarding/40-step4.fact1 4.95–6.60.
- 5.35 'SETU does not deliver' at (140,400); ring .fact2 5.35–6.60.
- 5.75 'SETU approves and records' at (140,470); ring .fact3 5.75–6.60.
6.95–7.25 the three lines fade out (each held ≥1.2 s from its entrance).
6.90 ring--blue on the switch, measured box {x:313,y:622,w:46,h:27} (mask and fact rings are gone). 7.10 K.tap the switch (centre (336,635)) → 7.45 circular reveal of onboarding/41-step4-ack.png from (336,635), r 0 → 340 (0.35 s; the farthest changed pixel, the ack card's left border at (16,584)/(16,686), is 324 px away); 7.80 set the 41 layer's clip-path to none. The switch turns on and 'Start ordering' becomes active.
7.85 ring--blue on onboarding/41-step4-ack.start. 8.40 K.tap start ('Start ordering'; 0.6 s after the reveal settled) → 8.75 commit wipe: a #0033DA circle (inside the screen) grows from the button centre (255.8,742.7) to cover the whole screen (0.45 s, power2.in); 9.20 home/01-first-home.png is set underneath and the circle fades (0.3 s, done 9.50).
9.15–9.45 the kicker fades out. 9.50–9.55 hold on Home.""",
 transitionIn='Continuous: Step 2 (filled) is on screen at identity.',
 transitionOut="'Start ordering' → blue commit wipe → Home (day one, address set), settled at identity.",
 handoffIn=handoff(screen='onboarding/23-step2-done.png', notes='Same frame as s05 ends.'),
 handoffOut=handoff(screen='home/01-first-home.png', notes="Day one's Home ('Home' over 'Room B-212 · Nehru Hall of Residence') at identity; wipe circle, mask, list and kicker gone."),
 demoBadge=[],
 soundCues=[(0.40, 'UI tap'), (0.75, 'Page push'), (1.90, 'Chip tap (pitch 1)'), (2.50, 'Chip tap (pitch 2)'), (3.10, 'Chip tap (pitch 3)'),
            (4.30, 'Page push'), (4.95, 'Low tick'), (5.35, 'Low tick'), (5.75, 'Low tick'), (7.10, 'Toggle click'),
            (8.40, 'UI tap (Start ordering)'), (8.75, 'Blue wipe swoosh into Home')],
 accuracyNotes="""- Chips are tapped in the capture's order (South Indian, Street Food, Chinese); 30-step3 and 31-step3-picked differ only in those three chips, so the circular reveals (r ≤ 56, each confined to its own chip) composite two real captures and never pre-select a chip. The taps are a quick multi-select (0.6 s apart); the beat after the last chip is 0.6 s.
- Step 4's three titles are quoted exactly. The focus mask keeps 'Every seller listed here cleared a licence check…' and 'Required. Recorded against your account with today's date.' dim; never ring, zoom on or caption them (the acknowledgement is not stored; not every stall is licence-gated). Fact 1's body ('no checkout … UPI to the seller's own handle') is likewise never featured. The mask and rings are gone before the switch is ringed and tapped.
- The ack reveal grows to r 340 (the farthest changed pixel is 324 px from the switch) and the full 41 layer is then set, so no half-changed card border is ever shown.
- 'They show up first' = 'Stalls serving these move to the top of the home page'; the liked cuisines also lead the Home tabs (visible in s07, not featured).
- No tap is drawn on Step 3's Continue: it is below the captured viewport.""",
)

# ---------------------------------------------------------------- s07
SLIP_OVERLAY = ("Order slip #sNN-slip: two kit .dish-chip rows in one wrapper at left 140, top 340 (600×132), fully opaque, at rest: row 1 at top 340 "
                "'[veg] 1 × Masala Dosa ₹80', row 2 at top 412 '[veg] 2 × Filter Coffee ₹60' ('1 ×'/'2 ×' Space Mono 700 26 px #EC5A2A; names "
                "Plus Jakarta Sans 700 28 px white; prices Space Mono 700 26 px #B8C7FF; kit .dish-chip padding 16/24, radius 22, height 62).")
scene(
 id='s07', compositionName='find-and-add', title='Back to tonight — saved Home, then dosa from Southside Tiffins', chapter='05 · Find & add', dur=13.55,
 captions=[(0.20, 4.45, 'New phone, same account:\nhe picks his saved Home.'),
           (4.55, 7.10, 'Good evening, Aarav.\nTonight: dosa.'),
           (7.50, 9.80, 'Southside Tiffins: approved by SETU.'),
           (9.90, 13.00, 'Tap ADD: one Masala Dosa,\ntwo filter coffees.')],
 onScreenText=[
  ('TONIGHT', 0.40, 2.00, 'tag (tag row at (140,112): Lucide moon + Space Mono 700 18 px caps)'),
  ('05 · Find & add', 0.45, 13.45, 'kicker (kit .kicker)'),
  ('Demo environment · sample stalls', 2.00, 10.60, 'honesty note (tag row; Space Mono 700 18 px caps, shown once in the body)'),
  ('Masala Dosa ₹80', 7.25, 11.15, 'dish chip (kit .dish-chip: name Plus Jakarta Sans 700 28 px, price Space Mono 700 26 px #B8C7FF; exact menu line)'),
  ('Ghee Roast Dosa ₹110', 7.40, 9.80, 'dish chip (kit .dish-chip: Plus Jakarta Sans name, Space Mono price; exact menu line)'),
  ('1 × Masala Dosa ₹80', 11.15, 13.55, "order-slip row (kit .dish-chip; '1 ×' Space Mono 700 26 px #EC5A2A, name Plus Jakarta Sans, price Space Mono; exact cart line)"),
  ('2 × Filter Coffee ₹60', 12.95, 13.55, "order-slip row (kit .dish-chip; '2 ×' Space Mono, name Plus Jakarta Sans, price Space Mono; exact cart line)"),
 ],
 shots=[
  ('home/01-first-home.png', 0.0, 0.29, "Frame 0 (day one's Home, from s06) under the return band; hidden at 0.29 while the band covers the phone."),
  ('graphic:editorial return band (right → left)', 0.0, 0.70, 'Marks the jump back to tonight; the phone switches to tonight\'s Home under it (0.29).'),
  ('location/30-home-unset.png', 0.29, 1.95, "Tonight, new phone: 'Set your delivery location' over 'Tap to pick it on the map'; ring--blue + tap the Deliver-to row (1.00); covered by the picker's scrim 1.35–1.95."),
  ('location/31-picker-saved.png', 1.35, 3.15, "K.swapSheet (sheetTop 433): 'Select a location' with SAVED LOCATIONS · 'Home' over 'B-212 · Nehru Hall of Residence, Cricket Gro…'; identity only; ring--blue + tap the Home row (2.55); fades out 2.90–3.15."),
  ('location/32-confirm-saved.png', 2.90, 4.55, "swapFade: 'Confirm delivery location' (SAVED LOCATION, Home, B-212 filled); ring--blue + tap 'Confirm location' (3.75); the sheet closes 4.10–4.55."),
  ('location/33-home-set.png', 4.10, 6.35, "Revealed as the sheet closes: 'Home' over 'Room B-212 · Nehru Hall of Residence'; ring; ring--blue + tap search (5.45); pushed out 5.80–6.35."),
  ('search/01-search-empty.png', 5.80, 6.45, 'swapPush in; the box is auto-focused.'),
  ('search/02-type-dosa/', 6.45, 6.95, "Typing clip, clipSeconds 0.5: 'dosa'.", 0.5),
  ('search/03-results.png', 6.95, 9.40, "Southside Tiffins with 'Masala Dosa ₹80' / 'Ghee Roast Dosa ₹110'; dish chips rise out; tap the stall card (8.50); pushed out 8.85–9.40."),
  ('stall/01-stall.png', 8.85, 11.45, "swapPush in; ring on 'Approved by SETU · you pay the seller directly'; tap Masala Dosa ADD (10.75); the base layer until the full 02 layer is set at 11.45."),
  ('stall/02-dosa-added.png', 11.10, 12.90, "Circular reveal at the ADD button (ADD → '− 1 +') + bottom wipe revealing 'View cart'; full layer from 11.45."),
  ('stall/04-coffee.png', 11.10, 12.90, "Pixel-identical to 02 (no swap needed): Filter Coffee ADD (11.95) then '+' (12.30) are tapped on this state."),
  ('stall/05-coffee-two.png', 12.65, 13.55, "Circular reveal at the coffee stepper: '− 2 +'; full layer from 12.90."),
 ],
 uiState="Back to tonight on the new phone: Home reads 'Set your delivery location' over 'Tap to pick it on the map' (the selected delivery location is stored per browser; the saved addresses belong to the account) → the Deliver-to row opens 'Select a location' with SAVED LOCATIONS · 'Home' over 'B-212 · Nehru Hall of Residence, Cricket Gro…' → 'Confirm delivery location' (SAVED LOCATION 'Nehru Hall of Residence, Cricket Ground', 'Location is within the IIT Kharagpur delivery area.', SAVE AS Home, ADDRESS DETAILS 'B-212') → 'Confirm location' → Home: 'Home' over 'Room B-212 · Nehru Hall of Residence', 'Good evening, Aarav', tabs All · Chinese · South Indian · Street Food · Amer…, 'Approved sellers', '13 open now' → Search 'dosa' → Southside Tiffins ('Masala Dosa ₹80', 'Ghee Roast Dosa ₹110') → stall page ('Approved by SETU · you pay the seller directly') → Masala Dosa 1, Filter Coffee 2, 'View cart'.",
 animation=f"""Local times. Frame 0 = home/01-first-home.png (day one's Home) at identity; the whole scene stays at identity (never push in on the picker sheet: its subtitle 'SETU delivers inside the IIT Kharagpur campus boundary' sits at screen y≈475–500).
0.00–0.70 return band: the s04 band style (760 px, linear-gradient(270deg,#151E4D,#22307A), 3 px orange leading edge on its LEFT side) sweeps right → left, x 1920 → −760 (power2.inOut 0.7 s), above the phone and the left column (the caption track stays on top). It fully covers the phone (x 1150–1599) only between ≈0.265 and 0.314 s, and the phone is fully uncovered again from ≈0.38.
0.29 instant swap under the band: home/01-first-home.png → location/30-home-unset.png (set the new layer visible, hide the old one; verify the 0.27–0.31 frames in a snapshot). Tonight, on his new phone, Home reads 'Set your delivery location' over 'Tap to pick it on the map' — the same fresh-device state s03 ended on.
0.40–0.70 tag 'TONIGHT' (Lucide moon 20 px + Space Mono 700 18 px caps) fades in at the tag row (140,112); 1.70–2.00 it fades out. 0.45 kicker '05 · Find & add' K.fadeUp at (140,200).
Picking the saved Home takes three real taps, each 0.35 s before the change it causes. Readable windows (counting the sheets' expo entrances/exits): 30's header ≈0.38–1.6, 31's Home row ≈1.6–2.9, 32's confirm step ≈3.0–4.3, 33's header ≈4.4–5.9 — each ≥1.2 s:
0.75 ring--blue on location/30-home-unset.deliverTo (canvas {bx(None,(18,18.1,304,41))}). 1.00 K.tap deliverTo (centre (170,38.6)) → 1.35 K.swapSheet → location/31-picker-saved.png (sheetTop 433, 0.6 s; settled 1.95).
1.95 ring--blue on location/31-picker-saved.homeRow (the 'Home' row under 'SAVED LOCATIONS'; canvas {bx(None,(18,760,354,66))}). 2.55 K.tap homeRow (centre (195,793); 0.6 s after the sheet settled) → 2.90 K.swapFade (0.25 s) → location/32-confirm-saved.png: 'Confirm delivery location' with SAVED LOCATION 'Nehru Hall of Residence, Cricket Ground', 'Location is within the IIT Kharagpur delivery area.', SAVE AS Home and ADDRESS DETAILS 'B-212' already filled (settled 3.15). No ring on its zone line (s05 explained it).
2.00–2.30 note 'Demo environment · sample stalls' (Space Mono 700 18 px caps, #B8C7FF at 80%, a 6 px orange dot first) fades in at the tag row as soon as TONIGHT has left — before any stall card is held on screen (33-home-set from 4.55); 10.30–10.60 it fades out.
3.25 ring--blue on location/32-confirm-saved.confirm (canvas {bx(None,(181.6,782,190.4,48))}). 3.75 K.tap confirm ('Confirm location', centre (276.8,806); 0.6 s after the step settled) → 4.10 the sheet closes: location/33-home-set.png sits underneath; the 32 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 592px 0)) fades out (0.35 s) while its sheet part (clip-path inset(252px 0 0 0)) slides y 0 → +592 (expo.in 0.45 s, done 4.55).
4.55–5.30 orange ring on location/33-home-set.deliverTo ('Home' over 'Room B-212 · Nehru Hall of Residence'), fading 5.30–5.65; the header stays readable until the push (settled 4.55–5.80 = 1.25 s). Never ring or zoom on 33's tab bar ('Orders' shows a hover blue there, screen y 798–829).
5.25 ring--blue on the search box, measured box {{x:18,y:129.1,w:354,h:46}} (33-home-set is pixel-identical to home/01-first-home.png above y 636, so home/01-first-home.search applies). 5.45 K.tap search (centre (195,152.1)) → 5.80 K.swapPush → search/01-search-empty.png (0.55 s; the box is auto-focused, no tap needed).
6.45 clip layer search/02-type-dosa/ (clipSeconds 0.5; f0000 = 01-search-empty) types 'dosa' 6.45–6.95; 6.95 the clip ends: cut to search/03-results.png (set it visible under the clip layer at 6.95; the filtered results replace the clip's last frame).
7.15–8.35 orange ring on the Southside Tiffins dish lines, measured box {{x:128,y:256,w:236,h:46}} ('Masala Dosa ₹80' / 'Ghee Roast Dosa ₹110').
7.25 dish chip 'Masala Dosa ₹80' (kit .dish-chip with .veg mark; name Plus Jakarta Sans 700 28 px, price in <b> Space Mono 700 26 px #B8C7FF) rises at left 140, top 340: fromTo y +30/opacity 0 → 0/1 (expo.out 0.5 s). 7.40 'Ghee Roast Dosa ₹110' the same at left 140, top 412. They move OUT of the phone; nothing flies in.
8.30 ring--blue on search/03-results.stall. 8.50 K.tap the stall card (centre (195,220.5)) → 8.85 K.swapPush → stall/01-stall.png (0.55 s).
9.45–10.65 orange ring on stall/01-stall.trust ('Approved by SETU · you pay the seller directly'). 9.50–9.80 the 'Ghee Roast Dosa ₹110' chip fades out.
10.50 ring--blue on stall/01-stall.dosaAdd. 10.75 K.tap dosaAdd ('ADD') → 11.10 circular reveal of a stall/02-dosa-added.png layer from (299,611), r 0 → 90 (0.25 s): ADD becomes '− 1 +' (stall/02-dosa-added.stepper); 11.10–11.40 a second 02 layer clipped to the bottom strip (screen y ≥ 790) wipes up from the bottom, revealing 'View cart'; 11.45 set one full 02 layer visible (stall/04-coffee.png is pixel-identical, so it stands for both). Accepted at 11.45: the 'Dosas' tab label (screen x 163–201, y 232–241) drops from 01's hover weight to regular — a capture artifact, too small to read as a change.
11.15 the Masala Dosa chip gains an orange '1 ×' prefix (Space Mono 700 26 px #EC5A2A, slides in from the left 0.25 s): it now reads '1 × Masala Dosa ₹80', the cart's line.
11.95 K.tap stall/04-coffee.coffeeAdd (Filter Coffee 'ADD', centre (299,362); 0.6 s after the dosa stepper settled); 12.30 K.tap stall/05-coffee-two.plus ('+', centre (327,362)); nothing changes between the two taps (there is no capture of the '1' state). 12.65 circular reveal of stall/05-coffee-two.png from (299,362), r 0 → 80 (0.25 s): '− 2 +' (the only change from 04); 12.90 set the full 05 layer visible.
12.95 slip row 2 '2 × Filter Coffee ₹60' (same chip style) fromTo y +20/opacity 0 → 0/1 at left 140, top 412 (expo.out 0.4 s). The two chips now form the order slip: wrap them in one element #s07-slip (left 140, top 340, 600×132) so s08 can move them.
13.15–13.45 the kicker fades out. 13.45–13.55 hold (slip visible, phone on 05-coffee-two at identity).""",
 transitionIn="Editorial return band (right → left) from day one back to tonight. Under it (0.29) the phone switches to tonight's Home on the new phone ('Set your delivery location'), because the delivery choice is stored per device; Aarav picks his saved Home with three taps.",
 transitionOut='Holds on the stall with both items added and the order slip (two cart lines) in the left column — carried into s08.',
 handoffIn=handoff(screen='home/01-first-home.png', notes='Same frame as s06 ends.'),
 handoffOut=handoff(screen='stall/05-coffee-two.png', left='1 × Masala Dosa ₹80 / 2 × Filter Coffee ₹60 (order slip; no kicker, no tag)',
                    overlays=SLIP_OVERLAY, notes='Phone at identity on stall/05-coffee-two.png; the only canvas element is the order slip.'),
 demoBadge=[],
 soundCues=[(0.0, 'Band whoosh (back to tonight) + light evening swell'), (1.00, 'UI tap (Deliver-to row)'), (1.35, 'Sheet slide up'),
            (2.55, 'UI tap (saved Home)'), (3.75, 'UI tap (Confirm location)'), (4.10, 'Sheet slides down + soft settle'),
            (5.45, 'UI tap'), (5.80, 'Page push'), (6.45, 'Four keyboard ticks'), (7.25, 'Two soft pops (dish chips)'),
            (8.50, 'UI tap'), (8.85, 'Page push'), (10.75, 'ADD tap + soft pop'), (11.95, 'UI tap'), (12.30, 'UI tap + tick (× 2)')],
 accuracyNotes="""- Tonight's Home is location/30-home-unset.png ('Set your delivery location' over 'Tap to pick it on the map'): the selected delivery location is stored per browser (setu-svc-loc), so the new phone starts unset although the account holds the saved Home — exactly what the capture stack shows (signin/07-home.png ends s03 in the same state). It takes three real taps, in the capture's order: the Deliver-to row → the 'Home' row under SAVED LOCATIONS → 'Confirm location' (location/30 → 31 → 32 → 33). Never imply the saved address applies itself.
- 31-picker-saved stays at identity and briefly on screen: its subtitle 'SETU delivers inside the IIT Kharagpur campus boundary' (screen y≈475–500) is never ringed, zoomed or captioned.
- 33-home-set's tab bar shows 'Orders' in a hover blue next to the active 'Home' (a capture artifact, screen y 798–829); never ring or zoom on it. Above y 636 it is pixel-identical to home/01-first-home.png, so the search box {x:18,y:129.1,w:354,h:46} is the same.
- 'Demo environment · sample stalls' appears here once (2.00, as soon as the TONIGHT tag leaves and before any stall card is held), and again in the end-card fine print.
- The liked cuisines lead the Home tabs (capture order: All, Chinese, South Indian, Street Food…): visible, not featured.
- Search 'dosa' → Southside Tiffins with 'Masala Dosa ₹80' and 'Ghee Roast Dosa ₹110' (exact). Never ring or zoom on the result rows' '20–20 min' or the stall's '20 min'; no delivery-time claim.
- The stall line is quoted: 'Approved by SETU · you pay the seller directly'. The stall shows 'New' (fresh demo data).
- Coffee: ADD, then '+', then the 2 appears (no capture of the '1' state). stall/04-coffee.png is pixel-identical to 02-dosa-added. stall/03-scroll-menu/ is not used (it snaps back).
- Dish chips and slip rows quote the real menu and cart lines; prices are never set in Sora.""",
)

# ---------------------------------------------------------------- s08
FT, FK = 'Ftotals', 'Fcard'
scene(
 id='s08', compositionName='cart', title='Cart — ₹150, payable to the seller', chapter='06 · Cart', dur=9.3,
 captions=[(0.10, 3.20, 'Tap “View cart”:\none stall per order.'),
           (3.30, 6.40, "Items ₹140, plus the stall's\ndelivery charge: ₹10."),
           (6.50, 9.20, '₹150 to the seller.\nNo platform fee.')],
 onScreenText=[
  ('1 × Masala Dosa ₹80', 0.0, 1.60, "order-slip row carried from s07 (Space Mono count/price, Plus Jakarta Sans name); flies first, onto the cart's Masala Dosa line"),
  ('2 × Filter Coffee ₹60', 0.0, 1.95, "order-slip row carried from s07 (Space Mono count/price, Plus Jakarta Sans name); flies second, onto the cart's Filter Coffee line"),
  ('06 · Cart', 0.10, 9.15, 'kicker (kit .kicker)'),
  ('ITEM TOTAL ₹140', 3.40, 7.65, "math row: label Space Mono 700 18 px caps + value '₹140' Plus Jakarta Sans 800 64 px"),
  ('+ SELLER DELIVERY CHARGE ₹10', 4.60, 7.65, "math row: label Space Mono 700 18 px caps + value '₹10' Plus Jakarta Sans 800 64 px"),
  ('SET BY THE STALL', 4.70, 5.90, 'label (short caps, Space Mono 700 18 px, callout lane)'),
  ('= PAYABLE TO SELLER ₹150', 5.85, 7.65, "math result: label Space Mono 700 18 px caps + value '₹150' Plus Jakarta Sans 800 64 px white"),
  ('₹150', 7.80, 8.85, 'number flight (Plus Jakarta Sans 800, white) from the cart total onto the Confirm card amount'),
 ],
 shots=[
  ('stall/05-coffee-two.png', 0.0, 1.60, "Frame 0 with the order slip; ring--blue + tap 'View cart' (0.70)."),
  ('cart/01-cart.png', 1.05, 8.30, "swapPush in; the two slip rows fly in one after the other, each onto its own cart line, and dissolve; camera Ftotals; rings on the three total rows; tap 'Review order' (7.40)."),
  ('checkout/01-confirm-cash.png', 7.75, 9.30, "swapPush in ('Confirm order'); camera Ftotals → Fcard; the ₹150 number flight lands on 'AMOUNT PAYABLE TO THE SELLER ₹150'."),
 ],
 uiState="Stall with both items → cart 'Your order' over 'Southside Tiffins' (Masala Dosa '₹80 each' × 1 = ₹80; Filter Coffee '₹30 each' × 2 = ₹60; DELIVER TO 'Home' over 'Room B-212 · Aarav Mehta'; 'Item total' ₹140; 'Seller delivery charge' ₹10 with 'Set by the seller, collected by the seller'; 'Payable to seller' ₹150) → 'Confirm order' with 'AMOUNT PAYABLE TO THE SELLER' ₹150 and Cash on delivery selected.",
 animation=f"""Local times. Frame 0 = stall/05-coffee-two.png at identity with the order slip from s07 (handoffIn). Framings: Ftotals = {frame(FT)} (canvas of a screen point = (1124.1 + 1.62·x, −387.2 + 1.62·y)); Fcard = {frame(FK)} (canvas = (1125.16 + 1.512·x, 85.24 + 1.512·y)).
0.10 kicker '06 · Cart' K.fadeUp at (140,200).
0.40 ring--blue on stall/05-coffee-two.viewCart. 0.70 K.tap viewCart ('View cart') → 1.05 K.swapPush → cart/01-cart.png (0.55 s).
Order-slip rows fly ONE AT A TIME (never together), each onto its own cart line, and dissolve as they land. Each row is a kit .dish-chip 62 px tall; give each row transform-origin 0% 50%, so its anchor is its left-middle point:
- 1.10–1.50 row 1 '1 × Masala Dosa ₹80' (anchor at rest (140,371)): translate x +1059.6, y −139.2 and scale 1 → 0.64 (expo.inOut 0.4 s), landing its anchor on canvas (1199.6,231.8) = cart/01-cart.png screen (33,136.9), the veg mark's left edge on the Masala Dosa line's centre line (the line's ink spans screen y 116.7–157.0); 1.40–1.60 it dissolves (opacity → 0).
- 1.45–1.85 row 2 '2 × Filter Coffee ₹60' (anchor at rest (140,443)): translate x +1059.6, y −101.3 and scale 1 → 0.64 (expo.inOut 0.4 s), landing on (1199.6,341.7) = screen (33,238.7) on the Filter Coffee line (ink y 218.3–259.0); 1.75–1.95 it dissolves.
The cart has settled by 1.60; the rows never cover app text after they land.
2.30–3.30 K.focus Ftotals (1.0 s).
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
                   overlays=SLIP_OVERLAY, notes='Phone at identity on stall/05-coffee-two.png; the only canvas element is the order slip.'),
 handoffOut=handoff(screen='checkout/01-confirm-cash.png', rig_=rigobj(FK), notes='Camera held at Fcard (dark amount card, HOW WILL YOU PAY?, Cash on delivery and Pay by QR in frame); number flight dissolved; math and kicker gone.'),
 demoBadge=[],
 soundCues=[(0.70, 'UI tap (View cart)'), (1.05, 'Page push'), (1.10, 'Soft whoosh (slip row 1 lands)'), (1.45, 'Soft whoosh (slip row 2 lands)'), (3.40, 'Number tick'), (4.60, 'Number tick'),
            (5.85, 'Soft resolve tone (= ₹150)'), (7.40, 'UI tap (Review order)'), (7.80, 'Number-flight swish'), (8.65, 'Soft lock-in')],
 accuracyNotes="""- Cart values are exact: items ₹140, 'Seller delivery charge' ₹10 'Set by the seller, collected by the seller', 'Payable to seller' ₹150.
- Each stall sets its own delivery charge (₹0–₹500; the row is hidden at ₹0) — 'the stall's delivery charge' and the label 'SET BY THE STALL' cover that. Never 'free', 'zero cost' or 'minimal'.
- No platform fee or commission exists: payable = items + the stall's own charge.
- One order goes to one stall (adding from another stall replaces the cart).
- The slip rows and the ₹150 flight link real values and land exactly on the real UI, one object at a time; they never cover app text after landing.
- checkout/03-scroll-summary/ and checkout/04-summary.png are not used (captured with Pay by QR selected; Aarav pays cash).""",
)

# ---------------------------------------------------------------- s09
scene(
 id='s09', compositionName='pay', title='Pay the stall directly — cash, or the stall\'s QR', chapter='07 · Pay', dur=12.0,
 captions=[(0.10, 3.95, "Pay cash at your door,\nor scan the stall's QR."),
           (4.05, 7.55, 'With QR, the stall accepts first,\nthen you pay.'),
           (9.75, 11.90, 'Aarav picks cash: “Place order”.')],
 onScreenText=[
  ('07 · Pay', 0.10, 11.90, 'kicker (kit .kicker; faded out 2.75–3.05 and back in from 9.85 while the QR branch is up)'),
  ('DEMO QR · NOT A REAL PAYMENT CODE', 3.10, 9.60, 'demo tag (orange outline pill, Space Mono 700 18 px caps; enters and leaves with the QR phone)'),
  ('IF THE STALL OFFERS QR', 3.25, 9.60, 'kicker-style heading for the side branch (Space Mono 700 22 px caps)'),
  ('1 · Stall accepts', 3.80, 9.60, 'step list (Space Mono 700 22 px)'),
  ('2 · You pay · five minutes', 4.60, 9.60, 'step list (Space Mono 700 22 px)'),
  ('3 · Stall confirms', 7.80, 9.60, 'step list (Space Mono 700 22 px)'),
 ],
 shots=[
  ('checkout/01-confirm-cash.png', 0.0, 9.45, "Main phone at Fcard: rings on 'SETU does not collect this…', Cash on delivery and Pay by QR; then it shrinks left and dims for the QR branch; swapped to order-cash/00-confirm under the dim at 9.45."),
  ('order-qr/02-pay-qr.png', 3.10, 6.45, "Second phone (default spec, above the main rig) slides in from the right 3.10–3.80: a separate demo QR order after the stall accepted — 'Pay to continue', countdown, the stall's labelled DEMO QR; tap 'I've paid' (5.85)."),
  ('order-qr/04-payment-review.png', 6.20, 7.95, "swapFade: 'Seller is checking your payment' (settled 6.45–7.70 = 1.25 s)."),
  ('order-qr/05-payment-confirmed.png', 7.70, 9.60, "swapFade (the stall's confirmation): 'Order confirmed', 'The stall confirmed your payment.' (settled 7.95–9.20 = 1.25 s); the second phone fades out to the right 9.20–9.60."),
  ('order-cash/00-confirm.png', 9.45, 11.65, "Main phone back at the default spec (identical to checkout/01 except the button shade); ring Cash; tap 'Place order · ₹150' (10.85)."),
  ('order-cash/01-placed.png', 11.65, 12.0, "Revealed by the 'Place order' commit wipe: 'Waiting for the seller'."),
  ('graphic:commit wipe (#0033DA circle from the Place order button)', 11.20, 11.95, 'Action → result transition.'),
 ],
 uiState="'Confirm order': 'AMOUNT PAYABLE TO THE SELLER' ₹150 and 'SETU does not collect this. Southside Tiffins receives it directly.'; HOW WILL YOU PAY? Cash on delivery 'Hand ₹150 to the seller at your door.' / Pay by QR 'Southside Tiffins's QR appears here once they accept. You will have five minutes to pay…' (offered only because this stall has a QR on file). Side branch on a second phone (separate demo QR order CE1013-VGKQ): accepted → 'Pay to continue' with the stall's DEMO QR and countdown → 'Seller is checking your payment' → 'Order confirmed' / 'The stall confirmed your payment.'. Back on Aarav's phone: Cash on delivery → 'Place order · ₹150' → 'Waiting for the seller'.",
 animation=f"""Local times. Frame 0 = checkout/01-confirm-cash.png with the main rig at Fcard = {frame(FK)} (canvas of a screen point = (1125.16 + 1.512·x, 85.24 + 1.512·y)). Fsplit = {{s 0.7407, P [195,422], T [346.4,497.9]}} puts the main phone at x 180–513, y 150–846 (= spec {{left:180, top:150, k:0.8}}).
0.10 kicker '07 · Pay' K.fadeUp at (140,200).
0.20–1.00 orange ring on 'SETU does not collect this. Southside Tiffins receives it directly.', measured box {{x:33,y:162,w:270,h:36}} (canvas {bx(FK,(33,162,270,36))}).
0.85–1.75 orange ring on checkout/01-confirm-cash.cash (canvas {bx(FK,(18,260,354,70))}).
1.60–2.50 orange ring on checkout/01-confirm-cash.qr (canvas {bx(FK,(18,340,354,102))}), fading 2.50–2.85.
2.55–3.35 split: K.focus main rig Fcard → Fsplit (0.8 s, expo.inOut); a kit .dim layer inside the main screen fades to opacity 1 (rgba(8,12,32,.55)) over 2.55–3.05. 2.75–3.05 the kicker fades out. The main phone's right edge is left of x 560 from 3.10 (sampled: 3.00 → 769, 3.10 → 558, 3.20 → 521, settled 513).
3.10–3.80 the QR phone — a second kit .phone at the default spec {{left:1150,top:70,k:1.08}} with its own screen, OUTSIDE and ABOVE the main rig in z-order — fromTo x +900 → 0 (expo.out 0.7 s) showing order-qr/02-pay-qr.png; it is opacity 0 (tl.set) before 3.10 and starts at x +900 (left edge 2050, glow off-canvas). It starts only after the main phone has cleared its path: the closest approach is >900 px (3.20: QR left edge 1484 vs main right edge 521).
3.10–3.40 tag 'DEMO QR · NOT A REAL PAYMENT CODE' (orange 2 px outline pill, Space Mono 700 18 px caps, ≈454×38) fades in at (560,296) together with the QR phone; it stays while any QR is on screen. 3.25 heading 'IF THE STALL OFFERS QR' (kit .kicker style, Space Mono 700 22 px caps) K.fadeUp at (560,250). Both sit in the middle column (x 560–1110, canvas-level), clear of the shrunken main phone.
Step list (Space Mono 700 22 px white, numerals #EC5A2A; a Lucide check (#19B36B, 22 px) appears at a row's left when it is reached):
- 3.80 '1 · Stall accepts' at (560,390), checked at once; orange ring on order-qr/02-pay-qr.headline ('Pay to continue' — the state the order enters once the stall accepts) 3.80–4.70. Never ring the thread pill 'Order confirmed by Southside Tiffins' here: it is the app's premature 'confirmed' wording before any payment.
- 4.60 '2 · You pay · five minutes' at (560,450); orange rings on order-qr/02-pay-qr.timer 4.60–5.50 and order-qr/02-pay-qr.qrImg 4.80–5.70.
5.60 ring--blue on order-qr/02-pay-qr.paid. 5.85 K.tap paid ('I've paid') → 6.20 K.swapFade → order-qr/04-payment-review.png (0.25 s, settled 6.45); row 2 gets its check at 6.20; 6.50–7.70 orange ring on order-qr/04-payment-review.headline ('Seller is checking your payment').
7.70 K.swapFade → order-qr/05-payment-confirmed.png (0.25 s, settled 7.95; the stall's confirmation, no customer tap). 7.80 '3 · Stall confirms' at (560,510) with its check; 8.00–9.00 green ring on order-qr/05-payment-confirmed.qrCard ('The stall confirmed your payment.').
9.20–9.60 the QR phone leaves: x 0 → +160 and opacity 1 → 0 (power2.in 0.4 s), then it stays hidden. 9.20–9.60 the heading, the DEMO QR tag and the step list fade out with it (the tag never outlives the QR, and the QR never shows without the tag after 3.40).
9.45–10.25 K.focus main rig Fsplit → identity (0.8 s, expo.inOut); the dim fades out 9.45–9.95; at 9.45 the main screen's still is swapped to order-cash/00-confirm.png under the dim (identical layout; only the button shade differs). The growing phone reaches x 560 only at ≈9.71, after the branch type is gone. 9.85 the kicker fades back in.
10.20–10.80 orange ring on the Cash on delivery card (same box as checkout/01-confirm-cash.cash; canvas at identity {bx(None,(18,260,354,70))}).
10.60 ring--blue on order-cash/00-confirm.place (canvas {bx(None,(18,782,354,48))}). 10.85 K.tap place ('Place order · ₹150') → 11.20 commit wipe: a #0033DA circle grows from the button centre (195,806) to cover the screen (0.45 s, power2.in); 11.65 order-cash/01-placed.png is set underneath and the circle fades (0.3 s, done 11.95).
11.60–11.90 the kicker fades out. 11.95–12.00 hold.""",
 transitionIn='Continuous from s08: the camera is already framing the amount card and the payment options (Fcard).',
 transitionOut="'Place order · ₹150' → blue commit wipe → 'Waiting for the seller', settled at identity.",
 handoffIn=handoff(screen='checkout/01-confirm-cash.png', rig_=rigobj(FK), notes='Same frame as s08 ends: camera at Fcard, nothing on canvas.'),
 handoffOut=handoff(screen='order-cash/01-placed.png', notes="Order thread 'Waiting for the seller' at identity; the second phone, branch type, wipe and kicker are gone."),
 demoBadge=[],
 soundCues=[(0.85, 'Ring swish (cash)'), (1.60, 'Ring swish (QR)'), (2.55, 'Dual-phone slide whoosh'), (4.60, 'Soft timer tick'),
            (5.85, "UI tap (I've paid)"), (7.70, 'Soft confirm ping (stall confirms)'), (9.20, 'Whoosh out'), (10.85, 'UI tap (Place order)'),
            (11.20, 'Warm confirm swell into the order')],
 accuracyNotes="""- Cash copy is quoted ('Hand ₹150 to the seller at your door.'); the dark card line 'SETU does not collect this. Southside Tiffins receives it directly.' is the app's.
- 'Pay by QR' appears only when the stall has a QR on file (cash on delivery is always offered; the seeded stalls have none, the prepared demo stall has one), so the branch heading says 'IF THE STALL OFFERS QR'.
- QR order of events: the stall accepts first, then its own QR appears in the order thread with a five-minute window; 'I've paid' → 'Seller is checking your payment' → the stall confirms ('The stall confirmed your payment.'). Never 'pay first' or 'QR at checkout'. Order status and payment status stay separate: step 1 rings the headline 'Pay to continue', never the thread pill 'Order confirmed by Southside Tiffins' (the app's premature 'confirmed' wording, shown before payment); 'Order confirmed' is featured only at step 3.
- The QR is the labelled demo QR (capture/make-demo-qr.mjs encodes a plain sentence, not a UPI address). Its in-capture 'DEMO QR' pill and 'Not a real payment code' line are too small to read at k 1.08 (≈7 px and ≈6.5 px lettering), so the overlay tag 'DEMO QR · NOT A REAL PAYMENT CODE' is the legible label: it enters with the QR phone (3.10) and leaves with it (9.20–9.60). Never trim it. Nothing implies money moved.
- The QR phone is a separate demo order (CE1013-VGKQ), framed as 'if the stall offers QR'; Aarav's order (CE1013-BCQK) continues with cash.
- Both QR states that carry text ('Seller is checking your payment', 'Order confirmed') are held settled for 1.25 s.
- No pickup option exists and nothing suggests one.""",
)

# ---------------------------------------------------------------- s10
FH = 'Fhand'
scene(
 id='s10', compositionName='track-handover', title='Track it, then hand over cash and the code', chapter='08 · Track & hand over', dur=12.0,
 captions=[(0.20, 4.95, 'Now follow along:\nconfirmed, cooking, on the way.'),
           (5.40, 8.60, 'At the door, Aarav pays ₹150 in cash.'),
           (8.70, 11.80, 'Then he tells them his code.\nOrder complete.')],
 onScreenText=[
  ('08 · Track & hand over', 0.10, 11.90, 'kicker (kit .kicker)'),
  ('TIME-LAPSE', 0.20, 5.40, 'tag (tag row at (140,112): Lucide fast-forward + Space Mono 700 18 px caps)'),
  ('STATUS TIMELINE · NOT A MAP', 0.20, 11.90, 'rail header (Space Mono 700 18 px caps, #B8C7FF)'),
  ('Placed · Confirmed · Preparing · Ready · Out for delivery · Delivered', 0.20, 11.90, "status rail rows (Plus Jakarta Sans 600 28 px; the progress view's exact labels)"),
  ('HANDOVER CODE', 7.05, 8.25, 'label (short caps, Space Mono 700 18 px, callout lane)'),
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
6.10–7.00 orange ring on 'Please pay ₹150 in cash', measured box {{x:25,y:455,w:340,h:34}} (canvas {bx(FH,(25,455,340,34))}), fading 7.00–7.35.
7.00–7.95 orange ring (look here; the code is never tapped) on order-cash/07-on-the-way-code.code (canvas {bx(FH,(25,498.8,340,48))}), fading 7.95–8.30, + label 'HANDOVER CODE' (≈209×38) at x 880–1089, y 464–502, in 7.05 (0.3 s), out 7.95–8.25 (both gone before the 8.30 swap moves the code 18 px down); leader (1089,483)→(1167.9,483).
8.30 K.swapFade → order-cash/08-cash-confirmed.png (0.25 s; the stall tapped 'Yes, cash received'; its panel sits 18 px lower, the camera stays).
8.60–9.80 green ring on 'The stall has confirmed your ₹150 cash payment', measured box {{x:25,y:473,w:340,h:34}} (canvas {bx(FH,(25,473,340,34))}).
9.60–11.10 orange ring on order-cash/08-cash-confirmed.code (canvas {bx(FH,(25,517,340,48))}) and on 'Now tell them this code — that completes your order.', measured box {{x:25,y:576,w:310,h:18}}. 9.80–11.10 three concentric 2 px pale (#B8C7FF) arcs ripple once each, 0.35 s apart — the code is said out loud: all centred at canvas (1080,516) (level with the code), radii 20/34/48 px, each spanning 140°–220° (the LEFT side of its circle, angles from +x), so they bulge left, away from the phone, like '(((' — they occupy x ≈ 1032–1065, y ≈ 485–547, clear of the Fhand bezel (x ≈ 1098).
11.10–11.90 K.unfocus (0.8 s).
11.30 K.swapSheet → order-cash/09-delivered-review.png (sheetTop 412, 0.55 s; the stall entered the right code — no customer tap); the rail's 'Delivered' row lights with a soft orange flash.
11.55–11.90 the rail and the kicker fade out. 11.90–12.00 hold at identity.""",
 transitionIn="Continuous from s09's commit wipe: 'Waiting for the seller' at identity.",
 transitionOut="The review sheet rises over 'Delivered'; settled at identity for the cut.",
 handoffIn=handoff(screen='order-cash/01-placed.png', notes='Same frame as s09 ends.'),
 handoffOut=handoff(screen='order-cash/09-delivered-review.png', notes="'Delivered' with the review sheet up ('How was Southside Tiffins?') at identity; rail, tag, label and kicker gone."),
 demoBadge=[],
 soundCues=[(0.40, 'Status tick (Placed)'), (1.20, 'Tick + soft chime (Confirmed)'), (2.40, 'Tick (Preparing)'), (3.60, 'Tick (Ready)'),
            (4.80, 'Tick (Out for delivery) + light whoosh'), (7.00, 'Code shimmer'), (8.30, 'Soft ping (cash confirmed)'),
            (9.80, 'Two soft voice-arc pulses'), (11.30, 'Sheet slide + gentle success chord (Delivered)')],
 accuracyNotes="""- Status headlines are the app's own ('Waiting for the seller', 'Order confirmed', 'Being cooked now', 'Ready', 'On the way'); the rail uses the progress view's labels (Placed, Confirmed, Preparing, Ready, Out for delivery, Delivered).
- The TIME-LAPSE tag is on for the whole status run: the real order took 7:02 → 7:25 pm. 'Being prepared · usually ready by 7:24 pm' is a prep target — shown in the capture, never featured or narrated; no delivery-time promise.
- Tracking is a status timeline in the order thread, not a map ('STATUS TIMELINE · NOT A MAP' paraphrases Step 4's 'You will see a status timeline, not a rider on a map.'). No live map or location tracking anywhere.
- Handover order is real: cash first ('Please pay ₹150 in cash' → 'The stall has confirmed your ₹150 cash payment'), then the code completes it ('Now tell them this code — that completes your order.'). 'Them' = the stall owner or the delivery partner, as the app says.
- The handover code in 07/08 is 806688 as captured; never type it into captions or overlays; don't alter the captured times.""",
)

# ---------------------------------------------------------------- s11
scene(
 id='s11', compositionName='rate-report', title='Delivered, rated — and reportable', chapter='09 · Rate & report', dur=5.8,
 captions=[(0.10, 2.50, 'Delivered. Five stars\nfor Southside Tiffins.'),
           (2.60, 3.95, 'Dinner, sorted.'),
           (4.05, 5.75, 'Something off? Tap “Report”.')],
 onScreenText=[
  ('09 · Rate & report', 0.10, 5.70, 'kicker (kit .kicker)'),
  ('TO SETU STAFF', 4.30, 5.70, 'label (short caps, Space Mono 700 18 px, callout lane)'),
 ],
 shots=[
  ('order-cash/09-delivered-review.png', 0.0, 1.30, "Frame 0: 'How was Southside Tiffins?'; tap the 5th star (0.60)."),
  ('order-cash/10-review-5.png', 0.95, 3.25, "Circular reveal from the 5th star: five stars, 'Excellent'; tap 'Submit review' (2.45)."),
  ('order-cash/12-review-sent.png', 2.80, 5.80, "The sheet slides down: the thread ends 'Delivered · handover code verified · ₹150 paid in cash'; ring 'Report' + 'TO SETU STAFF'; holds to the cut."),
 ],
 uiState="Delivered order: review sheet 'How was Southside Tiffins?' (1 × Masala Dosa · 2 × Filter Coffee) → 5 stars 'Excellent' → 'Submit review' → the thread ends 'Delivered · handover code verified · ₹150 paid in cash' with 'Report' / 'Order again' in the bar.",
 animation=f"""Local times. Frame 0 = order-cash/09-delivered-review.png at identity; the scene stays at identity (no push on the review sheet, so its note placeholder is never featured).
0.10 kicker '09 · Rate & report' K.fadeUp at (140,200).
0.35 ring--blue on the 5th star, measured box {{x:292,y:514,w:36,h:36}} (inside order-cash/09-delivered-review.stars). 0.60 K.tap the 5th star (centre (310,532)) → 0.95 circular reveal of order-cash/10-review-5.png from (310,532), r 0 → 330 (0.35 s): five stars fill and 'Excellent' appears (the farthest changed pixel, the Submit button's corner, is 317 px away); 1.30 set the full 10 layer visible.
1.35–2.35 orange ring on order-cash/10-review-5.word ('Excellent').
2.20 ring--blue on order-cash/09-delivered-review.submit. 2.45 K.tap submit ('Submit review') → 2.80 the sheet closes: order-cash/12-review-sent.png sits underneath; the 10 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 432px 0)) fades out (0.35 s) while its sheet part (clip-path inset(412px 0 0 0)) slides y 0 → +432 (expo.in 0.45 s, done 3.25).
3.30–4.30 orange ring on the thread's last line 'Delivered · handover code verified · ₹150 paid in cash', measured box {{x:14,y:484,w:362,h:32}}, fading 4.30–4.65.
4.25 orange ring on the 'Report' button, measured box {{x:18,y:720,w:170,h:48}} (canvas {bx(None,(18,720,170,48))}) until 5.35 (fading 5.35–5.70) + label 'TO SETU STAFF' (≈209×38) at x 911–1120, y 795–833, in 4.30 (0.3 s), out 5.40–5.70; leader (1120,814)→(1183.4,880) — the label stays above the caption zone. Report is pointed at, not tapped (the caption names the button).
5.40–5.70 the kicker fades out. 5.70–5.80 hold on order-cash/12-review-sent.png.""",
 transitionIn='Continuous: the review sheet is already up.',
 transitionOut="The completed thread holds at identity with nothing on canvas; s12 opens by pulling the phone back.",
 handoffIn=handoff(screen='order-cash/09-delivered-review.png', notes='Same frame as s10 ends.'),
 handoffOut=handoff(screen='order-cash/12-review-sent.png', notes="Thread ending 'Delivered · handover code verified · ₹150 paid in cash' with 'Report' / 'Order again', at identity; rings, label and kicker gone."),
 demoBadge=[],
 soundCues=[(0.60, 'Star tap: rising five-note arpeggio'), (2.45, 'UI tap (Submit review)'), (2.80, 'Sheet slides down'),
            (3.30, 'Soft confirm ping'), (4.25, 'Ring swish (Report)')],
 accuracyNotes="""- Review copy: 'How was Southside Tiffins?'; five stars → 'Excellent'; 'Submit review'. The note is optional, 'Don't ask again' exists, and a rating can be given later from Orders.
- 11-review-note.png is not used (its note says 'On time.'); the camera never features the note placeholder ('Hot, on time…'): the scene stays at identity.
- 'Delivered · handover code verified · ₹150 paid in cash' is the app's own line.
- 'Report' exists on ended orders; reports go to SETU campus staff as a record against the stall (not a refund claim against SETU). The label says 'TO SETU STAFF' — never just 'campus staff', which the film's audience line ('students, faculty, staff') could make read as general IIT staff.
- The progress view (13-progress-delivered) is no longer shown: the beat was too short to read, and its time pays for the saved-Home pick in s07.
- 'Dinner, sorted.' is story copy, not a product claim.""",
)

# ---------------------------------------------------------------- s12
DISCLAIMER = ('SETU connects customers with approved campus food providers. Food preparation, delivery and payment are handled by the '
              'respective provider. SETU does not collect payments or independently guarantee food hygiene.')
scene(
 id='s12', compositionName='end-card', title='End card', chapter=None, dur=8.0,
 captions=[],
 onScreenText=[
  ('Your campus. Your food. Your SETU.', 0.80, 8.00, "tagline (Sora 800 64 px, centred; 'Your SETU.' in #B8C7FF; no rupee sign)"),
  ('Explore SETU Food', 1.20, 8.00, 'CTA pill (Plus Jakarta Sans 700 30 px #0033DA on white, Lucide arrow-right)'),
  (DISCLAIMER, 1.50, 8.00, 'disclaimer (verbatim; Plus Jakarta Sans 500 26 px; fully legible 1.95–8.00 = 6.05 s)'),
  ('Demo environment · sample stalls · demo QR, not a real payment code', 1.70, 8.00, 'fine print (Space Mono 400 18 px, 60% white)'),
 ],
 shots=[
  ('order-cash/12-review-sent.png', 0.0, 0.80, 'The phone pulls back (scale 1 → 0.72, sinks 60 px) and fades out.'),
  ('graphic:real campus boundary outline, faint (assets/data/campus-boundary.json)', 0.20, 8.00, 'Redraws at 18% opacity behind the type (x 480–1440, y 150–646); the Nehru Hall point glows once at (589.6,244.8), clear of all type.'),
  ('graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)', 0.40, 8.00, 'Tile 240×190 centred at (960,215); lockup 200 px wide, never recoloured.'),
  ('graphic:end-card type (tagline, CTA, disclaimer, fine print)', 0.80, 8.00, 'Kinetic type only.'),
 ],
 uiState='No app UI after 0.80 s: end-card motion graphics.',
 animation="""Local times. Frame 0 = order-cash/12-review-sent.png at identity. No captions in this scene (layout.json lists it as centred anyway); keep y 880–1050 empty.
0.00–0.80 the phone recedes: fromTo scale 1 → 0.72 (transform-origin its centre, canvas (1374.6,539.8)), y 0 → +60, opacity 1 → 0 (expo.in 0.8 s).
0.20–1.20 the real campus outline (assets/data/campus-boundary.json path) redraws centred, 960 px wide (scale 0.96): left 480, top 150 → x 480–1440, y 150–645.7; stroke #B8C7FF 2 px at 18% opacity (K.drawPath 1.0 s). 1.00–1.60 the Nehru Hall point (file (114.2,98.8) → canvas (589.6,244.8): left of the logo tile and above the tagline, clear of all type) glows once (8 px orange dot, opacity 0 → 1 → 0.6) and stays at 0.6.
0.40–1.00 white tile (kit .white-tile, 240×190, radius 32) centred at (960,215) → x 840–1080, y 120–310, with assets/brand/setu-logo.png at 200 px wide, centred: fromTo scale 0.94/opacity 0 → 1/1 (expo.out 0.6 s).
0.80 tagline 'Your campus. Your food. Your SETU.' (Sora 800 64 px, white, centred, top 350; 'Your SETU.' in #B8C7FF) K.revealWords (stagger 0.06).
1.20 CTA pill 'Explore SETU Food' (white, radius 999, padding 16/30, Plus Jakarta Sans 700 30 px #0033DA, Lucide arrow-right 26 px) centred, top 460: fromTo scale 0.9/opacity 0 → 1/1 (back.out(1.6) 0.5 s).
1.50–1.95 the disclaimer (verbatim) fades up: Plus Jakarta Sans 500 26 px / 1.45, rgba(255,255,255,.88), centred, max-width 1200 px (3 lines), top 580 (≈ y 580–693).
1.70–2.00 fine print 'Demo environment · sample stalls · demo QR, not a real payment code' (Space Mono 400 18 px, rgba(255,255,255,.6), centred, top 760) fades in.
After 2.00 nothing moves. Hold the complete card to 8.00 (no fade to black).""",
 transitionIn='The phone recedes into the indigo as the campus outline redraws faintly.',
 transitionOut='Hold to the last frame (no fade) so the owner can add sound or an outro.',
 handoffIn=handoff(screen='order-cash/12-review-sent.png', notes='Same frame as s11 ends.'),
 handoffOut=handoff(phone='none', overlays='End card (final frame): faint campus outline with the Nehru Hall dot, lockup tile, tagline, CTA pill, disclaimer and fine print.',
                    notes='Last frame of the film.'),
 demoBadge=[],
 soundCues=[(0.0, 'Pad swell resolves'), (0.40, 'Brand sting placeholder (owner\'s choice)'), (1.20, 'Soft pop (CTA)'), (7.80, 'Pad tail out')],
 accuracyNotes=f"""- The disclaimer is verbatim: '{DISCLAIMER}' It is fully legible from 1.95 s to the end (6.05 s), with no caption competing.
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
ANGLE = """STORY-FIRST ('Dinner at B-212'): one evening with Aarav (Nehru Hall of Residence, Room B-212). Tonight he signs in on a new phone with an emailed one-time code (DEMO-labelled; the password stays the main way in). A band wipe rewinds to his day one to show how a first-timer creates an account and runs the four onboarding steps — that is how his Home (Room B-212) was saved inside the campus boundary. A second band wipe returns to tonight: the new phone's Home first reads 'Set your delivery location' (the delivery choice is stored per device; the saved addresses belong to the account), so he picks his saved Home with three real taps (Deliver-to row → 'Home' under SAVED LOCATIONS → 'Confirm location'); then 1 × Masala Dosa + 2 × Filter Coffee from Southside Tiffins; items ₹140 + the stall's own delivery charge ₹10 = ₹150 payable to the seller. The QR route is a labelled side branch for stalls that offer it (the stall accepts first, then you pay, then it confirms). Aarav pays cash at the door, his six-digit handover code completes the order, he rates it five stars, and the Report path is pointed out. Nine numbered chapters (01 Sign in … 09 Rate & report) keep first-timers oriented, and captions name the exact button where it helps. Tone: warm, plain, lightly playful ('Tonight: dosa.', 'Dinner, sorted.'), never hype; 'students, faculty, staff' is said once. Motif: the real campus-boundary polygon opens the film, returns as the delivery-area check and closes the end card.
GLOBAL SYSTEM (every scene):
- Frame: 1920×1080, 60 fps, silent. One HyperFrames sub-composition per scene with one paused GSAP timeline; kit.js helpers plus plain GSAP only. Scene roots are transparent over the shared indigo background from index.html (it already carries a faint drifting campus outline; never paint a background).
- Boundaries are HARD CUTS: frame 0 must equal handoffIn and the last frame must equal handoffOut. Unless a handoff says otherwise: phone at the default spec, rig identity, left column empty, no overlays, the named capture fully visible and settled.
- Phone: kit .phone at phoneSpec {left:1150, top:70, k:1.08}; screen origin canvas (1164,84), 421.2×911.5. At identity a screen point (x,y) is canvas (1164 + 1.08·x, 84 + 1.08·y). The phone, its capture layers and every in-screen overlay (rings, taps, reveals, halos, masks) live inside the scene rig (.rig, transform-origin 0 0). Camera = K.focus(tl, rig, K.toCanvas(spec, P[0], P[1]), s, t, dur, {to:{x:T[0], y:T[1]}}), expo.inOut, 0.8–1.2 s; framings are given as {s, P (screen px), T (canvas px)} and K.unfocus returns to identity. Canvas-level type, labels, leader lines, chips and tags sit OUTSIDE the rig; every canvas position in a spec already accounts for the rig state at that moment.
- Grid: text column x140–820 (kicker at (140,200), headline top 250, nothing below y 860); callout lane x840–1130 (label right edge ≤1120); right margin x1620–1880 (unused); one tag row at (140,112) for ONE tag at a time (DEMO badge, DAY ONE, TONIGHT, the sample-stalls note, TIME-LAPSE); caption zone x120–1140, y880–1050 stays empty (captions centred only in s01; s12 has none). A pushed phone's bezel never reaches left of x 1095, and left caption plates end at x ≈ 900. At most 4 floating labels/chips/tags at once, never overlapping the phone, each other, the text column or the caption zone. Never fly several objects into the phone at once: when chips travel into the phone they go one at a time.
- Type: kicker = kit .kicker showing the scene's `chapter`, K.fadeUp at 0.10; its fade-out (0.3 s) ends at least 0.05 s before the scene's last frame, and its onScreenText end time is the end of that fade. Headline = .headline--md (Sora 800, 68 px), words only. Sora has no ₹ glyph: every string containing ₹ is set in Plus Jakarta Sans (names, amounts) or Space Mono (labels, prices, counts). Labels = short caps tags: .callout.callout--dark with font 700 18px/1 Space Mono, letter-spacing .08em, uppercase, padding 10px 16px (≈ 12.24 px × chars + 50 px wide, 38 px tall), plus a 2 px rgba(184,199,255,.7) straight leader from the label's right edge to the element; a label's right edge stays ≥8 px left of the phone's bezel for the framing in use (identity ≤1140; s 1.4 ≤1097; Ftotals ≤1095; Fhand ≤1090; Fconf ≤1087). Tag-row items: Space Mono 700 18 px caps, letter-spacing .16em, pill padding 10/16; the DEMO badge is kit .demo-badge with the text 'Demo environment'.
- Overlays on real UI: K.tap at the centre of the named box, always 0.35 s before the screen change it causes (inside the 0.25–0.45 s rule). K.ring orange = look here; {blue:true} = the next tap target only (≥0.2 s before its tap; never on something that is not tapped); green = a kit ring with border-color #19B36B and a green glow, used only for 'inside the delivery area', 'cash confirmed' and 'payment confirmed'; pale = a kit ring with border-color #B8C7FF and box-shadow 0 0 0 6px rgba(184,199,255,.16), 0 0 22px rgba(184,199,255,.3): context that is never tapped (s03's code-box glow, s05's 'Use my current location' row). Boxes are CSS px of the 390×844 screen: named marks from marks.json written <group>/<shot>.<mark>, or explicit {x,y,w,h} measured on the final PNGs. Nothing opaque over app text; UI is never recoloured.
- Screen changes: K.swapPush = forward navigation (0.55 s); K.swapSheet = sheets (sheetTop given); K.swapFade = in-place state change (0.15–0.35 s); circular reveal = a local state change caused by a tap (the 'after' capture as a new layer whose clip-path circle(r at x y) grows from 0 at the tap point, 0.25–0.35 s, power2.out); commit wipe = for 'Start ordering' and 'Place order · ₹150' a #0033DA circle grows from the button centre to cover the screen (0.45 s, power2.in), the next capture is set underneath, then the circle fades (0.3 s).
- Clips: play inside a non-timed .layer in the screen (data-hf-media-start-basis="local"); never animate the <video>; the next still sits underneath to hold the last frame; chained clips start exactly where the previous ends. clipSeconds = the length used (a speed variant is pre-rendered; each captured frame gets clipSeconds / frames). Where a clip's last frame differs from the still under it only by input focus, the cut is a deliberate focus-loss cut (named in the scene).
- Shot windows: a shot starts when its layer first becomes visible and ends when it is fully covered or hidden, i.e. at the END of the transition that removes it.
- Rhythm: tap → result → ≥0.6 s beat; text that matters is held ≥1.2 s; exits 0.3–0.5 s; nothing is visible before its entrance (fromTo with opacity 0); no drifting, spinning, particles or glitch.
- Icons: Lucide line icons only (stroke 1.85–2.5); no emoji, food photos, clip-art or filled pins.
- Honesty: only real captures for app screens; DEMO badge across the whole OTP portion (code request → Home); the sample-stalls note once (s07) plus the end-card fine print; the demo QR stays labelled; no 'SETU delivers', pickup, map or location tracking, delivery-time promise, free/zero-cost/minimal-charge wording or competitor names anywhere. Never ring, zoom on or caption the app's own 'SETU delivers inside…' lines, the location dialog's body sentences ('…to find nearby stalls…', 'It is only read when you ask for it.' — the code contradicts both), Step 4's licence and 'Recorded…' sub-lines, search rows' '20–20 min', the stall's '20 min', the prep time, the QR thread pill 'Order confirmed by …' (shown before payment), 33-home-set's hover-blue 'Orders' tab or the review note placeholder."""

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
              'the disclaimer must have the frame to itself); those scenes keep y 900–1050 empty across the whole width. A pushed phone\'s outer (bezel) left edge stays at '
              'x ≥ 1095 (F1/Fcreate/Fcard 1105.6, Ftotals 1103.1, Fhand 1098.2, Fconf 1095.7), and the widest left caption plate ends at x ≈ 900, so a pushed phone never sits '
              'under a caption. A "\\n" in a caption is the intended line break (one plate per line).'),
}
if '--write' in sys.argv:
    with open(OUT + '/scene-timing.json', 'w', encoding='utf-8') as fh:
        json.dump(final, fh, ensure_ascii=False, indent=2); fh.write('\n')
    with open(OUT + '/layout.json', 'w', encoding='utf-8') as fh:
        json.dump(layout, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print('wrote', OUT)
