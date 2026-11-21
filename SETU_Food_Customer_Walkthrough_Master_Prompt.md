Loading older messages…
Now your task is to create a big thing, like I'm saying from scratch. So, as if first planned it accordingly, suppose you are a proper user, customer, and etc., who already knows the UI, like how to log in, how to do things from A to Z, proper flow of the Setu food app. So basically your task is to create a proper overview of the current project from customer perspective, like if the customer is new, create a proper onboarding page from starting to end, and if it is an existing customer, just simply sign in with OTP and all. Like for now create a fake OTP screenshot that user is getting logged in, because like OTP thing is not being properly set up right now. So you can use fake loading and getting into the home screen for now. And after that the customer log into the home page, they select the location according to the codebase flow. You have to go through that also, and then selecting the location, or it will automatically fetch out the location, selecting the home address, selecting the food item to order from restaurants, and then paying, the pay structure, and the whole UI in a perspective, and then pay via cash or the restaurant QR directly, and mentioning that Setu does not provide any kind of payment handling food or hygiene thing, mentioning that in a way. You can mention that into the onboarding flow also. So basically the video will be for based criteria users. I will be giving that prompt to the cloud, and he will make the video properly. So your task is to define everything in a structured way, like the video format would be 1080p for now, 60fps, and the video shouldn't be more than long enough for 1.30, I mean 1 minute 30 seconds to 2 minutes. Within that range, if required you can extend that or decrease that video length. So basically it will be a proper user interface guided flow of the video. Use realistic after-effects motion animation rather than a static video edit. You can use the HyperFrames API or whatever the API suits for you. For context, you can do one thing.You can plan the task into seven different steps. As the first step, the Claude will be the editor, and the transcriptor, like after, at the second, it could be a transcriptor where Perakit, Nvidia can be used to transcribe everything, like auto subtitling and all. And the animator is Hyperframes at the third step, where it will give the motion and all. You have to do that step by step. Like if required any of those things, you can use the MCP. The fourth step, a Google Chrome researcher or any kind of web scraping, if screenshot and etc. required. That is not mandatory or required for now. But yeah, if there occurs something, like I don't think so that would occur, but if it is, then you can use that. Then comes the screen editor. You can use Tella, T-E-L-L-A, to the screen editor section. If any permission or login or anything is required, then you can ask me. For the sound designer, I will give you the sound after the video is completed. The sound selection will be manually done by me, accordingly to the motion and graphics, and the finisher, like you can show me the finisher and stuff. So basically, your task is to create the proper video with a good enough after effect, like of motion graphics, rather than a static video frame by frame edit. And after completion, like video should be good enough for the user side, that they would easily grasp everything. Like it would be better. And the main thing, most importantly, the script pitch. So you can do one thing. You can't directly name the competitors like Swiggy, Zomato. You can use other similar names of that company's name, like Higi, Tomato. They all usually charge you with the food item just because they want to earn commission and all. Like don't mention that. Like all other platforms, like Swiggy, Tomato charges for one to hundred rupees food, can go up to four hundred. For that, IIT Kharagpur Institute of Technology, Indian Institute of Technology Kharagpur, has built their own food delivering app where students and anywhere any customers, like mention professors and all, like whatever it is, so on, can order food delivery. Like this text should be from motion segment, so you can use the researcher part. Can order the food without any zero cost, and that should be with the minimal delivery charge. This is for the user side. Like make it attracting, eye-catching for all kind of generations, specifically target Gen Zs, along with, like, don't make purely Gen Z, because there will be certain professors or other users that are using this. So this is my appreciatable approach to you. You can analyze the whole thing and ask me question if required, then you can give me the prompt properly.
…
Worked for 47s
SETU Food — Complete Customer Journey & Product Walkthrough Video

The strongest approach is to make this a cinematic product walkthrough that teaches customers how to use SETU Food, rather than a conventional advertisement or a slideshow of screenshots.

The video should take someone who has never used the app, introduce the service, demonstrate the customer journey from sign-in to placing an order, explain how payment works, and finish with a clear understanding of what SETU does and what the customer should expect.

The experience should appeal to IIT Kharagpur students and other campus users, including professors, faculty members, and staff. The visual style should feel modern enough for Gen Z without looking immature or unprofessional.

I'll structure the master prompt around seven production stages, with Claude Code coordinating the workflow and the other tools used where appropriate.
1. The product story

The central message should be:

Your campus. Your food. A simpler way to order.

SETU Food is a campus food-ordering PWA for IIT Kharagpur. Customers can discover approved campus food providers, browse menus, place orders, and coordinate payment and fulfilment directly with the relevant stakeholder.

The video should communicate three things:

    Convenience: Discover campus food options and order through one interface.
    Transparency: Understand the order, applicable delivery charges, and payment arrangements before proceeding.
    Direct transactions: SETU facilitates the ordering experience but does not itself collect or process the customer's food payment.

One important distinction: we should promote SETU's no-platform-commission model without claiming that every order is completely free. If a delivery charge applies, the video must acknowledge it rather than promising zero total cost.

Similarly, we should explain that SETU lists and facilitates access to approved providers without implying that it independently guarantees food hygiene or handles delivery itself.
2. The actual customer journey to demonstrate

The project documentation identifies the main customer routes as /signin, /onboarding, /, /search, /seller/:id, /cart, /confirm, /track/:id, /orders, /report/:orderId, and /profile. It also documents campus geofencing, saved locations, cash and seller-QR payments, and live order conversations. The video should follow this product flow rather than inventing a different application.

Here's the proposed journey.
Stage	What the viewer sees	What the viewer learns
1. Introduction	SETU branding, campus imagery, food cards, animated headlines	What SETU Food is and who can use it
2. Sign in	Existing-customer sign-in and a separate new-customer path	How returning customers sign in and new customers get started
3. OTP demonstration	Enter email, show a simulated OTP notification, enter the demonstration code, transition into the app	How the intended OTP journey will look
4. First-time onboarding	A short sequence of the actual onboarding steps	How a new customer sets up their account
5. Location	Automatic location detection, address selection, map interaction, saved Home address	How to choose an eligible campus delivery location
6. Discover food	Home screen, approved restaurants, menu browsing, filters, item selection, cart	How to find food and build an order
7. Checkout and payment	Order summary, delivery or pickup, applicable charges, cash or seller QR, confirmation, order tracking	How to place an order and understand the direct-payment process

The existing customer should reach the home screen quickly. The new customer should receive a little more explanation during onboarding, but we must keep the overall video within the time limit.
Important: the OTP must be simulated honestly

Since the real email OTP delivery is not currently dependable, the video should simulate the OTP interaction without changing the application's authentication code or backend.

The simulation should include:

    A customer entering their email address.
    A demonstration notification showing a clearly labelled Demo OTP.
    The customer entering the demonstration code.
    A brief verification/loading animation.
    A transition to the home screen.

The demonstration must not imply that a real email was sent or that actual authentication was successfully verified. A small DEMO label can appear during the simulated OTP portion and disappear when the walkthrough moves into the normal product demonstration.

The real application must not be made less secure just to produce the video.
The location flow

The documented application supports automatic location detection, Google Places search, saved addresses such as Home and Office/College, and campus-boundary validation.

