# Asset manifest

Film: Dinner at B-212 — a SETU Food walkthrough · 118.85 s · 1920x1080 · 60 fps. Paths are relative to `video-production/hyperframes/` unless they start with `assets/screens/` (relative to `video-production/`).

Every app screen in the film is a real capture of the app, recorded with Playwright on an isolated demo copy (demo stalls, a demo persona and a labelled demo payment QR). Motion graphics are drawn in HTML/CSS/SVG inside the compositions.

## Scene compositions

| Scene | File | Time | Title | Present |
| --- | --- | --- | --- | --- |
| s01 | `compositions/s01-hook.html` | 0–5.4 s | Hook — your campus, your food | yes |
| s02 | `compositions/s02-what-setu-does.html` | 5.4–12 s | What SETU does | yes |
| s03 | `compositions/s03-sign-in.html` | 12–21.1 s | Have an account? Sign in with your email and a code | yes |
| s04 | `compositions/s04-new-here.html` | 21.1–31.1 s | New here? Create a User account | yes |
| s05 | `compositions/s05-delivery-spot.html` | 31.1–47.15 s | Where should orders arrive? | yes |
| s06 | `compositions/s06-your-picks.html` | 47.15–56.7 s | Your picks — and three things SETU does not do | yes |
| s07 | `compositions/s07-find-and-add.html` | 56.7–70.25 s | Back to tonight — saved Home, then dosa from Southside Tiffins | yes |
| s08 | `compositions/s08-cart.html` | 70.25–79.55 s | Cart — ₹150, payable to the seller | yes |
| s09 | `compositions/s09-pay.html` | 79.55–93.05 s | Pay the stall directly — cash, or online via UPI | yes |
| s10 | `compositions/s10-track-handover.html` | 93.05–105.05 s | Track it, then hand over cash and the code | yes |
| s11 | `compositions/s11-rate-report.html` | 105.05–110.85 s | Delivered, rated — and reportable | yes |
| s12 | `compositions/s12-end-card.html` | 110.85–118.85 s | End card | yes |

## Media used by the storyboard

