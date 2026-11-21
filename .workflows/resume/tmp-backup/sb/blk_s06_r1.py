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