The video should show the following:

    The app requests location permission.
    If permission is granted, it attempts to detect the user's location.
    The user can confirm an existing saved address or search for a location manually.
    The user selects an eligible campus delivery point.
    The app confirms the address and makes it available for the order.

The video must not suggest that automatic detection is mandatory or always successful. It must also not show an arbitrary off-campus address being accepted as a valid delivery point.
Ordering and payment

The product documentation confirms that the customer flow supports restaurant discovery, menus, a server-side cart, delivery or pickup, checkout, live order tracking, and reviews. The cart is limited to one seller at a time.

The payment section must demonstrate the actual options.

Option A — Cash

    The customer selects cash.
    The order is placed.
    The seller accepts and prepares it.
    At handover, the customer pays the seller directly.
    The existing cash flow uses a six-digit handover verification code. The seller confirms receipt of cash before entering the code to complete the payment and handover process.

Option B — Seller's QR

    The customer selects the seller's QR payment option.
    The seller's payment QR is displayed.
    The customer pays the seller directly using their preferred UPI app.
    The customer uploads payment proof where required by the existing flow.
    The seller reviews and confirms the payment.
    The order proceeds according to its actual state.

The QR payment path includes an awaiting-payment/payment-review stage before seller acceptance. The video must not skip this detail if it shows the order progressing through that path.

The disclaimer should be clear but not alarming:

    SETU connects customers with approved campus food providers. Food preparation, delivery, and payment are handled directly by the respective provider. SETU does not collect payments or independently guarantee food hygiene. Please review the provider's information and report concerns through the available reporting process.

This explains SETU's role without suggesting that the platform itself cooks food, operates a delivery fleet, processes payments, or independently guarantees hygiene.
3. Seven-stage production plan

The production should be coordinated as one project, with seven distinct stages and clear deliverables at each stage.
Stage	Role	Main responsibility	Deliverable
1	Claude Code — director/editor	Inspect the codebase, map the user journey, write the script, storyboard and scene plan	Approved script, storyboard and asset checklist
2	Transcription and captions	Prepare the narration text, subtitle timing, and SRT/VTT files; use NVIDIA Parakeet or another available transcription tool when appropriate	Narration script and timed captions
3	HyperFrames — motion animator	Create animated UI transitions, typography, callouts, highlights and motion graphics	Animated scene sequence
4	Browser researcher	Inspect the actual app, capture genuine screens, verify text and interactions, gather missing references if necessary	Verified screenshots and interaction references
5	Tella — screen editor	Capture or assemble clean app interactions and screen recordings, subject to available access	Clean screen-recording assets
6	Sound design preparation	Leave the soundtrack ready for the sound you will provide later	Music-free master and sound cue/timing notes
7	Finishing and quality control	Assemble the complete video, check timing, readability, factual accuracy and export quality	Final MP4, project/source files, subtitles and production notes

Tool-selection rule: Claude should inspect which tools, integrations, APIs, and permissions are actually available before using them. It must not assume that a Tella account, HyperFrames API key, NVIDIA transcription endpoint, or browser automation integration is already connected.

If a required tool needs login, permission, or a credential, Claude should request it from you. If a tool is unavailable, it should report that fact and propose a compatible alternative rather than pretending the task was completed.
4. Master prompt for Claude Code

Copy the entire prompt below into Claude Code from the Setu-Food-PWA project directory.

This prompt makes Claude the production coordinator. It must inspect the actual application, create the script and storyboard, build the animated video, and verify the final export. It must not change the real application just to make the demonstration easier.
PROJECT: SETU FOOD — CINEMATIC CUSTOMER JOURNEY VIDEO
PRODUCTION TYPE: Animated product walkthrough + customer onboarding
PRODUCTION OWNER: Claude Code
PROJECT DIRECTORY: Existing Setu-Food-PWA repository

========================================================
01. PRIMARY OBJECTIVE
========================================================

Create a polished, cinematic, user-friendly product walkthrough
video explaining how a customer uses SETU Food from their first
visit through placing an order and completing the handover.

This is not a static slideshow.

The video must feature:
- Real application UI and realistic interactions.
- Smooth, professional motion graphics.
- After Effects-style typography and transitions.
- Animated UI highlights and camera movements.
- Carefully timed captions and text overlays.
- A clear, persuasive, accurate narration script.
- A complete customer journey from login to order completion.

The final video should help a first-time user understand the
product without needing a separate tutorial.

The target audience includes:
- IIT Kharagpur students.
- Professors and faculty members.
- Campus staff.
- Other eligible campus customers.

The visual language must appeal to younger users without
looking immature or excluding older users.

The product must remain the focus. Animation should explain
the interface, not distract from it.

========================================================
02. OUTPUT SPECIFICATIONS
========================================================

Primary deliverable:
- Format: MP4
- Resolution: 1920 × 1080
- Frame rate: 60 FPS
- Aspect ratio: 16:9
- Target duration: 1 minute 50 seconds
- Acceptable duration: 1 minute 45 seconds to 2 minutes
- Orientation: Landscape
- Text: Readable at normal desktop and mobile playback sizes
- Captions: Include a subtitle file
- Audio: Do not add final background music or sound effects.
  The project owner will provide the soundtrack later.

Prepare:
1. Final rendered MP4.
2. Editable video project/source files.
3. Scene-by-scene storyboard.
4. Final narration script.
5. SRT or VTT subtitles.
6. Asset manifest.
7. Render instructions.
8. Final quality-control report.

Use the existing repository's working directory conventions.
Keep all production assets in a clearly named video-production
directory.

Do not overwrite application files or production data.

========================================================
03. FIRST ACTION — INSPECT THE PROJECT
========================================================

Before writing the script, inspect the existing codebase.

Repository: Setu-Food-PWA

Frontend:
- React 18
- Vite
- Existing responsive PWA
- Existing design system and theme support

Inspect the actual customer-facing implementation.

Start with these routes where they exist:

/signin
/onboarding
/
/search
/seller/:id
/cart
/confirm
/track/:id
/orders
/report/:orderId
/profile

Locate the actual components, route configuration, screenshots,
assets, styles, authentication handlers and location components.

Inspect the following features:

A. Sign-in and customer onboarding.
B. Customer home screen.
C. Location permission and automatic detection.
D. Campus location selection and saved addresses.
E. Restaurant discovery and menu browsing.
F. Search and filters.
G. Item selection and cart.
H. Delivery versus pickup.
I. Checkout and order confirmation.
J. Cash and seller QR payment.
K. Payment proof upload and seller confirmation.
L. Order tracking and live conversation.
M. Delivery handover verification.
N. Relevant reporting and support functionality.

Use browser automation or existing Playwright tests to inspect
the UI where appropriate.

Do not assume the route list above represents every current
implementation detail. Verify the actual code before recording.

Create:

video-production/research/
video-production/storyboard/
video-production/assets/
video-production/captions/
video-production/renders/
video-production/reports/

If an equivalent production structure already exists, reuse it.

IMPORTANT:
Do not modify authentication, backend logic, database contents,
payment behavior or live QA data to produce this video.

========================================================
04. PRODUCT TRUTH — NON-NEGOTIABLE
========================================================

