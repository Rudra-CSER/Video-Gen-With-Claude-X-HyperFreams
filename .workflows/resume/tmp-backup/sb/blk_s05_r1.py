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

