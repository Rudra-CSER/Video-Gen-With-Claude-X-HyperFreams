# SETU Services (SETU Food): customer flow, as built

Compiled from code research with adversarial verification on 2026-10-13.

- Sources: six code-research topics (auth-onboarding, location, discovery-cart, checkout-payment-tracking, isolated-stack, brand-claims), each checked by an adversarial fact-checker. Every "partial" verdict's correction is applied and the checkers' missed facts are folded in. No fact was refuted.
- Paths are relative to `/home/rudra-cser/Setu-Food-PWA`. Evidence is `path:line`.
- Quoted strings are exact UI copy in DOM case. CSS shows some of them in capitals: eyebrows, "Soon", the sign-in stat labels and "Campus" (`client/src/styles.css:89, 317, 321-322, 928-929, 2760-2761`).
- "Phone" means a viewport under 760 px and "web" means 760 px or wider (`client/src/state/UiContext.jsx:42`). The sign-in art panel needs 981 px or more (`client/src/styles.css:411-417, 952`).
- API responses use the envelope `{success, statusCode, message, data}`. The client unwraps `data` and shows `error` or `message` on failure (`server/system/core/CalmResponse.js:57-75`; `client/src/lib/api.js:63-83`).

## 1. Summary

**What it is**
- The name on screen is "SETU Services". The tab title and PWA name are "SETU Services — Campus Marketplace" (`client/index.html:22`; `client/public/manifest.webmanifest:2-3`).
- "SETU Food" never appears in the client. It is the email brand: the code email's subject is "Your SETU Food sign-in code", with "SETU Food" in the header band and footer (`server/src/services/mail.templates.js:12-13, 36, 55, 57, 68, 73`).
- Food is one service among three pills: "Food" (live), "Commute" and "Utilities" (both "Soon") (`client/src/data/campus.js:26-30`).
- SETU's role, in the app's words: "SETU approves and lists providers; it does not sell food, deliver it, or take payment for it." (`client/src/pages/SignIn.jsx:431-432`). Policy: "SETU Services is a directory of campus food stalls that SETU has checked and approved." / "You order from a stall; the stall cooks, delivers and takes payment." (`client/src/data/policies.js:15-17`).

**Who it is for**
- Customers pick the "Customer" role, "Order from approved campus stakeholders". Stall owners pick "Stakeholder", "Register a stall and run live orders" (`client/src/data/campus.js:41-42`). Admins use the same form, but the role is never offered (`client/src/data/campus.js:32-36`).
- Audience copy: "IIT Kharagpur campus accounts only" (`client/src/pages/SignIn.jsx:254`) and "SETU Services is for campus accounts." (`client/src/data/policies.js:86`). No UI string names faculty, professors or staff, and the docs call customers students (`claude.md:14`; `README.md:11`). Password sign-up accepts any valid email (`server/src/modules/user/user.service.js:175-178, 204`).

**Brand on screen**
- The banner with the crest, the SETU tile and the 75-years mark appears only on `/signin` (`client/src/ui/BrandBanner.jsx:14-24`). Phone customer screens draw no SETU wordmark; only the install banner shows the logo. The web nav shows the SETU mark plus "SETU Services" (`client/src/layouts/ConsumerLayout.jsx:48-50, 199-218`; `client/src/components/PWAInstallBanner.jsx:91-97`).
- Phone header bands are solid indigo: #0033DA in light, #151E4D in dark. Web bands are gradients (`client/src/styles.css:2662-2663, 2764-2768`). The theme follows the OS unless localStorage `setu-svc-theme` is set (`client/src/state/UiContext.jsx:4, 23-26`).

**Customer routes**

| Route | Screen |
|---|---|
| `/signin` | Sign in (guest-only). "Enter the code" and "Create your Customer account" are modes of this page, not routes |
| `/onboarding` | Four-step setup; forced for a customer with no saved address |
| `/` | Home: approved stalls, filters, live-order card |
| `/search` | Search sellers, dishes, cuisines |
| `/seller/:id` | Stall page and menu |
| `/cart` | Cart ("Your order") |
| `/confirm` | "Confirm order": payment choice and "Place order" |
| `/track/:id` | Order thread, handover panel, progress view |
| `/orders` | "Your orders" |
| `/report/:orderId` | "Report an issue" |
| `/profile` | Details, saved locations, preferences, "Help and policies" |

- Routing: `client/src/App.jsx:57-71, 97-135`; `client/src/pages/SignIn.jsx:41`. Every route except `/signin` needs a signed-in customer. A customer with no saved address is sent to `/onboarding`, which never redirects away (`client/src/App.jsx:67-71`).
- The policy pages `/help/how-it-works`, `/help/marketplace-policy` and `/help/terms-privacy` open signed out too (`client/src/App.jsx:111-112`). The phone tab bar reads "Home", "Search", "Orders", "Profile" and is hidden on the stall, cart, confirm and report pages (`client/src/layouts/ConsumerLayout.jsx:17-22, 32`).

**The journey in one paragraph**
A campus customer signs in with an email or mobile number and a password, or asks for a one-time code by email. A new account goes through four onboarding steps, including a delivery location that must fall inside the IIT Kharagpur campus boundary. Home lists approved stalls with live open or closed status. The customer filters or searches, opens a stall and adds dishes; a cart holds one stall. The cart shows the item total, any seller delivery charge and "Payable to seller". On "Confirm order" the customer picks "Cash on delivery", or "Pay by QR" if the stall has uploaded a QR, and taps "Place order". Tracking is a chat thread with the stall: it accepts, cooks, marks the order ready and sends it out. A QR customer pays the stall's QR after acceptance, and the stall confirms the payment before cooking. At the door a cash customer pays, the stall taps "Yes, cash received", and the customer tells the stall a six-digit handover code. The stall enters it and the order becomes "Delivered". A review sheet then pops up, and "Report" sends an issue to SETU campus staff.

## 2. Customer journey

### 2.1 Sign-in (password first, email code second)

**Screens and copy** (`/signin`, start mode)
- Cards: "Customer" ("Order from approved campus stakeholders"), preselected, and "Stakeholder" ("Register a stall and run live orders") (`client/src/data/campus.js:41-42`; `client/src/pages/SignIn.jsx:40, 263-280`).
- At 981 px and up, a dark art panel is headed by the brand row (crest, the SETU tile with "SETU Services" / "Campus", the 75-years mark) (`client/src/ui/BrandBanner.jsx:45-53`). It reads "The campus, and only the campus." and "Approved local stakeholders, delivered to your hall. SETU checks the licence and holds the record. You pay the stakeholder directly — no wallet, no commission, no middle layer.", then the stats "Delivery" / "Campus only", "Commission" / "None", "Payment" / "Direct" (`client/src/pages/SignIn.jsx:212-224`).
- The wide form column opens with a Light/Dark/System picker, then "Signing in as" / "Customer", then "IIT Kharagpur campus accounts only" (`client/src/pages/SignIn.jsx:235-257`). At 980 px or less, the art panel, hero, lede and stats are hidden; the brand row heads the page and the theme control floats (`client/src/styles.css:411-417, 952, 979-984`).
- Fields: "Mobile number or email" (placeholder "you@kgpian.iitkgp.ac.in", hint "Your institute email, or the mobile number on your account.") and "Password" with a show/hide eye. Then "Sign in" ("Signing in…") and the link "Email me a one-time code instead" ("Sending a code…") (`client/src/pages/SignIn.jsx:290-330`).
- Card: "New here? Create a customer account — it takes a moment, and your orders follow the account on any device." with "Create a Customer account" (`client/src/pages/SignIn.jsx:357-365`).
- Footer: "By continuing you accept the SETU Services terms and the campus marketplace policy. SETU approves and lists providers; it does not sell food, deliver it, or take payment for it." The two named documents link to `/help/terms-privacy` and `/help/marketplace-policy` (`client/src/pages/SignIn.jsx:429-433`).

**Behaviour**
- "Sign in" stays disabled (outline style, 40% opacity) until the identifier is valid and a password is typed (`client/src/pages/SignIn.jsx:321-322`; `client/src/styles.css:165`).
- A valid identifier is x@y.z, or 10 digits starting 6-9 once non-digits are removed and a leading 91 or 0 is dropped (`client/src/lib/validate.js:7-12, 35`). The error shows after the field loses focus (or the code link is pressed), then stays live (`client/src/pages/SignIn.jsx:78, 134, 302`).
- Input with no "@" and at least one digit gets "Enter a 10-digit Indian mobile number."; other invalid input gets "Enter a valid email address or a 10-digit mobile number."; an empty field shows nothing (`client/src/lib/validate.js:28, 41-42`).
- Success stores the token in localStorage `ce_token`, opens Socket.IO and sends a CUSTOMER to `/` (replace); with no saved address it then lands on `/onboarding` (`client/src/state/AuthContext.jsx:19-35, 72-81`; `client/src/pages/SignIn.jsx:117-119`; `client/src/App.jsx:69-71`).
- Errors: wrong details 401 "Those sign-in details did not match an account"; a customer account on the Stakeholder card 403 'This is a Customer account. Select "Customer" above to sign in.'; a mobile shared by two accounts 409 "More than one account uses this mobile number. Sign in with your email address instead." (`server/src/modules/user/user.service.js:52-57, 122-129, 154-157`).

**API**
- `POST /api/auth/login` {identifier, password, portal:"customer"} → 200 "Login successful", data {token, user} (`client/src/state/AuthContext.jsx:84-87`; `server/src/modules/user/user.controller.js:22-28`).
- Right after sign-in: `GET /api/cart` (`client/src/state/CartContext.jsx:84-87`). Home then loads `GET /api/orders`, `GET /api/restaurants` and `GET /api/restaurants/cuisines` (`client/src/lib/useOrders.js:22`; `client/src/lib/useProviders.js:29, 49`).
- No `GET /api/auth/me` follows a customer sign-in; it runs only at boot with a stored token. `GET /api/auth/campus` runs on every page load (`client/src/state/AuthContext.jsx:43-62, 76`).
- Login, signup and stakeholder signup share one per-IP bucket of 10 requests per 15 minutes; over it: 429 "Too many attempts. Wait a minute and try again." It is skipped only when `RATE_LIMIT_DISABLED` is 'true' (`server/src/middleware/rate-limit.js:5-41`).

**Alternative: one-time code by email**
- The link needs a valid identifier but no password, and is disabled while busy or during a server cooldown (`client/src/pages/SignIn.jsx:134, 329`).
- `POST /api/auth/otp/request` {identifier, portal:"customer"} → data {success, message "We emailed a code to <masked>", identifier, sentTo, expiresInSeconds: 600} (`server/src/modules/user/user.service.js:419-426`). `sentTo` is the account's email masked to two characters plus "***@domain" (e.g. st***@campus.local), even when a mobile number was typed (`server/src/services/MailService.js:49-53`; `server/src/modules/user/user.service.js:376`).
- Code screen: "Back", "Enter the code", "We emailed a six-digit code to <sentTo>. It expires in 10 minutes." (the 10 minutes is hard-coded) and six digit boxes (`client/src/pages/SignIn.jsx:372-385`). Below: "Verify and continue" ("Checking…"), then "Resend available in 30s" beside a grey "Resend code"; at zero, "Did not get the code? Check spam, or" with a live "Resend code" (`client/src/pages/SignIn.jsx:387-395`).
- `POST /api/auth/otp/verify` {identifier, code, portal} → 200 "OTP verified", data {token, user} (`client/src/state/AuthContext.jsx:103`; `server/src/modules/user/user.controller.js:49`). A wrong code gets 400 "That code is incorrect or has expired. N attempts left."; the fifth failure names a lock time and says to sign in with the password (`server/src/modules/user/user.service.js:460-473`).
- The email: subject "Your SETU Food sign-in code", with "SETU Food" in an #0033DA header band and in the footer (`server/src/services/mail.templates.js:12-13, 36, 55, 57, 68, 73`). The research did not record the rest of the body text.
- Limits: a code lives 10 minutes. Each identifier gets 5 requests and 5 wrong codes per 3 hours (the 5th failure starts a 3-hour lock), and each IP 50 failed verifications (`server/src/modules/auth/otp.policy.js:5-23`). Request and verify share a per-IP bucket of 6 per 10 minutes (`server/src/middleware/rate-limit.js:5-41`).
- On the Customer tab, an unregistered iitkgp.ac.in address (or subdomain) still gets a code, and verifying creates a CUSTOMER named after the part before "@". Any other unknown identifier gets 404 "No account found. Create one first — it takes a moment — or sign in with the email address on your account." (`server/src/modules/user/user.service.js:26, 331-345, 483-491`).

