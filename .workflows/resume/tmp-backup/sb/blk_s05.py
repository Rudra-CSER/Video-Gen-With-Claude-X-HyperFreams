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
  ('OPTIONAL', 0.60, 2.20, 'label chip on the explainer inset (Space Mono 700 20 px caps, orange outline)'),
  ('CAMPUS ONLY', T5(6.55), T5(7.85), 'label (short caps, callout lane)'),
  ('CAMPUS BOUNDARY', T5(8.60), T5(9.95), 'label (short caps, callout lane)'),
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
0.60–1.00 explainer inset: a white card (radius 24, shadow 0 30px 80px rgba(0,0,0,.45)) holding location/01-allow-dialog.png cropped to CSS {{x:20,y:276,w:350,h:293}} at 1.15× (402.5×337) at left 420, top 300: fromTo scale 0.94/opacity 0 → 1/1 (back.out(1.4) 0.4 s). Label chip 'OPTIONAL' (orange 2 px outline, Space Mono 700 20 px caps, ≈165×40) at (420,250). Dashed leader (2 px rgba(184,199,255,.7), 6/6 dash) from (822.5,468) to the GPS row's left edge (1181.3,596.7).
1.10–1.80 a 3 px orange underline sweeps left → right under 'It is only read when you ask for it.' inside the inset (canvas x 473–717, y 504).
1.90–2.20 inset, label and leader fade out (0.3 s).
1.85 ring--blue on onboarding/21-step2-prompt.box. 2.05 K.tap box (centre (195,361.7)) → 2.40 K.swapSheet → location/10-picker-select.png (sheetTop 537, 0.5 s).
3.30 ring--blue on location/10-picker-select.search (pad 12). 3.50 K.tap search → 3.85 K.swapFade (0.2 s) → clip layer location/11-type-search/ (clipSeconds 0.8; f0000 = the sheet expanded to the top with the field focused) 3.85–4.65; 4.65 the clip ends: cut to location/12-search-results.png (set it visible under the clip layer at 4.65; its results list differs from the clip's last frame).
4.80–{t5(5.75)} orange ring on location/12-search-results.first. {t5(5.40)} K.tap first → {t5(5.75)} K.swapFade (0.3 s) → location/13-confirm-search.png (the sheet shrinks to 'Confirm delivery location').
{t5(5.80)}–{t5(6.80)} K.focus Fconf (1.0 s).
{t5(6.45)}–{t5(7.75)} green ring (border #19B36B + green glow) on location/13-confirm-search.zoneOk (canvas {bx(FC, (55,469,292,17))}) + label 'CAMPUS ONLY' (≈206×40) at x 900–1106, y 350–390 from {t5(6.55)} to {t5(7.85)}; leader (1106,370)→(1227.8,370).
{t5(7.55)} ring--blue on the 'Adjust on the map' row, measured box {{x:18,y:684,w:354,h:66}}. {t5(7.75)} K.tap location/13-confirm-search.adjust (centre (205.5,708)) → {t5(8.10)} K.swapFade (0.35 s) → location/20-map.png (no layer movement: at Fconf both sheet tops are off-frame and the blurred page behind them is the same).
{t5(8.50)}–{t5(9.70)} pin halo: two 2 px orange rings grow from the map pin's tip (screen (195,456); pin head (195,433); canvas tip {pt(FC,195,456)}) to r 36 CSS px, 0.6 s each, 0.3 s apart.
{t5(8.60)}–{t5(9.95)} label 'CAMPUS BOUNDARY' (≈260×40) at x 860–1120, y 278–318; leader (1120,298)→{pt(FC,91.3,440)} — the faint blue boundary line on the map passes through screen (91.3,440) (it runs ≈(164.7,330)→(18.6,549)). The Google logo and 'Map data ©2026' strip (screen y 566–588) stay unobstructed.
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