SETU Food is a campus food-ordering marketplace associated
with IIT Kharagpur.

The product connects customers with approved campus food
providers.

The following statements must remain accurate:

1. SETU does not collect or process customer payments.
2. SETU does not operate its own delivery fleet.
3. The relevant food provider handles food preparation.
4. Delivery or pickup is fulfilled according to the provider's
   actual service offering.
5. Customers pay the provider directly.
6. Payment options include cash and the provider's own UPI QR,
   according to the actual order flow.
7. SETU does not charge a platform commission.
8. A delivery charge may apply where applicable.
9. The actual charges displayed by the application must be used.
10. SETU lists approved providers but must not claim to
    independently guarantee food hygiene.
11. Order status and payment status are separate.
12. QR-payment orders may require payment review before
    the provider accepts the order.

Never invent prices, discounts, restaurants, menu items,
delivery times, ratings, or payment confirmations.

Use real application data where safe and available.

If test data is required, use clearly identified demonstration
data in an isolated environment.

Never expose personal information, credentials, API keys,
customer details, payment screenshots or private records.

========================================================
05. SCRIPT PITCH AND BRAND POSITIONING
========================================================

The main pitch:

"Your campus. Your food. A simpler way to order."

Alternative opening:

"From your hall to your favourite campus food spot,
ordering just got simpler."

The narrative should explain that SETU Food brings approved
campus food providers and customers into one convenient
ordering experience.

Emphasize:
- Convenience.
- Campus-focused food discovery.
- Transparent order totals.
- No platform commission.
- Direct payment to the food provider.
- Clear order progress.
- A straightforward customer experience.

Do not mention competing brands or use disguised competitor
names.

Do not claim that all other platforms charge a specific amount.

Do not claim that SETU food is completely free.

Do not describe the product as a free delivery service unless
the actual order confirms that delivery is free.

The preferred positioning is:

"Discover approved campus food providers, order in a few
simple steps, and pay the provider directly. No platform
commission, with any applicable delivery charges shown
before you place your order."

Keep the script conversational, confident and concise.

Avoid:
- Excessive marketing language.
- Overly dramatic claims.
- Technical jargon.
- Long paragraphs.
- Unverified claims about food safety.
- Unverified promises about delivery speed.
- Unsupported claims about universal eligibility.

========================================================
06. CUSTOMER JOURNEY — REQUIRED STORYBOARD
========================================================

Create a storyboard with a target duration of 110–120 seconds.

Every scene must have:
- Scene number.
- Start and end time.
- Narration.
- On-screen text.
- Actual UI state.
- Animation description.
- Transition description.
- Caption text.
- Asset references.
- Sound cue placeholders for later editing.

SCENE 01 — OPENING HOOK
Duration: 0–8 seconds

Visual:
Begin with a clean, dark campus-inspired background.

Reveal SETU Services / SETU Food branding using a restrained
cinematic logo animation.

Transition into attractive campus food imagery and an
animated phone/browser interface.

Main text:
"Your campus. Your food. A simpler way to order."

Narration:
"Meet SETU Food, a simpler way to discover and order food
from approved providers around your campus."

Animation:
- Smooth logo reveal.
- Subtle depth and parallax.
- Typography enters with controlled easing.
- Food imagery moves into the application interface.
- No excessive particles or distracting effects.

SCENE 02 — WHAT SETU FOOD DOES
Duration: 8–18 seconds

Visual:
Show the actual home screen and approved restaurant cards.

Highlight:
- Restaurant discovery.
- Food categories.
- Menu browsing.
- Campus delivery or pickup, where available.

Narration:
"Explore approved campus food providers, browse their menus,
and choose what you would like to order."

On-screen text:
"Discover. Choose. Order."

Do not invent unavailable features.

SCENE 03 — EXISTING CUSTOMER SIGN-IN
Duration: 18–30 seconds

Visual:
Show the real sign-in page.

Demonstrate an existing customer entering their email address
and selecting the email OTP sign-in option where available.

Because actual OTP delivery may not be dependable in the
demonstration environment, create a video-only OTP simulation.

Simulation:
1. Show a clearly labelled demonstration OTP notification.
2. Display a sample six-digit demonstration code.
3. Animate entry of the demonstration code.
4. Show a brief verification/loading state.
5. Transition into the home screen.

Display a subtle "DEMO" label during the simulation.

Narration:
"Already have an account? Sign in and continue to your
campus food experience."

IMPORTANT:
The displayed OTP is fictional demonstration content.

Do not claim a real email was delivered or a real OTP was
verified if that did not happen.

Do not hardcode a fake OTP into the actual application.
Do not disable authentication or change backend behavior.

Use an editing overlay, a dedicated mock screen or a
video-only animation for this sequence.

If the application currently supports password sign-in,
do not remove it or imply that OTP is the only supported method.

SCENE 04 — NEW CUSTOMER ONBOARDING
Duration: 30–42 seconds

Visual:
Show the new-customer account creation path.

Inspect the actual onboarding page and demonstrate its
real steps in a concise montage.

The project documentation identifies a four-step onboarding
flow. Verify the actual step labels and order in the codebase.

Show only the real fields and controls.

Explain how a new customer completes the required account
setup before ordering.

Narration:
"New to SETU Food? Complete the short onboarding process,
set up your account, and prepare to explore campus food."

Do not invent additional registration requirements.

If the OTP remains simulated, retain the demonstration label.

SCENE 05 — LOCATION AND CAMPUS ELIGIBILITY
Duration: 42–55 seconds

Visual:
Show the actual location-selection interface.

Sequence:
1. Location permission request.
2. Automatic location detection, when available.
3. Saved-address selection.
4. Manual location search as a fallback.
5. Confirmation of an eligible campus location.

Show a saved Home address if that option exists in the current
application.

Show the user confirming the intended delivery location.

Narration:
"Confirm where you would like your order delivered.
You can use your detected location, select a saved address,
or search for an eligible campus location."

Animation:
- Map pin drops into position.
- Address card slides into view.
- The selected address receives a clear visual highlight.
- Transition from the map to restaurant discovery.

Respect the actual campus geofence.

Do not show an arbitrary off-campus point being accepted.

Do not imply that GPS detection always succeeds.

Do not invent location options absent from the application.

SCENE 06 — DISCOVER FOOD AND SELECT ITEMS
Duration: 55–71 seconds

Visual:
Show the home screen, restaurant listings and search interface.

Demonstrate actual available controls such as:
- Search.
- Cuisine filters.
- Vegetarian filters.
- Open-now filtering.
- Available preparation-time filtering.

Use a real or isolated demonstration restaurant.

Open its page, browse the menu, open an item, and add it
to the cart.

Show the item quantity and price updating naturally.

Narration:
"Browse available stalls, explore the menu, and add your
favourites to the cart. Clear item details help you decide
what works for you."

Animation:
- Scroll with realistic inertia.
- Smooth transitions between restaurant and menu screens.
- Item card highlights.
- Cart count updates.
- Subtle camera push-in on the selected dish.

Do not add multiple sellers to one cart if the current
application supports only one seller per cart.

SCENE 07 — CART AND CHECKOUT
Duration: 71–83 seconds

Visual:
Open the actual cart.

