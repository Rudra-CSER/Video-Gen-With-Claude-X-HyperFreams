# SETU Food walkthrough — scene build guide

One film, many builders. Every scene composition follows this guide so the cut reads as one piece.

## Project layout

```
hyperframes/
  index.html                 root orchestrator (generated): shared background, scene slots, captions slot
  compositions/sNN-*.html    one sub-composition per scene (you write exactly one)
  compositions/captions.html burned-in captions for the whole film (generated — never put captions in a scene)
  assets/css/kit.css         tokens, fonts, phone frame, overlays, type styles   (linked inside each <template>)
  assets/js/kit.js           window.SetuKit motion helpers (loaded once by index.html)
  assets/ui/<group>/<shot>.png   REAL app captures, 1170x2532 = 390x844 CSS px at 3x
  assets/clips/<group>-<seq>.mp4 REAL typing/scrolling captures as 60 fps clips (1170x2532)
  assets/data/marks.json     CSS-px boxes {x,y,w,h} of UI elements per shot; clip lengths
  assets/data/campus-boundary.json  real campus boundary polygon as an SVG path (viewBox 0 0 1000 516.4)
  assets/brand/setu-logo.png official SETU lockup (always on a WHITE rounded tile, never recoloured)
  assets/brand/setu-mark.svg the app's vector mark
```

All asset paths are written **root-relative** (`assets/ui/cart/01-cart.png`), never `../`.

## Canvas grid (1920 x 1080)

| Zone | Box | Use |
|---|---|---|
| Text column | x 140–820, vertically centred, keep clear of y > 880 | kicker, headline, subline |
| Callout lane | x 840–1130 | callout pills with a leader line to the phone; never on top of key UI |
| Phone (default) | spec `{ left: 1150, top: 70, k: 1.08 }` → outer 449 x 940, bottom at y≈1010 | the real app |
| Right margin | x 1620–1880 | secondary labels only |
| **Caption zone (reserved)** | x 120–1140, y 880–1050 (left) or centred y 900–1050 on full-screen scenes | burned-in captions live here, drawn by captions.html; keep it empty |

Full-screen moments (opening, end card, desktop shot) may use the whole canvas but must keep the centred caption zone (y 900–1050) free.

## Type

- Kicker: `.kicker` (Space Mono, uppercase, orange rule). Format `Step N · Name` or a short label. Max ~32 chars.
- Headline: `.headline` (Sora 800, 86 px; `.headline--md` 68 px; `.headline--xl` 116 px). 2–6 words, max two lines in the column. Use `<span class="accent">` (pale indigo) for one key word; `accent-o` (orange) sparingly.
- Subline: `.subline` (Plus Jakarta Sans 32 px). One sentence, max two lines.
- Never emoji. Icons only if they are the app's own line icons (Lucide style, stroke 1.85).
- Rupee sign: Sora has no `₹` glyph. kit.css falls back to Plus Jakarta Sans for it, but set prices and totals in Space Mono (`var(--font-mono)`) or Plus Jakarta Sans on purpose, never rely on Sora for a line that is mostly numbers.
- Quote app copy exactly when you show it as text.

## Colour

Canvas is the shared indigo background from index.html — scene roots are transparent. Accents: brand blue `#0033DA` / bright `#2E5BEE`, pale indigo `#B8C7FF`, SETU orange `#EC5A2A` (rings, rules, one highlight at a time), success green `#19B36B`.

## The phone

```html
<div class="rig" id="sNN-rig">                <!-- camera wrapper: transform-origin 0 0, full canvas -->
  <div class="phone" id="sNN-phone">
    <div class="side-btn" style="top:190px;height:70px"></div>
    <div class="side-btn" style="top:290px;height:120px"></div>
    <div class="glass"><div class="screen" id="sNN-screen"></div></div>
  </div>
</div>
```

```css
#root .rig { position: absolute; inset: 0; transform-origin: 0 0; }
```

```js
const K = window.SetuKit;
const spec = { left: 1150, top: 70, k: 1.08 };
K.placePhone(document.getElementById('sNN-phone'), spec);
const screen = document.getElementById('sNN-screen');
const a = K.layer(screen, 'assets/ui/cart/01-cart.png', 'sNN-a', { visible: true });
const b = K.layer(screen, 'assets/ui/checkout/01-confirm-cash.png', 'sNN-b');
```

Layers stack in creation order; later layers are on top.

### Clips (typing / scrolling) inside the phone

A `<video>` must be a direct child of a **non-timed** layer div and carry its own timing:

```html
<div class="layer" id="sNN-typing"><video id="sNN-v1" class="clip" src="assets/clips/signin-02-type-email.mp4"
  muted playsinline data-start="2.0" data-duration="2.1" data-hf-media-start-basis="local" data-track-index="3"></video></div>
```

`data-start` is scene-local. Clip lengths are in `marks.json` under `clip:<group>/<seq>` (`seconds`). When the clip ends, hold its last frame with the matching still (`<shot>.png`) underneath or cut to the next still. Never animate the `<video>` itself; animate its layer.

## Motion vocabulary (kit.js)

| Helper | Use |
|---|---|
| `K.revealWords(tl, el, t)` | headline entrance (rise + unblur, staggered) |
| `K.fadeUp(tl, target, t)` / `K.fadeOut(tl, target, t)` | kicker, subline, labels |
| `K.tap(tl, screen, box, t)` | finger tap on a real control (touch dot + ripple, ~0.65 s) — tap BEFORE the screen changes |
| `K.ring(tl, screen, box, t, dur, {blue})` | highlight a real element (orange by default) |
| `K.swapPush / swapBack / swapFade` | navigation between captured screens |
| `K.swapSheet(screen, tl, from, src, t, sheetTop)` | bottom sheet opening (picker, review sheet) |
| `K.focus(tl, rig, P, s, t, dur, {to})` / `K.unfocus` | camera push-in on a canvas point P (use `K.toCanvas(spec, x, y)`), scale 1.4–2.2 |
| `K.drawPath(tl, path, t, dur)` | draw an SVG line (campus outline, leader lines) |
| `K.callout(tl, el, t, dur)` | callout pill in/out |

Easing: `expo.out` for entrances, `expo.inOut` for camera and navigation, `back.out(1.6–2)` for small pops. The app's own curve is `cubic-bezier(.22,1,.36,1)`.

Rhythm: one idea at a time. A tap, then the result, then a beat (≥ 0.6 s) to read it. Hold any screen whose text matters for ≥ 1.2 s. Camera moves 0.8–1.2 s. No constant drifting, no spinning, no particles, no glitch.

Lessons from the prototypes (do not repeat):
- An element that enters later must be fully hidden before its entrance: start off-canvas (`y: 1150`+) **and/or** `opacity: 0` in the `fromTo`, so nothing peeks in early.
- Floating labels and chips must not overlap the phone, each other, the text column or the caption zone, and must sit fully on canvas (right edge ≤ 1880). Measure: a 28 px chip is about 17 px per character + 70 px. Keep at most 4 on screen.
- Exits are clean and short (fade/slide out 0.3–0.5 s); never fly several objects into the phone at once.
- Callouts live in the callout lane (x 840–1130) or right margin; never on top of the text column or on key UI.

Marks are text-tight for some elements (e.g. `fee` is the label). For rings around whole rows, widen to the row: `{ x: 18, y: mark.y - 14, w: 354, h: mark.h + 28 }`.

## HyperFrames rules (lint enforces most)

- Sub-composition file: everything inside `<template>`; root `<div id="root" data-composition-id="sNN-..." data-width="1920" data-height="1080">`; style the root as `#root { position:absolute; inset:0; }`; link the kit inside the template: `<link rel="stylesheet" href="assets/css/kit.css">`.
- Exactly one paused timeline, registered last: `window.__timelines["sNN-..."] = tl;` — key = the `data-composition-id`, which must equal the host slot id in index.html.
- Prefix every element id with the scene id (`sNN-`), so ids stay unique in the assembled page.
- All twelve scenes and the caption track live in one page, so scope every custom CSS rule to your scene: select by your own prefixed ids or prefixed classes (`#s07-slip`, `.s07-chip`), never by a bare tag or an unprefixed class. Never restyle a kit class globally (no `.callout { … }` in a scene; write `#s07-call-fee.callout { … }` or add a prefixed modifier class). The only unprefixed selector allowed is the standard `#root { position: absolute; inset: 0; }` and `#root .rig { … }` from this guide.
- Prefer `fromTo` for entrances. No `Date.now()`, `Math.random()`, network, `getBoundingClientRect()` at tween time, `repeat: -1`.
- Never tween `visibility`/`display`/`autoAlpha` on a `.clip`. Don't pair a CSS `transform` with a GSAP tween on the same element (set initial transforms in `fromTo`).
- Never `<br>` in body text (titles may break deliberately per word).
- A `<video data-start>` must not have an ancestor with `data-start`.
- Scene timing is local: 0 = the slot's `data-start` in index.html. Scene boundaries are **hard cuts** (the root does not cross-fade): the last frame of scene N and the first frame of scene N+1 must match the shared handoff contract (see below), so the cut is invisible unless the storyboard designs it otherwise.

