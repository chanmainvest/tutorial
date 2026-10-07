# Chanma Podcast Video (Remotion)

Talking-head video for the Chanma Investment Tutorial podcast, built with
[Remotion](https://www.remotion.dev). The video is driven by the word-level
transcript JSON, so mouth movement, captions, and timing all follow the
actual audio.

## Layout

```
course/YouTube/
  week01_why_invest.mp3              # episode audio (imported, not copied)
  week01_why_invest_transcript.json  # word-level timing (imported)
  assets/
    studio_background.png            # 16:9 studio backdrop
    characters/
      horace_{base,mouth_half,mouth_open,blink}.png   # portraits (cream bg)
      stella_{base,mouth_half,mouth_open,blink}.png
      horace_body.png, horace_head_{base,mouth_half,mouth_open,blink}.png
      stella_body.png, stella_head_{...}.png, stella_ponytail.png  # rig layers
  remotion/                          # this project
    src/
      Root.tsx        # compositions: Week01 (full), Week01Preview (10s)
      PodcastVideo.tsx# scene: background, hosts, captions, title, audio
      Character.tsx   # the layered rig (static body, neck-pivot head, tail)
      transcript.ts   # timing helpers
```

Assets are imported via relative paths — no duplication into `public/`.

## The rig (`Character.tsx`)

Layered sprites (built by `assets/make_rig.py`, all 1600×1600 and
pixel-aligned): a **body** layer that never moves, a **head** layer
that pivots at the neck, and for Stella a **ponytail** layer nested
inside the head group. (The previous whole-portrait bob made the whole
body — name tag included — wobble.)

- **Mouth**: driven by the real voice — a per-frame RMS loudness
  envelope is precomputed offline from the mp3
  (`week01_loudness_envelope.json`; thresholds calibrated from the
  actual audio) and picks the head sprite (closed / `mouth_half` /
  `mouth_open`). Gated on the transcript's speaker turns, so only the
  active speaker's mouth moves; pauses read as a closed mouth.
- **Blink**: every ~3.5–5.5 s (deterministic per host, so they don't
  blink in sync), 4 frames of the `blink` head sprite — allowed while
  speaking, just not mid wide-open mouth.
- **Head**: while speaking, gentle nods pivoting at the neck (±~1.7°
  + a few px bob, amplitude scaled by loudness); while listening,
  a barely-there idle sway. The body and name pill never move.
- **Ponytail**: pendulum sway lagging the head nod (plus a soft idle
  sway), pivoting at the hair tie.
- **Focus**: the listener dims (`brightness(0.8) saturate(0.9)`).
  While a diagram is on screen, both hosts shrink to 85% and slide
  ±130 px apart, leaving the center to the chart.
- **Name pills** under each host (static); **captions** show one line
  at a time (transcript lines chunked on word boundaries: ≤7 words /
  ≤44 chars) in a bottom-center bar; an **intro title** fades in/out
  over the first 4.5 s.

## Diagrams (`Diagrams.tsx`)

Animated SVG overlays timed to the transcript, for visual learning:

- the four `[ANIMATION:]` cues from the YouTube script — the textbook
  chart draws then cracks into a jagged real chart with crash labels;
  Rule-of-72 doubling bars; the inflation treadmill (cash / bonds /
  stocks runners); the outro card —
- plus the CPI "three games" cards, M2 money-supply lines with the 2020
  jump, the cash-vs-T-bills-vs-stocks 55-year bars (morphing from
  nominal to 1971 purchasing power), and the three-takeaways cards.

To retime or add a diagram, edit `DIAGRAM_TIMELINE` and add a component.

## Commands

```bash
cd course/YouTube/remotion
npm install              # once

npm run start            # Remotion Studio — scrub the timeline in the browser

npm run render:preview   # 10 s test render -> out/preview.mp4
npm run render:week01    # full 12 min episode -> out/week01_why_invest_video.mp4
```

The first render downloads a headless Chromium (~150 MB); subsequent
renders reuse it.

### Rendering on this VM (not needed on your own machine)

Two environment quirks, both worked around outside the repo so the
project stays portable:

1. **Browser download**: Remotion's Node-based Chromium downloader stalls
   behind this VM's egress proxy (curl works fine). The official
   `chrome-headless-shell` is pre-fetched at
   `~/workspace/bin/chrome-headless-shell-linux64/chrome-headless-shell`
   — pass it explicitly:
   ```bash
   npx remotion render Week01 --browser-executable=$HOME/workspace/bin/chrome-headless-shell-linux64/chrome-headless-shell
   ```
   (`~/workspace/bin/remotion-shell.sh` wraps it with `--no-sandbox`,
   needed because we run as root.)
2. **Memory**: this VM has ~2 GB free RAM and the render browser OOMs on
   long sequences (`remotion still` works, full renders die). Render the
   full episode on a machine with headroom — the composition is verified
   via stills in `previews/`.

## Adding a new episode

1. Produce `weekNN_....mp3` + `weekNN_..._transcript.json` (see
   `course/YouTube/PODCAST.md`).
2. In `src/Root.tsx`, copy the `week01Props` block with the new files and
   add a `Composition` for it. The hosts, rig, and layout are reused
   unchanged.

## Regenerating character cutouts

If a host portrait is redrawn, rebuild the transparent cutouts:

```bash
cd course/YouTube/assets
python3 make_cutouts.py   # *_cutout.png from the cream-background originals
```

## Ideas for later (not built yet)

- Word-by-word caption highlighting (karaoke style) using `words[]`.
- Slide overlays: key charts/numbers from the lesson shown beside the hosts.
- Per-line camera emphasis (slight zoom on the active speaker).