Show:
- Selected food items.
- Quantity controls.
- Item totals.
- Delivery or pickup selection.
- Selected campus address.
- Applicable delivery charge.
- Final order total.

Narration:
"Review your items, confirm your location, and check the
complete order total before proceeding."

Highlight the final amount.

Do not invent discounts or fees.

Do not hide an applicable delivery charge.

Show the actual cart and confirmation flow rather than
creating an imaginary checkout page.

SCENE 08 — DIRECT PAYMENT OPTIONS
Duration: 83–101 seconds

Visual:
Show the real order-confirmation screen.

Explain the two payment options.

OPTION A — CASH

Show the customer selecting cash and placing the order.

Transition to the order progress screen.

At the handover stage, show the customer paying the provider
directly and the existing handover-verification interaction.

Do not reveal or reuse a real customer's verification code.

OPTION B — SELLER QR

Show the customer selecting the provider's QR option.

Show the provider's actual QR-payment interface using safe
demonstration data.

Explain that the customer pays the provider directly through
their own UPI app.

Show the payment-proof upload and seller confirmation stages
if supported by the actual flow.

Narration:
"Choose cash or pay directly to the provider using their
UPI QR, depending on the available options. SETU does not
collect or process the payment."

On-screen text:
"Payment goes directly to the provider."

IMPORTANT:
Do not simulate a successful financial transaction as if
money actually moved.

Clearly distinguish video-only UI animation from a genuine
payment confirmation.

Show the QR order's payment-review stage where appropriate.

SCENE 09 — LIVE ORDER TRACKING
Duration: 101–113 seconds

Visual:
Show the actual order-tracking screen.

Demonstrate the real status progression where supported:

PLACED
ACCEPTED
PREPARING
READY / OUT FOR DELIVERY
COMPLETED

Use the states appropriate to the selected order and payment
method. Do not imply that every state appears in every order.

Show the live conversation, timeline or status updates
where available.

Narration:
"Follow your order as the provider accepts it, prepares it,
and moves it towards collection or delivery."

Do not fabricate a live GPS delivery vehicle.

Do not show statuses that the application has not actually
reached unless the sequence is clearly a demonstration.

SCENE 10 — RESPONSIBILITY AND FINAL BRAND FRAME
Duration: 113–120 seconds

Visual:
Return to SETU branding.

Show a concise final summary and a clear call to action.

Primary text:
"Your campus. Your food. Your SETU."

CTA:
"Explore SETU Food."

Show this disclaimer legibly:

"SETU connects customers with approved campus food providers.
Food preparation, delivery and payment are handled by the
respective provider. SETU does not collect payments or
independently guarantee food hygiene."

Narration:
"Discover campus food through SETU Food. Simple ordering,
transparent charges, and direct payment to your provider."

Keep the disclaimer visible long enough to read.

Do not make the final screen overcrowded.

========================================================
07. STAGE ONE — CLAUDE CODE AS DIRECTOR AND EDITOR
========================================================

Responsibilities:
- Inspect the repository.
- Verify the product flow.
- Write the narration.
- Create the storyboard.
- Identify the required screenshots and assets.
- Produce a scene-by-scene production specification.
- Define timing and transitions.
- Prepare the caption text.

Before animation begins, save:

video-production/storyboard/script.md
video-production/storyboard/storyboard.md
video-production/storyboard/scene-timing.json
video-production/reports/codebase-flow.md
video-production/reports/asset-checklist.md

The script must be written for spoken narration.

Keep individual narration segments short enough to fit the
specified scenes without rushed delivery.

Target approximately 200–240 spoken words for the entire
video, adjusting as necessary for natural pacing.

Do not generate unnecessary narration just to fill time.

========================================================
08. STAGE TWO — TRANSCRIPTION AND CAPTIONS
========================================================

Prepare the final narration text and subtitle timing.

Inspect available transcription tools and integrations.

If NVIDIA Parakeet or an appropriate NVIDIA transcription
service is available, use it when suitable.

Otherwise, use an available compatible transcription tool.

Do not assume an API or account is already configured.

The caption workflow must:
- Preserve the exact narration.
- Use correct punctuation.
- Synchronize captions with the relevant scenes.
- Avoid excessively long subtitle lines.
- Use readable typography and adequate contrast.
- Avoid covering important UI controls.
- Keep subtitles within safe screen margins.

Deliver:
video-production/captions/narration.txt
video-production/captions/subtitles.srt
video-production/captions/subtitles.vtt

Because the final soundtrack will be supplied later, the
captions may initially be timed to the approved narration
script and scene timing.

If actual narration audio becomes available, align captions
to the audio rather than relying only on estimated timings.

Do not fabricate a transcription of audio that does not exist.

========================================================
09. STAGE THREE — HYPERFRAMES MOTION ANIMATION
========================================================

Use HyperFrames if the required tool or API is available.

First inspect its installed version, documentation,
integration requirements and rendering workflow.

Do not assume API methods that have not been verified.

Use the existing project conventions wherever practical.

Create motion graphics with:
- Smooth easing.
- Controlled camera movements.
- Layered UI cards.
- Animated text reveals.
- Screen transitions.
- Cursor and touch interaction cues.
- Focus highlights.
- Subtle shadows and depth.
- Consistent blue-accented branding.
- Restrained cinematic lighting.
- Smooth scene-to-scene continuity.

Use the application's actual screenshots and assets.

Do not generate a fake application interface when the real
interface can be captured.

Do not rely on a sequence of static screenshots with only
simple crossfades.

Where practical, animate individual UI elements and build
transitions that connect the viewer's actions to the resulting
screen.

For example:
- A location pin transitions into a selected address card.
- A menu item moves visually into the cart.
- The cart total becomes the checkout summary.
- A payment selection transitions into order progress.
- Timeline states animate as the order progresses.

Animations must communicate real interactions.

Avoid unnecessary spinning logos, excessive zooms, random
particles, exaggerated glitches or constant camera movement.

Create reusable animation components so timing can be refined
without rebuilding every scene from scratch.

========================================================
10. STAGE FOUR — BROWSER RESEARCH AND UI CAPTURE
========================================================

Use browser research only when needed.

Inspect the existing application in a browser, preferably
through a safe development or QA environment.

Capture genuine application screens for:
- Sign-in.
- New-customer onboarding.
- Location selection.
- Home.
- Restaurant discovery.
- Menu.
- Cart.
- Checkout.
- Cash payment.
- Seller QR payment.
- Order tracking.

Prefer browser automation or Playwright when available.

Capture the real responsive layouts at desktop and mobile
viewports where appropriate.

Do not expose development credentials or customer data.

Do not use production accounts or modify production orders.

If a particular screen cannot be reached safely, document
the limitation and create an explicitly labelled demonstration
state rather than claiming it is a genuine live state.

Web research is optional and should be used only to verify
details or obtain assets that cannot be sourced locally.

Do not download copyrighted promotional material merely
to imitate another company's advertising.

========================================================
11. STAGE FIVE — TELLA SCREEN EDITING
========================================================

Use Tella if it is available and suitable for screen capture
or editing.

Check whether access, account login, permissions or an
integration is required.

Ask the project owner for access only when necessary.