| Asset | Kind | File | Source | KB | Scenes |
| --- | --- | --- | --- | --- | --- |
| `cart/01-cart.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/cart/01-cart.png` | `assets/screens/cart/01-cart.png` | 195 | s08-cart |
| `checkout/01-confirm-cash.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/checkout/01-confirm-cash.png` | `assets/screens/checkout/01-confirm-cash.png` | 368 | s08-cart, s09-pay |
| `clip:location/11-type-search` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/location-11-type-search.800ms.mp4` | `assets/screens/location/11-type-search/ (11 captured frames)` | 118 | s05-delivery-spot |
| `clip:location/14-type-room` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/location-14-type-room.800ms.mp4` | `assets/screens/location/14-type-room/ (6 captured frames)` | 153 | s05-delivery-spot |
| `clip:onboarding/03-type-name` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/onboarding-03-type-name.620ms.mp4` | `assets/screens/onboarding/03-type-name/ (12 captured frames)` | 174 | s04-new-here |
| `clip:onboarding/04-type-email` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/onboarding-04-type-email.1560ms.mp4` | `assets/screens/onboarding/04-type-email/ (31 captured frames)` | 196 | s04-new-here |
| `clip:onboarding/05-type-phone` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/onboarding-05-type-phone.560ms.mp4` | `assets/screens/onboarding/05-type-phone/ (11 captured frames)` | 186 | s04-new-here |
| `clip:onboarding/06-type-password` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/onboarding-06-type-password.710ms.mp4` | `assets/screens/onboarding/06-type-password/ (14 captured frames)` | 215 | s04-new-here |
| `clip:search/02-type-dosa` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/search-02-type-dosa.500ms.mp4` | `assets/screens/search/02-type-dosa/ (5 captured frames)` | 227 | s07-find-and-add |
| `clip:signin/02-type-email` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/signin-02-type-email.1560ms.mp4` | `assets/screens/signin/02-type-email/ (31 captured frames)` | 228 | s03-sign-in |
| `clip:signin/05-type-code` | real capture: typing/scroll frame sequence encoded as 60 fps clip | `assets/clips/signin-05-type-code.1200ms.mp4` | `assets/screens/signin/05-type-code/ (7 captured frames)` | 190 | s03-sign-in |
| `desktop/01-signin-wide.png` | real capture: desktop web page (1440x900 CSS at 2x) | `assets/ui/desktop/01-signin-wide.png` | `assets/screens/desktop/01-signin-wide.png` | 1295 | s02-what-setu-does |
| `graphic:commit wipe (#0033DA circle from the Place order button)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s09-pay |
| `graphic:commit wipe (#0033DA circle from the Start ordering button)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s06-your-picks |
| `graphic:editorial return band (right → left)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s07-find-and-add |
| `graphic:editorial rewind band (full-height indigo band, orange leading edge)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s04-new-here |
| `graphic:end-card type (tagline, CTA, disclaimer, fine print)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s12-end-card |
| `graphic:hand-off callout 'YOUR UPI APP OPENS · ₹150 FILLED IN' + leader, and a dark dim over the UPI phone's screen` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s09-pay |
| `graphic:hook type (SETU Food title, subline, persona chip)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s01-hook |
| `graphic:official SETU lockup on a white rounded tile (assets/brand/setu-logo.png)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s01-hook, s12-end-card |
| `graphic:pin → address card (Lucide outline map-pin, dotted trail left of the bezel, glass card)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s05-delivery-spot |
| `graphic:real campus boundary outline (assets/data/campus-boundary.json) with the Nehru Hall pin` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s01-hook |
| `graphic:real campus boundary outline, faint (assets/data/campus-boundary.json)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s12-end-card |
| `graphic:status rail (the app's six progress labels)` | motion graphic (built in HTML/CSS/SVG, not an app screen) | (built in the scene) |  |  | s10-track-handover |
| `home/01-first-home.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/home/01-first-home.png` | `assets/screens/home/01-first-home.png` | 181 | s06-your-picks, s07-find-and-add |
| `location/01-allow-dialog.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/01-allow-dialog.png` | `assets/screens/location/01-allow-dialog.png` | 395 | s05-delivery-spot |
| `location/10-picker-select.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/10-picker-select.png` | `assets/screens/location/10-picker-select.png` | 388 | s05-delivery-spot |
| `location/12-search-results.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/12-search-results.png` | `assets/screens/location/12-search-results.png` | 109 | s05-delivery-spot |
| `location/13-confirm-search.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/13-confirm-search.png` | `assets/screens/location/13-confirm-search.png` | 327 | s05-delivery-spot |
| `location/15-confirm-home.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/15-confirm-home.png` | `assets/screens/location/15-confirm-home.png` | 343 | s05-delivery-spot |
| `location/20-map.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/20-map.png` | `assets/screens/location/20-map.png` | 500 | s05-delivery-spot |
| `location/30-home-unset.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/30-home-unset.png` | `assets/screens/location/30-home-unset.png` | 186 | s07-find-and-add |
| `location/31-picker-saved.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/31-picker-saved.png` | `assets/screens/location/31-picker-saved.png` | 394 | s07-find-and-add |
| `location/32-confirm-saved.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/32-confirm-saved.png` | `assets/screens/location/32-confirm-saved.png` | 356 | s07-find-and-add |
| `location/33-home-set.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/location/33-home-set.png` | `assets/screens/location/33-home-set.png` | 181 | s07-find-and-add |
| `onboarding/01-signin.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/01-signin.png` | `assets/screens/onboarding/01-signin.png` | 325 | s04-new-here |
| `onboarding/02-signup-empty.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/02-signup-empty.png` | `assets/screens/onboarding/02-signup-empty.png` | 304 | s04-new-here |
| `onboarding/07-signup-filled.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/07-signup-filled.png` | `assets/screens/onboarding/07-signup-filled.png` | 320 | s04-new-here |
| `onboarding/10-step1-identity.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/10-step1-identity.png` | `assets/screens/onboarding/10-step1-identity.png` | 180 | s04-new-here |
| `onboarding/21-step2-prompt.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/21-step2-prompt.png` | `assets/screens/onboarding/21-step2-prompt.png` | 203 | s04-new-here, s05-delivery-spot |
| `onboarding/23-step2-done.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/23-step2-done.png` | `assets/screens/onboarding/23-step2-done.png` | 195 | s05-delivery-spot, s06-your-picks |
| `onboarding/30-step3.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/30-step3.png` | `assets/screens/onboarding/30-step3.png` | 255 | s06-your-picks |
| `onboarding/31-step3-picked.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/31-step3-picked.png` | `assets/screens/onboarding/31-step3-picked.png` | 261 | s06-your-picks |
| `onboarding/40-step4.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/40-step4.png` | `assets/screens/onboarding/40-step4.png` | 245 | s06-your-picks |
| `onboarding/41-step4-ack.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/onboarding/41-step4-ack.png` | `assets/screens/onboarding/41-step4-ack.png` | 246 | s06-your-picks |
| `order-cash/00-confirm.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/00-confirm.png` | `assets/screens/order-cash/00-confirm.png` | 368 | s09-pay |
| `order-cash/01-placed.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/01-placed.png` | `assets/screens/order-cash/01-placed.png` | 132 | s09-pay, s10-track-handover |
| `order-cash/02-accepted.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/02-accepted.png` | `assets/screens/order-cash/02-accepted.png` | 157 | s10-track-handover |
| `order-cash/04-preparing.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/04-preparing.png` | `assets/screens/order-cash/04-preparing.png` | 172 | s10-track-handover |
| `order-cash/06-ready.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/06-ready.png` | `assets/screens/order-cash/06-ready.png` | 163 | s10-track-handover |
| `order-cash/07-on-the-way-code.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/07-on-the-way-code.png` | `assets/screens/order-cash/07-on-the-way-code.png` | 273 | s10-track-handover |
| `order-cash/08-cash-confirmed.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/08-cash-confirmed.png` | `assets/screens/order-cash/08-cash-confirmed.png` | 287 | s10-track-handover |
| `order-cash/09-delivered-review.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/09-delivered-review.png` | `assets/screens/order-cash/09-delivered-review.png` | 257 | s10-track-handover, s11-rate-report |
| `order-cash/10-review-5.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/10-review-5.png` | `assets/screens/order-cash/10-review-5.png` | 253 | s11-rate-report |
| `order-cash/12-review-sent.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-cash/12-review-sent.png` | `assets/screens/order-cash/12-review-sent.png` | 268 | s11-rate-report, s12-end-card |
| `order-qr/02-pay-upi.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-qr/02-pay-upi.png` | `assets/screens/order-qr/02-pay-upi.png` | 215 | s09-pay |
| `order-qr/03-upi-opening.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-qr/03-upi-opening.png` | `assets/screens/order-qr/03-upi-opening.png` | 214 | s09-pay |
| `order-qr/04-upi-back.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-qr/04-upi-back.png` | `assets/screens/order-qr/04-upi-back.png` | 218 | s09-pay |
| `order-qr/05-payment-review.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-qr/05-payment-review.png` | `assets/screens/order-qr/05-payment-review.png` | 215 | s09-pay |
| `order-qr/06-payment-confirmed.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/order-qr/06-payment-confirmed.png` | `assets/screens/order-qr/06-payment-confirmed.png` | 229 | s09-pay |
| `search/01-search-empty.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/search/01-search-empty.png` | `assets/screens/search/01-search-empty.png` | 189 | s07-find-and-add |
| `search/03-results.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/search/03-results.png` | `assets/screens/search/03-results.png` | 170 | s07-find-and-add |
| `signin/01-signin.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/signin/01-signin.png` | `assets/screens/signin/01-signin.png` | 325 | s02-what-setu-does, s03-sign-in |
| `signin/03-email-typed.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/signin/03-email-typed.png` | `assets/screens/signin/03-email-typed.png` | 329 | s03-sign-in |
| `signin/04-enter-code.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/signin/04-enter-code.png` | `assets/screens/signin/04-enter-code.png` | 254 | s03-sign-in |
| `signin/06-code-entered.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/signin/06-code-entered.png` | `assets/screens/signin/06-code-entered.png` | 263 | s03-sign-in |
| `signin/07-home.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/signin/07-home.png` | `assets/screens/signin/07-home.png` | 189 | s03-sign-in, s04-new-here |
| `signin/email-otp.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/signin/email-otp.png` | `assets/screens/signin/email-otp.png` | 132 | s03-sign-in |
| `stall/01-stall.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/stall/01-stall.png` | `assets/screens/stall/01-stall.png` | 165 | s07-find-and-add |
| `stall/02-dosa-added.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/stall/02-dosa-added.png` | `assets/screens/stall/02-dosa-added.png` | 166 | s07-find-and-add |
| `stall/04-coffee.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/stall/04-coffee.png` | `assets/screens/stall/04-coffee.png` | 166 | s07-find-and-add |
| `stall/05-coffee-two.png` | real capture: phone screen (390x844 CSS at 3x) | `assets/ui/stall/05-coffee-two.png` | `assets/screens/stall/05-coffee-two.png` | 166 | s07-find-and-add, s08-cart |

## Shared assets

| File | What it is | KB |
| --- | --- | --- |
| `assets/brand/setu-logo.png` | official SETU lockup (shown on a white rounded tile, never recoloured) | 47 |
| `assets/brand/setu-mark.svg` | the app's vector mark | 0 |
| `assets/data/campus-boundary.json` | IIT Kharagpur campus boundary polygon from server/src/config/campus-zone.js (78 points), drawn as SVG | 2 |
| `assets/data/marks.json` | CSS-px boxes of UI elements per capture (for taps, rings, camera framing) | 18 |
| `assets/fonts/Sora-Variable.ttf` | the app's display font (OFL, licence alongside) | 109 |
| `assets/fonts/PlusJakartaSans-Variable.ttf` | the app's UI font (OFL) | 172 |
| `assets/fonts/SpaceMono-Regular.ttf` | the app's data font (OFL) | 97 |
| `assets/fonts/SpaceMono-Bold.ttf` | the app's data font, bold (OFL) | 96 |
| `assets/vendor/gsap.min.js` | GSAP 3.13.0 (animation engine; standard GSAP licence) | 71 |
| `assets/css/kit.css` | shared visual kit: tokens, phone frame, overlays, captions | 10 |
| `assets/js/kit.js` | shared motion helpers (window.SetuKit) | 8 |

## Captured but not used in this cut

- `assets/ui/checkout/02-confirm-qr.png`
- `assets/ui/checkout/04-summary.png`
- `assets/ui/desktop/02-home-web.png`
- `assets/ui/home/02-home.png`
- `assets/ui/home/04-scrolled.png`
- `assets/ui/home/05-pure-veg.png`
- `assets/ui/onboarding/20-step2-empty.png`
- `assets/ui/onboarding/22-step2-gps.png`
- `assets/ui/order-cash/03-progress-accepted.png`
- `assets/ui/order-cash/05-home-live-card.png`
- `assets/ui/order-cash/11-review-note.png`
- `assets/ui/order-cash/13-progress-delivered.png`
- `assets/ui/order-qr/00-confirm-qr.png`
- `assets/ui/order-qr/01-placed.png`
