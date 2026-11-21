# Video-Gen-With-Claude-X-HyperFreams

Automated, code-driven video production pipeline powered by **Claude** and **HyperFrames** (HTML/CSS/GSAP) to generate a cinematic, 60 fps walkthrough video (**"SETU Food — User Walkthrough"**) for the IIT Kharagpur campus food delivery platform.

- **Master Output:** `renders/setu-food-user-walkthrough.mp4` — 1920×1080, 60 fps, H.264 (`yuv420p`), **silent master** (soundtrack mixed separately). *(Prior cut retained as `renders/setu-food-customer-walkthrough.mp4`.)*
- **Narrative ("Dinner at B-212"):** Follows Aarav (Nehru Hall of Residence, Room B-212) signing in via email OTP, completing User onboarding, selecting an eligible campus delivery zone, ordering a Masala Dosa and two Filter Coffees from Southside Tiffins (₹140 food + ₹10 stall delivery = ₹150), paying via Cash or UPI hand-off, tracking the order, verifying the 6-digit handover code, and leaving a review.
- **100% Real App Captures:** Every UI screen is captured via Playwright against an isolated demo stack using sample stalls, demo personas, a labelled demo QR (`southside.demo@setudemo`), and a local test inbox—without modifying the core `client/` or `server/` codebases.

---

## Option 1: AI-Assisted Workflow (Claude Cowork / Claude Code / Codespace + HyperFrames MCP)

You can generate, edit, and preview scenes directly using natural-language prompts by linking this repository to Claude with the **HyperFrames MCP server**:

### 1. Open the Project Folder
- **Claude Cowork / Claude Desktop:** Open the **Cowork** tab (or Claude Code) and select this cloned repository folder (`Video-Gen-With-Claude-X-HyperFreams/`) as your active workspace directory.
- **GitHub Codespaces / VS Code:** Open the repo in a Codespace or local VS Code with Claude Code installed, and navigate to the project root.

### 2. Connect the HyperFrames MCP Server
Add the HyperFrames MCP server to your Claude / MCP configuration so Claude can inspect compositions, lint timelines, and capture preview snapshots directly:

```json
{
  "mcpServers": {
    "hyperframes": {
      "command": "npx",
      "args": ["-y", "hyperframes", "mcp"]
    }
  }
}
```
*(In Claude Desktop / Cowork, add this via **Settings → Developer → Edit Config**, or run `claude mcp add hyperframes -- npx -y hyperframes mcp` in Claude Code.)*

### 3. Prompt Claude to Build or Edit Scenes
Once the folder and HyperFrames MCP are connected, give Claude your creative or technical prompt referencing the project's source-of-truth files:

> **Example Prompt:**
> *"Read `storyboard/scene-timing.json` and `hyperframes/STYLE.md`. Create/update scene `s05` in `hyperframes/compositions/` using GSAP animations that match `handoffIn` and `handoffOut`, then lint and snapshot the scene via the HyperFrames MCP."*

---

## Option 2: Manual / CLI Pipeline

### Architecture & Workflow
1. **Single Source of Truth (`storyboard/scene-timing.json`):** Defines all 12 scenes, exact durations, narration, captions, time-coded GSAP animation specs, and scene-boundary handoff contracts (`handoffIn` / `handoffOut`).
2. **Automated Validation (`storyboard/validate_storyboard.py`):** Enforces timing math, caption line-break rules, asset existence, boundary continuity, and copy compliance (e.g., rejecting legacy `"customer"` terminology in favor of `"User"`).
3. **HTML/GSAP Compositions (`hyperframes/compositions/`):** Modular scene animations built with HyperFrames (`0.8.143`) and GSAP (`3.13.0`), compiled into `hyperframes/index.html` with a synchronized burned-in caption track (`captions.html`).
4. **Deterministic Headless Render & QC:** Renders frame-accurate PNG sequences via headless Chromium into 60 fps H.264 video, followed by automated black-frame, freeze-frame, and scene-cut boundary checks.

---

## Repository Map