Use Tella to capture or assemble clean interactions if its
available capabilities fit the workflow.

Capture:
- Smooth browser navigation.
- Natural scrolling.
- Correct button interactions.
- Real application loading states.
- Responsive layouts.
- Clear order progression.

Avoid recording:
- Browser developer tools.
- Personal notifications.
- Credentials.
- Irrelevant browser tabs.
- Debug overlays.
- Accidental cursor movements.
- Unnecessary waiting.

If Tella is unavailable, use an appropriate local screen
recording or browser automation workflow.

Do not block the entire project waiting for an optional tool.

========================================================
12. STAGE SIX — SOUND DESIGN PREPARATION
========================================================

The project owner will select and provide the final soundtrack.

Therefore:
- Do not select final background music.
- Do not embed unlicensed music.
- Do not mix a final soundtrack into the master.
- Do not invent a final audio mix.

Prepare a clean, music-free video master.

Create a sound cue sheet specifying where sound could be
added later, including:
- Logo reveal.
- OTP entry.
- Successful demonstration transition.
- Location confirmation.
- Item added to cart.
- Checkout transition.
- Payment selection.
- Order status transitions.
- Final brand reveal.

Use timecodes and concise cue descriptions.

Deliver:
video-production/reports/sound-cue-sheet.md

Keep the final sound design flexible so the owner can provide
a soundtrack that matches the motion graphics.

========================================================
13. STAGE SEVEN — FINISHING AND QUALITY CONTROL
========================================================

Assemble the complete sequence.

Check:
- Correct duration.
- 1920 × 1080 output.
- 60 FPS output.
- Correct aspect ratio.
- Smooth scene transitions.
- Readable captions.
- Accurate UI content.
- Correct order progression.
- Clear payment explanation.
- Correct responsibility disclaimer.
- No private data.
- No accidental OTP or credential exposure.
- No unsupported product claims.
- No misleading payment confirmation.
- No fake delivery GPS tracking.
- No unintended blank frames.
- No clipping or visual glitches.
- No final soundtrack embedded.

Verify that the final video plays from beginning to end.

If available, use FFmpeg or another suitable media tool
to validate the export and inspect its metadata.

Inspect the final video at normal playback speed rather than
relying only on individual frames.

Save the final output to:

video-production/renders/setu-food-customer-walkthrough.mp4

Also save:
- Editable source project.
- Final narration script.
- Subtitle files.
- Asset manifest.
- Sound cue sheet.
- Quality-control report.

If rendering fails, diagnose the error, fix the issue and
rerender. Do not report an unsuccessful export as complete.

========================================================
14. IMPLEMENTATION SAFETY
========================================================

This is a video-production task.

Do not change:
- Backend authentication.
- OTP verification.
- API contracts.
- Database schemas.
- Order processing.
- Payment logic.
- Payment confirmation.
- Delivery verification.
- RBAC permissions.
- Production data.
- Existing application behavior.

The simulated OTP belongs exclusively to the video-editing
or isolated demonstration layer.

Never hardcode a demonstration OTP into production code.

Never bypass authentication to create a successful real login.

Do not automatically commit or push changes.

Do not deploy the application.

Keep video assets and generated code separate from the
production application's runtime files.

========================================================
15. FINAL REPORT
========================================================

When finished, report:

1. The actual customer flow discovered in the codebase.
2. The final narration script.
3. The final storyboard and scene timings.
4. Which tools were actually used.
5. Which tools were unavailable or required access.
6. Whether the OTP section is a video-only simulation.
7. Whether the video is complete and its actual duration.
8. The exported resolution and frame rate.
9. Whether subtitles and source files are available.
10. The quality-control results.
11. Any remaining limitations.

Provide the exact output paths.

Do not claim that a tool was used if it was not available.
Do not claim that a scene was captured from the real app if
it was generated or simulated.

FINAL ACCEPTANCE CRITERIA:

The result must be a complete, professional, animated
customer walkthrough that accurately demonstrates SETU Food,
explains the customer journey from sign-in through order
completion, makes direct-payment responsibilities clear,
and remains within the specified video duration.

The video must be understandable without technical knowledge.

Prioritize product accuracy, clarity, visual quality and
trust over unnecessary effects.
5. My recommendation before you run the prompt

There are three details worth preserving throughout production.

First, show the real interface wherever possible. The application already has a defined customer journey, so Claude should capture the existing screens and animate the transitions around them. Generating an entirely fictional interface would make the video look impressive but teach users the wrong workflow.

Second, distinguish order placement from payment confirmation. In the QR flow, the customer paying the provider does not automatically mean the application has recorded a confirmed payment. The video must show the seller's confirmation step where required.

Third, keep the demonstration OTP isolated from the actual application. Your email OTP setup has had delivery limitations, so a video-only simulation is appropriate. It should never become a shortcut in the live authentication flow.
The intended final result

The video should feel like a combination of a premium product launch and a practical customer tutorial:

    Opening: An engaging campus-focused introduction.
    Middle: A clear, animated walkthrough of the actual customer experience.
    Ending: Order tracking, direct-payment clarification, and a concise call to action.

The narration, captions, and motion graphics should work together so that even a first-time customer can understand how to use SETU Food.

One final production rule: do not add your final soundtrack until you have reviewed the complete visual cut. That will let you select music that matches the actual pace and emotional tone of the finished animation, rather than forcing the edit to fit a track chosen too early.
I am trying to paste this, but it is not, like pasting, because I am in a SSH terminal to my laptop with my another laptop. So possibly create a MD file that I could paste it without any issue.

I've created the complete Markdown file with the master prompt, all seven production stages, the customer journey, animation requirements, OTP demo safeguards, and final export checks.

SETU Food — Customer Walkthrough Master Prompt

Markdown file · 16 KB · Ready to use with Claude Code
How to use it on your laptop over SSH

Option 1 — Download and transfer the file (recommended)

Download the file on the laptop where you're using ChatGPT, then transfer it to your other laptop using SCP:

scp SETU_Food_Customer_Walkthrough_Master_Prompt.md \
  username@YOUR_LAPTOP_IP:~/Setu-Food-PWA/

Run that command from the laptop that has the downloaded file. Replace the username and IP with your SSH laptop's details.

Option 2 — Open it directly in your terminal

Once the file is on the laptop running Claude Code:

cd ~/Setu-Food-PWA
cat SETU_Food_Customer_Walkthrough_Master_Prompt.md

Or open it in an editor:

nano SETU_Food_Customer_Walkthrough_Master_Prompt.md

You can then copy the prompt from the file or instruct Claude Code to read it directly:
Read SETU_Food_Customer_Walkthrough_Master_Prompt.md completely.
Follow it as the production specification. First inspect the codebase
and create the research, script, and storyboard deliverables.
Do not modify the application backend or deploy anything.

My recommendation: use the direct-file approach. It avoids SSH clipboard problems and preserves the entire prompt without losing formatting or sections.
SETU_Food_Customer_Walkthrough_Master_Prompt.mdDocument
It is continuously saying no image found in clipboard. You are in SSHD. Try scp. Why?

That message means your SSH session or terminal tool is trying to read an image from your clipboard, but it cannot find one. You're likely trying to transfer the master prompt file to the machine running Claude Code, but the tool is expecting an image or clipboard content instead.

