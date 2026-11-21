# Dinner at B-212 — a SETU Food walkthrough — storyboard

Angle: STORY-FIRST ('Dinner at B-212'): one evening with Aarav (Nehru Hall of Residence, Room B-212). Tonight he signs in on a new phone with his email and the six-digit code the app emails him. A band wipe rewinds to his day one to show how a first-timer creates a User account and runs the four onboarding steps — that is how his Home (Room B-212) was saved inside the campus boundary. A second band wipe returns to tonight: the new phone's Home first reads 'Set your delivery location' (the delivery choice is stored per device; the saved addresses belong to the account), so he picks his saved Home with three real taps (Deliver-to row → 'Home' under SAVED LOCATIONS → 'Confirm location'); then 1 × Masala Dosa + 2 × Filter Coffee from Southside Tiffins; items ₹140 + the stall's own delivery charge ₹10 = ₹150 payable to the seller. The UPI route is a labelled side branch for stalls that offer it (the stall accepts first, one tap opens the user's own UPI app — or they scan the stall's QR — then the stall confirms). Aarav pays cash at the door, his six-digit handover code completes the order, he rates it five stars, and the Report path is pointed out. Nine numbered chapters (01 Sign in … 09 Rate & report) keep first-timers oriented, and captions name the exact button where it helps. Tone: warm, plain, lightly playful ('Tonight: dosa.', 'Dinner, sorted.'), never hype. The app calls its people users: a User account, never 'customer'. Motif: the real campus-boundary polygon opens the film, returns as the delivery-area check and closes the end card.
GLOBAL SYSTEM (every scene):
- Frame: 1920×1080, 60 fps, silent. One HyperFrames sub-composition per scene with one paused GSAP timeline; kit.js helpers plus plain GSAP only. Scene roots are transparent over the shared indigo background from index.html (it already carries a faint drifting campus outline; never paint a background).
- Boundaries are HARD CUTS: frame 0 must equal handoffIn and the last frame must equal handoffOut. Unless a handoff says otherwise: phone at the default spec, rig identity, left column empty, no overlays, the named capture fully visible and settled.
- Phone: kit .phone at phoneSpec {left:1150, top:70, k:1.08}; screen origin canvas (1164,84), 421.2×911.5. At identity a screen point (x,y) is canvas (1164 + 1.08·x, 84 + 1.08·y). The phone, its capture layers and every in-screen overlay (rings, taps, reveals, halos, masks) live inside the scene rig (.rig, transform-origin 0 0). Camera = K.focus(tl, rig, K.toCanvas(spec, P[0], P[1]), s, t, dur, {to:{x:T[0], y:T[1]}}), expo.inOut, 0.8–1.2 s; framings are given as {s, P (screen px), T (canvas px)} and K.unfocus returns to identity. Canvas-level type, labels, leader lines, chips and tags sit OUTSIDE the rig; every canvas position in a spec already accounts for the rig state at that moment.
- Grid: text column x140–820 (kicker at (140,200), headline top 250, nothing below y 860); callout lane x840–1130 (label right edge ≤1120); right margin x1620–1880 (unused); one tag row at (140,112) for ONE tag at a time (DAY ONE, TONIGHT, the sample-stalls note, TIME-LAPSE); caption zone x120–1140, y880–1050 stays empty (captions centred only in s01; s12 has none). A pushed phone's bezel never reaches left of x 1095, and left caption plates end at x ≈ 900. At most 4 floating labels/chips/tags at once, never overlapping the phone, each other, the text column or the caption zone. Never fly several objects into the phone at once: when chips travel into the phone they go one at a time.
- Type: kicker = kit .kicker showing the scene's `chapter`, K.fadeUp at 0.10; its fade-out (0.3 s) ends at least 0.05 s before the scene's last frame, and its onScreenText end time is the end of that fade. Headline = .headline--md (Sora 800, 68 px), words only. Sora has no ₹ glyph: every string containing ₹ is set in Plus Jakarta Sans (names, amounts) or Space Mono (labels, prices, counts). Labels = short caps tags: .callout.callout--dark with font 700 18px/1 Space Mono, letter-spacing .08em, uppercase, padding 10px 16px (≈ 12.24 px × chars + 50 px wide, 38 px tall), plus a 2 px rgba(184,199,255,.7) straight leader from the label's right edge to the element; a label's right edge stays ≥8 px left of the phone's bezel for the framing in use (identity ≤1140; s 1.4 ≤1097; Ftotals ≤1095; Fhand ≤1090; Fconf ≤1087). Tag-row items: Space Mono 700 18 px caps, letter-spacing .16em, pill padding 10/16; the DEMO badge is kit .demo-badge with the text 'Demo environment'.
- Overlays on real UI: K.tap at the centre of the named box, always 0.35 s before the screen change it causes (inside the 0.25–0.45 s rule). K.ring orange = look here; {blue:true} = the next tap target only (≥0.2 s before its tap; never on something that is not tapped); green = a kit ring with border-color #19B36B and a green glow, used only for 'inside the delivery area', 'cash confirmed' and 'payment confirmed'; pale = a kit ring with border-color #B8C7FF and box-shadow 0 0 0 6px rgba(184,199,255,.16), 0 0 22px rgba(184,199,255,.3): context that is never tapped (s03's code-box glow, s05's 'Use my current location' row). Boxes are CSS px of the 390×844 screen: named marks from marks.json written <group>/<shot>.<mark>, or explicit {x,y,w,h} measured on the final PNGs. Nothing opaque over app text; UI is never recoloured.
- Screen changes: K.swapPush = forward navigation (0.55 s); K.swapSheet = sheets (sheetTop given); K.swapFade = in-place state change (0.15–0.35 s); circular reveal = a local state change caused by a tap (the 'after' capture as a new layer whose clip-path circle(r at x y) grows from 0 at the tap point, 0.25–0.35 s, power2.out); commit wipe = for 'Start ordering' and 'Place order · ₹150' a #0033DA circle grows from the button centre to cover the screen (0.45 s, power2.in), the next capture is set underneath, then the circle fades (0.3 s).
- Clips: play inside a non-timed .layer in the screen (data-hf-media-start-basis="local"); never animate the <video>; the next still sits underneath to hold the last frame; chained clips start exactly where the previous ends. clipSeconds = the length used (a speed variant is pre-rendered; each captured frame gets clipSeconds / frames). Where a clip's last frame differs from the still under it only by input focus, the cut is a deliberate focus-loss cut (named in the scene).
- Shot windows: a shot starts when its layer first becomes visible and ends when it is fully covered or hidden, i.e. at the END of the transition that removes it.
- Rhythm: tap → result → ≥0.6 s beat; text that matters is held ≥1.2 s; exits 0.3–0.5 s; nothing is visible before its entrance (fromTo with opacity 0); no drifting, spinning, particles or glitch.
- Icons: Lucide line icons only (stroke 1.85–2.5); no emoji, food photos, clip-art or filled pins.
- Honesty: only real captures for app screens; the emailed one-time code is a released sign-in method (no DEMO badge; the code came from the isolated demo stack's local inbox for the demo persona); the sample-stalls note once (s07) plus the end-card fine print; the demo QR and its demo UPI ID stay labelled; the user's UPI app is never drawn (the hand-off is an editorial callout); no 'SETU delivers', pickup, map or location tracking, delivery-time promise, free/zero-cost/minimal-charge wording or competitor names anywhere. Never ring, zoom on or caption the app's own 'SETU delivers inside…' lines, the location dialog's body sentences ('…to find nearby stalls…', 'It is only read when you ask for it.' — the code contradicts both), Step 4's licence and 'Recorded…' sub-lines, search rows' '20–20 min', the stall's '20 min', the prep time, the QR thread pill 'Order confirmed by …' (shown before payment), 33-home-set's hover-blue 'Orders' tab or the review note placeholder.

1920x1080 · 60 fps · 1:58.8 · 12 scenes · 233 narration words · 35 captions

| Scene | Time | Title | Real UI shown |
| --- | --- | --- | --- |
| s01 | 0:00.0–0:05.4 | Hook — your campus, your food | `graphic:real campus boundary outline (assets/data/campus-boundary.json) with the Nehru Hall pin`<br>`graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)`<br>`graphic:hook type (SETU Food title, subline, persona chip)` |
| s02 | 0:05.4–0:12.0 | What SETU does | `desktop/01-signin-wide.png`<br>`signin/01-signin.png` |
| s03 | 0:12.0–0:21.1 | Have an account? Sign in with your email and a code | `signin/01-signin.png`<br>`signin/02-type-email/`<br>`signin/03-email-typed.png`<br>`signin/04-enter-code.png`<br>`signin/email-otp.png`<br>`signin/05-type-code/`<br>`signin/06-code-entered.png`<br>`signin/07-home.png` |
| s04 | 0:21.1–0:31.1 | New here? Create a User account | `signin/07-home.png`<br>`graphic:editorial rewind band (full-height indigo band, orange leading edge)`<br>`onboarding/01-signin.png`<br>`onboarding/02-signup-empty.png`<br>`onboarding/03-type-name/`<br>`onboarding/04-type-email/`<br>`onboarding/05-type-phone/`<br>`onboarding/06-type-password/`<br>`onboarding/07-signup-filled.png`<br>`onboarding/10-step1-identity.png`<br>`onboarding/21-step2-prompt.png` |
| s05 | 0:31.1–0:47.1 | Where should orders arrive? | `onboarding/21-step2-prompt.png`<br>`location/01-allow-dialog.png`<br>`location/10-picker-select.png`<br>`location/11-type-search/`<br>`location/12-search-results.png`<br>`location/13-confirm-search.png`<br>`location/20-map.png`<br>`location/13-confirm-search.png`<br>`location/14-type-room/`<br>`location/15-confirm-home.png`<br>`onboarding/23-step2-done.png`<br>`graphic:pin → address card (Lucide outline map-pin, dotted trail left of the bezel, glass card)` |
| s06 | 0:47.1–0:56.7 | Your picks — and three things SETU does not do | `onboarding/23-step2-done.png`<br>`onboarding/30-step3.png`<br>`onboarding/31-step3-picked.png`<br>`onboarding/40-step4.png`<br>`onboarding/41-step4-ack.png`<br>`home/01-first-home.png`<br>`graphic:commit wipe (#0033DA circle from the Start ordering button)` |
| s07 | 0:56.7–1:10.3 | Back to tonight — saved Home, then dosa from Southside Tiffins | `home/01-first-home.png`<br>`graphic:editorial return band (right → left)`<br>`location/30-home-unset.png`<br>`location/31-picker-saved.png`<br>`location/32-confirm-saved.png`<br>`location/33-home-set.png`<br>`search/01-search-empty.png`<br>`search/02-type-dosa/`<br>`search/03-results.png`<br>`stall/01-stall.png`<br>`stall/02-dosa-added.png`<br>`stall/04-coffee.png`<br>`stall/05-coffee-two.png` |
| s08 | 1:10.3–1:19.5 | Cart — ₹150, payable to the seller | `stall/05-coffee-two.png`<br>`cart/01-cart.png`<br>`checkout/01-confirm-cash.png` |
| s09 | 1:19.5–1:33.0 | Pay the stall directly — cash, or online via UPI | `checkout/01-confirm-cash.png`<br>`order-qr/02-pay-upi.png`<br>`order-qr/03-upi-opening.png`<br>`order-qr/04-upi-back.png`<br>`order-qr/05-payment-review.png`<br>`order-qr/06-payment-confirmed.png`<br>`graphic:hand-off callout 'YOUR UPI APP OPENS · ₹150 FILLED IN' + leader, and a dark dim over the UPI phone's screen`<br>`order-cash/00-confirm.png`<br>`order-cash/01-placed.png`<br>`graphic:commit wipe (#0033DA circle from the Place order button)` |
| s10 | 1:33.0–1:45.0 | Track it, then hand over cash and the code | `order-cash/01-placed.png`<br>`order-cash/02-accepted.png`<br>`order-cash/04-preparing.png`<br>`order-cash/06-ready.png`<br>`order-cash/07-on-the-way-code.png`<br>`order-cash/08-cash-confirmed.png`<br>`order-cash/09-delivered-review.png`<br>`graphic:status rail (the app's six progress labels)` |
| s11 | 1:45.0–1:50.8 | Delivered, rated — and reportable | `order-cash/09-delivered-review.png`<br>`order-cash/10-review-5.png`<br>`order-cash/12-review-sent.png` |
| s12 | 1:50.8–1:58.8 | End card | `order-cash/12-review-sent.png`<br>`graphic:real campus boundary outline, faint (assets/data/campus-boundary.json)`<br>`graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)`<br>`graphic:end-card type (tagline, CTA, disclaimer, fine print)` |

## s01 · Hook — your campus, your food

**Time** 0:00.0 → 0:05.4 (5.4 s)

**Narration** Your campus. Your food. A simpler way to order. Meet Aarav, Nehru Hall.

**On-screen text**
- 0:01.7–0:05.3 · *title (Sora 800, 84 px, white, centred under the lockup tile; no rupee sign)* · SETU Food
- 0:02.1–0:05.3 · *subline (Space Mono 700, 18 px caps, #B8C7FF, centred)* · ON SETU SERVICES · IIT KHARAGPUR
- 0:03.9–0:05.3 · *persona chip beside the Nehru Hall pin (Space Mono 700, 20 px)* · Aarav · Room B-212

**UI state** No app UI: motion graphics built from real data (campus boundary polygon and its Nehru Hall point) plus the official SETU lockup.

**Shots**
- 0:00.0–0:05.4 · `graphic:real campus boundary outline (assets/data/campus-boundary.json) with the Nehru Hall pin` · Motion graphic from real data: the 78-point Main Campus Boundary path drawn 1000×516.4 at canvas (460,150); orange outline map-pin on the file's nehruHall point.
- 0:01.4–0:05.4 · `graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)` · Tile 260×206 centred at (960,360); lockup 216 px wide, downscaled only, never recoloured.
- 0:01.7–0:05.4 · `graphic:hook type (SETU Food title, subline, persona chip)` · Kinetic type only; the product is named by ≈2.6 s.

**Animation** Local times. Full-screen motion graphic, no phone. Captions are CENTRED in this scene (layout.json), so keep y 880–1050 empty across the width. The hook names the product early: 'SETU Food' is fully readable by ≈2.6 s.
Outline group (#s01-map): the real 'Main Campus Boundary' path from assets/data/campus-boundary.json (viewBox 0 0 1000 516.4) as an inline SVG 1000×516.4 at left 460, top 150 (x 460–1460, y 150–666). Stroke #B8C7FF 3 px, round joins, filter drop-shadow(0 0 10px rgba(130,160,255,.55)); fill rgba(46,91,238,.06) (starts at fill-opacity 0).
0.10–1.40 K.drawPath on the outline (1.3 s, power2.inOut). 0.90–1.50 the fill fades in.
1.00 Nehru Hall marker at the file's nehruHall point (114.2, 98.8) → canvas (574.2, 248.8): a Lucide map-pin (OUTLINE, stroke 2.5 px #EC5A2A, 40 px tall, tip on the point) fromTo y −60/opacity 0 → 0/1 (expo.out 0.45 s), plus an 8 px orange dot exactly on the point; 1.25–1.95 one 2 px orange ripple ring grows 0→80 px and fades.
1.40–2.10 the outline group tweens to opacity 0.30 (power2.out); the pin and dot stay at 100%.
1.40 white tile (kit .white-tile, 260×206, radius 32) centred at (960,360) → x 830–1090, y 257–463, holding assets/brand/setu-logo.png at 216 px wide (≈170 px tall), centred: fromTo scale 0.94/opacity 0 → 1/1 (expo.out 0.7 s).
1.70 title 'SETU Food' (Sora 800, 84 px, white, letter-spacing −.03em, centred, top 492) K.revealWords (stagger 0.08; 'Food' is fully in at ≈2.58).
2.10 subline 'ON SETU SERVICES · IIT KHARAGPUR' (Space Mono 700 18 px caps, letter-spacing .2em, #B8C7FF, centred, top 600) K.fadeUp.
3.85 persona chip 'Aarav · Room B-212' (Space Mono 700 20 px, white on rgba(12,18,51,.88), 1 px rgba(255,255,255,.18) border, radius 12, padding 10/16; ≈300×42) at left 604, top 196 (right of the pin head, clear of the tile): fromTo x −16/opacity 0 → 0/1 (expo.out 0.5 s).
4.95–5.35 exit: tile, title, subline and chip rise −16 px and fade (power2.in 0.4 s); outline, pin and dot fade (0.4 s). The frame at 5.35–5.40 is the empty shared background.

**Transition in** Cold open on the shared indigo background; the outline starts drawing at 0.10 s. · **out** Every hook element exits 4.95–5.35; the last frame is the empty background (hard cut; s02 starts empty).

**Captions**
- 0:00.2–0:03.7 · Your campus. Your food. / A simpler way to order.
- 0:03.8–0:05.3 · Meet Aarav, Nehru Hall.

**Sound cues (placeholders)**
- 0:00.0 · Placeholder bed: low warm pad fades in (owner replaces)
- 0:00.1 · Fine line-draw shimmer following the outline (1.3 s)
- 0:01.0 · Pin drop: short wooden tick
- 0:01.4 · Soft paper tick as the white logo tile lands
- 0:03.9 · Two-note soft chime for the Aarav chip
- 0:04.10 · Air whoosh out

**Accuracy notes** - The outline is the real 78-point 'Main Campus Boundary' (server campus-zone config, via assets/data/campus-boundary.json) and its nehruHall point; it is a motion graphic, never presented as a map screenshot.
- The lockup is the official raster on a WHITE rounded tile, downscaled only, never recoloured; the 75-years mark is not used.
- 'SETU Food' is the walkthrough's name for the Food service of SETU Services (the app's on-screen brand is 'SETU Services'; 'SETU Food' is the email brand and the CTA). It is set as plain title type under the tile, never fused into a logo, and the subline says 'on SETU Services'.
- No app UI is recreated (the Food / Commute / Utilities pills are not redrawn).
- The opening line is the owner's. 'Room B-212' is the demo persona's room (it appears later in the Home header).

## s02 · What SETU does

**Time** 0:05.4 → 0:12.0 (6.6 s)

**Narration** SETU Food lists approved stalls. They cook and deliver. You pay the stall directly. No commission.

**On-screen text**
- 0:05.5–0:10.8 · *kicker (kit .kicker)* · What SETU does

**UI state** Signed-out web sign-in page (desktop wide layout): art panel 'The campus, and only the campus.', the lede 'Discover approved campus food providers, order in a few simple steps, and pay the provider directly. No platform commission, with any applicable delivery charges shown before you place your order.' and the stats 'DELIVERY' over 'Campus only', 'COMMISSION' over 'None', 'PAYMENT' over 'Direct' (each with its icon); the form 'IIT KGP'S FOOD WITH ZERO COMMISSION' / 'Sign in with your User account'; then the phone's own sign-in screen (same heading).

**Shots**
- 0:05.4–0:11.6 · `desktop/01-signin-wide.png` · Kit .laptop frame (--lk .7, no browser/OS chrome) at left 760, top 150. Camera on the laptop rig: lede, then the stats row; rings; then a move that lands the desktop heading 'Sign in with your User account' on the phone's own heading for the dissolve.
- 0:11.2–0:12.0 · `signin/01-signin.png` · Phone at the default spec fades in over the aligned desktop form (web → phone dissolve) and holds.

**Animation** Local times. Two layers: #s02-rig-desk (a full-canvas .rig) holds the laptop; the phone is OUTSIDE it at the default spec and only appears at the end.
Laptop at rest: kit .laptop with --lk .7 showing desktop/01-signin-wide.png (an <img> filling .lscreen) at left 760, top 150 → lid x 760–1804, y 150–824; screen x 778–1786, y 168–798; base y 824–846. Desktop CSS (1440×900) → canvas at rest: X = 778 + 0.7·x, Y = 168 + 0.7·y. Rings below are drawn inside the laptop screen in desktop CSS px, so they scale with the camera.
0.00–0.80 the laptop fromTo y +90/opacity 0 → 0/1 (expo.out 0.8 s). 0.15 kicker 'What SETU does' K.fadeUp at (140,200).
0.70–1.70 camera: K.focus(desk rig, D(392,470), s 1.3, 0.70, 1.0, {to:{x:1110,y:420}}) — headline and lede fill the frame.
0.90–2.30 pale-indigo ring (2.5 px #B8C7FF, radius 10, no fill) around the lede's first phrase only: desktop box {x:60,y:455,w:397,h:34} 'Discover approved campus food providers,' (text measured in the page: x 65.8–450.9, y 460–483); both halves draw left → right.
2.10–3.10 camera: K.focus(desk rig, D(355,812), s 1.35, 2.10, 1.0, {to:{x:1080,y:520}}) — the stats row.
2.60–3.80 orange ring on 'DELIVERY' over 'Campus only', desktop {x:58,y:778,w:216,h:68}; 3.80–5.00 on 'COMMISSION' over 'None' {x:318,y:778,w:110,h:68}; 4.10–5.20 on 'PAYMENT' over 'Direct' {x:543,y:778,w:110,h:68}; one scale pulse each (labels and values are where they were; the new icons sit above them, unringed).
5.10–5.90 match move: K.focus(desk rig, D(895.8,138), s 1.1, 5.10, 0.8, {to:{x:1181.3,y:250.0}}) — the desktop heading 'Sign in with your User account' (desktop box {x:895.8,y:138,w:440,h:80.6}, two left-aligned lines) lands top-left on the phone's heading (signin/01-signin.title, screen (16,153.7) → canvas (1181.3,250.0)); s 1.1 keeps the laptop's base above the caption zone. 5.10–5.40 the kicker fades out.
5.75–6.15 the phone (default spec) fromTo scale 0.97/opacity 0 → 1/1 showing signin/01-signin.png; 5.70–6.20 the laptop blurs to 5 px and 5.85–6.20 fades out — a near-size dissolve (the two headings share their words and alignment; the desktop one is ≈0.88× the phone's size).
6.20–6.60 hold: phone at the default spec on signin/01-signin.png; the laptop is invisible (desk rig reset to identity); left column empty.

**Transition in** Starts on the empty background; the laptop rises 0.00–0.80. · **out** Web → phone dissolve on the shared heading 'Sign in with your User account' (top-left aligned, 5.10–6.20), then a 0.4 s settled hold on the phone.

**Captions**
- 0:05.5–0:09.1 · SETU Food lists approved stalls. / They cook and deliver.
- 0:09.2–0:11.9 · You pay the stall directly. / No commission.

**Sound cues (placeholders)**
- 0:05.4 · Card settle: soft low thud as the laptop rises
- 0:06.3 · Highlight swish (lede ring)
- 0:08.0 · Tiny tick (Campus only)
- 0:09.2 · Tiny tick (None)
- 0:09.5 · Tiny tick (Direct)
- 0:10.5 · Glassy whoosh on the web → phone dissolve

**Accuracy notes** - desktop/01-signin-wide.png is real UI shown in the kit's neutral laptop frame: no browser chrome, URL bar or OS UI.
- Ring only 'Discover approved campus food providers,' and the three stats.
- desktop/02-home-web.png is not used.
- 'They cook and deliver' = the stalls (app: 'The seller brings the order themselves'); never 'SETU delivers'. 'No commission' = the stat 'COMMISSION' over 'None' (and the lede's 'No platform commission').
- The panel's crest / 75-years row is never featured: both push-ins centre below it.

## s03 · Have an account? Sign in with your email and a code

**Time** 0:12.0 → 0:21.1 (9.1 s)

**Narration** Have an account? Sign in with your email. Tap “Email me a one-time code”. Six digits by email, and Aarav's in.

**On-screen text**
- 0:12.1–0:20.8 · *kicker (kit .kicker)* · 01 · Sign in
- 0:12.3–0:16.6 · *headline (.headline--md, Sora 800 68 px, two lines 'Your email,' / 'then a code.' with 'then a code.' in #B8C7FF; no rupee sign)* · Your email, then a code.
- 0:15.3–0:16.7 · *label (short caps, Space Mono 700 18 px, callout lane)* · EMAIL ME A CODE
- 0:16.9–0:20.1 · *mail-card head strip (Lucide mail icon + Space Mono 700 16 px)* · Your sign-in code · by email

**UI state** Signed-out phone sign-in ('IIT KGP'S FOOD WITH ZERO COMMISSION', 'Sign in with your User account', 'Mobile number or email', Password, 'Email me a one-time code instead') → email typed → 'Enter the code' under 'SIGNING IN AS User' (sent to aa***@kgpian.iitkgp.ac.in, 'It expires in 10 minutes.') → six digits entered → Home on a fresh device ('Set your delivery location' over 'Tap to pick it on the map'; 'Good evening, Aarav').

**Shots**
- 0:12.0–0:13.6 · `signin/01-signin.png` · Phone at the default spec; camera F1 from 0.30; ring on 'User account' (the heading's second line) 0.60; tap id at 1.20.
- 0:13.6–0:15.1 · `signin/02-type-email/` · Typing clip, clipSeconds 1.56: 'aarav.demo@kgpian.iitkgp.ac.in' into the id field.
- 0:15.1–0:17.0 · `signin/03-email-typed.png` · Still under the clip, then held (deliberate focus-loss cut at 3.11); ring--blue + label 'EMAIL ME A CODE' on otpLink 3.25; tap 4.10; pushes out 4.45–5.00.
- 0:16.4–0:18.5 · `signin/04-enter-code.png` · swapPush in; ring sentTo ('We emailed a six-digit code to aa***@kgpian.iitkgp.ac.in. It expires in 10 minutes.') 5.00.
- 0:16.9–0:20.1 · `signin/email-otp.png` · Mail card in the left column (left 590, top 400, width 480): the real sign-in email cropped to email CSS x12–378, y196–412 (the code box, the expiry line and 'Never share this code…'; the template's greeting line is left out) under a plain head strip; code-box glow; light trails to the phone.
- 0:18.1–0:19.3 · `signin/05-type-code/` · Typing clip, clipSeconds 1.2 (7 frames × 0.1714 s): the six digits, synced to the light trails.
- 0:19.3–0:20.4 · `signin/06-code-entered.png` · Still under the clip, then held; ring--blue + tap 'Verify and continue' (7.75).
- 0:20.1–0:21.1 · `signin/07-home.png` · swapFade in 8.10–8.40; camera back to identity by 9.00; fresh-device Home ('Set your delivery location').

**Animation** Local times. Phone at the default spec from frame 0 (handoffIn). Camera framing F1 = {s 1.4, P [195,236], T [1420,200]}: header logos (screen y<100) stay off-frame; visible screen y≈104–818; canvas of a screen point = (1125.16 + 1.512·x, −156.86 + 1.512·y).
0.10 kicker '01 · Sign in' K.fadeUp at (140,200). 0.30 headline 'Your email,' / 'then a code.' (.headline--md, top 250, width 680; 'then a code.' in #B8C7FF) K.revealWords. 0.30–1.30 K.focus F1 (1.0 s).
0.60–1.60 orange ring (radius 12) on the heading's second line 'User account', measured box {x:9,y:182,w:174,h:33} (signin/01-signin.title holds both lines).
1.20 K.tap signin/01-signin.id → 1.55 clip layer signin/02-type-email/ (clipSeconds 1.56) plays 1.55–3.11; signin/03-email-typed.png sits underneath and holds from 3.11 — a deliberate focus-loss cut.
3.25–4.10 ring--blue (radius 30) on signin/03-email-typed.otpLink, the full-width button 'Email me a one-time code instead' (canvas (1149.4,628.8)–(1690.6,701.4)); 3.30 label 'EMAIL ME A CODE' (≈230×38) right edge 1092, top 646, leader (1092,665)→(1140,665) drawn 3.40–3.70; label and leader fade 4.35–4.70.
4.10 K.tap signin/03-email-typed.otpLink → 4.45 K.swapPush → signin/04-enter-code.png (0.55 s). 4.20–4.60 the headline fades out.
4.90–5.50 mail card (kit .mailcard, width 480) at left 590, top 400: head strip 52 px = Lucide mail icon + 'Your sign-in code' + 'by email' (no sender, time, inbox or OS chrome); body = signin/email-otp.png cropped to email CSS x12–378, y196–412 at 1.3115× (480×283). Entrance fromTo x −40/opacity 0/rotate 1.5° → 0/1/0 (expo.out 0.6 s).
5.00–6.10 orange ring on signin/04-enter-code.sentTo. 5.50–6.10 pale glow ring around the email's code box (card-local top 64.75).
6.10–7.30 clip layer signin/05-type-code/ (clipSeconds 1.2); signin/06-code-entered.png underneath from 6.50. Six light trails, each from a card digit (canvas y 516.2) to its phone box (signin/04-enter-code.boxes, canvas y 310.4), finishing on the clip frame where that digit appears (frames 10, 22, 31, 41, 50, 62 → 6.267 … 7.133); the card digit lights as its trail leaves.
7.40 ring--blue on signin/06-code-entered.verify; 7.75 K.tap verify ('Verify and continue'); 7.75–8.15 the mail card leaves (x −60, opacity 0). 8.10 K.swapFade → signin/07-home.png (0.30 s); 8.10–9.00 K.unfocus. 8.50–8.80 the kicker fades out. 8.80–9.10 hold at identity.

**Transition in** Continuous from the web → phone dissolve: the phone is already at its default spec on the sign-in screen. · **out** Settles on fresh-device Home at identity with the left column empty; s04's rewind band opens on this frame.

**Captions**
- 0:12.1–0:15.2 · Have an account? Sign in / with your email.
- 0:15.3–0:17.6 · Tap “Email me a one-time code”.
- 0:17.8–0:20.9 · Six digits by email, / and Aarav's in.

**Sound cues (placeholders)**
- 0:12.6 · Ring swish (User account)
- 0:13.6 · Quiet keyboard ticks for 1.5 s
- 0:15.3 · Ring swish (Email me a code)
- 0:16.1 · UI tap
- 0:16.4 · Page push swish
- 0:16.9 · Gentle chime: the sign-in email card (not an OS notification sound)
- 0:18.3 · Six soft digit ticks, 0.17 s apart
- 0:19.8 · UI tap (Verify and continue)
- 0:20.1 · Success: soft two-note rise

**Accuracy notes** - The emailed one-time code is a released sign-in method ('Email me a one-time code instead' on the sign-in page; mobile-number codes do not exist). The headline and captions name only the email path; the password field is visible but not featured.
- The code really was emailed, by the isolated demo stack to its local inbox for the demo persona. The card shows the real email render, cropped to the code box, the expiry line and 'Never share this code. SETU staff will never ask you for it.' The crop leaves out the template's greeting line, which still says 'as Customer' (an app wording to fix in the email template).
- Digits 220504 match in signin/email-otp.png and the code clip; never retype or invent digits; keep the masked address as captured.
- 'Sign in with your User account' and 'SIGNING IN AS User' are the app's own words; the ring is on 'User account'.
- F1 keeps the crest row off-frame; the 75-years mark is never enlarged.
- signin/07-home.png ('Set your delivery location') is the real fresh-device state; it sets up the flashback.

## s04 · New here? Create a User account

**Time** 0:21.1 → 0:31.1 (10.0 s)

**Narration** New here? Rewind to Aarav's day one. Create a User account: name, email, phone, password. Then four quick steps.

**On-screen text**
- 0:21.5–0:24.0 · *tag (tag row at (140,112): Lucide rotate-ccw + Space Mono 700 18 px caps)* · DAY ONE
- 0:21.6–0:31.0 · *kicker (kit .kicker)* · 02 · New here?

**UI state** Rewind to day one: sign-in page with the card 'New here? Create a user account' and the button 'Create a User account' → 'Create your User account' under 'SIGNING IN AS User' (Name / User email / Phone / Password; empty → filled: Aarav Mehta, aarav.demo@kgpian.iitkgp.ac.in, 9000012345, masked password, 'Strong enough.') → onboarding Step 1 of 4 'Confirm your campus identity' → Step 2 of 4 'Where should orders arrive?'.

**Shots**
- 0:21.1–0:21.5 · `signin/07-home.png` · Frame 0 (from s03), covered by the rewind band at 0.41.
- 0:21.1–0:21.8 · `graphic:editorial rewind band (full-height indigo band, orange leading edge)` · Sweeps left → right; the screen changes under it.
- 0:21.5–0:23.3 · `onboarding/01-signin.png` · Swapped in under the band; ring--blue + tap 'Create a User account' (1.30) at identity.
- 0:22.8–0:24.3 · `onboarding/02-signup-empty.png` · swapPush in ('Create your User account') while the camera moves to Fcreate; tap Name (2.80).
- 0:24.3–0:24.9 · `onboarding/03-type-name/` · Typing clip, clipSeconds 0.62: 'Aarav Mehta'.
- 0:24.9–0:26.4 · `onboarding/04-type-email/` · Typing clip, clipSeconds 1.56: 'aarav.demo@kgpian.iitkgp.ac.in'.
- 0:26.4–0:26.10 · `onboarding/05-type-phone/` · Typing clip, clipSeconds 0.56: '9000012345'; ring on the helper line.
- 0:26.10–0:27.7 · `onboarding/06-type-password/` · Typing clip, clipSeconds 0.71: masked dots.
- 0:27.7–0:29.2 · `onboarding/07-signup-filled.png` · Still under the clips ('Strong enough.'; deliberate focus-loss cut at 6.60); ring--blue + tap 'Create account' (7.20).
- 0:28.6–0:31.1 · `onboarding/10-step1-identity.png` · swapPush in (Step 1 of 4 'Confirm your campus identity'); ring the app's stepper; tap 'Continue' (9.05).
- 0:30.5–0:31.1 · `onboarding/21-step2-prompt.png` · swapPush in (Step 2 of 4 'Where should orders arrive?') and settle.

**Animation** Local times. Frame 0 = s03's last frame (signin/07-home.png at identity). Camera framing Fcreate = {s 1.4, P [195,709], T [1420,700]} (the new form sits 25 px higher): canvas of a screen point = (1125.16 + 1.512·x, −372.0 + 1.512·y); the header logos stay off-frame.
0.00–0.70 rewind band: a full-height band 760 px wide (linear-gradient(90deg,#151E4D,#22307A)) with a 3 px #EC5A2A leading edge on its right side, x −760 → 1920 (power2.inOut 0.7 s), above the phone and the left column (the caption track stays on top). It fully covers the phone between ≈0.39 and 0.43 s.
0.41 instant swap under the band: signin/07-home.png → onboarding/01-signin.png (set the new layer visible, hide the old one; verify the frame in a snapshot).
0.40–0.70 tag 'DAY ONE' (Lucide rotate-ccw 20 px + Space Mono 700 18 px caps, #B8C7FF, pill padding 10/16) fades in at the tag row (140,112); 2.60–2.90 it fades out. 0.45 kicker '02 · New here?' K.fadeUp at (140,200).
1.05 ring--blue on onboarding/01-signin.createAccount (at identity, canvas (1196.4,794.2)–(1552.8,846.0)) — the band has cleared at 0.70, so the sign-in page reads for 0.6 s first. 1.30 K.tap createAccount ('Create a User account') → 1.65 K.swapPush → onboarding/02-signup-empty.png (0.55 s).
1.65–2.65 K.focus Fcreate (1.0 s), moving with the page push; the form fills the frame (name (1149.4,94.1)–(1690.6,166.7), submit (1149.4,614.3)–(1690.6,686.8)).
2.80 K.tap onboarding/02-signup-empty.name → 3.15 the typing clips play back-to-back in one non-timed layer stack, each starting on the frame where the previous one ends (the field-to-field focus changes are in the captures, so no extra taps are drawn): onboarding/03-type-name/ 3.15–3.77 (0.62), onboarding/04-type-email/ 3.77–5.33 (1.56), onboarding/05-type-phone/ 5.33–5.89 (0.56), onboarding/06-type-password/ 5.89–6.60 (0.71); onboarding/07-signup-filled.png holds underneath from 6.60 — a deliberate focus-loss cut (the clip ends with the password field focused, the still has it unfocused; the next action, the 'Create account' ring, follows at 6.95).
5.35–6.20 orange ring on the phone helper line, measured box {x:10,y:519,w:254,h:20.5} 'The seller calls this number at handover.' (text x16–257.4, y521.3–536.3).
6.95 ring--blue on onboarding/07-signup-filled.submit. 7.20 K.tap submit ('Create account') → 7.55 K.swapPush → onboarding/10-step1-identity.png (0.55 s). 7.55–8.45 K.unfocus (0.9 s).
8.10–9.30 orange ring (radius 15) on the app's own stepper, measured box {x:16,y:58,w:358,h:30} (canvas at identity (1181.3,146.6)–(1567.9,179)).
8.80 ring--blue on onboarding/10-step1-identity.cont. 9.05 K.tap cont ('Continue') → 9.40 K.swapPush → onboarding/21-step2-prompt.png (0.55 s), settled at 9.95.
9.50–9.90 the kicker fades out. 9.95–10.00 hold.

**Transition in** Editorial rewind band (left → right) wipes from tonight's Home to the sign-in page of day one — a chapter wipe, not in-app navigation. · **out** Tap 'Continue' on Step 1; Step 2 pushes in and settles at identity before the cut.

**Captions**
- 0:21.2–0:23.9 · New here? Rewind to Aarav's day one.
- 0:24.0–0:27.9 · Create a User account: / name, email, phone, password.
- 0:28.7–0:30.6 · Then four quick steps.

**Sound cues (placeholders)**
- 0:21.1 · Band wipe whoosh (rewind)
- 0:22.4 · UI tap
- 0:22.8 · Page push
- 0:24.3 · Fast keyboard ticks through 6.6 s
- 0:28.3 · UI tap (Create account)
- 0:28.6 · Page push + soft step chime
- 0:30.1 · UI tap (Continue)
- 0:30.5 · Page push

**Accuracy notes** - The band is an editorial 'rewind' to the day Aarav set up his account (it makes the second path explicit), not an in-app back navigation.
- The fields are exactly Name / User email / Phone / Password; the helper 'The seller calls this number at handover.' is the form's own copy. 'Create a User account' is the card's exact button text (the form's title is 'Create your User account').
- Onboarding has four steps ('Step N of 4'); the ring is on the app's own stepper.
- The second caption describes the form ('Create a User account: name, email, phone, password.') rather than the tap, because the 'Create a User account' tap (1.30) happens under the first caption; the button itself is ringed blue before it is tapped.
- Typing is real (four clips at ≈0.76× of their base length; no keyboard is added); the password shows masked dots only.
- Step 1's line about what sellers see is visible but not featured (not in the verified facts); its 'Signed in as customer' note, still the app's wording, is never featured.
- Demo persona data only (Aarav Mehta, aarav.demo@kgpian.iitkgp.ac.in, 9000012345).

## s05 · Where should orders arrive?

**Time** 0:31.1 → 0:47.1 (16.0 s)

**Narration** Next: where should orders arrive? Location access is optional. Search works too. Nehru Hall: inside the delivery area. Check the pin on the map. Save it as Home, add B-212.

**On-screen text**
- 0:31.2–0:47.0 · *kicker (kit .kicker)* · 03 · Delivery spot
- 0:31.4–0:33.3 · *label chip on the explainer inset (Space Mono 700 18 px caps, orange outline)* · OPTIONAL
- 0:37.9–0:39.1 · *label (short caps, Space Mono 700 18 px, callout lane)* · CAMPUS ONLY
- 0:39.8–0:41.1 · *label (short caps, Space Mono 700 18 px, callout lane)* · CAMPUS BOUNDARY
- 0:45.1–0:47.0 · *address card title (Plus Jakarta Sans 700 32 px; our summary of two real values, not app copy)* · Home · B-212
- 0:45.1–0:47.0 · *address card subline (Plus Jakarta Sans 500 22 px, #B8C7FF)* · Nehru Hall of Residence

**UI state** Onboarding Step 2 of 4 'Where should orders arrive?' (inset: SETU's own explainer 'Allow location for SETU?' with 'Not now' / 'Allow location') → 'Select a location' picker → search 'Nehru Hall' → 'Confirm delivery location' ('Location is within the IIT Kharagpur delivery area.') → map 'Select delivery location' (red pin, faint blue campus-boundary line, Google attribution) → back to Confirm → SAVE AS Home + ADDRESS DETAILS 'B-212' → 'Confirm location' → Step 2 filled ('Nehru Hall of Residence, Cricket Groun…', 22.319759, 87.298041, Room B-212, Home).

**Shots**
- 0:31.1–0:34.0 · `onboarding/21-step2-prompt.png` · Identity; pale ring on 'Use my current location' (never tapped) beside the explainer inset; ring--blue + tap the Delivery location box (2.05); covered by the picker sheet 2.40–2.90.
- 0:31.4–0:33.3 · `location/01-allow-dialog.png` · INSET outside the phone: crop CSS {x:20,y:276,w:350,h:293} (SETU's own 'Allow location for SETU?' explainer) at the phone's own scale 1.08× (378×316) in a white card at x 420–798, y 300–616; labelled OPTIONAL; orange ring on 'Not now' only; no tap; dashed leader to the GPS row.
- 0:33.5–0:35.1 · `location/10-picker-select.png` · swapSheet (sheetTop 537) — 'Select a location'; identity framing keeps the sheet subtitle tiny; tap search (3.50); the clip layer fades in over it 3.85–4.05.
- 0:34.10–0:35.8 · `location/11-type-search/` · Typing clip, clipSeconds 0.8: the expanded sheet, 'Nehru Hall' typed.
- 0:35.8–0:37.4 · `location/12-search-results.png` · Results ('Nehru Hall of Residence' over 'Pan Loop, IIT Kharagpur…' first); ring--blue + tap the first result (5.60); fades out 5.95–6.25.
- 0:37.0–0:39.8 · `location/13-confirm-search.png` · 'Confirm delivery location'; camera Fconf; green ring on 'Location is within the IIT Kharagpur delivery area.'; tap 'Adjust on the map' (7.95); the map fades in over it 8.30–8.65.
- 0:39.4–0:41.1 · `location/20-map.png` · 'Select delivery location' map at Fconf (s 1.8 at screen y 575, raised 32 px): the sheet subtitle is off-frame; pin halo; boundary label; tap 'Use this location' (9.35).
- 0:40.8–0:42.3 · `location/13-confirm-search.png` · Back on Confirm (the map hands the same pin back); ring--blue + tap the 'Home' chip (10.65); the clip layer fades in over it 11.00–11.20.
- 0:42.1–0:42.9 · `location/14-type-room/` · Typing clip, clipSeconds 0.8: f0000 has Home selected (sheet 25 px lower), then 'B-212' into Address details.
- 0:42.9–0:44.6 · `location/15-confirm-home.png` · Still under the clip (identical to its last frame); rings; tap 'Confirm location' (12.70); the sheet closes 13.05–13.50.
- 0:44.1–0:47.1 · `onboarding/23-step2-done.png` · Revealed as the sheet closes; pin → address card; ring on the filled box; camera back to identity.
- 0:44.5–0:47.0 · `graphic:pin → address card (Lucide outline map-pin, dotted trail left of the bezel, glass card)` · Action → result: the field's pin flies out and unfolds into the saved-address card; the trail is drawn only on the canvas left of the phone.

**Animation** Local times. Frame 0 = onboarding/21-step2-prompt.png at identity. Camera framing Fconf = {s 1.8, P [195,575], T [1500,528]} (A's map framing, raised 32 px): visible screen y≈303–844, and the phone's bottom bezel shows at canvas y≈1051–1076; canvas of a screen point = (1120.92 + 1.944·x, −589.8 + 1.944·y). It keeps every 'SETU delivers inside the IIT Kharagpur campus boundary' subtitle (map: screen y 226–258) and every Confirm sheet title (13: y≈259–277; 14-type-room and 15: y≈284–302) off-frame. The picker and search shots stay at identity, where their subtitle is tiny.
0.10 kicker '03 · Delivery spot' K.fadeUp at (140,200).
0.25–0.65 explainer inset: a white card (radius 24, shadow 0 30px 80px rgba(0,0,0,.45)) holding location/01-allow-dialog.png cropped to CSS {x:20,y:276,w:350,h:293} at the phone's own scale 1.08× (378×316.4, so nothing in it is magnified relative to the app) at left 420, top 300 (x 420–798, y 300–616.4): fromTo scale 0.94/opacity 0 → 1/1 (back.out(1.4) 0.4 s). Crop CSS → canvas: X = 420 + (x−20)·1.08, Y = 300 + (y−276)·1.08. With it, label chip 'OPTIONAL' (orange 2 px outline, Space Mono 700 18 px caps, ≈148×38) at (420,250) fades up, and a dashed leader (2 px rgba(184,199,255,.7), 6/6 dash) draws from the card's right edge (798,458) to the GPS row's left edge (1181.3,596.7) (K.drawPath 0.35–0.75).
0.35–1.75 pale ring (GLOBAL ring vocabulary: context, never a tap target) on onboarding/21-step2-prompt.gps ('Use my current location'), fading 1.75–2.10; it is never tapped.
0.75–1.80 orange ring (radius 30; drawn in the inset card, canvas-level) on location/01-allow-dialog.notNow ('Not now'): canvas x 443.8–603.4, y 511.1–563 (pad 6): the choice is optional. Nothing marks the dialog's body text: never ring, underline, zoom or caption '…to find nearby stalls…' or 'It is only read when you ask for it.' (the code contradicts both).
1.90–2.20 inset, label, leader and ring fade out (0.3 s; the inset was settled 0.65–1.90 = 1.25 s).
1.85 ring--blue on onboarding/21-step2-prompt.box. 2.05 K.tap box (centre (195,361.7)) → 2.40 K.swapSheet → location/10-picker-select.png (sheetTop 537, 0.5 s).
3.30 ring--blue on location/10-picker-select.search (pad 12). 3.50 K.tap search → 3.85 K.swapFade (0.2 s) → clip layer location/11-type-search/ (clipSeconds 0.8; f0000 = the sheet expanded to the top with the field focused) 3.85–4.65; 4.65 the clip ends: cut to location/12-search-results.png (set it visible under the clip layer at 4.65; its results list differs from the clip's last frame).
4.85 ring--blue on location/12-search-results.first ('Nehru Hall of Residence' over 'Pan Loop, IIT Kharagpur, Kharagpur, West Be…'). 5.60 K.tap first → 5.95 K.swapFade (0.3 s) → location/13-confirm-search.png (the sheet shrinks to 'Confirm delivery location'). The results were readable 4.65–5.95 (1.3 s).
6.00–7.00 K.focus Fconf (1.0 s).
6.65–7.95 green ring on location/13-confirm-search.zoneOk (canvas (1227.8,321.9)–(1795.5,355)) + label 'CAMPUS ONLY' (≈185×38) at x 900–1085, y 319.5–357.5, in 6.75 (0.3 s), out 7.75–8.05; leader (1085,338.5)→(1227.8,338.5).
7.75 ring--blue on the 'Adjust on the map' row, measured box {x:18,y:684,w:354,h:66}. 7.95 K.tap location/13-confirm-search.adjust (centre (205.5,708)) → 8.30 K.swapFade (0.35 s) → location/20-map.png (no layer movement: at Fconf both sheet tops are off-frame and the blurred page behind them is the same).
8.65–9.45 pin halo: two 2 px orange rings grow from the map pin's tip (screen (195,456); pin head (195,433); canvas tip (1500,296.7)) to r 36 CSS px, 0.5 s each, 0.3 s apart.
8.70–10.00 label 'CAMPUS BOUNDARY' (≈234×38) at x 852–1086, y 246.6–284.6 (in 0.3 s; out 9.70–10.00); leader (1086,265.6)→(1298.4,265.6) — the faint blue boundary line on the map passes through screen (91.3,440) (it runs ≈(164.7,330)→(18.6,549)). The Google logo and 'Map data ©2026' strip (screen y 566–588) stay unobstructed.
9.15 ring--blue on location/20-map.useThis (canvas (1477.6,930.4)–(1844.1,1023.7)). 9.35 K.tap useThis ('Use this location') → 9.70 K.swapFade (0.35 s) → location/13-confirm-search.png. The map was fully visible 8.65–9.70 (the shortened round trip).
10.40 ring--blue on location/13-confirm-search.home (the 'Home' chip). 10.65 K.tap home (centre (63,538)) → 11.00 K.swapFade (0.2 s) → clip layer location/14-type-room/ (clipSeconds 0.8: f0000 Home selected and the sheet 25 px lower because the 'Choose one…' line disappears; then 'B-212' typed) 11.00–11.80; location/15-confirm-home.png holds underneath from 11.80 (identical to the clip's last frame).
11.85–12.65 orange rings on location/15-confirm-home.home and location/15-confirm-home.details.
12.50 ring--blue on location/15-confirm-home.confirm. 12.70 K.tap confirm ('Confirm location') → 13.05 the sheet closes: onboarding/23-step2-done.png sits underneath; the 15 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 576px 0)) fades out (0.35 s) while its sheet part (clip-path inset(268px 0 0 0)) slides y 0 → +576 (expo.in 0.45 s, done 13.50).
13.45 pin → address card: a Lucide map-pin (OUTLINE, stroke 2.5 px #EC5A2A, 36 px) pops (scale 0→1, back.out(2) 0.25 s) at the Delivery-location field's pin icon — 23's screen (346,363) → canvas (1793.5,115.9) under Fconf. 13.55–14.05 it flies in a straight line to (300,470) (expo.inOut 0.5 s); it crosses the screen only in flight. Its 2 px dotted pale trail is drawn ONLY on the canvas left of the phone, from (1090,282.7) to (300,470) (K.drawPath 13.80–14.05, in step with the pin), so no trail ever lies on app text. 14.00–14.45 the pin unfolds into a glass card (kit .glass-card, left 140, top 420, 420×110): Lucide house icon + 'Home · B-212' (Plus Jakarta Sans 700 32 px, white) over 'Nehru Hall of Residence' (Plus Jakarta Sans 500 22 px, #B8C7FF) (expo.out 0.45 s). Pin, trail and card are canvas-level (outside the rig). 14.20–14.50 the trail fades out, before any camera move.
13.55–14.55 orange ring on onboarding/23-step2-done.box (canvas (1152,12.3)–(1848,214.4)), fading 14.55–14.90.
14.65–15.55 K.unfocus (0.9 s); the card holds still (one movement at a time).
15.65–15.95 card and kicker fade out (the card was settled 14.45–15.65 = 1.2 s). 15.95–16.05 hold at identity.

**Transition in** Continuous: Step 2 is already on screen at identity. · **out** The saved address becomes a card in the left column, the camera returns to identity, then everything clears; Step 2 (filled) holds at identity for the cut.

**Captions**
- 0:31.2–0:34.7 · Next: where should orders arrive? / Location access is optional.
- 0:34.8–0:36.4 · Search works too.
- 0:36.5–0:39.3 · Nehru Hall: inside the delivery area.
- 0:39.4–0:41.8 · Check the pin on the map.
- 0:41.9–0:44.5 · Save it as Home, add B-212.

**Sound cues (placeholders)**
- 0:31.4 · Soft card pop (explainer inset)
- 0:33.1 · UI tap
- 0:33.5 · Sheet slide up
- 0:34.6 · UI tap
- 0:34.10 · Keyboard ticks (10)
- 0:36.7 · UI tap
- 0:37.8 · Positive ping (inside the delivery area)
- 0:39.0 · UI tap
- 0:39.4 · Map slide + soft pin settle
- 0:40.5 · UI tap
- 0:41.8 · UI tap (Home chip)
- 0:42.1 · Keyboard ticks (5)
- 0:43.8 · UI tap (Confirm location)
- 0:44.5 · Card lock-in: soft click + shimmer

**Accuracy notes** - Location access is optional: SETU's own explainer ('Allow location for SETU?' with 'Not now' / 'Allow location') is shown as a labelled inset beside the phone at the phone's own scale; only 'Not now' is ringed. 'Use my current location' gets a pale context ring but is never tapped, and no detection result is claimed. Search is the path demonstrated.
- Never ring, underline, zoom or caption the dialog's body sentences 'SETU uses your location to find nearby stalls…' and 'It is only read when you ask for it.': on phones, auto-detect reads a fix each time the app opens and after a sign-in once permission is granted (client/src/state/useAutoLocation.js, client/src/layouts/ConsumerLayout.jsx), and no listing is sorted by distance. The caption says only 'Location access is optional.', which is true.
- Do not push in on location/10-picker-select.png: its dimmed background carries a blurred GPS reading from the capture run, an unreadable smudge at identity.
- Search result and zone check are the app's own: the first result reads 'Nehru Hall of Residence' over 'Pan Loop, IIT Kharagpur, Kharagpur, West Be…' (two lines), and Confirm says 'Location is within the IIT Kharagpur delivery area.' The off-campus refusal is not shown or faked.
- The map shows the real red pin, the faint blue campus-boundary polygon (#0033DA at 0.5 opacity) and the Google attribution; nothing covers them. 'Check the pin' = viewing it; no pin move is claimed or shown. The round trip is short (map fully visible 1.05 s, 1.75 s with its fades) but kept.
- Never ring, zoom on or caption 'SETU delivers inside the IIT Kharagpur campus boundary' (picker and map subtitles) or Step 2's lede '…SETU delivers inside the campus area only.' Fconf (T [1500,528]) shows screen y ≥ 303.4 only, so the map subtitle and every Confirm sheet title stay off-frame; the picker shots stay at identity.
- 'Use this location' returns the unchanged pin to Confirm, so location/13-confirm-search.png is reused honestly. 'Home' is tapped on 13 before the cut to 14-type-room/f0000.
- 'Nehru Hall of Residence, Cricket Ground', 22.319759, 87.298041 and 'B-212' are the real saved values. The card's 'Home · B-212' is the film's own summary label (saved name + room), not a quoted app string.

## s06 · Your picks — and three things SETU does not do

**Time** 0:47.1 → 0:56.7 (9.6 s)

**Narration** Pick cuisines you like. They show up first. Then three things SETU does not do. Confirm, then “Start ordering”.

**On-screen text**
- 0:47.3–0:56.6 · *kicker (kit .kicker)* · 04 · Your picks
- 0:52.1–0:54.4 · *kinetic list line (Sora 700 40 px; exact app title; no rupee sign)* · SETU never takes your money
- 0:52.5–0:54.4 · *kinetic list line (Sora 700 40 px; exact app title)* · SETU does not deliver
- 0:52.9–0:54.4 · *kinetic list line (Sora 700 40 px; exact app title)* · SETU approves and records

**UI state** Onboarding Step 3 of 4 'What should we show first?' (South Indian, Street Food, Chinese selected) → Step 4 of 4 'Three things SETU does not do' → switch 'I understand SETU is a directory and approval gate' on → 'Start ordering' → Home ('Home' over 'Room B-212 · Nehru Hall of Residence'; 'Good evening, Aarav').

**Shots**
- 0:47.1–0:48.5 · `onboarding/23-step2-done.png` · Frame 0; ring--blue + tap 'Continue' (0.40); pushed out 0.75–1.30.
- 0:47.9–0:50.9 · `onboarding/30-step3.png` · swapPush in: Step 3 of 4 'What should we show first?'; the base layer until the full 31 layer is set at 3.70.
- 0:49.4–0:52.0 · `onboarding/31-step3-picked.png` · Pixel-aligned; revealed through a circle (r 0 → 56) at each tapped chip (only those three chips differ from 30); full layer from 3.70; pushed out 4.30–4.85.
- 0:51.5–0:54.10 · `onboarding/40-step4.png` · swapPush in (no tap: Step 3's Continue sits below the captured viewport); focus mask on the three titles; rings; kinetic list; the base layer until the full 41 layer is set at 7.80.
- 0:54.6–0:56.4 · `onboarding/41-step4-ack.png` · Circular reveal from the tapped switch (r 0 → 340, then the full layer): toggle on, 'Start ordering' enabled; ring--blue + tap 'Start ordering' (8.40).
- 0:56.4–0:56.7 · `home/01-first-home.png` · Revealed by the 'Start ordering' commit wipe: Home with 'Home' over 'Room B-212 · Nehru Hall of Residence'.
- 0:55.9–0:56.6 · `graphic:commit wipe (#0033DA circle from the Start ordering button)` · Action → result transition.

**Animation** Local times. Frame 0 = onboarding/23-step2-done.png at identity; the whole scene stays at identity.
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
9.15–9.45 the kicker fades out. 9.50–9.55 hold on Home.

**Transition in** Continuous: Step 2 (filled) is on screen at identity. · **out** 'Start ordering' → blue commit wipe → Home (day one, address set), settled at identity.

**Captions**
- 0:47.6–0:50.7 · Pick cuisines you like. / They show up first.
- 0:51.5–0:54.1 · Then three things SETU does not do.
- 0:54.3–0:56.0 · Confirm, then “Start ordering”.

**Sound cues (placeholders)**
- 0:47.5 · UI tap
- 0:47.9 · Page push
- 0:49.0 · Chip tap (pitch 1)
- 0:49.6 · Chip tap (pitch 2)
- 0:50.3 · Chip tap (pitch 3)
- 0:51.5 · Page push
- 0:52.1 · Low tick
- 0:52.5 · Low tick
- 0:52.9 · Low tick
- 0:54.3 · Toggle click
- 0:55.5 · UI tap (Start ordering)
- 0:55.9 · Blue wipe swoosh into Home

**Accuracy notes** - Chips are tapped in the capture's order (South Indian, Street Food, Chinese); 30-step3 and 31-step3-picked differ only in those three chips, so the circular reveals (r ≤ 56, each confined to its own chip) composite two real captures and never pre-select a chip. The taps are a quick multi-select (0.6 s apart); the beat after the last chip is 0.6 s.
- Step 4's three titles are quoted exactly. The focus mask keeps 'Every seller listed here cleared a licence check…' and 'Required. Recorded against your account with today's date.' dim; never ring, zoom on or caption them (the acknowledgement is not stored; not every stall is licence-gated). Fact 1's body ('no checkout … UPI to the seller's own handle') is likewise never featured. The mask and rings are gone before the switch is ringed and tapped.
- The ack reveal grows to r 340 (the farthest changed pixel is 324 px from the switch) and the full 41 layer is then set, so no half-changed card border is ever shown.
- 'They show up first' = 'Stalls serving these move to the top of the home page'; the liked cuisines also lead the Home tabs (visible in s07, not featured).
- No tap is drawn on Step 3's Continue: it is below the captured viewport.

## s07 · Back to tonight — saved Home, then dosa from Southside Tiffins

**Time** 0:56.7 → 1:10.3 (13.5 s)

**Narration** New phone, same account: he picks his saved Home. Good evening, Aarav. Tonight: dosa. Southside Tiffins: approved by SETU. Tap ADD: one Masala Dosa, two filter coffees.

**On-screen text**
- 0:57.1–0:58.7 · *tag (tag row at (140,112): Lucide moon + Space Mono 700 18 px caps)* · TONIGHT
- 0:57.1–1:10.2 · *kicker (kit .kicker)* · 05 · Find & add
- 0:58.7–1:07.3 · *honesty note (tag row; Space Mono 700 18 px caps, shown once in the body)* · Demo environment · sample stalls
- 1:03.10–1:07.8 · *dish chip (kit .dish-chip: name Plus Jakarta Sans 700 28 px, price Space Mono 700 26 px #B8C7FF; exact menu line)* · Masala Dosa ₹80
- 1:04.1–1:06.5 · *dish chip (kit .dish-chip: Plus Jakarta Sans name, Space Mono price; exact menu line)* · Ghee Roast Dosa ₹110
- 1:07.8–1:10.3 · *order-slip row (kit .dish-chip; '1 ×' Space Mono 700 26 px #EC5A2A, name Plus Jakarta Sans, price Space Mono; exact cart line)* · 1 × Masala Dosa ₹80
- 1:09.7–1:10.3 · *order-slip row (kit .dish-chip; '2 ×' Space Mono, name Plus Jakarta Sans, price Space Mono; exact cart line)* · 2 × Filter Coffee ₹60

**UI state** Back to tonight on the new phone: Home reads 'Set your delivery location' over 'Tap to pick it on the map' (the selected delivery location is stored per browser; the saved addresses belong to the account) → the Deliver-to row opens 'Select a location' with SAVED LOCATIONS · 'Home' over 'B-212 · Nehru Hall of Residence, Cricket Gro…' → 'Confirm delivery location' (SAVED LOCATION 'Nehru Hall of Residence, Cricket Ground', 'Location is within the IIT Kharagpur delivery area.', SAVE AS Home, ADDRESS DETAILS 'B-212') → 'Confirm location' → Home: 'Home' over 'Room B-212 · Nehru Hall of Residence', 'Good evening, Aarav', tabs All · Chinese · South Indian · Street Food · Amer…, 'Approved sellers', '13 open now' → Search 'dosa' → Southside Tiffins ('Masala Dosa ₹80', 'Ghee Roast Dosa ₹110') → stall page ('Approved by SETU · you pay the seller directly') → Masala Dosa 1, Filter Coffee 2, 'View cart'.

**Shots**
- 0:56.7–0:56.10 · `home/01-first-home.png` · Frame 0 (day one's Home, from s06) under the return band; hidden at 0.29 while the band covers the phone.
- 0:56.7–0:57.4 · `graphic:editorial return band (right → left)` · Marks the jump back to tonight; the phone switches to tonight's Home under it (0.29).
- 0:56.10–0:58.6 · `location/30-home-unset.png` · Tonight, new phone: 'Set your delivery location' over 'Tap to pick it on the map'; ring--blue + tap the Deliver-to row (1.00); covered by the picker's scrim 1.35–1.95.
- 0:58.0–0:59.9 · `location/31-picker-saved.png` · K.swapSheet (sheetTop 433): 'Select a location' with SAVED LOCATIONS · 'Home' over 'B-212 · Nehru Hall of Residence, Cricket Gro…'; identity only; ring--blue + tap the Home row (2.55); fades out 2.90–3.15.
- 0:59.6–1:01.3 · `location/32-confirm-saved.png` · swapFade: 'Confirm delivery location' (SAVED LOCATION, Home, B-212 filled); ring--blue + tap 'Confirm location' (3.75); the sheet closes 4.10–4.55.
- 1:00.8–1:03.0 · `location/33-home-set.png` · Revealed as the sheet closes: 'Home' over 'Room B-212 · Nehru Hall of Residence'; ring; ring--blue + tap search (5.45); pushed out 5.80–6.35.
- 1:02.5–1:03.1 · `search/01-search-empty.png` · swapPush in; the box is auto-focused.
- 1:03.1–1:03.6 · `search/02-type-dosa/` · Typing clip, clipSeconds 0.5: 'dosa'.
- 1:03.6–1:06.1 · `search/03-results.png` · Southside Tiffins with 'Masala Dosa ₹80' / 'Ghee Roast Dosa ₹110'; dish chips rise out; tap the stall card (8.50); pushed out 8.85–9.40.
- 1:05.5–1:08.2 · `stall/01-stall.png` · swapPush in; ring on 'Approved by SETU · you pay the seller directly'; tap Masala Dosa ADD (10.75); the base layer until the full 02 layer is set at 11.45.
- 1:07.8–1:09.6 · `stall/02-dosa-added.png` · Circular reveal at the ADD button (ADD → '− 1 +') + bottom wipe revealing 'View cart'; full layer from 11.45.
- 1:07.8–1:09.6 · `stall/04-coffee.png` · Pixel-identical to 02 (no swap needed): Filter Coffee ADD (11.95) then '+' (12.30) are tapped on this state.
- 1:09.3–1:10.3 · `stall/05-coffee-two.png` · Circular reveal at the coffee stepper: '− 2 +'; full layer from 12.90.

**Animation** Local times. Frame 0 = home/01-first-home.png (day one's Home) at identity; the whole scene stays at identity (never push in on the picker sheet: its subtitle 'SETU delivers inside the IIT Kharagpur campus boundary' sits at screen y≈475–500).
0.00–0.70 return band: the s04 band style (760 px, linear-gradient(270deg,#151E4D,#22307A), 3 px orange leading edge on its LEFT side) sweeps right → left, x 1920 → −760 (power2.inOut 0.7 s), above the phone and the left column (the caption track stays on top). It fully covers the phone (x 1150–1599) only between ≈0.265 and 0.314 s, and the phone is fully uncovered again from ≈0.38.
0.29 instant swap under the band: home/01-first-home.png → location/30-home-unset.png (set the new layer visible, hide the old one; verify the 0.27–0.31 frames in a snapshot). Tonight, on his new phone, Home reads 'Set your delivery location' over 'Tap to pick it on the map' — the same fresh-device state s03 ended on.
0.40–0.70 tag 'TONIGHT' (Lucide moon 20 px + Space Mono 700 18 px caps) fades in at the tag row (140,112); 1.70–2.00 it fades out. 0.45 kicker '05 · Find & add' K.fadeUp at (140,200).
Picking the saved Home takes three real taps, each 0.35 s before the change it causes. Readable windows (counting the sheets' expo entrances/exits): 30's header ≈0.38–1.6, 31's Home row ≈1.6–2.9, 32's confirm step ≈3.0–4.3, 33's header ≈4.4–5.9 — each ≥1.2 s:
0.75 ring--blue on location/30-home-unset.deliverTo (canvas (1183.4,103.5)–(1511.8,147.8)). 1.00 K.tap deliverTo (centre (170,38.6)) → 1.35 K.swapSheet → location/31-picker-saved.png (sheetTop 433, 0.6 s; settled 1.95).
1.95 ring--blue on location/31-picker-saved.homeRow (the 'Home' row under 'SAVED LOCATIONS'; canvas (1183.4,904.8)–(1565.8,976.1)). 2.55 K.tap homeRow (centre (195,793); 0.6 s after the sheet settled) → 2.90 K.swapFade (0.25 s) → location/32-confirm-saved.png: 'Confirm delivery location' with SAVED LOCATION 'Nehru Hall of Residence, Cricket Ground', 'Location is within the IIT Kharagpur delivery area.', SAVE AS Home and ADDRESS DETAILS 'B-212' already filled (settled 3.15). No ring on its zone line (s05 explained it).
2.00–2.30 note 'Demo environment · sample stalls' (Space Mono 700 18 px caps, #B8C7FF at 80%, a 6 px orange dot first) fades in at the tag row as soon as TONIGHT has left — before any stall card is held on screen (33-home-set from 4.55); 10.30–10.60 it fades out.
3.25 ring--blue on location/32-confirm-saved.confirm (canvas (1360.1,928.6)–(1565.8,980.4)). 3.75 K.tap confirm ('Confirm location', centre (276.8,806); 0.6 s after the step settled) → 4.10 the sheet closes: location/33-home-set.png sits underneath; the 32 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 592px 0)) fades out (0.35 s) while its sheet part (clip-path inset(252px 0 0 0)) slides y 0 → +592 (expo.in 0.45 s, done 4.55).
4.55–5.30 orange ring on location/33-home-set.deliverTo ('Home' over 'Room B-212 · Nehru Hall of Residence'), fading 5.30–5.65; the header stays readable until the push (settled 4.55–5.80 = 1.25 s). Never ring or zoom on 33's tab bar ('Orders' shows a hover blue there, screen y 798–829).
5.25 ring--blue on the search box, measured box {x:18,y:129.1,w:354,h:46} (33-home-set is pixel-identical to home/01-first-home.png above y 636, so home/01-first-home.search applies). 5.45 K.tap search (centre (195,152.1)) → 5.80 K.swapPush → search/01-search-empty.png (0.55 s; the box is auto-focused, no tap needed).
6.45 clip layer search/02-type-dosa/ (clipSeconds 0.5; f0000 = 01-search-empty) types 'dosa' 6.45–6.95; 6.95 the clip ends: cut to search/03-results.png (set it visible under the clip layer at 6.95; the filtered results replace the clip's last frame).
7.15–8.35 orange ring on the Southside Tiffins dish lines, measured box {x:128,y:256,w:236,h:46} ('Masala Dosa ₹80' / 'Ghee Roast Dosa ₹110').
7.25 dish chip 'Masala Dosa ₹80' (kit .dish-chip with .veg mark; name Plus Jakarta Sans 700 28 px, price in <b> Space Mono 700 26 px #B8C7FF) rises at left 140, top 340: fromTo y +30/opacity 0 → 0/1 (expo.out 0.5 s). 7.40 'Ghee Roast Dosa ₹110' the same at left 140, top 412. They move OUT of the phone; nothing flies in.
8.30 ring--blue on search/03-results.stall. 8.50 K.tap the stall card (centre (195,220.5)) → 8.85 K.swapPush → stall/01-stall.png (0.55 s).
9.45–10.65 orange ring on stall/01-stall.trust ('Approved by SETU · you pay the seller directly'). 9.50–9.80 the 'Ghee Roast Dosa ₹110' chip fades out.
10.50 ring--blue on stall/01-stall.dosaAdd. 10.75 K.tap dosaAdd ('ADD') → 11.10 circular reveal of a stall/02-dosa-added.png layer from (299,611), r 0 → 90 (0.25 s): ADD becomes '− 1 +' (stall/02-dosa-added.stepper); 11.10–11.40 a second 02 layer clipped to the bottom strip (screen y ≥ 790) wipes up from the bottom, revealing 'View cart'; 11.45 set one full 02 layer visible (stall/04-coffee.png is pixel-identical, so it stands for both). Accepted at 11.45: the 'Dosas' tab label (screen x 163–201, y 232–241) drops from 01's hover weight to regular — a capture artifact, too small to read as a change.
11.15 the Masala Dosa chip gains an orange '1 ×' prefix (Space Mono 700 26 px #EC5A2A, slides in from the left 0.25 s): it now reads '1 × Masala Dosa ₹80', the cart's line.
11.95 K.tap stall/04-coffee.coffeeAdd (Filter Coffee 'ADD', centre (299,362); 0.6 s after the dosa stepper settled); 12.30 K.tap stall/05-coffee-two.plus ('+', centre (327,362)); nothing changes between the two taps (there is no capture of the '1' state). 12.65 circular reveal of stall/05-coffee-two.png from (299,362), r 0 → 80 (0.25 s): '− 2 +' (the only change from 04); 12.90 set the full 05 layer visible.
12.95 slip row 2 '2 × Filter Coffee ₹60' (same chip style) fromTo y +20/opacity 0 → 0/1 at left 140, top 412 (expo.out 0.4 s). The two chips now form the order slip: wrap them in one element #s07-slip (left 140, top 340, 600×132) so s08 can move them.
13.15–13.45 the kicker fades out. 13.45–13.55 hold (slip visible, phone on 05-coffee-two at identity).

**Transition in** Editorial return band (right → left) from day one back to tonight. Under it (0.29) the phone switches to tonight's Home on the new phone ('Set your delivery location'), because the delivery choice is stored per device; Aarav picks his saved Home with three taps. · **out** Holds on the stall with both items added and the order slip (two cart lines) in the left column — carried into s08.

**Captions**
- 0:56.9–1:01.1 · New phone, same account: / he picks his saved Home.
- 1:01.3–1:03.8 · Good evening, Aarav. / Tonight: dosa.
- 1:04.2–1:06.5 · Southside Tiffins: approved by SETU.
- 1:06.6–1:09.7 · Tap ADD: one Masala Dosa, / two filter coffees.

**Sound cues (placeholders)**
- 0:56.7 · Band whoosh (back to tonight) + light evening swell
- 0:57.7 · UI tap (Deliver-to row)
- 0:58.0 · Sheet slide up
- 0:59.3 · UI tap (saved Home)
- 1:00.5 · UI tap (Confirm location)
- 1:00.8 · Sheet slides down + soft settle
- 1:02.1 · UI tap
- 1:02.5 · Page push
- 1:03.1 · Four keyboard ticks
- 1:03.10 · Two soft pops (dish chips)
- 1:05.2 · UI tap
- 1:05.5 · Page push
- 1:07.5 · ADD tap + soft pop
- 1:08.7 · UI tap
- 1:09.0 · UI tap + tick (× 2)

**Accuracy notes** - Tonight's Home is location/30-home-unset.png ('Set your delivery location' over 'Tap to pick it on the map'): the selected delivery location is stored per browser (setu-svc-loc), so the new phone starts unset although the account holds the saved Home — exactly what the capture stack shows (signin/07-home.png ends s03 in the same state). It takes three real taps, in the capture's order: the Deliver-to row → the 'Home' row under SAVED LOCATIONS → 'Confirm location' (location/30 → 31 → 32 → 33). Never imply the saved address applies itself.
- 31-picker-saved stays at identity and briefly on screen: its subtitle 'SETU delivers inside the IIT Kharagpur campus boundary' (screen y≈475–500) is never ringed, zoomed or captioned.
- 33-home-set's tab bar shows 'Orders' in a hover blue next to the active 'Home' (a capture artifact, screen y 798–829); never ring or zoom on it. Above y 636 it is pixel-identical to home/01-first-home.png, so the search box {x:18,y:129.1,w:354,h:46} is the same.
- 'Demo environment · sample stalls' appears here once (2.00, as soon as the TONIGHT tag leaves and before any stall card is held), and again in the end-card fine print.
- The liked cuisines lead the Home tabs (capture order: All, Chinese, South Indian, Street Food…): visible, not featured.
- Search 'dosa' → Southside Tiffins with 'Masala Dosa ₹80' and 'Ghee Roast Dosa ₹110' (exact). Never ring or zoom on the result rows' '20–20 min' or the stall's '20 min'; no delivery-time claim.
- The stall line is quoted: 'Approved by SETU · you pay the seller directly'. The stall shows 'New' (fresh demo data).
- Coffee: ADD, then '+', then the 2 appears (no capture of the '1' state). stall/04-coffee.png is pixel-identical to 02-dosa-added. stall/03-scroll-menu/ is not used (it snaps back).
- Dish chips and slip rows quote the real menu and cart lines; prices are never set in Sora.

## s08 · Cart — ₹150, payable to the seller

**Time** 1:10.3 → 1:19.5 (9.3 s)

**Narration** Tap “View cart”: one stall per order. Items ₹140, plus the stall's delivery charge: ₹10. ₹150 to the seller. No platform fee.

**On-screen text**
- 1:10.3–1:11.8 · *order-slip row carried from s07 (Space Mono count/price, Plus Jakarta Sans name); flies first, onto the cart's Masala Dosa line* · 1 × Masala Dosa ₹80
- 1:10.3–1:12.2 · *order-slip row carried from s07 (Space Mono count/price, Plus Jakarta Sans name); flies second, onto the cart's Filter Coffee line* · 2 × Filter Coffee ₹60
- 1:10.3–1:19.4 · *kicker (kit .kicker)* · 06 · Cart
- 1:13.7–1:17.9 · *math row: label Space Mono 700 18 px caps + value '₹140' Plus Jakarta Sans 800 64 px* · ITEM TOTAL ₹140
- 1:14.8–1:17.9 · *math row: label Space Mono 700 18 px caps + value '₹10' Plus Jakarta Sans 800 64 px* · + SELLER DELIVERY CHARGE ₹10
- 1:14.10–1:16.2 · *label (short caps, Space Mono 700 18 px, callout lane)* · SET BY THE STALL
- 1:16.1–1:17.9 · *math result: label Space Mono 700 18 px caps + value '₹150' Plus Jakarta Sans 800 64 px white* · = PAYABLE TO SELLER ₹150
- 1:18.0–1:19.1 · *number flight (Plus Jakarta Sans 800, white) from the cart total onto the Confirm card amount* · ₹150

**UI state** Stall with both items → cart 'Your order' over 'Southside Tiffins' (Masala Dosa '₹80 each' × 1 = ₹80; Filter Coffee '₹30 each' × 2 = ₹60; DELIVER TO 'Home' over 'Room B-212 · Aarav Mehta'; 'Item total' ₹140; 'Seller delivery charge' ₹10 with 'Set by the seller, collected by the seller'; 'Payable to seller' ₹150) → 'Confirm order' with 'AMOUNT PAYABLE TO THE SELLER' ₹150 and Cash on delivery selected.

**Shots**
- 1:10.3–1:11.8 · `stall/05-coffee-two.png` · Frame 0 with the order slip; ring--blue + tap 'View cart' (0.70).
- 1:11.3–1:18.5 · `cart/01-cart.png` · swapPush in; the two slip rows fly in one after the other, each onto its own cart line, and dissolve; camera Ftotals; rings on the three total rows; tap 'Review order' (7.40).
- 1:18.0–1:19.5 · `checkout/01-confirm-cash.png` · swapPush in ('Confirm order'); camera Ftotals → Fcard; the ₹150 number flight lands on 'AMOUNT PAYABLE TO THE SELLER ₹150'.

**Animation** Local times. Frame 0 = stall/05-coffee-two.png at identity with the order slip from s07 (handoffIn). Framings: Ftotals = {s 1.5, P [195,560], T [1440,520]} (canvas of a screen point = (1124.1 + 1.62·x, −387.2 + 1.62·y)); Fcard = {s 1.4, P [195,142], T [1420,300]} (canvas = (1125.16 + 1.512·x, 85.24 + 1.512·y)).
0.10 kicker '06 · Cart' K.fadeUp at (140,200).
0.40 ring--blue on stall/05-coffee-two.viewCart. 0.70 K.tap viewCart ('View cart') → 1.05 K.swapPush → cart/01-cart.png (0.55 s).
Order-slip rows fly ONE AT A TIME (never together), each onto its own cart line, and dissolve as they land. Each row is a kit .dish-chip 62 px tall; give each row transform-origin 0% 50%, so its anchor is its left-middle point:
- 1.10–1.50 row 1 '1 × Masala Dosa ₹80' (anchor at rest (140,371)): translate x +1059.6, y −139.2 and scale 1 → 0.64 (expo.inOut 0.4 s), landing its anchor on canvas (1199.6,231.8) = cart/01-cart.png screen (33,136.9), the veg mark's left edge on the Masala Dosa line's centre line (the line's ink spans screen y 116.7–157.0); 1.40–1.60 it dissolves (opacity → 0).
- 1.45–1.85 row 2 '2 × Filter Coffee ₹60' (anchor at rest (140,443)): translate x +1059.6, y −101.3 and scale 1 → 0.64 (expo.inOut 0.4 s), landing on (1199.6,341.7) = screen (33,238.7) on the Filter Coffee line (ink y 218.3–259.0); 1.75–1.95 it dissolves.
The cart has settled by 1.60; the rows never cover app text after they land.
2.30–3.30 K.focus Ftotals (1.0 s).
Left-column math (canvas-level, x 140–700; labels Space Mono 700 18 px caps #B8C7FF; values Plus Jakarta Sans 800 64 px white — never Sora; each value fromTo y 18/opacity 0 → 0/1, expo.out 0.4 s):
- 3.40 'ITEM TOTAL' (top 300) + '₹140' (top 322); orange ring on the Item total row, measured box {x:26,y:462,w:338,h:30} (canvas (1166.2,361.2)–(1713.8,409.8)) 3.40–4.60.
- 4.60 '+ SELLER DELIVERY CHARGE' (top 410) + '₹10' (top 432); orange ring on the fee row, measured box {x:26,y:518,w:338,h:56} (label, sub-label and ₹10; canvas (1166.2,452)–(1713.8,542.7)) 4.60–5.80; label 'SET BY THE STALL' (≈246×38) at x 846–1092, y 478–516 from 4.70 to 5.90; leader (1092,497)→(1166.2,497).
- 5.70 a 2 px rule draws (x 140–600, y 524, 0.25 s). 5.85 '= PAYABLE TO SELLER' (top 540) + '₹150' (top 562; the two rows above dim to 70%); orange ring on the payable row, measured box {x:26,y:603,w:338,h:32} (canvas (1166.2,589.7)–(1713.8,641.5)) 5.85–7.15.
7.15 ring--blue on cart/01-cart.review (canvas (1357.1,879.6)–(1726.7,957.4)). 7.40 K.tap review ('Review order') → 7.75 K.swapPush → checkout/01-confirm-cash.png (0.55 s). 7.30–7.65 the math fades out.
7.75–8.65 K.focus Fcard (0.9 s).
7.80–8.65 number flight (canvas-level): a '₹150' (Plus Jakarta Sans 800, white) lifts from the cart's payable value — canvas box (1637.6,601.0)–(1702.4,630.2) under Ftotals — and arcs onto the Confirm card's big amount, landing exactly over its box under Fcard, measured screen {x:33,y:105,w:108,h:40} → canvas (1175.1,244.1)–(1338.4,304.5), at 8.65 (font size grows ≈30 → 60 px; expo.inOut, timed with the camera); 8.65–8.85 it dissolves into the real UI.
8.80–9.15 the kicker fades out. 8.85–9.30 hold on checkout/01-confirm-cash.png at Fcard.

**Transition in** Continuous from s07: the order slip is on canvas; the 'View cart' tap starts the chapter. · **out** The ₹150 lands on the Confirm card; the camera holds at Fcard for s09.

**Captions**
- 1:10.3–1:13.5 · Tap “View cart”: / one stall per order.
- 1:13.5–1:16.7 · Items ₹140, plus the stall's / delivery charge: ₹10.
- 1:16.8–1:19.5 · ₹150 to the seller. / No platform fee.

**Sound cues (placeholders)**
- 1:10.10 · UI tap (View cart)
- 1:11.3 · Page push
- 1:11.3 · Soft whoosh (slip row 1 lands)
- 1:11.7 · Soft whoosh (slip row 2 lands)
- 1:13.7 · Number tick
- 1:14.8 · Number tick
- 1:16.1 · Soft resolve tone (= ₹150)
- 1:17.7 · UI tap (Review order)
- 1:18.0 · Number-flight swish
- 1:18.9 · Soft lock-in

**Accuracy notes** - Cart values are exact: items ₹140, 'Seller delivery charge' ₹10 'Set by the seller, collected by the seller', 'Payable to seller' ₹150.
- Each stall sets its own delivery charge (₹0–₹500; the row is hidden at ₹0) — 'the stall's delivery charge' and the label 'SET BY THE STALL' cover that. Never 'free', 'zero cost' or 'minimal'.
- No platform fee or commission exists: payable = items + the stall's own charge.
- One order goes to one stall (adding from another stall replaces the cart).
- The slip rows and the ₹150 flight link real values and land exactly on the real UI, one object at a time; they never cover app text after landing.
- checkout/03-scroll-summary/ and checkout/04-summary.png are not used (captured with Pay by QR selected; Aarav pays cash).

## s09 · Pay the stall directly — cash, or online via UPI

**Time** 1:19.5 → 1:33.0 (13.5 s)

**Narration** Pay cash at your door, or online via UPI. After the stall accepts, one tap opens your UPI app. Then the stall confirms the payment. Aarav picks cash: “Place order”.

**On-screen text**
- 1:19.7–1:32.10 · *kicker (kit .kicker; faded out 2.75–3.05 and back in from 11.35 while the UPI branch is up)* · 07 · Pay
- 1:22.7–1:30.7 · *demo tag (orange outline pill, Space Mono 700 18 px caps; enters and leaves with the UPI phone)* · DEMO QR & UPI ID · NOT REAL
- 1:22.8–1:30.7 · *kicker-style heading for the side branch (Space Mono 700 22 px caps)* · IF THE STALL OFFERS UPI
- 1:23.3–1:30.7 · *step list (Space Mono 700 22 px)* · 1 · Stall accepts
- 1:24.0–1:30.7 · *step list (Space Mono 700 22 px)* · 2 · Pay in your UPI app · or the QR
- 1:25.1–1:26.5 · *label (short caps, Space Mono 700 18 px, callout lane, with a leader to the phone)* · YOUR UPI APP OPENS · ₹150 FILLED IN
- 1:29.0–1:30.7 · *step list (Space Mono 700 22 px)* · 3 · Stall confirms

**UI state** 'Confirm order': 'AMOUNT PAYABLE TO THE SELLER' ₹150 and 'SETU does not collect this. Southside Tiffins receives it directly.'; HOW WILL YOU PAY? Cash on delivery 'Hand ₹150 to the seller at your door.' / Pay online via UPI 'Once Southside Tiffins accepts, pay ₹150 in your UPI app or scan their QR. You will have five minutes, and can send a screenshot if it takes longer. They confirm the money arrived.' (offered only because this stall's QR and UPI ID are verified). Side branch on a second phone (separate demo order): accepted → 'Pay to continue' with 'Pay ₹150 in your UPI app', the demo UPI ID southside.demo@setudemo and the stall's DEMO QR → 'Opening your UPI app…' → back: 'Paid? Tap “I’ve paid” below…' → 'Seller is checking your payment' → 'Order confirmed' / 'The stall confirmed your payment.'. Back on Aarav's phone: Cash on delivery → 'Place order · ₹150' → 'Waiting for the seller'.

**Shots**
- 1:19.5–1:30.5 · `checkout/01-confirm-cash.png` · Main phone at Fcard: rings on 'SETU does not collect this…', Cash on delivery and Pay online via UPI; then it shrinks left and dims for the UPI branch; swapped to order-cash/00-confirm under the dim at 10.95.
- 1:22.7–1:24.8 · `order-qr/02-pay-upi.png` · Second phone (default spec, above the main rig) slides in from the right 3.10–3.80: a separate demo order after the stall accepted — 'Pay to continue', the countdown, 'Pay ₹150 in your UPI app', the demo UPI ID and the stall's labelled DEMO QR; tap the UPI button (4.95).
- 1:24.7–1:26.4 · `order-qr/03-upi-opening.png` · swapFade (0.12 s): 'Opening your UPI app…'; ring on 'Opens Google Pay, PhonePe, Paytm or any UPI app with ₹150 and the note … filled in.'; the screen dims 5.80–6.10 while the user is in their UPI app.
- 1:26.0–1:27.9 · `order-qr/04-upi-back.png` · Back from the app (set under the dim at 6.50, undimmed 6.55–6.90): 'Paid? Tap “I’ve paid” below so Southside Tiffins can check…'; tap 'I've paid' (7.75).
- 1:27.7–1:29.2 · `order-qr/05-payment-review.png` · swapFade: 'Seller is checking your payment'.
- 1:28.10–1:30.7 · `order-qr/06-payment-confirmed.png` · swapFade (the stall's confirmation): 'Order confirmed', 'The stall confirmed your payment.'; the second phone fades out to the right 10.70–11.10.
- 1:25.1–1:26.5 · `graphic:hand-off callout 'YOUR UPI APP OPENS · ₹150 FILLED IN' + leader, and a dark dim over the UPI phone's screen` · Editorial only: no UPI app screen is drawn.
- 1:30.5–1:32.7 · `order-cash/00-confirm.png` · Main phone back at the default spec (identical to checkout/01 except the button shade); ring Cash; tap 'Place order · ₹150' (12.35).
- 1:32.7–1:33.0 · `order-cash/01-placed.png` · Revealed by the 'Place order' commit wipe: 'Waiting for the seller'.
- 1:32.3–1:33.0 · `graphic:commit wipe (#0033DA circle from the Place order button)` · 0.45 s grow, 0.3 s fade over 01-placed.

**Animation** Local times. Frame 0 = checkout/01-confirm-cash.png with the main rig at Fcard = {s 1.4, P [195,142], T [1420,300]} (canvas of a screen point = (1125.16 + 1.512·x, 85.24 + 1.512·y)). Fsplit = {s 0.7407, P [195,422], T [346.4,497.9]} puts the main phone at x 180–513, y 150–846.
0.10 kicker '07 · Pay' K.fadeUp at (140,200).
0.20–1.00 orange ring on 'SETU does not collect this. Southside Tiffins receives it directly.', measured box {x:33,y:162,w:270,h:36}. 0.85–1.75 orange ring on checkout/01-confirm-cash.cash. 1.60–2.50 orange ring on checkout/01-confirm-cash.qr ('Pay online via UPI', box h 135), fading 2.50–2.85.
2.55–3.35 split: main rig Fcard → Fsplit (0.8 s, expo.inOut); a kit .dim inside the main screen fades in 2.55–3.05; 2.75–3.05 the kicker fades out.
3.10–3.80 the UPI phone — a second kit .phone at the default spec, OUTSIDE and ABOVE the main rig — fromTo x +900 → 0 (expo.out 0.7 s) showing order-qr/02-pay-upi.png. 3.10 tag 'DEMO QR & UPI ID · NOT REAL' at (560,296); 3.25 heading 'IF THE STALL OFFERS UPI' at (560,250).
Step list (Space Mono 700 22 px white, numerals #EC5A2A; a Lucide check (#19B36B) appears when a row is reached):
- 3.80 '1 · Stall accepts' at (560,390), checked at once; fine ring on 'Pay to continue' (the state the order enters once the stall accepts) 3.80–4.60. Never ring the thread pill 'Order confirmed by …' (shown before payment).
- 4.50 '2 · Pay in your UPI app · or the QR' at (560,450); orange ring on order-qr/02-pay-upi.timer 4.50–5.20; ring--blue on order-qr/02-pay-upi.upiBtn 4.60–5.15; 4.95 K.tap upiBtn ('Pay ₹150 in your UPI app') → 5.15 K.swapFade → order-qr/03-upi-opening.png (0.12 s; identical layout, 'Opening your UPI app…'); 5.30–6.25 orange ring on order-qr/03-upi-opening.upiSub ('Opens Google Pay, PhonePe, Paytm or any UPI app with ₹150 and the note … filled in.').
5.55 label 'YOUR UPI APP OPENS · ₹150 FILLED IN' (right edge 1092, top 600) + leader (1092,619)→(1150,619) drawn 5.65–5.95; 5.80–6.10 a dark dim (#0B1020, 0.62) over the UPI phone's screen while the user is in their UPI app; 6.50 order-qr/04-upi-back.png set under the dim; 6.55–6.90 the dim clears; 6.70–7.00 label and leader fade. No UPI app screen is drawn.
6.90–7.75 orange ring on order-qr/04-upi-back.upiNote ('Paid? Tap “I’ve paid” below so Southside Tiffins can check…'); 7.45 ring--blue on order-qr/04-upi-back.paid; 7.75 K.tap paid → 8.10 K.swapFade → order-qr/05-payment-review.png (0.25 s); row 2 checked at 8.10; 8.35–9.30 fine ring on 'Seller is checking your payment'.
9.40 K.swapFade → order-qr/06-payment-confirmed.png (0.25 s; the stall's confirmation, no tap by the user). 9.50 '3 · Stall confirms' at (560,510) with its check; 9.65–10.60 green ring on the card 'The stall confirmed your payment.' {x:14,y:526,w:362,h:72}.
10.70–11.10 the UPI branch leaves together: phone x 0 → 160 + fade, tag, heading and steps fade.
10.95–11.75 back on Aarav's phone: order-cash/00-confirm.png under the dim, main rig Fsplit → identity (0.8 s), dim out; 11.35 the kicker returns.
11.70–12.30 orange ring on Cash on delivery; 12.10 ring--blue on order-cash/00-confirm.place; 12.35 K.tap place ('Place order · ₹150'); 12.70–13.15 commit wipe; 13.15 order-cash/01-placed.png underneath, wipe fades 13.15–13.45; 13.10–13.40 kicker out; hold to 13.50.

**Transition in** Continuous from s08: the camera is already framing the amount card and the payment options (Fcard). · **out** 'Place order · ₹150' → blue commit wipe → 'Waiting for the seller', settled at identity.

**Captions**
- 1:19.7–1:23.2 · Pay cash at your door, / or online via UPI.
- 1:23.3–1:27.2 · After the stall accepts, / one tap opens your UPI app.
- 1:27.3–1:29.10 · Then the stall confirms / the payment.
- 1:30.8–1:32.10 · Aarav picks cash: “Place order”.

**Sound cues (placeholders)**
- 1:20.4 · Ring swish (cash)
- 1:21.2 · Ring swish (UPI)
- 1:22.7 · Dual-phone slide whoosh
- 1:24.0 · Soft timer tick
- 1:24.5 · UI tap (Pay ₹150 in your UPI app)
- 1:25.3 · Soft app-switch whoosh out
- 1:26.1 · Soft app-switch whoosh back
- 1:27.3 · UI tap (I've paid)
- 1:28.10 · Soft confirm ping (stall confirms)
- 1:30.3 · Whoosh out
- 1:31.9 · UI tap (Place order)
- 1:32.3 · Warm confirm swell into the order

**Accuracy notes** - Cash copy is quoted ('Hand ₹150 to the seller at your door.'); the dark card line 'SETU does not collect this. Southside Tiffins receives it directly.' is the app's.
- 'Pay online via UPI' appears only when the stall has a payment QR on file (cash on delivery is always offered); 'Pay ₹150 in your UPI app' appears only once campus staff verified that QR, whose UPI ID the app reads out of it. So the branch heading says 'IF THE STALL OFFERS UPI'.
- Order of events: the stall accepts first, then the pay card appears in the order thread with a five-minute window; one tap hands a UPI link (the stall's UPI ID, the order's amount and the note 'SETU <order number>') to the phone's UPI app; the user pays there, comes back and taps 'I've paid' → 'Seller is checking your payment' → the stall confirms. Opening the app proves nothing; the order is paid only when the stall confirms. Never 'pay first' or 'QR at checkout'.
- The capture browser has no UPI app: 'Opening your UPI app…' is filmed straight after the tap, and the return state ('Paid? Tap “I’ve paid” below…') is the app's own state for a phone that left for the UPI app. The UPI app itself is never drawn — the hand-off is an editorial callout over a dimmed screen.
- The QR and its UPI ID are demo values (southside.demo@setudemo, on a handle no bank or UPI app issues; the card says 'DEMO QR · Not a real payment code'); the tag 'DEMO QR & UPI ID · NOT REAL' enters and leaves with the UPI phone. Nothing implies money moved.
- The UPI phone is a separate demo order, framed as 'if the stall offers UPI'; Aarav's order continues with cash.
- Order status and payment status stay separate: step 1 rings 'Pay to continue', never the thread pill 'Order confirmed by Southside Tiffins'; 'Order confirmed' is featured only at step 3.

## s10 · Track it, then hand over cash and the code

**Time** 1:33.0 → 1:45.0 (12.0 s)

**Narration** Now follow along: confirmed, cooking, on the way. At the door, Aarav pays ₹150 in cash. Then he tells them his code. Order complete.

**On-screen text**
- 1:33.2–1:44.10 · *kicker (kit .kicker)* · 08 · Track & hand over
- 1:33.3–1:38.5 · *tag (tag row at (140,112): Lucide fast-forward + Space Mono 700 18 px caps)* · TIME-LAPSE
- 1:33.3–1:44.10 · *rail header (Space Mono 700 18 px caps, #B8C7FF)* · STATUS TIMELINE · NOT A MAP
- 1:33.3–1:44.10 · *status rail rows (Plus Jakarta Sans 600 28 px; the progress view's exact labels)* · Placed · Confirmed · Preparing · Ready · Out for delivery · Delivered
- 1:40.1–1:41.3 · *label (short caps, Space Mono 700 18 px, callout lane)* · HANDOVER CODE

**UI state** Aarav's cash order thread: 'Waiting for the seller' → 'Order confirmed' ('Being prepared · usually ready by 7:24 pm') → 'Being cooked now' → 'Ready' → 'On the way' with the handover panel ('Please pay ₹150 in cash', six-digit code, 'Then tell this code to the stall owner or the delivery partner — that completes your order. SETU staff will never ask for it.') → 'The stall has confirmed your ₹150 cash payment' / 'Now tell them this code — that completes your order.' → 'Delivered' (review sheet rises).

**Shots**
- 1:33.0–1:34.5 · `order-cash/01-placed.png` · Frame 0 ('Waiting for the seller').
- 1:34.3–1:35.7 · `order-cash/02-accepted.png` · swapFade: 'Order confirmed' (the prep time is not featured).
- 1:35.5–1:36.9 · `order-cash/04-preparing.png` · swapFade: 'Being cooked now'.
- 1:36.7–1:38.1 · `order-cash/06-ready.png` · swapFade: 'Ready'.
- 1:37.8–1:41.6 · `order-cash/07-on-the-way-code.png` · swapFade: 'On the way' + handover panel; camera Fhand; rings on 'Please pay ₹150 in cash' and the six-digit code.
- 1:41.3–1:44.9 · `order-cash/08-cash-confirmed.png` · swapFade (the stall confirmed the cash): green 'The stall has confirmed your ₹150 cash payment'; code + 'Now tell them this code — that completes your order.'
- 1:44.3–1:45.0 · `order-cash/09-delivered-review.png` · swapSheet (sheetTop 412): 'Delivered' with the review sheet rising; camera back to identity.
- 1:33.3–1:44.10 · `graphic:status rail (the app's six progress labels)` · Left-column motion graphic lit in sync with each status change.

**Animation** Local times. Frame 0 = order-cash/01-placed.png at identity. Camera framing Fhand = {s 1.7, P [195,532], T [1480,500]} (canvas of a screen point = (1121.98 + 1.836·x, −476.75 + 1.836·y)).
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
6.10–7.00 orange ring on 'Please pay ₹150 in cash', measured box {x:25,y:455,w:340,h:34} (canvas (1167.9,358.6)–(1792.1,421.1)), fading 7.00–7.35.
7.00–7.95 orange ring (look here; the code is never tapped) on order-cash/07-on-the-way-code.code (canvas (1167.9,439)–(1792.1,527.2)), fading 7.95–8.30, + label 'HANDOVER CODE' (≈209×38) at x 880–1089, y 464–502, in 7.05 (0.3 s), out 7.95–8.25 (both gone before the 8.30 swap moves the code 18 px down); leader (1089,483)→(1167.9,483).
8.30 K.swapFade → order-cash/08-cash-confirmed.png (0.25 s; the stall tapped 'Yes, cash received'; its panel sits 18 px lower, the camera stays).
8.60–9.80 green ring on 'The stall has confirmed your ₹150 cash payment', measured box {x:25,y:473,w:340,h:34} (canvas (1167.9,391.7)–(1792.1,454.1)).
9.60–11.10 orange ring on order-cash/08-cash-confirmed.code (canvas (1167.9,472.5)–(1792.1,560.6)) and on 'Now tell them this code — that completes your order.', measured box {x:25,y:576,w:310,h:18}. 9.80–11.10 three concentric 2 px pale (#B8C7FF) arcs ripple once each, 0.35 s apart — the code is said out loud: all centred at canvas (1080,516) (level with the code), radii 20/34/48 px, each spanning 140°–220° (the LEFT side of its circle, angles from +x), so they bulge left, away from the phone, like '(((' — they occupy x ≈ 1032–1065, y ≈ 485–547, clear of the Fhand bezel (x ≈ 1098).
11.10–11.90 K.unfocus (0.8 s).
11.30 K.swapSheet → order-cash/09-delivered-review.png (sheetTop 412, 0.55 s; the stall entered the right code — no customer tap); the rail's 'Delivered' row lights with a soft orange flash.
11.55–11.90 the rail and the kicker fade out. 11.90–12.00 hold at identity.

**Transition in** Continuous from s09's commit wipe: 'Waiting for the seller' at identity. · **out** The review sheet rises over 'Delivered'; settled at identity for the cut.

**Captions**
- 1:33.3–1:38.0 · Now follow along: / confirmed, cooking, on the way.
- 1:38.5–1:41.7 · At the door, Aarav pays ₹150 in cash.
- 1:41.8–1:44.8 · Then he tells them his code. / Order complete.

**Sound cues (placeholders)**
- 1:33.5 · Status tick (Placed)
- 1:34.3 · Tick + soft chime (Confirmed)
- 1:35.5 · Tick (Preparing)
- 1:36.7 · Tick (Ready)
- 1:37.8 · Tick (Out for delivery) + light whoosh
- 1:40.0 · Code shimmer
- 1:41.3 · Soft ping (cash confirmed)
- 1:42.8 · Two soft voice-arc pulses
- 1:44.3 · Sheet slide + gentle success chord (Delivered)

**Accuracy notes** - Status headlines are the app's own ('Waiting for the seller', 'Order confirmed', 'Being cooked now', 'Ready', 'On the way'); the rail uses the progress view's labels (Placed, Confirmed, Preparing, Ready, Out for delivery, Delivered).
- The TIME-LAPSE tag is on for the whole status run: the real order took 7:02 → 7:25 pm. 'Being prepared · usually ready by 7:24 pm' is a prep target — shown in the capture, never featured or narrated; no delivery-time promise.
- Tracking is a status timeline in the order thread, not a map ('STATUS TIMELINE · NOT A MAP' paraphrases Step 4's 'You will see a status timeline, not a rider on a map.'). No live map or location tracking anywhere.
- Handover order is real: cash first ('Please pay ₹150 in cash' → 'The stall has confirmed your ₹150 cash payment'), then the code completes it ('Now tell them this code — that completes your order.'). 'Them' = the stall owner or the delivery partner, as the app says.
- The handover code in 07/08 is 806688 as captured; never type it into captions or overlays; don't alter the captured times.

## s11 · Delivered, rated — and reportable

**Time** 1:45.0 → 1:50.8 (5.8 s)

**Narration** Delivered. Five stars for Southside Tiffins. Dinner, sorted. Something off? Tap “Report”.

**On-screen text**
- 1:45.2–1:50.8 · *kicker (kit .kicker)* · 09 · Rate & report
- 1:49.3–1:50.8 · *label (short caps, Space Mono 700 18 px, callout lane)* · TO SETU STAFF

**UI state** Delivered order: review sheet 'How was Southside Tiffins?' (1 × Masala Dosa · 2 × Filter Coffee) → 5 stars 'Excellent' → 'Submit review' → the thread ends 'Delivered · handover code verified · ₹150 paid in cash' with 'Report' / 'Order again' in the bar.

**Shots**
- 1:45.0–1:46.3 · `order-cash/09-delivered-review.png` · Frame 0: 'How was Southside Tiffins?'; tap the 5th star (0.60).
- 1:46.0–1:48.3 · `order-cash/10-review-5.png` · Circular reveal from the 5th star: five stars, 'Excellent'; tap 'Submit review' (2.45).
- 1:47.8–1:50.8 · `order-cash/12-review-sent.png` · The sheet slides down: the thread ends 'Delivered · handover code verified · ₹150 paid in cash'; ring 'Report' + 'TO SETU STAFF'; holds to the cut.

**Animation** Local times. Frame 0 = order-cash/09-delivered-review.png at identity; the scene stays at identity (no push on the review sheet, so its note placeholder is never featured).
0.10 kicker '09 · Rate & report' K.fadeUp at (140,200).
0.35 ring--blue on the 5th star, measured box {x:292,y:514,w:36,h:36} (inside order-cash/09-delivered-review.stars). 0.60 K.tap the 5th star (centre (310,532)) → 0.95 circular reveal of order-cash/10-review-5.png from (310,532), r 0 → 330 (0.35 s): five stars fill and 'Excellent' appears (the farthest changed pixel, the Submit button's corner, is 317 px away); 1.30 set the full 10 layer visible.
1.35–2.35 orange ring on order-cash/10-review-5.word ('Excellent').
2.20 ring--blue on order-cash/09-delivered-review.submit. 2.45 K.tap submit ('Submit review') → 2.80 the sheet closes: order-cash/12-review-sent.png sits underneath; the 10 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 432px 0)) fades out (0.35 s) while its sheet part (clip-path inset(412px 0 0 0)) slides y 0 → +432 (expo.in 0.45 s, done 3.25).
3.30–4.30 orange ring on the thread's last line 'Delivered · handover code verified · ₹150 paid in cash', measured box {x:14,y:484,w:362,h:32}, fading 4.30–4.65.
4.25 orange ring on the 'Report' button, measured box {x:18,y:720,w:170,h:48} (canvas (1183.4,861.6)–(1367,913.4)) until 5.35 (fading 5.35–5.70) + label 'TO SETU STAFF' (≈209×38) at x 911–1120, y 795–833, in 4.30 (0.3 s), out 5.40–5.70; leader (1120,814)→(1183.4,880) — the label stays above the caption zone. Report is pointed at, not tapped (the caption names the button).
5.40–5.70 the kicker fades out. 5.70–5.80 hold on order-cash/12-review-sent.png.

**Transition in** Continuous: the review sheet is already up. · **out** The completed thread holds at identity with nothing on canvas; s12 opens by pulling the phone back.

**Captions**
- 1:45.2–1:47.5 · Delivered. Five stars / for Southside Tiffins.
- 1:47.7–1:49.0 · Dinner, sorted.
- 1:49.1–1:50.8 · Something off? Tap “Report”.

**Sound cues (placeholders)**
- 1:45.7 · Star tap: rising five-note arpeggio
- 1:47.5 · UI tap (Submit review)
- 1:47.8 · Sheet slides down
- 1:48.3 · Soft confirm ping
- 1:49.3 · Ring swish (Report)

**Accuracy notes** - Review copy: 'How was Southside Tiffins?'; five stars → 'Excellent'; 'Submit review'. The note is optional, 'Don't ask again' exists, and a rating can be given later from Orders.
- 11-review-note.png is not used (its note says 'On time.'); the camera never features the note placeholder ('Hot, on time…'): the scene stays at identity.
- 'Delivered · handover code verified · ₹150 paid in cash' is the app's own line.
- 'Report' exists on ended orders; reports go to SETU campus staff as a record against the stall (not a refund claim against SETU). The label says 'TO SETU STAFF' — never just 'campus staff', which the film's audience line ('students, faculty, staff') could make read as general IIT staff.
- The progress view (13-progress-delivered) is no longer shown: the beat was too short to read, and its time pays for the saved-Home pick in s07.
- 'Dinner, sorted.' is story copy, not a product claim.

## s12 · End card

**Time** 1:50.8 → 1:58.8 (8.0 s)

**Narration** 

**On-screen text**
- 1:51.7–1:58.8 · *tagline (Sora 800 64 px, centred; 'Your SETU.' in #B8C7FF; no rupee sign)* · Your campus. Your food. Your SETU.
- 1:52.0–1:58.8 · *CTA pill (Plus Jakarta Sans 700 30 px #0033DA on white, Lucide arrow-right)* · Explore SETU Food
- 1:52.3–1:58.8 · *disclaimer (verbatim; Plus Jakarta Sans 500 26 px; fully legible 1.95–8.00 = 6.05 s)* · SETU connects users with approved campus food providers. Food preparation, delivery and payment are handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene.
- 1:52.5–1:58.8 · *fine print (Space Mono 400 18 px, 60% white)* · Demo environment · sample stalls · demo QR and UPI ID, not real payment details

**UI state** No app UI after 0.80 s: end-card motion graphics.

**Shots**
- 1:50.8–1:51.7 · `order-cash/12-review-sent.png` · The phone pulls back (scale 1 → 0.72, sinks 60 px) and fades out.
- 1:51.0–1:58.8 · `graphic:real campus boundary outline, faint (assets/data/campus-boundary.json)` · Redraws at 18% opacity behind the type (x 480–1440, y 150–646); the Nehru Hall point glows once at (589.6,244.8), clear of all type.
- 1:51.3–1:58.8 · `graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)` · Tile 240×190 centred at (960,215); lockup 200 px wide, never recoloured.
- 1:51.7–1:58.8 · `graphic:end-card type (tagline, CTA, disclaimer, fine print)` · Kinetic type only.

**Animation** Local times. Frame 0 = order-cash/12-review-sent.png at identity. No captions in this scene (layout.json lists it as centred anyway); keep y 880–1050 empty.
0.00–0.80 the phone recedes: fromTo scale 1 → 0.72 (transform-origin its centre, canvas (1374.6,539.8)), y 0 → +60, opacity 1 → 0 (expo.in 0.8 s).
0.20–1.20 the real campus outline (assets/data/campus-boundary.json path) redraws centred, 960 px wide (scale 0.96): left 480, top 150 → x 480–1440, y 150–645.7; stroke #B8C7FF 2 px at 18% opacity (K.drawPath 1.0 s). 1.00–1.60 the Nehru Hall point (file (114.2,98.8) → canvas (589.6,244.8): left of the logo tile and above the tagline, clear of all type) glows once (8 px orange dot, opacity 0 → 1 → 0.6) and stays at 0.6.
0.40–1.00 white tile (kit .white-tile, 240×190, radius 32) centred at (960,215) → x 840–1080, y 120–310, with assets/brand/setu-logo.png at 200 px wide, centred: fromTo scale 0.94/opacity 0 → 1/1 (expo.out 0.6 s).
0.80 tagline 'Your campus. Your food. Your SETU.' (Sora 800 64 px, white, centred, top 350; 'Your SETU.' in #B8C7FF) K.revealWords (stagger 0.06).
1.20 CTA pill 'Explore SETU Food' (white, radius 999, padding 16/30, Plus Jakarta Sans 700 30 px #0033DA, Lucide arrow-right 26 px) centred, top 460: fromTo scale 0.9/opacity 0 → 1/1 (back.out(1.6) 0.5 s).
1.50–1.95 the disclaimer (verbatim) fades up: Plus Jakarta Sans 500 26 px / 1.45, rgba(255,255,255,.88), centred, max-width 1200 px (3 lines), top 580 (≈ y 580–693).
1.70–2.00 fine print 'Demo environment · sample stalls · demo QR, not a real payment code' (Space Mono 400 18 px, rgba(255,255,255,.6), centred, top 760) fades in.
After 2.00 nothing moves. Hold the complete card to 8.00 (no fade to black).

**Transition in** The phone recedes into the indigo as the campus outline redraws faintly. · **out** Hold to the last frame (no fade) so the owner can add sound or an outro.

**Captions**

**Sound cues (placeholders)**
- 1:50.8 · Pad swell resolves
- 1:51.3 · Brand sting placeholder (owner's choice)
- 1:52.0 · Soft pop (CTA)
- 1:58.7 · Pad tail out

**Accuracy notes** - The disclaimer is verbatim: 'SETU connects users with approved campus food providers. Food preparation, delivery and payment are handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene.' It is fully legible from 1.95 s to the end (6.05 s), with no caption competing.
- Tagline 'Your campus. Your food. Your SETU.' and CTA 'Explore SETU Food' are exactly as briefed; the CTA is type in a pill, not a store badge or link.
- The lockup is the official raster on a white rounded tile, downscaled only, never recoloured; the 75-years mark is not used.
- The fine print repeats the demo-environment note (shown once in the body, s07) and the demo QR / UPI ID note.
- No 'free', no claims about other platforms.