## Honesty rules (non-negotiable)

- Only real captures for app screens. Overlays may point, highlight, zoom — never alter what the app says.
- The emailed one-time code is a released sign-in method: no DEMO badge on it (since the November 2026 update). Demo data stays labelled: the demo QR and its demo UPI ID, the sample-stalls note and the end-card fine print. The user's UPI app is never drawn.
- The app calls its people users (a User account): never write 'customer' in captions, narration or on-screen text.
- The demo QR is labelled in the capture itself; never imply real money moved.
- Never write "SETU delivers", pickup, rider GPS, delivery-time promises, "free", "zero cost", competitor names.

## Storyboard contract (storyboard/scene-timing.json → .packets/<sceneId>.json)

Every builder works from its packet (`node tools/make-packets.mjs` writes them). In the packet, captions, on-screen text, shots, sound cues and the DEMO windows are already **scene-local**; `animationLocal` is the time-coded build spec in local seconds.

- `shots[].asset.src` is the exact file to use. A clip may point at a pre-rendered speed variant (`assets/clips/<group>-<seq>.<ms>ms.mp4`, made by `node tools/clip-variant.mjs --from-storyboard`); its `asset.seconds` is its real length.
- `handoffIn` / `handoffOut` describe the boundary frames: phone placement (`default` = the packet's `phoneSpec`, `none`, or a custom spec), the capture fully visible in the phone, the rig transform (`identity` or `{s, P:[screenX,screenY], T:[canvasX,canvasY]}` = `K.focus(tl, rig, K.toCanvas(spec, P[0], P[1]), s, ...)` landing P at T), the left column text and any overlays. Frame 0 of your scene must equal `handoffIn`; your last frame must equal `handoffOut`. Both are contracts shared with the neighbouring scene's builder.
- `demoBadgeLocal`: the `.demo-badge` ("Demo environment") is fully visible for these windows.

## Starting point

`tests/scene-template.html` is a lint-clean sub-composition (0 errors, 0 warnings) that uses the phone, a still under a typing clip, a tap, a swap, a callout, a camera push-in and the DEMO badge. Copy its structure: everything inside `<template>`, kit.css linked inside the template, one paused timeline registered as `window.__timelines['<sceneId>']`, the script wrapped in an IIFE. Fonts are declared by the root page; do not add @font-face rules.

A camera push-in scales the whole rig (phone and everything inside it) around canvas point P, so the phone grows towards the text column and the callout lane: check that canvas-level callouts and the left column never end up under or on top of the enlarged phone.

## Preview and verify loop (do this for every scene)

```bash
cd video-production/hyperframes
node tools/preview-scene.mjs sNN                                   # writes .preview/<sceneId>/ (scene at t=0, film background, its own captions)
tools/hf-lock.sh hyperframes lint .preview/<sceneId>               # structure rules
tools/hf-lock.sh hyperframes snapshot .preview/<sceneId> --at 0,0.5,1.2,... -o .preview/<sceneId>/snaps
tools/check-scene.sh sNN                                            # runtime + layout + motion + contrast check of the scene
```

- Never run `hyperframes check .preview/<sceneId>` without the wrapper: the preview links the scene file, the check bundler reports a linked file as "empty" and passes without checking anything. `tools/check-scene.sh sNN` (or `tools/hf-lock.sh hyperframes check .preview/<sceneId>`) checks a real copy in `.checks/<sceneId>/`.

- Always run Chrome-based commands (`snapshot`, `check`, `validate`, `inspect`, `render`) through `tools/hf-lock.sh`. This machine is a shared QA box with little free memory; the wrapper limits the number of concurrent headless Chromes.
- Look at the PNGs (they are full 1920x1080 frames). Check every beat: the frame just before and just after each tap, swap, camera move and callout; t=0 and the last frame against the handoff contracts; and that the caption zone stays clear.
- `hyperframes snapshot --zoom x,y,w,h` crops a region at high density, which helps with small UI text.
- Never write outside your own `compositions/<sceneId>.html` (plus `.preview/<sceneId>/`). Shared files (kit.js, kit.css, STYLE.md, tools, index.html, captions) belong to the director; if you need a kit change, report it instead of editing.