You don't need the clipboard. Use scp to transfer the Markdown file.
Step 1: Download the prompt file

Download the file I created:

Save it to your local computer.
Step 2: Open a separate terminal on your local computer

Run:

scp ~/Downloads/SETU_Food_Customer_Walkthrough_Master_Prompt.md YOUR_USERNAME@YOUR_SERVER_IP:~/

Replace YOUR_USERNAME and YOUR_SERVER_IP with the SSH username and IP address of the machine running Claude Code.

For example:

scp ~/Downloads/SETU_Food_Customer_Walkthrough_Master_Prompt.md developer@192.168.1.100:~/

Important: This example IP is illustrative. Use your actual server address.
Step 3: On the SSH machine

cd ~/Setu-Food-PWA

If you uploaded the file to your home directory, move it into the project:

mv ~/SETU_Food_Customer_Walkthrough_Master_Prompt.md .

Verify that it exists:

ls -lh SETU_Food_Customer_Walkthrough_Master_Prompt.md

Step 4: Give the prompt to Claude Code

Start Claude Code and enter:
Read SETU_Food_Customer_Walkthrough_Master_Prompt.md completely.
Follow it as the production specification for the SETU Food customer
walkthrough video. First inspect the codebase and prepare the research,
script, and storyboard deliverables. Do not modify backend authentication,
payment logic, production data, or deploy anything.
If scp itself fails

Run these commands on your local computer, not inside the remote SSH session:

ls -lh ~/Downloads/SETU_Food_Customer_Walkthrough_Master_Prompt.md
ssh YOUR_USERNAME@YOUR_SERVER_IP

If SSH works, exit that session and try the scp command again.

One question: Are you running Claude Code in a remote SSH terminal, or are you using a browser-based terminal that says “No image found in clipboard”? That distinction will help me give you the exact fix.
SETU_Food_Customer_Walkthrough_Master_Prompt.mdDocument
Unfortunately, I'm not near to the local computer. Is there any alternative way?
Worked for 12s

Yes. You can do this entirely from your current SSH session without accessing your local computer. You don't need the clipboard, and you don't need to transfer the downloaded file.

The easiest option is to have Claude Code create the prompt file directly on the remote machine using a terminal heredoc. Since the full master prompt is fairly long, there are two practical approaches:

    Use the existing ChatGPT conversation on your phone to copy the prompt text into your SSH terminal, if your terminal supports text pasting.
    Ask Claude Code to generate the production specification directly from the project files and the instructions below, avoiding file transfer entirely.

Let's try the second approach first.
Option A — Run Claude Code directly (recommended)

If Claude Code is already open on the SSH machine, copy the prompt below into Claude Code's input. You don't need to create or transfer a file first.
You are the director, researcher, animator, and quality-control lead for the SETU Food customer walkthrough video.

First inspect the existing Setu-Food-PWA repository and verify the real customer experience. Then create a complete, professional, cinematic product walkthrough.

VIDEO SPECIFICATIONS
- Duration: 1 minute 50 seconds, acceptable range 1:45–2:00.
- Resolution: 1920×1080, 60 FPS, 16:9.
- Audience: IIT Kharagpur students, professors, faculty, and campus staff.
- Style: Modern, polished, engaging, professional motion graphics; not a static slideshow.
- Output: video-production/renders/setu-food-customer-walkthrough.mp4
- Do not embed background music; I will add it later.

FIRST: INSPECT THE PROJECT
Inspect the React/Vite frontend, actual routes, styles, assets, authentication, onboarding, location, menus, cart, checkout, payment, and order tracking. Use browser automation or Playwright if available and safe.

Create a video-production/ directory, reusing any existing equivalent structure. Save:
- storyboard/script.md
- storyboard/storyboard.md
- storyboard/scene-timing.json
- research/codebase-flow.md
- reports/asset-checklist.md
- reports/sound-cue-sheet.md
- reports/quality-control.md
- captions/narration.txt
- captions/subtitles.srt
- captions/subtitles.vtt
- renders/setu-food-customer-walkthrough.mp4
- All editable animation source files, assets manifest, and render instructions.

VIDEO STORYBOARD
1. 0–8s: SETU Food branding and an animated campus-inspired opening.
2. 8–18s: Show the real home screen and campus food-provider discovery.
3. 18–30s: Demonstrate existing-customer sign-in. If OTP delivery is unavailable, simulate the OTP exclusively as a clearly labelled video overlay.
4. 30–42s: Show the actual new-customer onboarding flow.
5. 42–55s: Demonstrate location detection, saved addresses, or manual location search, as actually supported.
6. 55–71s: Browse available providers and menus, select food, and add it to the cart.
7. 71–83s: Review the cart, delivery/pickup option, address, applicable delivery charge, and total.
8. 83–101s: Explain cash and provider UPI QR payment, showing only the payment flows actually supported.
9. 101–113s: Demonstrate real order-tracking screens and supported order-status progression.
10. 113–120s: End with SETU branding, a call to action, and the provider-responsibility disclaimer.

BRAND MESSAGE
“Your campus. Your food. A simpler way to order.”

Explain the product in plain language. Emphasize convenient campus discovery, simple ordering, transparent charges, and direct payment to the provider.

IMPORTANT PRODUCT ACCURACY
- SETU connects customers with approved campus food providers.
- Customers pay the provider directly.
- SETU does not collect or process payments.
- SETU does not charge a platform commission.
- Delivery charges may apply; show actual charges.
- Food preparation and fulfilment are handled by the respective provider.
- Payment status and order status are different.
- QR orders may require payment review before acceptance.
- Never invent menu items, prices, discounts, features, delivery times, or successful transactions.
- Never claim GPS tracking exists unless verified.
- Never expose private data, credentials, real OTPs, or real payment evidence.

Use this disclaimer on the closing frame:
“SETU connects customers with approved campus food providers. Food preparation, delivery and payment are handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene.”

TOOLS AND ANIMATION
Inspect which tools are actually available. Use HyperFrames if installed and compatible; otherwise choose an available rendering workflow. Use Playwright or browser automation for safe screen capture if available. Consider Tella only if accessible and useful. Do not invent tool APIs or claim a tool was used if it was not.

Create polished typography, smooth easing, animated UI highlights, cursor/touch cues, clean transitions, and readable captions. Use genuine application screens wherever possible. Clearly label any simulated screen.

SECURITY BOUNDARIES
This is a video-production task only.
DO NOT modify backend authentication, OTP verification, APIs, database schemas, payment logic, order processing, handover verification, role-based access, production data, or server configuration.
Never hardcode a fake OTP or bypass authentication in the actual application.
Do not commit, push, or deploy anything.

WORKFLOW
1. Inspect the repository and available tools.
2. Report the actual customer flow and any missing or inaccessible screens.
3. Write the narration, storyboard, and timing.
4. Capture genuine UI screens safely.
5. Build the animated video and subtitles.
6. Render and inspect the finished video.
7. Validate duration, resolution, FPS, captions, visual quality, and product accuracy.
8. Report the exact output paths, actual tools used, limitations, and QC results.