**Gotchas**
- Codes need SMTP (`SMTP_HOST`, `SMTP_PORT`, `SMTP_FROM`) and a ready Redis; without them: 503 "Sign-in codes cannot be emailed right now. Sign in with your password, or try again later." (`server/src/modules/user/user.service.js:45, 371`; `server/src/modules/auth/otp.limiter.js:183-185`). The API never returns or logs a code (`claude.md:124-126`).
- There is no auto-submit and Enter does nothing: type six separate digits from box 1, then click "Verify and continue". Each box holds one character, so a pasted code keeps only its first digit (`client/src/pages/SignIn.jsx:80-86, 101-107, 381`).
- During a password sign-in the code link also reads "Sending a code…" (shared busy flag) (`client/src/pages/SignIn.jsx:171, 330`).
- An account auto-created by code has no real name, so Home greets it like "Good morning, 22cs10099" (`server/src/modules/user/user.service.js:483-491`; `client/src/pages/Home.jsx:19-24, 110-114`).
- On every route a banner "Install SETU Services" / "Add to home screen for a faster, app-like experience" with "Install" and × is fixed over the bottom (z-index 9999) unless the app runs standalone. Dismissing it lasts only until reload, and "Install" with no captured prompt calls `window.alert()` (`client/src/components/PWAInstallBanner.jsx:33, 45, 82-110`; `client/src/styles.css:1636-1643`).
- A 401 deletes `ce_token` but leaves the user on screen until a reload (`client/src/lib/api.js:67`).

### 2.2 New account and four-step onboarding

**Sign-up** (a mode of `/signin`)
- Heading "Create your Customer account"; sub "Your orders follow the account, so history works on any device. Stakeholders see your first name, your hall and your phone number." (`client/src/pages/SignIn.jsx:405-408`).
- Fields: "Name", "Institute email", "Phone" (hint "The seller calls this number at handover.") and "Password" (`client/src/pages/SignIn.jsx:410-418`). The password hint shows "At least 8 characters, with an uppercase letter, a lowercase letter and a symbol.", then "Still needs <missing items>.", then "Strong enough." (`client/src/lib/validate.js:48-61`).
- "Create account" ("Creating…") unlocks once the password passes. The form is not noValidate, so the browser's own required and email checks appear first (`client/src/pages/SignIn.jsx:288, 410-422`).
- `POST /api/auth/signup` {name, email, phone, password} → 201 "Signup successful", data {token, user} (`client/src/state/AuthContext.jsx:89-92`; `server/src/modules/user/user.controller.js:30-33`).
- Server errors: 400 "Choose a stronger password — it needs …"; 409 "An account with this email already exists" or "An account already uses this mobile number"; 400 "Enter a valid 10-digit mobile number" (`server/src/modules/auth/password.policy.js:37`; `server/src/modules/user/user.service.js:180-194`).
- There is no institute-domain rule: any valid email works, and an iitkgp.ac.in address is only copied into instEmail (`server/src/modules/user/user.service.js:175-178, 204`). The new account has no address, so it lands on `/onboarding` (`server/src/modules/user/user.service.js:198-206`; `client/src/App.jsx:69-71`).

**Onboarding screens** (`/onboarding`)
- Art panel, at 981 px and up only: the small SETU mark, "SETU Services" "Campus", "Four questions, then you can order.", "We ask only what a delivery needs. Everything here is editable later in your profile.", and "Signed in as customer" over the email. Phones get no brand row at all, only the stepper (`client/src/pages/Onboarding.jsx:107-135`; `client/src/styles.css:416`).
- Stepper: "You", "Where you live", "Preferences", "How this works". Footer: "Step N of 4 · <step name>" (`client/src/pages/Onboarding.jsx:19, 126-135, 306`).
- Step 1: "Confirm your campus identity" / "Stakeholders see your first name, your delivery location and your phone number — nothing else." Read-only Name, Institute email and Phone (Name and Phone hint "Change it from your profile."), plus "Roll number and department arrive with the account once institute sign-in is connected. You will find them under Profile → Your details." (`client/src/pages/Onboarding.jsx:139-151`).
- Step 2: "Where should orders arrive?" / "Set it on the map so the stakeholder reaches the right door, not just the right building. SETU delivers inside the campus area only." (`client/src/pages/Onboarding.jsx:157-161`).
- Step 2 controls: a "Delivery location" box, "Choose on the map" ("Use your device location, search for your hall, or drop a pin."; later "lat, lng · ±Nm"), and "Use my current location" / "Fastest way to set this — we will confirm it on the map" (`client/src/pages/Onboarding.jsx:165-212`).
- Then "Room or wing" (placeholder "B-212", hint "Shown to the stakeholder at handover.") and "Save as" chips "Home", "Office/College", "Other" (`client/src/pages/Onboarding.jsx:222-226`; `client/src/ui/SaveAs.jsx:34-51`). Continue needs coordinates, a non-blank room and a Save-as choice; an "Other" name may not be "Home" or "Office/College" (`client/src/pages/Onboarding.jsx:73`; `client/src/lib/addressTags.js:27-31`). Section 2.3 covers the picker.
- Step 3: "What should we show first?" / "Stalls serving these move to the top of the home page. Nothing is hidden from you, and you can change this in Profile." Cuisine chips come from `GET /api/restaurants/cuisines`, with "Loading cuisines…" while the list is empty (`client/src/pages/Onboarding.jsx:250-256`).
- Step 3 toggles: "Start with vegetarian only" (off) with "Home and search open with the Veg filter on. You can clear it any time.", and "Notify me about my orders" (on) with "Each step from accepted to delivered, plus payment reminders and cancellations. Nothing promotional." (`client/src/pages/Onboarding.jsx:62-63, 263-266`).
- Step 4: "Three things SETU does not do" / "Worth reading once. It is what makes this different from a delivery app." (`client/src/pages/Onboarding.jsx:273-274`). Its three cards (`client/src/pages/Onboarding.jsx:21-28`):
  - "SETU never takes your money": "There is no checkout, card form or wallet. You pay the seller directly on delivery, or by UPI to the seller’s own handle." (`client/src/pages/Onboarding.jsx:22-23`)
  - "SETU does not deliver": "The seller brings the order themselves. You will see a status timeline, not a rider on a map." (`client/src/pages/Onboarding.jsx:24-25`)
  - "SETU approves and records": "Every seller listed here cleared a licence check. Issues you report are held against the seller’s record." (`client/src/pages/Onboarding.jsx:26-27`)
- Toggle "I understand SETU is a directory and approval gate", sub "Required. Recorded against your account with today’s date." "Start ordering" ("Saving…") unlocks only when it is on (`client/src/pages/Onboarding.jsx:73, 285-301`).

**What "Start ordering" does** (`client/src/pages/Onboarding.jsx:75-104`)
1. If notifications are on and supported, it starts push sign-up without waiting (`client/src/pages/Onboarding.jsx:79-81`).
2. `POST /api/auth/addresses` {label, tag, details, latitude, longitude, formattedAddress, placeId, accuracyMeters, source, …} → 201 "Address added", data {user} (`client/src/lib/adapt.js:226-246`; `server/src/modules/user/user.controller.js:87-90`).
3. It saves the chosen label in localStorage `setu-svc-loc` (`client/src/state/UiContext.jsx:5`).
4. `PATCH /api/auth/me/preferences` {cuisines (up to 30, 1-40 characters each), vegOnly} → 200 "Preferences saved" (`server/src/modules/auth/auth.validation.js:169-174`).
5. It navigates to `/` (replace) (`client/src/pages/Onboarding.jsx:98`).
- The acknowledgement is never sent, and no field or route stores it (`client/src/pages/Onboarding.jsx:75-104`).
- An address error toasts and stays on step 4, e.g. "This location is outside the IIT Kharagpur campus boundary." (name from `CAMPUS_NAME`). A preferences error toasts "Your food preferences did not save — you can set them in Profile." and still navigates (`server/src/services/LocationService.js:138`; `client/src/pages/Onboarding.jsx:93-101`).
- Push: `GET /api/notifications/public-key` (public), the browser permission prompt, then `POST /api/notifications/subscribe` {endpoint, keys} (`client/src/lib/push.js:30-58`). A refusal toasts "Notifications not turned on: <reason>." for 3.6 s, which can land over Home (`client/src/pages/Onboarding.jsx:80`; `client/src/state/UiContext.jsx:84-88`).
- Later sign-ins re-subscribe only when permission is already granted; they never ask (`client/src/state/AuthContext.jsx:66-69`; `client/src/lib/push.js:68-75`).

**Gotchas**
- "Loading cuisines…" stays for good if the request fails or no stall names a cuisine (`client/src/lib/useProviders.js:46-51`).
- "Use my current location" fills the box with no map, and Continue does not check the zone. An off-campus fix only warns "… Pick a campus location on the map instead." and fails at "Start ordering"; a fix less precise than 100 m shows "Your device placed you to within about Nm — open the map to check it is the right door." (`client/src/pages/Onboarding.jsx:48-59, 73`).
- The sign-up inputs and "Room or wing" have no accessible name, so select them by position or placeholder (`client/src/ui/kit.jsx:32-43`).

### 2.3 Delivery location

**Where it opens**
- On the phone Home header, DeliverTo shows the saved name (or the first part of the place) with a chevron, and "Room {room} · {area}" under it (room only when saved). With nothing chosen it reads "Set your delivery location" / "Tap to pick it on the map". On web Home it sits inline in the search bar (`client/src/ui/DeliverTo.jsx:23-49`; `client/src/pages/Home.jsx:176, 185, 227`).
- Other openers: the cart's "Deliver to" row and Profile's "Saved campus locations" (both "Pick a campus location" when empty), the web nav pill and auto-detect (`client/src/pages/Cart.jsx:118-122`; `client/src/pages/Profile.jsx:218-223`; `client/src/layouts/ConsumerLayout.jsx:55-59, 131-134`). Onboarding mounts its own copy (`client/src/pages/Onboarding.jsx:232`).
- On phones the picker is a bottom sheet (up to 94vh while searching); on web, a centred dialog up to 560 px wide with a 320 px map (`client/src/styles.css:1180, 1231, 1294-1309`).

**Permission explainer** (shown only when needed: `client/src/state/useLocationRequest.js:101-121`)
- Already granted: GPS is read at once (high accuracy, 12 s timeout, maximumAge 0) (`client/src/lib/geolocation.js:124-157`).
- Not yet asked: "Allow location for SETU?" / "SETU uses your location to find nearby stalls and to confirm whether delivery reaches where you are. It is only read when you ask for it." with "Not now" and "Allow location". Footnote: "Your device will ask next. Choose Allow." (phone user agent) or "Your browser will ask next. Choose Allow." (desktop) (`client/src/ui/LocationPermissionDialog.jsx:37-45, 87-104`; `client/src/lib/platform.js:13-21`).
- Denied: "Location access is blocked" / "Your browser has blocked location for this site, so it will not ask again on its own. Turn it back on and SETU will pick up where it left off.", with steps under "On iPhone or iPad", "On Android" and "In this browser", plus "Not now" and "Try again" (`client/src/ui/LocationPermissionDialog.jsx:39-48, 67-94`). "Try again" while still blocked adds "Still blocked. Set Location to Allow for this site, then try again." (`client/src/state/useLocationRequest.js:133-148`).
- A denial that cannot be confirmed (e.g. iOS) reads "SETU couldn’t get your location", with "The request was declined, or Location Services is turned off on this device. Check the settings below, then try again — your phone may ask for permission the next time." on phones (`client/src/ui/LocationPermissionDialog.jsx:41, 49-53`).

