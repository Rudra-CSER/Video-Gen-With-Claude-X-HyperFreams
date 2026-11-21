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
Picking the saved Home takes three real taps, each 0.35 s before the change it causes:
0.75 ring--blue on location/30-home-unset.deliverTo (canvas {bx(None,(18,18.1,304,41))}). 1.00 K.tap deliverTo (centre (170,38.6)) → 1.35 K.swapSheet → location/31-picker-saved.png (sheetTop 433, 0.6 s; settled 1.95).
1.95 ring--blue on location/31-picker-saved.homeRow (the 'Home' row under 'SAVED LOCATIONS'; canvas {bx(None,(18,760,354,66))}). 2.55 K.tap homeRow (centre (195,793); 0.6 s after the sheet settled) → 2.90 K.swapFade (0.25 s) → location/32-confirm-saved.png: 'Confirm delivery location' with SAVED LOCATION 'Nehru Hall of Residence, Cricket Ground', 'Location is within the IIT Kharagpur delivery area.', SAVE AS Home and ADDRESS DETAILS 'B-212' already filled (settled 3.15). No ring on its zone line (s05 explained it).
3.25 ring--blue on location/32-confirm-saved.confirm (canvas {bx(None,(181.6,782,190.4,48))}). 3.75 K.tap confirm ('Confirm location', centre (276.8,806); 0.6 s after the step settled) → 4.10 the sheet closes: location/33-home-set.png sits underneath; the 32 capture is split like K.swapSheet in reverse — its scrim part (clip-path inset(0 0 592px 0)) fades out (0.35 s) while its sheet part (clip-path inset(252px 0 0 0)) slides y 0 → +592 (expo.in 0.45 s, done 4.55).
4.55–5.30 orange ring on location/33-home-set.deliverTo ('Home' over 'Room B-212 · Nehru Hall of Residence'), fading 5.30–5.65; the header stays readable until the push (settled 4.55–5.80 = 1.25 s). Never ring or zoom on 33's tab bar ('Orders' shows a hover blue there, screen y 798–829).
2.00–2.30 note 'Demo environment · sample stalls' (Space Mono 700 18 px caps, #B8C7FF at 80%, a 6 px orange dot first) fades in at the tag row as soon as TONIGHT has left — before any stall card is held on screen (33-home-set from 4.55); 10.30–10.60 it fades out.
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