Do not stop after writing a plan. Continue with implementation wherever the available environment permits. Never claim a finished video exists unless it has actually been rendered and checked.
Option B — Create the master-prompt file on the SSH machine

If you specifically need the .md file, you can create one directly in your repository:

cd ~/Setu-Food-PWA
nano SETU_Food_Customer_Walkthrough_Master_Prompt.md

Paste the prompt into the editor, then save with Ctrl+O, press Enter, and exit with Ctrl+X.

You can then tell Claude Code to read that file.
One important distinction

If the message “No image found in clipboard” appears because you're using an image-paste feature, cancel that operation and use the normal text input instead. If your SSH interface does not allow pasting text at all, tell me which app or terminal you are using (for example, Termius, browser-based SSH, VS Code Remote SSH, or another service). I'll give you a method that works with that specific setup.
MASTER PROMPT — SETU Food Cinematic Customer Journey Video

Production owner: Claude Code
Repository: Setu-Food-PWA
Deliverable: Professional animated customer walkthrough
Target duration: 1:50 (acceptable range 1:45–2:00)
Output: MP4, 1920×1080, 60 FPS, 16:9
Audio: Music-free master; the project owner will supply the soundtrack later.
1. Objective

Create a polished, cinematic, easy-to-follow product walkthrough showing how a customer uses SETU Food from first visit through placing an order and completing the handover.

This must be a genuinely animated product video, not a static slideshow. Use real application screens and realistic interactions, with professional typography, smooth motion graphics, transitions, UI highlights, and restrained cinematic effects.

Target audience:

    IIT Kharagpur students
    Professors and faculty
    Campus staff
    Other eligible campus customers

Keep the visual style modern and engaging without looking immature or excluding older users.
2. Required deliverables

Create a clearly organized video-production/ directory, reusing any existing equivalent structure. Prepare:

    renders/setu-food-customer-walkthrough.mp4
    Editable source/project files
    storyboard/script.md
    storyboard/storyboard.md
    storyboard/scene-timing.json
    research/codebase-flow.md
    reports/asset-checklist.md
    reports/sound-cue-sheet.md
    reports/quality-control.md
    captions/narration.txt
    captions/subtitles.srt
    captions/subtitles.vtt
    Asset manifest and render instructions

Do not overwrite application files or production data.
3. Inspect the real codebase first

Before scripting, inspect the actual React/Vite customer UI, route configuration, components, styling, assets, authentication handlers, location flow, cart, checkout, payment, and order tracking.

Inspect these routes where they exist:

    /signin
    /onboarding
    /
    /search
    /seller/:id
    /cart
    /confirm
    /track/:id
    /orders
    /report/:orderId
    /profile

Verify actual behavior before recording. Use browser automation or Playwright where available and safe. Do not assume route names or features are implemented exactly as described; verify the repository.

Never expose personal information, credentials, API keys, customer details, private payment screenshots, or private records.
4. Product truth — mandatory

SETU Food connects customers with approved campus food providers.

Keep these facts accurate:

    SETU does not collect or process customer payments.
    SETU does not operate its own delivery fleet.
    Food preparation and fulfilment are handled by the respective provider.
    Customers pay the provider directly.
    Payment options include cash and the provider's own UPI QR, depending on the actual order flow.
    SETU does not charge a platform commission.
    A delivery charge may apply; show the actual charges from the application.
    SETU does not independently guarantee food hygiene.
    Order status and payment status are separate.
    QR orders may require payment review before provider acceptance.

Never invent prices, discounts, restaurants, menu items, delivery times, ratings, payment confirmations, or features. Use real application data when safe, or isolated and clearly identified demonstration data.
5. Brand positioning and script pitch

Primary line:

    Your campus. Your food. A simpler way to order.

Suggested opening:

    From your hall to your favourite campus food spot, ordering just got simpler.

Explain that SETU Food brings approved campus food providers and customers into one convenient ordering experience.

Emphasize convenience, campus-focused discovery, transparent totals, no platform commission, direct payment to the provider, and clear order progress.

Preferred wording:

    Discover approved campus food providers, order in a few simple steps, and pay the provider directly. No platform commission, with any applicable delivery charges shown before you place your order.

Do not name competitors or use disguised competitor names. Do not claim that other platforms charge specific amounts. Do not claim every order is completely free or that delivery is always free. Avoid unsupported promises about speed, safety, eligibility, or hygiene.

Narration should sound conversational, confident, concise, and natural.
6. Storyboard — target 110–120 seconds

Every scene must specify start/end time, narration, on-screen text, actual UI state, animation, transition, captions, and asset references.
Scene 1 — Opening hook (0–8s)

Reveal SETU Services / SETU Food branding on a campus-inspired background. Transition into attractive food imagery and an animated app interface.

Text: “Your campus. Your food. A simpler way to order.”

Narration: “Meet SETU Food, a simpler way to discover and order food from approved providers around your campus.”

Use restrained logo animation, subtle depth/parallax, and clean typography. Avoid excessive effects.
Scene 2 — What SETU does (8–18s)

Show the real home screen and approved provider cards. Highlight restaurant discovery, categories, menus, and delivery/pickup only where supported.

Narration: “Explore approved campus food providers, browse their menus, and choose what you would like to order.”

Text: “Discover. Choose. Order.”
Scene 3 — Existing customer sign-in (18–30s)

Show the actual sign-in page. Demonstrate a customer entering their email and choosing the email OTP option if that is supported in the current UI.

The OTP delivery may not work in the demo environment. Therefore create a video-only simulation:

    Show a clearly labelled demonstration OTP notification.
    Display a sample six-digit demonstration code.
    Animate entering the code.
    Show a short verification/loading state.
    Transition into the home screen.

Show a subtle DEMO label during the simulation.

Narration: “Already have an account? Sign in and continue to your campus food experience.”

Do not claim a real email was delivered or a real OTP verified if that did not happen. Do not hardcode a fake OTP into the real application or bypass authentication. Use a video overlay, isolated mock screen, or editing animation. If password sign-in also exists, do not imply OTP is the only option.
Scene 4 — New customer onboarding (30–42s)

Show the actual new-customer path and real onboarding steps. Project notes describe a four-step onboarding flow; verify the current code and labels before filming.

Narration: “New to SETU Food? Complete the short onboarding process, set up your account, and prepare to explore campus food.”

Do not invent registration requirements. If OTP is simulated, keep the demonstration clearly labelled.
Scene 5 — Location (42–55s)

Show the real location flow:

    Location permission request.
    Automatic detection if available.
    Saved-address selection.
    Manual search fallback.
    Confirmation of an eligible campus location.

Show a saved Home address only if the actual UI supports it.

Narration: “Confirm where you would like your order delivered. You can use your detected location, select a saved address, or search for an eligible campus location.”

Animate a map pin, address card, and selected-location highlight. Respect the actual campus boundary. Do not show an arbitrary off-campus location accepted. Do not imply GPS detection always succeeds.
Scene 6 — Discover food and select items (55–71s)

Show the actual home/search interface and available filters, such as cuisine, vegetarian, open-now, or preparation-time filters only if implemented.

Open a real or isolated demonstration provider, browse the menu, open an item, and add it to the cart. Animate the quantity and cart count.