**Picker, select step**
- Title "Select a location"; subtitle "SETU delivers inside the IIT Kharagpur campus boundary", shown once `GET /api/location/zone` answers (`client/src/ui/LocationPicker.jsx:70-76, 231-238`). Search box: "Search for a hall, gate or area" (`client/src/ui/LocationPicker.jsx:248-249`).
- GPS row: "Use current location" / "Detect where you are right now" ("Locating…"); when denied, "Turn on location" / "Blocked for this site — tap to fix it"; on unsupported devices, "This device cannot report its location" (`client/src/ui/LocationPicker.jsx:268-289`). Map row: "Select another location" / "Place a pin on the map yourself" (`client/src/ui/LocationPicker.jsx:294-301`).
- "Saved locations": tag icon (house, building or map pin), name, "room · address" and a check on the current one; sorted Home, Office/College, then the rest. A legacy row with no coordinates reads "Tap to set this on the map" (`client/src/ui/LocationPicker.jsx:304-328`; `client/src/lib/addressTags.js:8-12, 22-24`).
- Search runs after 2 characters and 250 ms, limited to India and the campus box plus 8 km (`client/src/ui/PlaceSearch.jsx:6-9`; `client/src/lib/places.js:16-33`). Copy: "Searching…", "Getting the address…", "No places found for “{term}”" / "Check the spelling, or try a nearby hall or gate", "Search is not working right now", and below the results "Place a pin on the map" / "Pick the exact spot yourself" (`client/src/ui/PlaceSearch.jsx:162-172, 217-259`).

**Picker, confirm step**
- Title "Confirm delivery location". While a GPS fix resolves: "Getting your location…" / "Checking where your device thinks you are." (`client/src/ui/LocationPicker.jsx:107-112, 232, 340-349`).
- Card: eyebrow "Current location" (GPS), "Saved location" or "Selected location"; the place; the full address; "lat, lng · ±Nm", e.g. "22.316000, 87.303500 · ±20m" (±m only for GPS) (`client/src/ui/LocationPicker.jsx:356-367`).
- Inside the zone: "Location is within the IIT Kharagpur delivery area." Outside: "This location is outside the IIT Kharagpur campus boundary. About 1.4 km outside it." and a disabled "Outside delivery area" (`server/src/services/LocationService.js:132-139`; `client/src/lib/geo.js:18-22`; `client/src/ui/LocationPicker.jsx:369-377, 413-418`).
- A fix vaguer than 100 m adds "Your device could only place you to within about {N}m. Check it on the map before confirming." (`client/src/ui/LocationPicker.jsx:114-119`).
- "Save as" is required ("Home", "Office/College", "Other"); until chosen: "Choose one to save this address."; "Other" asks "Name this place, e.g. Friend's house" (max 30) (`client/src/ui/SaveAs.jsx:34-56`). Warnings: "Replaces your saved Home (…)." or "You already have “X” (…). This replaces it." An account holds one Home, one Office/College and one row per Other name (`client/src/ui/SaveAs.jsx:57-62`; `server/src/modules/user/user.service.js:592-609`).
- "Address details" ("Floor / room / hall / block (optional)", max 120) and "Adjust on the map" / "Move the pin to the exact spot". Footer: "Back" and "Confirm location", disabled until the server says serviceable and a name is chosen (`client/src/ui/LocationPicker.jsx:393-419`).
- Confirm saves a new or changed address (`POST /api/auth/addresses`), selects it, writes `setu-svc-loc` and closes, with no success toast. An unchanged saved row writes nothing (`client/src/layouts/ConsumerLayout.jsx:157-166`; `client/src/ui/LocationPicker.jsx:175-186`).

**Map step**
- "Select delivery location", the same boundary subtitle, and a floating search "Search for a hall, gate or department" (`client/src/ui/MapLocationPicker.jsx:317-336`). A fresh map frames the campus with no pin: "Use your location, search for a hall, or tap the map to drop a pin." (`client/src/ui/MapLocationPicker.jsx:208-209, 226, 381-385`).
- A tap drops the pin and it can be dragged; each position is checked with `POST /api/location/check`. The card shows "Selected location", the coordinates at once, and "Looking up the address…" until the browser geocoder returns an address or "Dropped pin" (`client/src/ui/MapLocationPicker.jsx:64-111, 216-249, 387-398`).
- The GPS button reads "Use my location" (tooltip "Use my current location"). Footer: "Back" and "Use this location", which hands the pin back to Confirm without saving (`client/src/ui/MapLocationPicker.jsx:359-370, 413-428`).
- The boundary is drawn as a non-clickable polygon: stroke #0033DA at 0.5 opacity, fill #0033DA at 0.035 (`client/src/ui/MapLocationPicker.jsx:190-207`).

**Campus boundary** (the server decides)
- A 78-point "Main Campus Boundary" polygon of 4.69 km² replaced a 2 km circle; it is validated at startup (`server/src/config/campus-zone.js:6-9, 16-51`).
- It is re-checked on every address save and every order: 400 "This location is outside the IIT Kharagpur campus boundary." (`server/src/modules/user/user.service.js:550-555`; `server/src/modules/order/order.service.js:262-267`; `server/src/services/LocationService.js:143-148`).
- A point within 0.5 m of the line counts as inside; (0,0) is refused with "That location could not be read — pick it on the map" (`server/src/utils/geo.js:103-104`; `server/src/services/LocationService.js:91-95`). `CAMPUS_ZONE_ENABLED` set to 'false' turns the checks off; `server/.env` has them on (`server/system/configs/config.js:164`).
- Points checked with `server/src/services/LocationService.js` in a scratch run: P1 22.3160, 87.3035; P2 22.3146, 87.3110; P3 22.3134, 87.3180 are inside (708/829/627 m from the edge). OUT 22.3350, 87.3110 is 1368 m outside ("About 1.4 km outside it."). The seed address 22.3149, 87.3105 is inside (`server/src/seed/seed.js:328-334`).

**Saved addresses in Profile**
- "Saved campus locations": the default row reads "Default · Room {room} · {place}". "Use {label}" (check) selects a row without the picker; "Remove {label}" (trash) calls `DELETE /api/auth/addresses/:id` → "Address removed" (`client/src/pages/Profile.jsx:218-255`; `server/src/modules/user/user.route.js:48-49`).
- "Room or wing" ("Shown to the seller at handover.") with "Save" toasts "Room saved." (`client/src/pages/Profile.jsx:112-130`). Edits reuse `POST /api/auth/addresses` with `id`; there is no PUT or PATCH (`server/src/modules/user/user.service.js:582-609`).

**Auto-detect** (phones only)
- It runs only below 760 px, for a CUSTOMER, once per app load or sign-in, and only when location is already granted; it never asks (`client/src/layouts/ConsumerLayout.jsx:122-135`; `client/src/state/useAutoLocation.js:27-64`). It takes a 10 s fix and calls `POST /api/location/detect` {latitude, longitude, accuracyMeters, addressId?} (`client/src/state/useAutoLocation.js:65-68`; `client/src/lib/resolveLocation.js:71-78`).
- Server rules: a device is "at" a saved address within its fix accuracy, clamped to 100-250 m; "moved" means more than 500 m away; fixes vaguer than 500 m are ignored (`server/src/services/LocationService.js:16-25, 209-223`).
- "keep": nothing visible. "switch": the matching saved address is selected, with the toast "Delivering to {name} — you're there now" (`client/src/layouts/ConsumerLayout.jsx:127-130`).
- "confirm": the picker opens on Confirm (eyebrow "Current location") with "You seem to be somewhere new. Name this place to deliver here, or close to keep your current address."; a 101-500 m fix adds " Your device placed you only roughly, so check it on the map first." (`client/src/ui/LocationPicker.jsx:46-50, 380-385`).
- Closing without saving silences that spot (about 110 m) for 12 hours via localStorage `setu-autoloc-skip` (`client/src/state/useAutoLocation.js:5-25`). Detection is read-only: the coordinate is compared and dropped (`server/src/services/LocationService.js:165-166`).

**Location API**
- `GET /api/location/zone` is public; `POST /api/location/check` takes any signed-in role with no rate limit; `POST /api/location/detect` is CUSTOMER-only (`server/src/modules/location/location.route.js:14-26`).
- `GET /api/location/reverse?latitude=&longitude=` (signed in) serves the GPS path, falling back to `/check` (`client/src/lib/resolveLocation.js:17-43`). `/reverse` and `/detect` share 20 lookups per minute per account (`server/src/middleware/rate-limit.js:43-62`).

**Gotchas**
- The GPS wording varies: the picker row says "Use current location", only onboarding says "Use my current location", and the map button says "Use my location" (`client/src/ui/LocationPicker.jsx:281`; `client/src/pages/Onboarding.jsx:201`; `client/src/ui/MapLocationPicker.jsx:361-368`).
- The selection is per browser (`setu-svc-loc`), and the research disagrees on whether sign-in fills an empty one. Two checks found it is never filled (`client/src/state/AuthContext.jsx:140`): a fresh browser shows "Set your delivery location", and "Review order" and "Place order" stay disabled until a saved location is picked. A third says the isDefault address (or the first) is selected (`client/src/state/AuthContext.jsx:135-143`). Check this on the capture stack.
- GPS timeouts fail silently; the row just returns to idle (`client/src/state/useLocationRequest.js:66-71`). Geolocation needs HTTPS or localhost (`client/src/lib/geolocation.js:20-43`). The dialog copy follows the user agent, while auto-detect follows the viewport width (`client/src/lib/platform.js:13-21`).
- Customers never see "Too many location lookups…", because the client swallows it (`client/src/lib/resolveLocation.js:31-43`).

### 2.4 Discover: home, filters, search, stall page, one-stall cart