| Path | Description |
| :--- | :--- |
| `storyboard/scene-timing.json` | **Source of truth:** 12 scenes with timing, captions, animation specs, handoff contracts, and sound cues |
| `storyboard/script.md`, `storyboard/storyboard.md` | Human-readable script and storyboard auto-generated from the JSON |
| `storyboard/layout.json` | Per-scene caption positioning rules |
| `storyboard/validate_storyboard.py` | Pre-build validator checking timing, captions, handoffs, and terminology |
| `captions/` | Timed `narration.txt`, `subtitles.srt`, and `subtitles.vtt` |
| `hyperframes/` | Core HyperFrames + GSAP animation project |
| `hyperframes/compositions/sNN-*.html` | Individual scene compositions + `captions.html` burned-in subtitle track |
| `hyperframes/index.html` | Auto-generated root timeline assembling background, scenes, and captions |
| `hyperframes/assets/` | UI captures (`ui/`), typing/scroll clips (`clips/`), fonts, motion kit (`js/kit.js`, `css/kit.css`), and campus boundary data |
| `hyperframes/STYLE.md` | Visual & motion design system (grid, typography, colors, honesty rules) |
| `hyperframes/tools/` | Build, preview, render, boundary-check, and QC automation scripts |
| `capture/` | Playwright capture scripts and isolated demo-stack helpers |
| `reports/` | Asset manifests, sound cue sheet (`sound-cue-sheet.md`), capture logs, and QC outputs |
| `renders/` | Rendered video outputs (excluded from Git via `.gitignore`) |

---

## November 2026 Cut Updates (1:58.85)

1. **Customer → User Terminology:** Updated UI captures, captions, narration, and end-card disclaimers to use *User account* (`validate_storyboard.py` blocks `"customer"` in on-screen text).
2. **Email One-Time-Code Sign-In (Scene 3):** Updated to the released email OTP flow (`Email me a one-time code instead` → 6-digit code → `Verify and continue`), trimming Scene 3 by `1.5s`.
3. **UPI Hand-Off Flow (Scenes 8–9):** Added `"Pay online via UPI"` at checkout and an editorial callout branch for the external UPI app hand-off (`Pay ₹150 in your UPI app` → `Seller is checking your payment` → `Order confirmed`), extending Scene 9 by `1.5s`.

---

## Prerequisites

- **Node.js 22+** (`npm ci` inside `hyperframes/`)
- **Python 3** (for storyboard validation)
- **FFmpeg / FFprobe 7.0+** (configured at `~/.local/bin/ffmpeg`)
- **Playwright Chromium** (`~/.cache/ms-playwright/chromium-1234`)
- **Environment Wrapper:** `hyperframes/hf-env.sh` and `tools/hf-lock.sh` configure binary paths, disable telemetry, and throttle concurrent headless Chromium workers.

---

## Build, Render & Quality Control

Run the full pipeline from the `hyperframes/` directory:

```bash
cd hyperframes

npm run build      # Generate docs, subtitles, root timeline, caption track & asset manifest
npm run lint       # Validate HyperFrames compositions (must pass with 0 errors)
npm run render     # Render 1080p 60fps master -> ../renders/setu-food-user-walkthrough.mp4
npm run qc         # Run ffprobe, black/freeze frame detection & contact sheets -> ../reports/qc/
```

---

## Editing & Previewing Scenes

- **Update Copy, Timing, or Captions:**
  1. Edit `storyboard/scene-timing.json`.
  2. Run `python3 storyboard/validate_storyboard.py`.
  3. Run `npm run build && npm run render` inside `hyperframes/`.
- **Preview a Single Scene:**
  ```bash
  node tools/preview-scene.mjs s05
  tools/hf-lock.sh hyperframes lint .preview/s05-delivery-spot
  tools/hf-lock.sh hyperframes snapshot .preview/s05-delivery-spot --at 0.5,2,4 -o .preview/s05-delivery-spot/snaps
  ```
  *(Ensure the first and last frames match `handoffIn` and `handoffOut` to keep scene cuts seamless.)*
- **Inspect Scene Transitions:** Run `npm run boundaries` to export side-by-side cut frames to `.qc/boundaries/`.
- **Interactive Studio:** Run `npx hyperframes preview` inside `hyperframes/`.

---

## Mixing the Soundtrack

Use the timecoded cues in `reports/sound-cue-sheet.md` to prepare your audio track, then mux it onto the silent master without re-encoding the video stream:

```bash
ffmpeg -i renders/setu-food-user-walkthrough.mp4 -i soundtrack.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -shortest \
  renders/setu-food-user-walkthrough-with-sound.mp4
```

---

## Demo & Honesty Notes

- All stalls, menu items, user personas, email OTP inbox captures, and payment QR codes (`southside.demo@setudemo`) were recorded in an isolated demo environment with no real financial transactions or external UPI app rendering.