Narration: “Browse available stalls, explore the menu, and add your favourites to the cart. Clear item details help you decide what works for you.”

Do not add multiple providers to one cart if the application only permits one provider per cart.
Scene 7 — Cart and checkout (71–83s)

Show actual cart details: items, quantities, prices, delivery/pickup, selected address, applicable delivery charge, and total.

Narration: “Review your items, confirm your location, and check the complete order total before proceeding.”

Highlight the total. Do not invent fees or discounts, and do not hide applicable delivery charges.
Scene 8 — Direct payment (83–101s)

Show the actual confirmation screen and explain the two options.

Cash: Select cash and place the order. Show the order progressing. At handover, show direct payment to the provider and the actual handover-verification interaction, without revealing any real customer's code.

Seller QR: Select the provider's QR option, show a safe demonstration QR UI, explain that the customer pays directly using their UPI app, then show payment-proof upload and provider confirmation if supported.

Narration: “Choose cash or pay directly to the provider using their UPI QR, depending on the available options. SETU does not collect or process the payment.”

Text: “Payment goes directly to the provider.”

Do not imply money actually moved in a simulated scene. Clearly distinguish demonstration graphics from a genuine transaction. Show the QR payment-review stage where applicable.
Scene 9 — Order tracking (101–113s)

Show the real tracking interface, live conversation/timeline, and status updates where available.

Possible progression, only where applicable:

PLACED → ACCEPTED → PREPARING → READY / OUT FOR DELIVERY → COMPLETED

Narration: “Follow your order as the provider accepts it, prepares it, and moves it towards collection or delivery.”

Do not fabricate GPS rider tracking. Do not imply every order follows an identical state sequence. Clearly label simulated states as demonstrations.
Scene 10 — Final frame (113–120s)

Return to SETU branding with a concise call to action.

Text:

    “Your campus. Your food. Your SETU.”
    “Explore SETU Food.”

Display this disclaimer legibly:

    SETU connects customers with approved campus food providers. Food preparation, delivery and payment are handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene.

Narration: “Discover campus food through SETU Food. Simple ordering, transparent charges, and direct payment to your provider.”

Keep the final frame clean and readable.
7. Stage One — Claude Code as director/editor

Inspect the repository, verify the user journey, write the spoken narration, storyboard, scene timing, and asset checklist.

Save:

    video-production/storyboard/script.md
    video-production/storyboard/storyboard.md
    video-production/storyboard/scene-timing.json
    video-production/research/codebase-flow.md
    video-production/reports/asset-checklist.md

Target approximately 200–240 spoken words, adjusting for natural pacing. Do not rush narration to fit the runtime.
8. Stage Two — Transcription and subtitles

Inspect available transcription tools. Use NVIDIA Parakeet or an appropriate NVIDIA transcription service if actually available; otherwise use a compatible available tool.

Do not assume APIs, keys, or accounts are configured.

Prepare accurate captions, correct punctuation, short readable lines, safe margins, and synchronization with narration. Do not claim audio transcription was performed if no audio exists.

Save:

    video-production/captions/narration.txt
    video-production/captions/subtitles.srt
    video-production/captions/subtitles.vtt

Initially timing may follow the approved script and scene timing. If narration audio is later supplied, align captions to the actual audio.
9. Stage Three — HyperFrames animation

Use HyperFrames if available. Inspect its actual installation, version, documentation, and rendering workflow before coding. Do not invent API methods.

Create:

    Smooth easing and camera movements.
    Layered UI cards and transitions.
    Animated text reveals and focus highlights.
    Cursor/touch interaction cues.
    Subtle depth, shadows, and restrained cinematic lighting.
    Consistent SETU blue-accented branding.
    Reusable animation components.

Use actual app screenshots and assets. Do not substitute a fictional UI when the real UI can be captured. Avoid simple screenshot crossfades as the only animation.

Transitions should communicate the actual interaction: location selection into address confirmation, item into cart, cart into checkout, payment selection into order progress, and timeline progression.
10. Stage Four — Browser research and capture

Inspect the app in a safe development or QA environment. Use Playwright or browser automation where available.

Capture genuine screens for sign-in, onboarding, location, home, restaurant/menu, cart, checkout, cash/QR payment, and tracking.

Do not expose credentials, personal data, private payment evidence, or production customer records. Do not modify production orders.

If a screen cannot be reached safely, document the limitation and create an explicitly labelled demo state. Do not pretend a simulated screen is a live app capture.

Web research is optional; use it only when required for accurate details or missing assets.
11. Stage Five — Tella screen editing

Use Tella if available and suitable. Check whether login, permission, or an integration is needed. Ask the project owner for access only when necessary.

Capture clean interactions, natural scrolling, correct button actions, real loading states, and responsive layouts. Avoid developer tools, personal notifications, credentials, unrelated tabs, and accidental cursor movements.

If Tella is unavailable, use an appropriate local screen-recording or browser automation alternative. Do not block the project on an optional tool.
12. Stage Six — Sound preparation

The project owner will supply the soundtrack. Do not select or embed final background music or unlicensed sound.

Prepare a music-free master and create:

video-production/reports/sound-cue-sheet.md

Include timecodes and suggested cues for logo reveal, OTP entry, location confirmation, adding to cart, checkout, payment selection, status changes, and final brand reveal.
13. Stage Seven — Finishing and quality control

Render the complete sequence and validate:

    MP4 format.
    1920×1080 resolution.
    60 FPS.
    16:9 aspect ratio.
    Actual duration within 1:45–2:00.
    Smooth transitions and readable captions.
    Accurate UI and order progression.
    Correct direct-payment explanation.
    Clear provider-responsibility disclaimer.
    No private data, credentials, or real OTP exposure.
    No unsupported claims, fake GPS tracking, or misleading payment confirmation.
    No blank frames, clipping, or visual glitches.
    No soundtrack embedded.

Inspect the video at normal playback speed. If available, use FFmpeg or an equivalent tool to verify media metadata and playback.

Final video path:

video-production/renders/setu-food-customer-walkthrough.mp4

Also save editable sources, subtitles, narration, asset manifest, cue sheet, render instructions, and quality-control report.

If rendering fails, diagnose and retry. Never claim success for an incomplete export.
14. Safety and repository boundaries

This is a video-production task. Do not change backend authentication, OTP verification, APIs, database schemas, order processing, payment logic, handover verification, RBAC, production data, or server configuration.

Keep all fake OTP and simulated states exclusively in the video-editing or isolated demo layer. Never bypass authentication or hardcode demo credentials in production.

Do not commit, push, or deploy changes.
15. Final report and acceptance criteria

Report:

    Actual customer flow discovered.
    Final narration and storyboard.
    Tools actually used and tools unavailable or needing access.
    Which scenes use real UI versus simulation.
    Whether the OTP is video-only simulated.
    Actual duration, resolution, and frame rate.
    Availability of subtitles and editable sources.
    Quality-control results and remaining limitations.
    Exact output paths.

The deliverable must be a complete, professional animated walkthrough that accurately teaches the customer journey from sign-in to order completion, explains direct payment, and is understandable without technical knowledge.

Prioritize product accuracy, clarity, visual quality, and trust over unnecessary effects.


