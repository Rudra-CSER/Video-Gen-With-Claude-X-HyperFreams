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

