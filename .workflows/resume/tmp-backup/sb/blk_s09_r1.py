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

