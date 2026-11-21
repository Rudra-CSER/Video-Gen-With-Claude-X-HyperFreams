<<<<<<< HEAD
# SETU Food — user walkthrough video

A cinematic, fully animated walkthrough of the SETU Food user journey for IIT Kharagpur campus users: sign in with your email and an emailed six-digit code, first-time onboarding (a User account), choosing an eligible campus delivery location, finding food, the cart, paying the stall directly (cash, or online via UPI — one tap opens the user's UPI app, or they scan the stall's QR), tracking, the six-digit handover code, and the review.

- **Master:** `renders/setu-food-user-walkthrough.mp4` — 1920×1080, 60 fps, H.264, yuv420p, **no audio track** (the soundtrack is added later by the owner). The earlier cut (before the November 2026 update) keeps its old name, `renders/setu-food-customer-walkthrough.mp4`.
- **Story:** "Dinner at B-212": one evening with Aarav (Nehru Hall of Residence, Room B-212) ordering a Masala Dosa and two Filter Coffees from Southside Tiffins; ₹140 of food + the stall's own ₹10 delivery charge = ₹150, paid to the stall in cash at the door.
- **Real UI only:** every app screen is a real capture of the app, recorded with Playwright on an isolated demo copy of the app (sample stalls, a demo persona, a labelled demo payment QR with a demo UPI ID, a local test inbox). Nothing in `client/` or `server/` was changed, and nothing was pushed to the repository.

## November 2026 update

Three changes to the existing cut, same story and length (1:58.85):

1. **Customer → User.** The app now says *User account* ('Sign in with your User account', 'Create a User account', 'SIGNING IN AS User'). Captions, narration, the voice-over script and the end-card disclaimer ('SETU connects users with approved campus food providers…') follow; `validate_storyboard.py` now rejects 'customer' in any on-screen wording.
2. **Email one-time-code sign-in.** Scene 3 shows the released email sign-in: email → 'Email me a one-time code instead' → the six-digit code from the sign-in email → 'Verify and continue'. It is no longer labelled as a demo; the password path is visible but not featured. Scene 3 is 1.5 s shorter.
3. **UPI hand-off on QR payments.** Checkout's second option is now 'Pay online via UPI'. Scene 9's side branch shows the stall accepting, 'Pay ₹150 in your UPI app' → 'Opening your UPI app…' → the return note 'Paid? Tap “I’ve paid” below…' → 'Seller is checking your payment' → 'Order confirmed'. The UPI app itself is never drawn (an editorial callout marks the hand-off). Scene 9 is 1.5 s longer; scenes 4–8 start 1.5 s earlier; scenes 10–12 are unchanged.

New captures: desktop sign-in (s02), sign-in (s03), sign-up and onboarding step 1 (s04), checkout and the UPI order (s08–s09). Every other capture is the earlier one (the screens are unchanged); see `reports/capture-2026-11.md`. Still-'customer' wording inside the app itself (not featured in the video): the sign-in email's 'sign in to SETU Food as Customer.', onboarding step 1's 'Signed in as customer', and the order thread's seller-side system lines.

## Folder map

| Path | What it holds |
|---|---|
| `storyboard/scene-timing.json` | **The source of truth**: 12 scenes with times, narration, captions, on-screen text, shots, time-coded animation specs, scene-boundary handoff contracts, sound cues and accuracy notes |
| `storyboard/script.md`, `storyboard/storyboard.md` | Readable script and storyboard (generated from the JSON) |
| `storyboard/layout.json` | Caption placement per scene |
| `storyboard/validate_storyboard.py` | Checks timing, caption rules, files, handoffs and forbidden claims |
| `captions/narration.txt`, `captions/subtitles.srt`, `captions/subtitles.vtt` | Narration and subtitles (timed to the script; there is no voice-over audio) |
| `hyperframes/` | The editable animation project (HyperFrames 0.8.143 + GSAP 3.13.0) |
| `hyperframes/compositions/sNN-*.html` | One animated scene per file; `captions.html` is the burned-in caption track |
| `hyperframes/index.html` | Root timeline (generated): shared background, scene slots, caption track |
| `hyperframes/assets/` | Real captures (`ui/`), typing/scroll clips (`clips/`), brand, fonts, motion kit (`js/kit.js`, `css/kit.css`), marks and the campus boundary (`data/`) |
| `hyperframes/STYLE.md` | Build guide every scene follows (grid, type, colour, motion, honesty rules) |
| `hyperframes/tools/` | Build, preview, render and QC tools (see below) |
| `assets/screens/` | Raw Playwright captures and frame sequences with element marks |
| `capture/` | The Playwright capture scripts and the isolated demo-stack helpers |
| `research/codebase-flow.md` | The customer flow as built, with code evidence, and what the video may and may not claim |
| `reports/` | Asset checklist, asset manifest, sound cue sheet, quality-control report |
| `renders/` | The rendered master |

## Requirements

- Node.js 22 (`node --version`), the packages in `hyperframes/node_modules` (`npm ci` in `hyperframes/`).
- ffmpeg/ffprobe (this machine: `~/.local/bin/ffmpeg`, 7.0.2 static).
- Chrome for Testing 151 from Playwright's cache (`~/.cache/ms-playwright/chromium-1234`, `chromium_headless_shell-1234`).
- `hyperframes/hf-env.sh` points HyperFrames at those binaries and turns off telemetry, update checks and auto-installs. Source it before any `hyperframes` command (the `tools/hf-lock.sh` wrapper does this for you).

