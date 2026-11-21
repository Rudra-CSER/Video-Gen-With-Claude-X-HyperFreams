# Capture pass — November 2026 update

What was re-captured for the three changes (Customer → User, email one-time-code sign-in, UPI hand-off on QR payments), and what was kept from the October capture.

## Where it ran

- An isolated demo copy of `setu-services` (read-only clone at commit `f7e70fe`, 3 Nov 2026 "feat: setu login api access token"), run in a scratch workspace — never the live portal and never the QA stack. Nothing was committed or pushed to the repository.
- Services: MongoDB 8.3, Redis, MinIO and Mailpit (the local test inbox), all on loopback ports. The API runs on the same demo evening clock as before (19:00 IST, 13 Oct 2026). A copy of the stack's `minio-js` signs requests with the real time, because MinIO refuses the shifted clock.
- Same demo persona (Aarav Mehta, `aarav.demo@kgpian.iitkgp.ac.in`, 9000012345), same seeded stall (Southside Tiffins, ₹10 delivery charge), same basket (1 Masala Dosa + 2 Filter Coffee = ₹150).
- Demo payment QR: `capture/make-demo-qr.mjs` now encodes a UPI link to the demo UPI ID `southside.demo@setudemo` (a handle no bank or UPI app issues), still labelled **DEMO QR · Not a real payment code**. `capture/30-stall-setup.mjs` uploads it as the stall's QR and as its PAYMENT_QR document, and the stack's campus admin verifies it: only a verified QR turns on "Pay in your UPI app" (`server/src/modules/order/order.upi.js`).

## Re-captured (now in `hyperframes/assets/ui/`)

| Scene | Captures | Why |
|---|---|---|
| s02 | `desktop/01-signin-wide` | New sign-in page: 'Sign in with your User account', new lede, stats with icons; no Customer/Stakeholder cards |
| s03 | `signin/01`–`07`, `02-type-email/`, `05-type-code/`, `email-otp` | 'User account', the 'Email me a one-time code instead' button, 'SIGNING IN AS User'; code 220504 |
| s04 | `onboarding/01-signin`, `02-signup-empty`, `03`–`06` typing, `07-signup-filled`, `10-step1-identity` | 'Create a User account', 'Create your User account', 'User email'; step 1 says 'Sellers see…' |
| s08–s09 | `checkout/01`–`04`, `order-cash/00-confirm` | The option is now 'Pay online via UPI' |
| s09 | `order-qr/00-confirm-qr`, `01-placed`, `02-pay-upi`, `03-upi-opening`, `04-upi-back`, `05-payment-review`, `06-payment-confirmed` | The UPI hand-off. Replaces `02-pay-qr`, `03-pay-qr-focus`, `04-payment-review`, `05-payment-confirmed` (no longer used) |

UPI capture notes: the capture browser has no UPI app. 'Opening your UPI app…' is filmed straight after the tap (the app holds that state for 2.5 s; its boxes are the ones measured on `02-pay-upi`). The switch to the app is reported the way a phone reports it (the page loses focus), so `04-upi-back` is the app's own return state ('Paid? Tap “I’ve paid” below…'). "I've paid" is then tapped on a fresh load of the same order screen. The live-updates note ('Notifications are blocked…'), which headless Chrome always triggers, is hidden in captures like the install-app prompt.

## Kept from the October capture

- **s05 location picker and map, s07 saved-Home picker** (`location/*`, `onboarding/21`–`23`). This stack has no Google Maps key, so search, the map and the picker show "Google Maps is not configured". The flow's layout is unchanged; two helper lines in the old captures say "stakeholder" where the app now says "seller" ('Set it on the map so the stakeholder reaches…', 'Shown to the stakeholder at handover.').
- **s06 onboarding steps 3–4, s07 home/search/stall, s08 cart, s10 tracking, s11 review**: re-captured for comparison and found unchanged apart from wording ('Restaurants serving these…', 'Every seller listed here has passed a licence check…') and the clock. The originals are kept because their order times run over a realistic 23 minutes (7:02 → 7:25 pm).

To re-capture everything, including the map screens, run `capture/run-final.sh` on a stack whose client has `VITE_GOOGLE_MAPS_API_KEY` set (without `SETU_NO_MAPS`).

## App wording that still says "customer" (not featured in the video)

- The sign-in email: "Use this code to sign in to SETU Food as Customer." (the Scene 3 mail card is cropped below this line).
- Onboarding step 1: "Signed in as customer".
- Order-thread system lines written for the seller, e.g. "Handover code sent to the customer's order screen…" (visible, small, in s10's captures).