**Home on a phone** (`client/src/pages/Home.jsx:183-209`)
- The header band is solid indigo (#0033DA, or #151E4D in dark) (`client/src/styles.css:2650-2663`). Rows: Deliver-to with profile initials; the greeting; a "Search sellers, dishes, cuisines" button that opens `/search`; service pills; cuisine tabs.
- The greeting uses the device clock: "Good morning" before 12:00, "Good afternoon" before 17:00, otherwise "Good evening", plus ", <first name>" (`client/src/pages/Home.jsx:19-24, 110-114`).
- Pills: "Food" (active), plus "Commute" and "Utilities", each with a "Soon" badge (#4A2E00 text on amber #FFD27A). Tapping a Soon pill toasts "<Service> launches in a later phase. The approval pipeline behind it is already built." (`client/src/ui/ServiceSwitcher.jsx:26`; `client/src/styles.css:2759-2761`; `client/src/pages/Home.jsx:118`).
- Cuisine tabs: "All", then each cuisine a listed stall serves (alphabetical), liked ones first; hidden when there are none (`client/src/pages/Home.jsx:47-49, 74, 199`; `client/src/lib/preferences.js:19-26`). On scroll, the location and search rows stay pinned while the greeting and tabs fold away (`client/src/lib/useCollapsingHeader.js:8-11`).
- "Approved sellers" heads the list with "N open now", "X of N open now" or "N listed"; with a tab chosen, "<Cuisine> · <count>" (`client/src/pages/Home.jsx:121-123, 203-204`).
- Chips: "Pure veg", "Open now", "Rated 4.0+", "Under 20 min" (`client/src/pages/Home.jsx:133-138`). The server runs "Pure veg", "Open now" (which includes closing soon) and the cuisine filter (`client/src/lib/useProviders.js:24-27`; `server/src/modules/restaurant/restaurant.service.js:94-111`).
- The client runs "Rated 4.0+" (which drops "New" stalls) and "Under 20 min" (prep of 20 or less). "Pure veg" starts on for VEG accounts (`client/src/pages/Home.jsx:82, 97`).
- Order: open stalls first, then by liked cuisines, then by rating and name (`client/src/pages/Home.jsx:98-102`; `server/src/modules/restaurant/restaurant.service.js:104`). Only approved stalls (or legacy ones with no status) that have a menu item are listed (`server/src/modules/restaurant/restaurant.service.js:45, 57-59, 86`).
- When nothing is open: "Nothing is open right now." ("Nothing here is open right now." with a filter on), then "Sellers serving <place> open again later — you can still browse menus." (`client/src/pages/Home.jsx:162-166`).
- Other states: "No sellers match" / "Clear a filter, or try a different cuisine." with "Clear filters"; "Couldn’t load sellers"; "No sellers listed yet" / "Once a campus admin approves a stall it appears here." (`client/src/pages/Home.jsx:147-158`).
- The list ends with "The seller is responsible for food quality, hygiene, delivery and collecting payment. SETU is the approval gate and directory only — it does not cook, deliver, or handle your money." Only "SETU is the approval gate and directory only" is bold (`client/src/ui/kit.jsx:96-101`).

**Stall cards** (`client/src/ui/StallCard.jsx:18-57`)
- Image: the cover, else the logo, else initials. Line 1: the name plus "4.3★" or "New" (never a review count). Line 2: cuisines joined by " · ", else the description, else "Campus kitchen". Meta: status dot and label, "<prep> min" while open, "Pure veg", and "Min ₹X" when a minimum is set.
- On a closed card only the image greys out; the dot is green when open, amber when closing soon, grey when closed (`client/src/styles.css:2832, 2846-2849`).
- Status labels come from the server in campus time (Asia/Kolkata), with default hours 10:00-22:00 and "closing soon" from 30 minutes before closing: "Open till 10:00 PM", "Closing in 20 min", "Closed · opens at 10:00 am", "Closed · opens tomorrow at 10:00 am", "Closed by the seller", "Closed · reopens at 4:00 pm", "Open" (`server/src/utils/store-hours.js:11-17, 147-253`).

**Home on the web**
- A gradient band adds "Every stall is licence-checked by SETU — you pay the seller directly." and an inline search with Deliver-to; cuisines collapse into one "Cuisines" chip ("All cuisines" plus the list) (`client/src/pages/Home.jsx:127-132, 215-249`). Nav: "SETU Services", "Browse", "Orders", "Profile", a theme toggle and a cart icon with a count badge (`client/src/layouts/ConsumerLayout.jsx:40-94`).

**Search** (`/search`)
- A back arrow and an auto-focused box "Sellers, dishes, cuisines". Chips: "Veg only", "Non-Veg only", "Open now", "Under 20 min", then one per cuisine; there is no "Rated 4.0+" (`client/src/pages/Search.jsx:33-59`).
- "Recent searches" shows a fixed list (Kathi roll, Ghee roast dosa, Chai, Momo) only while nothing is typed or toggled (`client/src/pages/Search.jsx:10, 29, 62-73`).
- It matches stall names, cuisines and descriptions, and dish names, categories and descriptions, 220 ms after typing stops; typo tolerance applies only to words of 5+ letters (`server/src/utils/dish-search.js:10-13, 60-62`; `client/src/lib/useProviders.js:38`).
- A typo gets "No exact match for “X”. Showing results for <best match>." (a dish, a stall or a cuisine, e.g. "Chicken Biriyani" → "Chicken Biryani"). A dish no menu has gets "“X” isn’t on any menu right now. Closest dishes:" plus up to 4 dish chips (`client/src/ui/SearchHits.jsx:29-55`).
- Rows show the logo or initials, name, "★4.3" or "New", cuisines, "Pure veg" or "Veg & non-veg", prep time, "Min ₹X" and status, plus up to 3 matching dishes with a price or "Sold out" (`client/src/ui/ProviderCard.jsx:13-45`; `client/src/ui/SearchHits.jsx:9-22`).
- No match: "Nothing matches “X”" / "No stall or dish on campus is close to that. Try a dish name, a stall or a cuisine — or clear a filter."; with nothing typed: "No sellers match that" / "Try a wider cuisine, or clear the open-now filter — some kitchens reopen later in the evening." Both offer "Clear filters" (`client/src/pages/Search.jsx:78-84`).

**Stall page** (`/seller/:id`)
- An indigo band shows the logo or initials (never the cover photo), the name and cuisines, then a facts row ("4.3★" or "New", status, "<prep> min" while open, "Min ₹X") and "Approved by SETU · you pay the seller directly" (`client/src/pages/SellerDetail.jsx:17-27, 61-98`).
- On phones a sticky back row always returns home, and there is no tab bar (`client/src/pages/SellerDetail.jsx:30-58, 389`).
- Closed: "Store closed" with "Opens at 10:00 am. You can look through the menu; ordering opens when the stall does." (or "The seller has closed for now. You can look through the menu; ordering opens when the stall does."); there are no ADD buttons (`client/src/pages/SellerDetail.jsx:106, 125, 234-248`).
- Menu bar: "Veg" and "Non-veg" chips, except on pure-veg stalls; phone tabs "All" plus categories when there are 2 or more. The bar scrolls away with the page (`client/src/pages/SellerDetail.jsx:145-213`; `client/src/styles.css:2908-2911`).
- Sections read "<Category> <count>" in alphabetical order. A dish row shows a veg mark, name, price and description, or "Out of stock today" with no ADD. "ADD" turns into a "− n +" stepper (`client/src/pages/SellerDetail.jsx:100-129, 222`; `client/src/ui/kit.jsx:230-241`).
- Only a dish whose photo has loaded opens an item sheet: "Vegetarian" or "Contains non-vegetarian ingredients", the price, the stall name, and "Add to cart" when orderable (`client/src/pages/SellerDetail.jsx:118-124, 354-382`).
- Below the menu: "Hours" (e.g. "10:00 AM – 10:00 PM"), the disclosure, and "What customers say · N reviews" (up to 3, rotating every 6 s) (`client/src/pages/SellerDetail.jsx:254-262`; `client/src/components/StallReviews.jsx:6-8, 43-87`). There is no phone number or address (`client/src/pages/SellerDetail.jsx:250-262`).

**One stall per cart**
- The cart lives on the server per customer, follows the account across devices and syncs between tabs; names and prices are re-read from the menu (`client/src/state/CartContext.jsx:22-33`; `server/src/modules/cart/cart.model.js:3-11`).
- A dish from another stall replaces the cart at once, with no confirmation, and toasts "One order goes to one seller — your earlier cart was replaced." (`client/src/state/CartContext.jsx:131-137`; `server/src/modules/cart/cart.service.js:96-108`). At most 50 of one dish (`server/src/modules/cart/cart.route.js:19-23`).
- Phones show a "View cart" button on Home and stall pages, with the count only in its screen-reader label (`client/src/ui/CartBar.jsx:13-24`). The web shows a floating bar "<stall>" / "N items · ₹X" with "Review order", which opens the cart (`client/src/ui/CartPopup.jsx:38-56`).

**APIs**
- `GET /api/restaurants?q=&food=veg|nonveg&openNow=1&cuisine=`, `GET /api/restaurants/cuisines`, `GET /api/restaurants/:id` (id or slug, with the menu) and `GET /api/restaurants/:id/reviews` (`server/src/modules/restaurant/restaurant.service.js:85-200`; `client/src/components/StallReviews.jsx:50-58`).
- `GET /api/cart` and `PUT /api/cart/items/:itemId` {qty 0-50, source} → {cart, replaced} (`server/src/modules/cart/cart.service.js:27-112`).

**Gotchas**
- Search rows read "20–20 min" (`client/src/ui/ProviderCard.jsx:34`). Labels, ADD buttons and the greeting all follow the capture clock. A completed, unreviewed order from the last 7 days pops a review sheet over Home (`client/src/components/ReviewPrompt.jsx:8-24`).

### 2.5 Cart and checkout

**Cart** (`/cart`)
- Header "Your order" with the stall name; each line has a veg mark, the name, "₹X each", a stepper and the line total (`client/src/pages/Cart.jsx:67-75, 98-108`). Below the stall's minimum: "Add ₹X more to reach this seller’s minimum of ₹Y." (`client/src/pages/Cart.jsx:111-116`).
- "Deliver to" shows the full location label, or "Pick a campus location"; under it is the customer's name, prefixed "Room <n> · " when a room is saved. Tapping it opens the picker (`client/src/pages/Cart.jsx:57, 118-128`).
- Totals: "Item total"; "Seller delivery charge" with "Set by the seller, collected by the seller" (only when the fee is above ₹0); "Payable to seller" in bold (`client/src/pages/Cart.jsx:130-136`).
- Disclosure: "You pay <stall> directly. SETU does not process this payment and is not the merchant of record. Quality and delivery are the seller’s responsibility." (`client/src/pages/Cart.jsx:138`; `client/src/ui/kit.jsx:102-105`).
- The bottom bar shows the total, "to <stall>" and "Review order", disabled below the minimum, when the stall is closed or not accepting orders, or with no location (`client/src/pages/Cart.jsx:54-56, 142-150`).
- Warnings: "<stall> closed while you were ordering." plus the status and "Your cart is kept — place it once they are back."; or "<stall> is closing soon." plus "<label> — place this order now if you want it today." (`client/src/pages/Cart.jsx:79-95`).
- Empty cart: header "Cart", then "Your cart is empty" / "One order goes to one seller. Add items from a seller page to start." and "Browse sellers" (`client/src/pages/Cart.jsx:36-51`).

**Confirm order** (`/confirm`)
- Header "Confirm order". A dark card shows "Amount payable to the seller", the total, and "SETU does not collect this. {stall} receives it directly." (`client/src/pages/Confirm.jsx:107, 112-117`).
- "How will you pay?": "Cash on delivery" ("Hand ₹X to the seller at your door."), and "Pay by QR" only when the stall has a QR on file ("{stall}’s QR appears here once they accept. You will have five minutes to pay, and can send a screenshot if it takes longer.") (`client/src/pages/Confirm.jsx:41-44, 127-147`).
- Without a QR: "{stall} has not put a payment QR on file, so this order is cash on delivery." (`client/src/pages/Confirm.jsx:155-160`).
- Then the "Order" lines, a non-tappable "Deliver to" ("{label} · {place} · Room {room}"), "Item total", "Seller delivery charge" ("Set and collected by the seller") and "Payable to seller" (`client/src/pages/Confirm.jsx:171-182`).
- "Note for the seller" (placeholder "Call on arrival — the gate closes at 11 PM", copy from the research's `/confirm` screen list) is sent as `note`, max 300 (`server/src/modules/order/order.schema.js:8-51`). The "You pay … directly" disclosure follows (`client/src/pages/Confirm.jsx:189`).
- "Place order · ₹X" ("Sending to seller…") is disabled only while sending or with no location. A saved location with no coordinates is refused: "Set this delivery location on the map before ordering." (`client/src/pages/Confirm.jsx:69-72, 193-196`). Success clears the cart and replaces the page with `/track/{orderId}` (`client/src/pages/Confirm.jsx:91-92`).

**Order API**
- `POST /api/orders` {restaurantId, items:[{itemId, quantity}], fulfilmentType:"DELIVERY" (hard-coded), deliveryAddress:{label, details, latitude, longitude, formattedAddress, placeId, accuracyMeters, source}, paymentMethod:"COD" or "QR", note} → 201 "Order placed", status PLACED, paymentStatus PENDING (`client/src/pages/Confirm.jsx:74-90`; `server/src/modules/order/order.schema.js:8-51`).
- The server prices items from the database. It refuses a closed stall ("{stall} is closed right now — reopens …"), an out-of-stock dish ("<dish> is out of stock today"), QR with no QR on file ("{name} has not uploaded a payment QR. Choose cash on delivery."), missing coordinates and off-campus points (`server/src/modules/order/order.service.js:139-180, 252-267`).
- It sets total = item total + the stall's delivery fee, empties the cart and never checks the minimum (`server/src/modules/order/order.service.js:195-237`). Order numbers look like CE1013-7L73: CE, month, day, then up to 4 characters (`server/src/modules/order/order.service.js:122-128`).

**Charges and payment choices**
- No platform fee, commission, service charge, tax or packaging fee exists in the code; a search found only "no commission" copy (`server/src/modules/order/order.service.js:195-203`; `client/src/data/policies.js:70`).
- Each stall sets its own delivery charge in whole rupees, ₹0-₹500; the default is ₹0, which hides the fee row (`server/src/modules/restaurant/restaurant.service.js:22-24, 252-258`). The minimum order defaults to 0, no seller screen edits it, and only the cart enforces it (`server/src/modules/restaurant/restaurant.model.js:17`; `client/src/pages/Cart.jsx:54-56`).
- Policy: "Any delivery charge is set and collected by the stall, and shown before you order." (`client/src/data/policies.js:32`).
- Cash on delivery is always offered; "Pay by QR" needs a stall QR (`client/src/lib/adapt.js:54`). Policy: "You pay the stall directly — in cash at handover, or by scanning the stall’s own UPI QR code." and "No card numbers, bank details or UPI PINs. Payment happens between you and the stall, outside SETU." (`client/src/data/policies.js:30, 111-114`).

**Gotchas**
- The cart total can briefly leave out the delivery charge until the stall record loads (`client/src/pages/Cart.jsx:21-28, 62`). A dish that sells out after being added stays in the cart unflagged, and checkout then fails (`server/src/modules/cart/cart.service.js:51`; `server/src/modules/order/order.service.js:178-180`).
- Seed stalls have no QR, a ₹0 fee and no minimum, so "Pay by QR", the fee row and "Min ₹X" need prepared data (`server/src/seed/seed.js:16-37, 345-350`).

### 2.6 Cash order lifecycle and the handover code

The stall sends actions, not statuses: `PATCH /api/orders/:id/status` {action} → 200 "Order updated" (`server/src/modules/order/order.route.js:62`; `server/src/modules/order/order.controller.js:103-114`). Steps cannot be skipped. A wrong step gets 400, e.g. "Cannot mark ready an order that is ACCEPTED"; a lost race gets 409 "This order is already {STATUS} — refresh to see where it is now." (`server/src/modules/order/order.lifecycle.js:81-85, 101-108`).

1. **Placed.** The thread opens with "Order {number} placed · ₹X · cash on delivery" and a card "Waiting for the stall to accept your order." (clock icon). Headline "Waiting for the seller", subheader "{stall} · {orderNumber} · ₹X", and "Cancel order" in the bar (`server/src/modules/order/order.service.js:308-324`; `client/src/components/OrderChat.jsx:179-183`; `client/src/pages/Tracking.jsx:18-31, 145`).
   - A placed order never times out; the worker re-alerts the stall every 2 minutes, up to 5 times (`server/src/jobs/escalation.js:18-62`).
2. **Accepted** (ACCEPT): status ACCEPTED and the prep clock starts. Thread "Order confirmed by {stall}"; card "The stall accepted your order."; headline "Order confirmed"; push "Order confirmed" / "{stall} accepted your order." (`server/src/modules/order/order.lifecycle.js:156-182`).
   - Timer "Being prepared · usually ready by {h:mm am/pm}"; the bar shows "Call {stall}" (`client/src/components/PrepTimer.jsx:13, 32-36, 55-60`). Or REJECT, which needs a reason: "Order rejected — {reason}", headline "Rejected by the seller" (`server/src/modules/order/order.lifecycle.js:189-207`).
3. **Preparing** (START_PREPARING): "Preparing your order", headline "Being cooked now". **Ready** (MARK_READY): "Your order is ready", headline "Ready", timer hidden. Each also pushes "Order update" with the same line (`server/src/modules/order/order.lifecycle.js:248-261, 277-279`).
   - The prep limit is the stall's prep time (default 20; sellers pick 15, 20 or 25), capped at 25 minutes (`server/src/modules/order/order.timers.js:33-44`). Past it, the thread says "Running late — not ready within 25 minutes of being accepted. The customer can cancel it now, or keep waiting." and the timer reads "Running late — it was not ready in time. You can cancel it below, or keep waiting." (`server/src/modules/order/order.timers.js:92-102`; `client/src/components/PrepTimer.jsx:44-51`).
4. **Out for delivery** (DISPATCH, which issues the code): "On the way to {saved location name} · {room}" (e.g. "On the way to Home · B-204"), then "Handover code sent to the customer's order screen. At the door: the customer pays ₹X in cash, the stall confirms it, then enters the customer's code to complete the order." (`server/src/modules/order/order.lifecycle.js:236-271`).
   - Headline "On the way"; push "Your order is on the way" / "Pay ₹X in cash, then tell the person handing it over your handover code. It is on your order screen." (`server/src/modules/order/order.lifecycle.js:273-275`).
5. **At the door.** A handover panel sits above the message box; only the customer and the stall see it (`client/src/components/OrderChat.jsx:357-358, 672-675`).
   - Customer: "Your order is out for delivery", "Please pay ₹X in cash", six boxed digits, "Then tell this code to the stall owner or the delivery partner — that completes your order. SETU staff will never ask for it.", and "Valid until your order is handed over" (`client/src/components/HandoverPanel.jsx:137-172`).
   - Stall: "Out for delivery · collect ₹X in cash" / "Did you receive ₹X in cash from the customer? Once you have, tap below, then enter their handover code." / "Yes, cash received" (`client/src/components/HandoverPanel.jsx:177-189`). That calls `POST /api/orders/:id/handover/cash` {} → "Cash received", which records cashReceivedAt only; paymentStatus stays PENDING (`server/src/modules/order/order.handover.js:135-160`).
   - The thread says "{stall} received ₹X in cash · next, the customer's handover code" (push "Cash payment confirmed" / "Now read out your handover code to complete your order."), and the customer's panel changes to "The stall has confirmed your ₹X cash payment" / "Now tell them this code — that completes your order. SETU staff will never ask for it." (`server/src/modules/order/order.handover.js:168-170`; `client/src/components/HandoverPanel.jsx:144-147, 165`).
   - The stall sees "₹X cash received", "Out for delivery · enter the customer’s code", a "6-digit code" field, "Verify" ("Checking…") and "The right code completes the order · N tries left" (`client/src/components/HandoverPanel.jsx:191-206`). "Verify" calls `POST /api/orders/:id/handover/verify` {code} → "Handover code verified · order complete" (`server/src/modules/order/order.route.js:87-88`).
6. **Delivered.** One guarded update sets status COMPLETED, paymentStatus PAID and cashSettledAt. Thread "Delivered · handover code verified · ₹X paid in cash"; headline "Delivered"; push "Delivered" / "Your order is complete."; the bar shows "Report" and "Order again" (`server/src/modules/order/order.handover.js:55-63, 243-275`; `client/src/pages/Tracking.jsx:188-208`).

**Handover code rules**
- The code is six digits, derived by HMAC, never stored and never expiring. It goes only to the customer, through their socket room or `GET /api/orders/:id/handover` with the customer's token; the stall never sees it (`server/src/modules/order/order.handover-code.js:7-29, 42-45, 133-146`; `server/src/modules/order/order.handover.js:72-84`).
- Entering a code before confirming cash gets 409 "Confirm you have received ₹X in cash first, then enter the customer's code." (not counted as a try) (`server/src/modules/order/order.handover.js:198-202`).
- A wrong code gets 400 "That is not the right code. N tries left." ("1 try left."); the fifth miss gets "That is not the right code. No tries left — the customer needs to get a new code." and locks the code (`server/src/modules/order/order.handover.js:224-241`).
- The customer then sees "Too many wrong codes were entered" and "Get a new code" (`POST /api/orders/:id/handover/code`). An order gets at most 5 codes, including the first; after that: "No more codes can be issued for this order. Contact campus staff to finish it." (`client/src/components/HandoverPanel.jsx:109, 209-226`).
- There is no one-tap "Delivered": MARK_DELIVERED is refused with "Handing over now needs the customer's code: enter it to complete the order. For cash, confirm the cash first." (`server/src/modules/order/order.lifecycle.js:217-226`).
- 45 minutes after dispatch: "Still on the way after 45 minutes — campus staff can see this order."; the panel adds "On the way for a while — call the stall if something is wrong."; a push asks "Is your order with you yet?" (`server/src/modules/order/order.timers.js:109-125`; `client/src/components/HandoverPanel.jsx:251-256`).
- Handover requests are capped at 30 per 10 minutes per account, even with `RATE_LIMIT_DISABLED` (`server/src/middleware/rate-limit.js:64-83`).

**Cancelling**
- The customer can cancel in PLACED, AWAITING_PAYMENT or PAYMENT_OVERDUE, or once an ACCEPTED or PREPARING order is flagged late. Otherwise: "This order is already under way — call the seller on the number in your order instead" (`server/src/modules/order/order.lifecycle.js:33-34, 503-514`).
- "Cancel order" is one tap with no confirmation: `POST /api/orders/:id/cancel` {}. It toasts "Order cancelled. The seller has been told."; the thread says "Cancelled by the customer" ("Cancelled by the customer — it was not ready in time" for a late order) (`client/src/pages/Tracking.jsx:94-105, 189-192`; `server/src/modules/order/order.lifecycle.js:516-530`).
- Cancelling a late order already paid by QR adds "{stall} should refund ₹X to {name}."; SETU records this but moves no money (`server/src/modules/order/order.lifecycle.js:531-538`).

### 2.7 Pay by QR (the stall's own QR)

1. **Placed** with "Pay by QR": the thread opens "Order {number} placed · ₹X · QR payment" (`server/src/modules/order/order.service.js:308-324`).
2. **The stall accepts** → AWAITING_PAYMENT. The deadline is now plus `PAYMENT_WINDOW_MS` (default 5 minutes), so the window starts at acceptance; paymentStatus stays PENDING (`server/src/modules/order/order.lifecycle.js:112-115, 159-169`; `server/system/configs/config.js:209`).
   - If the stall has no QR at that moment, the order quietly becomes cash: "{stall} has no payment QR on file, so this order is cash on delivery. Carry ₹X." (`server/src/modules/order/order.lifecycle.js:153-168, 179-181`).
3. **The customer sees** the headline "Pay to continue" and, before any payment, "Order confirmed by {stall}"; push "Order confirmed" / "Pay ₹X to {stall} to continue." (`server/src/modules/order/order.lifecycle.js:172-177`; `client/src/pages/Tracking.jsx:20`).
   - The QR card shows "Pay ₹X to {stall}", an m:ss countdown, the stall's QR image, "Scan with any UPI app", "Pay the seller directly, then tell them it is done.", and the buttons "Attach screenshot" and "I’ve paid" (`client/src/components/OrderChat.jsx:88-109, 130-140`).
   - A stall card reads "The stall is checking that your payment arrived.", and the bar shows "Cancel order" (`client/src/components/OrderChat.jsx:174-175`).
4. **The customer pays.** "I’ve paid" sends `POST /api/orders/:id/payment/initiated` {}. "Attach screenshot" shows a preview (thumbnail, name, size, "Replace", "Remove") and "Send to seller", which posts the multipart field `proof` to the same endpoint (`client/src/components/OrderChat.jsx:111-139, 515-541`).
   - Either way: 200 "Payment sent for confirmation", status PAYMENT_REVIEW, paymentStatus AWAITING_CONFIRMATION (`server/src/modules/order/order.lifecycle.js:351-362`).
   - The card collapses to "Payment sent — waiting on the seller to confirm."; the screenshot shows as the customer's own bubble "Paid ₹X", followed by "{name} marked the payment as sent"; the acceptance-time card resolves to "Payment sent for confirmation" (`client/src/components/OrderChat.jsx:104-105, 146-154, 611-616`; `server/src/modules/order/order.lifecycle.js:368-381`).
   - The headline becomes "Seller is checking your payment"; the customer can no longer cancel, and the bar shows "Call {stall}" (`client/src/pages/Tracking.jsx:16, 22, 204-207`).
   - Proof rules: one JPG, PNG, WebP or GIF of up to 12 MB ("Upload a JPG, PNG, WebP or GIF image"), stored privately as WebP; at most 5 per order ("This order already has 5 screenshots — wait for the seller to check them.") (`server/src/middleware/upload.js:18-19, 38-59`; `server/src/modules/order/order.lifecycle.js:289-316`).
5. **The stall confirms** ("Payment received": `POST /api/orders/:id/payment/confirm` {received:true}) → ACCEPTED and PAID, and the prep clock starts. It works from AWAITING_PAYMENT, PAYMENT_OVERDUE or PAYMENT_REVIEW (`server/src/modules/order/order.lifecycle.js:36-37, 396-425`).
   - Thread "Payment confirmed · ₹X"; card "The stall confirmed your payment."; push "Payment confirmed" / "{stall} confirmed ₹X."; headline "Order confirmed", with the prep timer (`client/src/components/OrderChat.jsx:174-177`).
   - "Not received" ({received:false}) is allowed only from PAYMENT_REVIEW. It returns the order to AWAITING_PAYMENT with a fresh 5 minutes and a new card "Try again — pay ₹X to {stall}" (push "Payment not received"), and the customer reads "The stall could not find your payment. If you paid, use Report below." (`server/src/modules/order/order.lifecycle.js:402-407, 428-447`; `client/src/components/OrderChat.jsx:177`).
6. **Cooking and handover** follow steps 3-6 of 2.6, with nothing due at the door. The panel reads "Tell this code to the stall owner or the delivery partner when you get your order — that completes it."; the dispatch line ends "… At the door, the stall enters the customer's code to complete the order."; completion reads "Delivered · handover code verified" (`client/src/components/HandoverPanel.jsx:166`; `server/src/modules/order/order.lifecycle.js:236-245`; `server/src/modules/order/order.handover.js:55-60`).

**Missed window** (needs the worker)
- Once the window lapses, the worker's 30-second sweep moves AWAITING_PAYMENT to PAYMENT_OVERDUE (not a cancellation) with a 15-minute grace. Thread "Payment window closed — already paid? Send your screenshot so the seller can confirm."; push "Payment window closed" / "Already paid? Send a screenshot so the seller can confirm."; headline "Payment window closed" (`server/src/modules/order/order.lifecycle.js:709-737`).
- The QR card shows a "Window closed" chip with "If you have already paid, send your screenshot. The seller can still confirm it.", and "Attach screenshot" becomes the main button. The stall's card reads "The payment window has closed. The stall may still accept a late payment, or cancel the order."; "Cancel order" stays available (`client/src/components/OrderChat.jsx:79-80, 92-93, 106-107, 133-138, 184-188`).
- With no proof after the grace, status and paymentStatus become EXPIRED: thread "Order expired — no payment was received"; push "Order expired" / "No payment arrived, so the order was cancelled." (`server/src/modules/order/order.lifecycle.js:744-779`). The headline reads "Expired — no payment received", and the progress view ends "Payment window ran out" / "{time} · Nothing was charged". Any screenshot stops the sweep (`client/src/pages/Tracking.jsx:30, 38, 52-65`).
- The stall can cancel an unpaid order (EXPIRE, from AWAITING_PAYMENT or PAYMENT_OVERDUE): "Cancelled by the seller — payment not received", push "The seller cancelled it because no payment arrived." (`server/src/modules/order/order.lifecycle.js:543-557`).

**Gotchas**
- Before the customer has paid, the thread already says "Order confirmed by {stall}" and "The stall is checking that your payment arrived." (`server/src/modules/order/order.lifecycle.js:172-176`).
- "I’ve paid" without a screenshot removes the card's buttons, and the UI then offers no way to add one (`client/src/components/OrderChat.jsx:111, 691-699`). A resolved QR card always reads "Payment sent — waiting on the seller to confirm.", even after confirmation, expiry or cancellation (`client/src/components/OrderChat.jsx:103-108`).
- "Window closed" appears when the browser countdown hits 0:00; the headline changes only at the next sweep (up to about 30 s later), and never if the worker is down (`client/src/components/OrderChat.jsx:79-80`; `server/src/jobs/paymentExpiry.js:15, 31`). The "five minutes" on Confirm is hard-coded, though `PAYMENT_WINDOW_MS` is configurable (`client/src/pages/Confirm.jsx:146`).

### 2.8 Tracking views

**Order thread** (the default view of `/track/:id`)
- The header shows the status headline and "{stall} · {orderNumber} · ₹X" (`client/src/pages/Tracking.jsx:18-31, 144-145`). System lines are centred pills with the time, e.g. "Preparing your order · Today, 7:45 pm" (`client/src/components/OrderChat.jsx:52-58`; `client/src/lib/format.js:21-34`).
- Stall action cards are reworded for the customer and show no buttons (`client/src/components/OrderChat.jsx:179-183, 214-229`). The composer reads "Message the stall…"; when the socket drops: "Reconnecting… messages will catch up when you are back." (`client/src/components/OrderChat.jsx:628-633, 693`).
- Bottom bar: "Cancel order" when allowed, "Report" and "Order again" once the order has ended, otherwise "Call {stall}". The phone tab bar stays visible (`client/src/pages/Tracking.jsx:135, 188-208`; `client/src/layouts/ConsumerLayout.jsx:17-21, 32`).
- The "Now · …" status-steps strip in the chat is shown only to the stall (`client/src/components/OrderChat.jsx:268-277, 354-356`).
- Live updates: the socket joins user:{id}, and the page re-fetches the order on order:updated, on reconnect, and when the tab is visible again after 5 s (`server/src/realtime/socket.js:126`; `client/src/components/OrderChat.jsx:427-495`).
- APIs: `GET /api/orders/:id`, `GET /api/orders/:id/messages`, `POST /api/orders/:id/messages` {message, up to 2000 characters}, `GET /api/orders/:id/handover` (the code only for the buyer) (`server/src/modules/order/order.route.js:52, 82`; `server/src/index.js:119`).

**Progress view**
- It opens from the clipboard icon (aria "Show order progress") and closes with X; the prep timer hides while it is open (`client/src/pages/Tracking.jsx:147-151, 176`).
- Steps: "Placed — Sent to the seller", (QR only) "Payment — Pay the seller to continue", "Confirmed — Seller confirmed your order", "Preparing — Being cooked now", "Ready — Packed and waiting", "Out for delivery — Seller is on the way", "Delivered — Handed over at your location" (`client/src/data/campus.js:49-60`).
- Reached steps carry their time, e.g. "7:42 pm · Seller confirmed your order" (`client/src/lib/adapt.js:134-142`; `client/src/ui/kit.jsx:140`). The view ends with the "You pay {stall} directly…" note, left out for ended orders; a failed order ends with a red cross, e.g. "Cancelled — {time} · Nothing was charged" (`client/src/pages/Tracking.jsx:52-65, 79, 158-174`).
- "Order tracking is a timeline, never a map." (code comment); tracking imports no map (`client/src/ui/kit.jsx:120`; `client/src/pages/Tracking.jsx:1-14`).

**Live-order card on Home**
- While an order is active, Home's card headline reads "Waiting for the stall to accept", "Pay the stall to confirm", "Payment window closed" or "Stall is checking your payment", then "Confirmed", "Preparing", "Ready" or "Out for delivery", over a segmented bar with "{stall} · N items · ₹X" (`client/src/components/LiveOrderTracker.jsx:14-34, 129-135`).
- Tapping it opens `/track/:id`; it disappears once the order completes (`client/src/layouts/ConsumerLayout.jsx:176`).

**Orders** (`/orders`)
- "Your orders". Cards show "{stall}", "Order #{number}", "{date} · {location}" and a tag: "Live", "Delivered", "Cancelled", "Rejected" or "Expired". Buttons: "Track" while live; otherwise "Open", "Report", "Reorder" and, when eligible, "Rate" (`client/src/pages/OrderHistory.jsx:22, 60-135, 152`).
- The money line reads "to pay the seller in cash" or "to pay the seller by UPI" while live, then "payment sent · seller confirming", "paid to seller", or "not charged" (`client/src/pages/OrderHistory.jsx:29-58`).
- Push titles name the event ("Order confirmed", "Order update", "Your order is on the way", "Cash payment confirmed", "Delivered"); "SETU Services" is only the fallback title (`client/public/sw.js:52-62`; `server/src/modules/order/order.lifecycle.js:177-182, 273`).

### 2.9 Review and report

**Review**
- The sheet opens by itself for a COMPLETED order not yet reviewed or skipped, within 7 days, on any customer screen except `/cart`, `/confirm` and `/report`. On `/track/:id` it appears the moment the code is verified (`client/src/components/ReviewPrompt.jsx:8-32`; `client/src/lib/useOrders.js:35-47`).
- Copy: "How was {stall}?", "1 × {item} · …", "Tap a star to rate" (then "Poor", "Okay", "Good", "Very good", "Excellent"), "Anything to add? (optional)" (placeholder "Hot, on time, generous portion…", hint "Shown on the stall's page with your first name. N characters left.", 500 max), and "Don't ask again" / "Submit review" ("Sending…") (`client/src/components/ReviewSheet.jsx:7, 25, 52-91`).
- Success toasts "Thanks — your review is on the stall’s page." (`client/src/components/ReviewPrompt.jsx:58`).
- `POST /api/orders/:id/review` {rating 1-5, comment up to 500} → 201 "Thanks for the review"; `POST /api/orders/:id/review/skip` → {skipped:true} (`server/src/modules/review/review.route.js:13-36`).
- Only the buyer can review, only a COMPLETED order ("You can review an order once it has been delivered"), within 30 days and once per order. The stall's rating becomes the average to one decimal (`server/src/modules/review/review.service.js:11, 23-63`).
- ✕ or the backdrop defers the sheet only for this tab session; "Don't ask again" records reviewSkippedAt. Orders keeps "Rate" for 30 days and shows "You rated this order N/5" once rated (`client/src/components/ReviewPrompt.jsx:13-17, 34-50`; `client/src/pages/OrderHistory.jsx:14-20, 66-70, 113-118`).

**Report** (`/report/:orderId`)
- It opens from "Report" on an ended order or an order card; Profile › "Report an issue" opens `/report`. Header "Report an issue" / "About {stall} · order CEmmdd-XXXX. A campus admin reads every report.", then "Which order?" (research screen lists).
- "What went wrong?" offers "Food quality or hygiene", "Order never arrived", "Wrong or missing items", "Overcharged at handover", "Behaviour of the seller" and "Something else" (`client/src/data/campus.js:74-81`). Then "Tell us what happened", "Attach a photo — Optional · helps the reviewer" and "Send report" (research screen list); report photos are stored privately (`server/src/services/StorageService.js:95-101`).
- Disclosure: "Reports go to SETU campus staff as a record against this seller. This is not a refund claim against SETU — money matters are settled with the seller." (only "This is not a refund claim against SETU" is bold) (`client/src/ui/kit.jsx:106-109`; `client/src/pages/ReportIssue.jsx:177`). Confirmation: "Report sent to SETU campus staff…" (`client/src/pages/ReportIssue.jsx:77-78, 93, 153`).

### 2.10 Order status vs payment status

Order status has 12 values, and payment is a separate field (`server/src/modules/order/order.model.js:4-6, 17-45`).

| Order status | Tracking headline | Home card | Reached by | paymentStatus | Customer can cancel |
|---|---|---|---|---|---|
| PLACED | "Waiting for the seller" | "Waiting for the stall to accept" | `POST /api/orders` | PENDING | Yes |
| AWAITING_PAYMENT (QR) | "Pay to continue" | "Pay the stall to confirm" | ACCEPT on a QR order, or "Not received" | PENDING | Yes |
| PAYMENT_REVIEW (QR) | "Seller is checking your payment" | "Stall is checking your payment" | "I’ve paid" or a screenshot | AWAITING_CONFIRMATION | No |
| PAYMENT_OVERDUE (QR) | "Payment window closed" | "Payment window closed" | Worker sweep after the window | PENDING | Yes |
| ACCEPTED ("Confirmed") | "Order confirmed" | "Confirmed" | ACCEPT (cash) or "Payment received" (QR) | Cash PENDING, QR PAID | Only once flagged late |
| PREPARING | "Being cooked now" | "Preparing" | START_PREPARING | Cash PENDING, QR PAID | Only once flagged late |
| READY | "Ready" | "Ready" | MARK_READY | Cash PENDING, QR PAID | No |
| OUT_FOR_DELIVERY | "On the way" | "Out for delivery" | DISPATCH (issues the code) | Cash PENDING (cash confirm only records cashReceivedAt), QR PAID | No |
| COMPLETED ("Delivered") | "Delivered" | Card disappears | Stall enters the right code | PAID | No |
| REJECTED | "Rejected by the seller" | none | REJECT with a reason | Not recorded in the research | Ended |
| CANCELLED | "Cancelled" | none | Customer cancel | Not recorded in the research | Ended |
| EXPIRED | "Expired — no payment received" | none | Sweep with no proof, or stall EXPIRE | EXPIRED | Ended |

- Headlines: `client/src/pages/Tracking.jsx:18-31`. Home card: `client/src/components/LiveOrderTracker.jsx:14-34`. Payment states: `server/src/modules/order/order.lifecycle.js:356, 416, 436, 550, 763`; `server/src/modules/order/order.handover.js:257`. Cancel rules: `server/src/modules/order/order.lifecycle.js:33-34, 503-514`.
- paymentStatus values: PENDING, AWAITING_CONFIRMATION, PAID, DISPUTED, EXPIRED, REFUNDED. Only the legacy cash card or campus staff set DISPUTED, and nothing sets REFUNDED (`server/src/modules/order/order.model.js:32-45`; `server/src/modules/order/order.lifecycle.js:472, 679`).
- paymentMethod is COD or QR; the legacy values CASH_ON_DELIVERY, UPI_DIRECT and UPI are normalised (`server/src/modules/order/order.service.js:27-31`). In Orders, a failed unpaid order reads "not charged" (`client/src/pages/OrderHistory.jsx:29-58`).

## 3. What the video may and may not say

### 3.1 Product truths the video may state
1. SETU Services is a directory and approval gate for campus food stalls; the stall cooks, delivers and takes payment (`client/src/data/policies.js:15-17, 47-49`; `client/src/pages/SignIn.jsx:431-432`).
2. You pay the stall directly, in cash at the door or by scanning the stall's own QR. SETU does not process the payment and is not the merchant of record (`client/src/pages/Confirm.jsx:112-117`; `client/src/ui/kit.jsx:102-105`; `client/src/data/policies.js:30`).
3. No commission: you pay the food price plus any delivery charge the stall sets (`server/src/modules/order/order.service.js:195-203`; `client/src/data/policies.js:68-71`).
4. Delivery is to campus locations only. The server checks the exact map point against the campus boundary when you save an address and again when you order (`client/src/data/policies.js:23`; `server/src/modules/user/user.service.js:550-555`; `server/src/modules/order/order.service.js:262-267`).
5. The stall brings the order; you follow a status timeline in the order thread, not a map (`client/src/pages/Onboarding.jsx:24-25`; `client/src/ui/kit.jsx:120`).
6. One order goes to one stall (`client/src/state/CartContext.jsx:131-137`; `server/src/modules/cart/cart.service.js:96-108`).
7. With Pay by QR, the stall's QR appears after the stall accepts. You get five minutes, can attach a screenshot, and the stall confirms your payment before cooking (`client/src/pages/Confirm.jsx:146-147`; `server/src/modules/order/order.lifecycle.js:159-177, 412-425`).
8. At the door, you pay cash and the stall confirms it; you then tell the stall your six-digit handover code, which completes the order. Only you see the code, and "SETU staff will never ask for it." (`client/src/components/HandoverPanel.jsx:137-172`; `server/src/modules/order/order.handover-code.js:133-146`).
9. You can cancel until the stall accepts, while a QR order still waits for payment (not after "I’ve paid"), or once the kitchen runs late (`server/src/modules/order/order.lifecycle.js:33-34, 503-514`).
10. Preparation is watched: past the prep limit (25 minutes by default) the order is flagged late and you may cancel (`server/src/modules/order/order.timers.js:33-44, 92-102`).
11. Ratings come only from customers' reviews of delivered orders; a new stall shows "New" (`server/src/modules/review/review.service.js:23-63`; `client/src/lib/adapt.js:47`).
12. Reports go to SETU campus staff as a record against the stall, not as a refund claim against SETU (`client/src/ui/kit.jsx:106-109`; `client/src/data/policies.js:70-71`).
13. To be approved through SETU, a stall needs its ID, trade licence, FSSAI certificate and UPI QR verified (`server/src/modules/admin/admin.service.js:301-313`; `server/src/config/documents.js:13-55`). Safe wording: "SETU checks each stall’s documents and licence before it is listed." (`client/src/data/policies.js:52-57`).
14. Open or closed is live, in campus time, and only stalls with a menu are listed (`server/src/utils/store-hours.js:11-17`; `server/src/modules/restaurant/restaurant.service.js:45-59`).
15. Food is live; "Commute" and "Utilities" are marked "Soon" (`client/src/data/campus.js:26-30`).
16. It is for IIT Kharagpur campus accounts (`client/src/pages/SignIn.jsx:254`; `client/src/data/policies.js:86`).

### 3.2 Statements the video must NOT make

| Do not say | Why | Evidence / say instead |
|---|---|---|
| "SETU delivers" | The stall delivers. Some app copy says "SETU delivers inside…", contradicting "SETU does not deliver" | Say "Delivery is to campus locations only" (`client/src/data/policies.js:23`; `client/src/pages/Onboarding.jsx:24, 160`) |
| A delivery-or-pickup choice | Checkout always sends DELIVERY, and no customer screen offers pickup | `client/src/pages/Confirm.jsx:77`; pickup exists only in policy text (`client/src/data/policies.js:63`) |
| Live rider tracking, GPS or a map | Tracking is a thread and a timeline; there is no location tracking | `client/src/ui/kit.jsx:120`; `client/src/pages/Tracking.jsx:1-14` |
| "Delivered in X minutes" | Only preparation is limited (25 minutes by default); nothing promises a delivery time | `README.md:551-557`; `server/system/configs/config.js:231` |
| "Free", "zero cost", "minimal delivery charge" | Stalls set prices and a ₹0-₹500 delivery charge, and may set a minimum | `server/src/modules/restaurant/restaurant.service.js:24, 252-257`; say "no commission" |
| "Every stall is licence-checked" (unqualified) | Legacy stalls with no status field are listed without the document gate (a code comment counted 11 of 15) | `server/src/modules/restaurant/restaurant.service.js:34-58`; say "SETU checks each stall’s documents and licence before it is listed" |
| "Your acknowledgement is recorded" | Nothing stores the onboarding toggle | `client/src/pages/Onboarding.jsx:75-104, 285-287` |
| "Pay first", "QR at checkout", "payment review before the stall accepts" | The QR appears only after acceptance; the order is confirmed only after the stall confirms payment | `server/src/modules/order/order.lifecycle.js:159-177, 412-422` |
| "Pay to the seller's UPI handle" | The app shows the stall's uploaded QR image | `client/src/pages/Onboarding.jsx:23`; `client/src/ui/kit.jsx:243-245` |
| "There is no checkout" | There is a "Confirm order" screen; say "no payment checkout" | `client/src/pages/Confirm.jsx:107`; `client/src/pages/Onboarding.jsx:23` |
| "SETU guarantees hygiene or quality" | The app makes the seller responsible for quality and hygiene | `client/src/ui/kit.jsx:98-101` |
| A "SETU Food" app logo or in-app name | The UI brand is "SETU Services"; only emails say "SETU Food"; no SETU Food lockup asset exists | `client/index.html:22`; `server/src/services/mail.templates.js:12` |
| "For faculty and staff" or "students only" | No UI string names an audience beyond campus accounts; in-app "campus staff" means SETU reviewers | `client/src/pages/SignIn.jsx:254`; `client/src/data/policies.js:86, 104-107` |
| "Only institute emails can sign up" | Password sign-up accepts any valid email | `server/src/modules/user/user.service.js:175-178` |
| "Your recent searches" | The list is hard-coded | `client/src/pages/Search.jsx:10` |
| "See the stall's FSSAI number" | Customers never see it (fssai is null) | `client/src/lib/adapt.js:57-58` |
| "Commute and Utilities are already built" | No server module exists; say "coming soon" | `client/src/pages/Home.jsx:118` |
| Exactly what stalls can see about you | Sign-up, onboarding and the terms disagree | `client/src/pages/SignIn.jsx:406-409`; `client/src/pages/Onboarding.jsx:140`; `client/src/data/policies.js:103` |
| "The minimum order is enforced" | Only the cart button blocks it; the server does not check | `server/src/modules/order/order.service.js:130-237` |
| That a real inbox received the demo code | On the demo stack codes go to a local Mailpit catcher; the brief requires a visible DEMO label and no claim of real delivery | `client/src/pages/SignIn.jsx:377`; `SETU_Food_Customer_Walkthrough_Master_Prompt.md:46-58` |

## 4. Observed inconsistencies and possible bugs (for the owner; nothing was fixed)

**Copy that contradicts the code or itself**
- The onboarding toggle says "Required. Recorded against your account with today’s date.", but finish() sends no acknowledgement and no field exists for it (`client/src/pages/Onboarding.jsx:75-104, 285-287`).
- "SETU does not deliver" sits beside "SETU delivers inside the campus area only" and "SETU delivers inside the IIT Kharagpur campus boundary" (`client/src/pages/Onboarding.jsx:24, 160`; `client/src/ui/LocationPicker.jsx:236`; `client/src/ui/MapLocationPicker.jsx:321`).
- The handover copy says "the stall owner or the delivery partner", while the README says "SETU does not deliver. The seller brings the order." (`client/src/components/HandoverPanel.jsx:141`; `README.md:435`).
- "Every stall is licence-checked by SETU" and "Every seller listed here cleared a licence check", yet legacy stalls are listed without the gate (`client/src/pages/Home.jsx:222`; `client/src/pages/Onboarding.jsx:27`; `server/src/modules/restaurant/restaurant.service.js:34-58`).
- "or by UPI to the seller’s own handle", while the real flow shows the stall's uploaded QR (`client/src/pages/Onboarding.jsx:23`; `client/src/ui/kit.jsx:243-245`).
- "There is no checkout, card form or wallet", next to a "Confirm order" page (`client/src/pages/Onboarding.jsx:23`; `client/src/pages/Confirm.jsx:107`).
- The Soon toast claims "The approval pipeline behind it is already built.", but server/src has no Commute or Utilities module (`client/src/pages/Home.jsx:118`).
- Sign-up labels "Institute email" and the eyebrow "IIT Kharagpur campus accounts only", yet any email is accepted (`client/src/pages/SignIn.jsx:254, 412`; `server/src/modules/user/user.service.js:175-178`).
- What stalls see differs between sign-up, onboarding and the terms (`client/src/pages/SignIn.jsx:406-409`; `client/src/pages/Onboarding.jsx:140`; `client/src/data/policies.js:103`).
- The fee sub-label is "Set by the seller, collected by the seller" in the cart but "Set and collected by the seller" on Confirm (`client/src/pages/Cart.jsx:132-134`; `client/src/pages/Confirm.jsx:179-181`).
- The room hint reads "Shown to the stakeholder at handover." in onboarding but "Shown to the seller at handover." in Profile; the picker's "Address details" is optional while onboarding's "Room or wing" is required (`client/src/pages/Onboarding.jsx:73, 222`; `client/src/pages/Profile.jsx:247`; `client/src/ui/LocationPicker.jsx:393-397`).
- The seller Store settings say the cover "runs across the top of your page", but the stall page shows only the logo (`client/src/pages/seller/StoreSettings.jsx:296-298`; `client/src/pages/SellerDetail.jsx:17-27`).
- The FSSAI document hint says "The number is shown on your stall page", but the client sets fssai to null (`server/src/config/documents.js:30-34`; `client/src/lib/adapt.js:57-58`).
- A QR order's thread says "Order confirmed by {stall}" and "The stall is checking that your payment arrived." before any payment (`server/src/modules/order/order.lifecycle.js:172-176`; `client/src/components/OrderChat.jsx:174-175`).
- After "Not received", the customer is told "If you paid, use Report below.", but "Report" appears only after the order ends (`client/src/components/OrderChat.jsx:177`; `client/src/pages/Tracking.jsx:188-208`).
- The policy and claude.md mention pickup ("or handover at the stall for pickup"), which customers cannot choose (`client/src/data/policies.js:63`; `claude.md:21`).

**Visible UI bugs**
- A saved address first captured by GPS shows the eyebrow "Current location", not "Saved location" (`client/src/ui/LocationPicker.jsx:357-358`; `client/src/lib/adapt.js:220`).
- A resolved QR card keeps "Payment sent — waiting on the seller to confirm." after confirmation, expiry or cancellation (`client/src/components/OrderChat.jsx:103-108`).
- The progress view draws "Delivered" as the current step with a clock icon, never a tick (`client/src/pages/Tracking.jsx:50`; `client/src/ui/kit.jsx:124-136`).
- Search rows show prep as "20–20 min" (`client/src/ui/ProviderCard.jsx:34`; `client/src/lib/adapt.js:40`).
- A stall held open late reads "Open until at 11:30 pm", and time labels mix "PM" with "pm" (`server/src/utils/store-hours.js:78-85, 185-196`; `client/src/lib/format.js:4-5`).
- A point 995-999 m outside reads "About 1000 m outside it." (`client/src/lib/geo.js:18-22`).
- The seed customer's address would read "Room Room B-204" (`server/src/seed/seed.js:330-331`; `client/src/ui/DeliverTo.jsx:32`).
- Toasts render under the picker overlay (z-index 120 vs 1300), so on phones only the in-sheet notice is readable (`client/src/styles.css:1180, 1518`).
- GPS timeouts are silent, and "Finding your location took too long." never appears (`client/src/state/useLocationRequest.js:66-71`; `client/src/ui/LocationPicker.jsx:425-435`).
- The locating line "Allow location access when your browser asks." can never show (`client/src/ui/LocationPicker.jsx:345-346`).
- Pasting a code into a box keeps only its first digit (`client/src/pages/SignIn.jsx:381`). The code link reads "Sending a code…" during a password sign-in (`client/src/pages/SignIn.jsx:171, 330`).
- Dismissing the install banner does not persist, and "Install" without a prompt calls `window.alert()` (`client/src/components/PWAInstallBanner.jsx:33, 45, 82-88`).
- A 401 wipes the token but leaves the user signed in on screen (`client/src/lib/api.js:67`). "Loading cuisines…" never clears if the request fails (`client/src/lib/useProviders.js:46-51`).
- The sign-up inputs and "Room or wing" have no accessible name (`client/src/ui/kit.jsx:32-43`). `var(--r-lg)` is used but never defined (`client/src/styles.css:1693`).
- The bundled 75-years mark reads "DEDICATED TO THE THE SERVICE OF THE NATION" and is only 320 px (`client/src/assets/images/kgp-75-logo.webp`).

**Behaviour gaps**
- After "I’ve paid" without a screenshot there is no way to add one, though the server accepts more in PAYMENT_REVIEW (`client/src/components/OrderChat.jsx:111`; `server/src/modules/order/order.lifecycle.js:331-349`).
- "Cancel order" is one tap with no confirmation (`client/src/pages/Tracking.jsx:189-192`).
- Only the cart button enforces the minimum order; Confirm and the server ignore it (`client/src/pages/Confirm.jsx:194`; `server/src/modules/order/order.service.js:130-237`).
- A dish that sells out after being added stays in the cart unflagged (`server/src/modules/cart/cart.service.js:51`; `client/src/pages/Cart.jsx:98-108`).
- Auto-detect opens "You seem to be somewhere new" even off campus, where the only action is a disabled "Outside delivery area" (`server/src/services/LocationService.js:220-223`).
- Onboarding's GPS shortcut accepts an off-campus fix and fails only at "Start ordering" (`client/src/pages/Onboarding.jsx:48-59, 73, 84-100`).
- An address edit is answered "Address added", and city, state, postcode and country pass validation but are not stored (`server/src/modules/user/user.controller.js:87-90`; `server/src/modules/user/user.service.js:557-568`).
- Search fuzziness: "Chinese" also lists "Indo-Chinese" (substring match), typo tolerance needs 5+ letters, and the notice can name a stall, e.g. "Tikka Junktion" → "Tikka Junction" (`server/src/modules/restaurant/restaurant.service.js:97-99`; `server/src/utils/dish-search.js:60-62, 223-241`).
- "Recent searches" is a fixed list, not history (`client/src/pages/Search.jsx:10`).
- The late text uses the browser clock, but "Cancel order" waits for the worker's lateAt stamp: up to about 30 s later, and never without the worker (`client/src/components/PrepTimer.jsx:44`; `client/src/pages/Tracking.jsx:135`).
- Stored "always open" hours (equal or blank) make later seller settings saves fail with "Opening and closing time cannot be the same" (`server/src/modules/restaurant/restaurant.service.js:266-272`).
- The cart reads the stall with lean(), so a raw-inserted stall without hours is always open in the cart but 10:00-22:00 elsewhere (`server/src/modules/cart/cart.service.js:30, 59`).

**Docs drift**
- The README says "One-time codes have no delivery channel in production" but also that codes are emailed and last 10 minutes; claude.md says they are emailed through SMTP (`README.md:239, 599-600`; `claude.md:124-126`).
- The README calls the sign-in tabs "Student" and "Seller" (`README.md:314`).
- The README says the "You pay … directly" note is on tracking; it sits only in the collapsed progress view (`README.md:439-440`; `client/src/pages/Tracking.jsx:79, 158-171`).
- claude.md still says large surfaces are black, but styles.css moved to indigo bands (web 2026-10-09, phone 2026-10-10) (`claude.md:48-49`; `client/src/styles.css:2648-2652`).
- claude.md says cart, confirm and tracking show the "approval gate" wording; they show the "order" disclosure (`claude.md:25-26`).
- The claude.md and README route tables omit `POST /api/location/detect` (`claude.md:331`; `README.md:418, 559-568`). claude.md's asset tree omits kgp-75-logo.webp (`claude.md:421-425`).
- Code comments disagree with the code: one describes a web cart side column, another calls the menu bar sticky (`client/src/ui/CartBar.jsx:10-11`; `client/src/pages/SellerDetail.jsx:132`).
- Geolocation comments disagree about iOS permission support (`client/src/lib/geolocation.js:59-61, 165-168`; `client/src/state/useAutoLocation.js:32-34`).

## 5. How the video's captures were produced

- **An isolated demo stack, never live QA.** The QA API on :5000, the QA preview on :4173 and the QA tunnel were not used. Any page host other than 127.0.0.1 or localhost would turn the API base into `<host>:5000`, the QA API (`client/src/lib/api.js:1-19`).
- **Scratch copies** of `server/` and `client/` in the session scratchpad. The API ran as `node -r ../timeshift.cjs src/index.js` in `scratchpad/stack/server`. The client was built into `scratchpad/stack/client-dist` and served by `vite preview --outDir ../client-dist --host 127.0.0.1 --strictPort`; that bundle calls `http://127.0.0.1:5990`, not the QA tunnel (process command lines, `scratchpad/stack/api.log:1-10` and a grep of the scratch bundle, per the isolated-stack research; `scratchpad` is this session's scratchpad folder).
- **Throwaway containers** (docker `--context default`): `setu-video-mongo` (mongo:8, 127.0.0.1:27991, db `setu_video_demo`), `setu-video-redis` (127.0.0.1:6391, key prefix `setu:video:`), `setu-video-mailpit` (SMTP 127.0.0.1:1031, web UI 127.0.0.1:8031) and `setu-video-s3` (moto S3, 127.0.0.1:5991) (`docker ps` and `ss -ltnp` on 2026-10-13, per the isolated-stack research).
- **Ports**: API :5990 (it binds every interface, `server/src/index.js:221`) and client 127.0.0.1:4990.
- **Data**: the repo's own seed, `server/src/seed/seed.js`: 13 fictional approved stalls with 10:00-22:00 hours, no photos, ₹0 delivery, no minimum, 20-minute prep, no QR, and every rating "New" as seeded (`server/src/seed/seed.js:16-37, 303-350`). The seed wipes all non-admin users, restaurants and menu items in its target database and refuses a non-local `MONGO_URI` without `--force` (`server/src/seed/seed.js:276-301`). On top of it: a labelled demo payment QR and the demo persona "Aarav Mehta".
- **Clock**: a scratch-only shift makes the demo read 7:00 pm campus time. timeshift.cjs, preloaded with `node -r`, adds `DEMO_TIME_OFFSET_MS` to the server's Date; the offset is read once at API start. Browser-side times (greeting, QR countdown, prep timer, thread times) use the browser's clock and timezone, so the capture browser needs the same shift and Asia/Kolkata. With 10:00-22:00 hours, stalls read "Closing in N min" from 21:30 demo time (`scratchpad/stack/timeshift.cjs:1-15`; `client/src/components/OrderChat.jsx:28-37, 79`; `client/src/components/PrepTimer.jsx:19-44`; `client/src/pages/Home.jsx:19-24`; `server/src/utils/store-hours.js:217-230`).
- **Email codes** work here because plain SMTP goes to a loopback catcher (Mailpit) and Redis is local (`server/src/services/MailService.js:17, 125-130`); codes land in Mailpit, never a real inbox. The order flow needs no worker process; overdue, expiry, late and stuck-handover states do (`server/src/worker.js:22-28`).
- The bundle embeds the browser Maps key from `client/.env`; confirm it is accepted on 127.0.0.1:4990, or the picker shows "Map unavailable" (`client/src/lib/googleMaps.js:51-55`).

**Environment variable names the API reads** (values deliberately omitted)
- Core: `NODE_ENV`, `PORT`, `CLIENT_ORIGIN`, `MONGO_URI`, `JWT_SECRET`, `JWT_EXPIRES_IN`, `SESSION_TTL_DAYS`, `API_KEY_TTL_DAYS`, `OTP_PEPPER`, `RATE_LIMIT_DISABLED`, `TRUST_PROXY`, `TIMEZONE` (`server/system/configs/config.js:5-23, 82-157`).
- Redis: `REDIS_URL` or `REDIS_HOST`/`REDIS_PORT`/`REDIS_PASSWORD`, plus `REDIS_REQUIRED`, `REDIS_KEY_PREFIX`, `REDIS_CONNECT_TIMEOUT_MS`, `REDIS_COMMAND_TIMEOUT_MS` (`server/system/configs/config.js:57-62, 124-151`; `server/system/configs/redis-target.js:21-28`).
- Mail and push: `SMTP_HOST`, `SMTP_PORT`, `SMTP_FROM` (all three needed); `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY`, `VAPID_SUBJECT`. Location: `GOOGLE_MAPS_API_KEY`, `GOOGLE_GEOCODE_URL`, `GEOCODE_PER_MINUTE`, `CAMPUS_NAME`, `CAMPUS_ZONE_ENABLED` (`server/system/configs/config.js:163-174`). Institute sign-in: `SETU_AUTH_URL`, `SETU_AUTH_KEY`, `SETU_UTILITY_API_KEY`, `SETU_AUTH_TIMEOUT_MS`.
- Storage: `MINIO_ENDPOINT`, `MINIO_PORT`, `MINIO_USE_SSL`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, `MINIO_BUCKET_NAME`, `MINIO_PRIVATE_BUCKET`, `MINIO_PUBLIC_URL`, `MINIO_MANAGE_POLICY`, `DOCUMENT_MAX_BYTES` (`server/system/configs/config.js:242-254`; `server/src/services/StorageService.js:294`).
- Orders and jobs: `ESCALATION_INTERVAL_MS`, `ESCALATION_AFTER_MS`, `ESCALATION_MAX_ATTEMPTS`, `PAYMENT_WINDOW_MS`, `PAYMENT_GRACE_MS`, `PAYMENT_SWEEP_MS`, `HANDOVER_MAX_ATTEMPTS`, `HANDOVER_MAX_CODES`, `HANDOVER_STUCK_MINUTES`, `PREP_LIMIT_MINUTES`, `PREP_WARN_BEFORE_MINUTES`, `ORDER_TIMERS_SWEEP_MS`, `STORE_SWEEP_MS` (`server/system/configs/config.js:201-237`). Seed only: `SEED_OWNER_PASSWORD`. Scratch only: `DEMO_TIME_OFFSET_MS`.
- Client build, set in the shell (it overrides `client/.env`; setting only `VITE_API_BASE` keeps QA's value): `VITE_PUBLIC_API_BASE`, `VITE_API_BASE`, `VITE_GOOGLE_MAPS_API_KEY` (`client/src/lib/api.js:1-19`; `client/src/lib/googleMaps.js:14`).
- Always set at least `PORT`, `MONGO_URI` and `MINIO_ENDPOINT`/`MINIO_PORT`: the defaults reach another project's Mongo on :27017 and QA's MinIO on :9000 (`server/system/configs/config.js:82-86, 242-246`).

**Rules for re-running it**
- Do not use `start.sh` (it runs `fuser -k 5000/tcp 5173/tcp` and would kill the QA API) or the repo's docker-compose (fixed names, ports 9000/9001/6379) (`start.sh:10, 18`; `docker-compose.yml:4-8, 29-32`). Never build into `client/dist`, which testers preview on :4173 (`claude.md:44-45`).
- Leave `server/.env` and `server/.private-uploads` out of the copy (`server/src/services/StorageService.js:95-101`). Stop servers by port PID, remove test containers with `-v`, and never prune docker volumes (project notes: `memory/setu-food-pwa-overview.md:20`; `memory/setu-client-visual-testing.md:16`).