## Render the master

```bash
cd video-production/hyperframes
npm run build      # docs + subtitles, root + caption track, scene packets, clip speed variants, asset manifest
npm run lint       # must report 0 errors
npm run render     # -> ../renders/setu-food-user-walkthrough.mp4 (60 fps, high quality, PNG frames for UI clips)
npm run qc         # -> ../reports/qc/: probe.json, black/freeze detection, contact sheets, pass/fail summary
```

`npm run render` runs `hyperframes render . -o ../renders/setu-food-user-walkthrough.mp4 --fps 60 --quality high --workers 4 --video-frame-format png --strict` through `tools/hf-lock.sh`, which limits concurrent headless Chromes and waits for free memory (this machine is shared). Lower `--workers` on a smaller machine.

## Edit something

- **Words, timing or captions:** edit `storyboard/scene-timing.json`, run `python3 storyboard/validate_storyboard.py`, then `npm run build` and re-render. Captions are drawn only by the generated caption track; a `\n` in a caption is the intended line break.
- **One scene's animation:** edit `hyperframes/compositions/sNN-*.html`, then preview just that scene:

  ```bash
  node tools/preview-scene.mjs s05                       # writes .preview/<sceneId>/ (scene + background + its captions)
  tools/hf-lock.sh hyperframes lint .preview/s05-delivery-spot
  tools/hf-lock.sh hyperframes snapshot .preview/s05-delivery-spot --at 0.5,2,4 -o .preview/s05-delivery-spot/snaps
  ```

  Keep the first and last frame equal to the scene's `handoffIn` / `handoffOut` in the storyboard, or the hard cut to the neighbouring scene will show.
- **Check every cut:** `npm run boundaries` writes side-by-side frames of each scene cut to `.qc/boundaries/`.
- **Studio preview:** `npx hyperframes preview` in `hyperframes/` opens the HyperFrames studio.

## Add the soundtrack later

The master is silent on purpose. `reports/sound-cue-sheet.md` lists timecoded cue suggestions (logo reveal, OTP entry, location confirmation, add to cart, checkout, payment choice, status changes, final brand frame). To lay a finished soundtrack under the picture without re-encoding the video:

```bash
ffmpeg -i renders/setu-food-user-walkthrough.mp4 -i soundtrack.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -shortest renders/setu-food-user-walkthrough-with-sound.mp4
```

## Honesty notes

- The one-time-code sign-in is the app's released email sign-in. For the capture, the code went to the isolated demo stack's local test inbox for the demo persona (no real inbox).
- Stalls, menu, persona, the payment QR and its UPI ID (`southside.demo@setudemo`, on a handle no bank or UPI app issues) are **demo data**; the demo QR is labelled in the capture itself and no money moved. The capture browser has no UPI app: 'Opening your UPI app…' is filmed right after the tap, and the return state is the app's own state for a phone that left for the UPI app.
- The video never claims that SETU delivers, offers pickup, tracks riders on a map, promises delivery times, is free, or guarantees hygiene, and it ends with the provider-responsibility disclaimer.

## Voice-over and sound-effects version

> **Needs a re-run after the November 2026 update.** `audio/voiceover-script.json` already has the new lines and timings (s03 and s09 rewritten, s04 'user account', s04–s08 1.5 s earlier). Run the three commands below on the machine that has the ElevenLabs key; `make_mix.py` now reads `renders/setu-food-user-walkthrough.mp4` and writes `renders/setu-food-user-walkthrough-voiceover.mp4`.


`renders/setu-food-customer-walkthrough-voiceover.mp4` (the earlier cut) was the master picture (stream copy, identical frames) with a voice-over and synthesized UI sound effects, mixed to −16 LUFS / −1.5 dBTP. The silent master is unchanged.

- **Voice:** a story script in `audio/voiceover-script.json` (34 lines in story order, each placed at the moment its action is on screen, at least 0.45 s of silence between lines; subtitles that match it: `audio/voiceover.srt`). `make_voice.py` uses the ElevenLabs voice `EaBs7G1VibMrNAuz2Na7` (`eleven_multilingual_v2`, neighbouring lines passed as context for a continuous read) when the key in `~/.config/elevenlabs/api_key` has the `text_to_speech` permission; otherwise it falls back to `en-IN-NeerjaExpressiveNeural` via `edge-tts` and says so. Edit the script, then re-run the three commands below.
- **Effects:** synthesized locally from `reports/sound-cue-sheet.md` (taps, ticks, typing timed to the real typing clips, whooshes, pops, chimes in E major). The placeholder music-pad cues are left for the owner's music.
- **Stems for the music edit:** `audio/stems/voice.wav`, `audio/stems/sfx.wav`, `audio/stems/voice-sfx.wav` (the finished mix).

```bash
cd video-production
PYTHONPATH=audio/.pylib python3 audio/make_voice.py   # needs: python3 -m pip install --target audio/.pylib --upgrade edge-tts==7.3.1
python3 audio/make_sfx.py
python3 audio/make_mix.py                              # -> renders/setu-food-user-walkthrough-voiceover.mp4
```
=======
# Video-Gen-With-Claude-X-HyperFreams
>>>>>>> 5a9cb4ed21f8a7f357b22e233551d6a6ab081c6d
