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
      horace_{base,mouth_half,mouth_open,blink}_cutout.png
      stella_{base,mouth_half,mouth_open,blink}_cutout.png
  remotion/                          # this project
    src/
      Root.tsx        # compositions: Week01 (full), Week01Preview (10s)
      PodcastVideo.tsx# scene: background, hosts, captions, title, audio
      Character.tsx   # the rig (mouth, blink, bob, lean, dimming)
      transcript.ts   # timing helpers
```

Assets are imported via relative paths — no duplication into `public/`.

## The rig (`Character.tsx`)

- **Mouth**: while one of the host's *words* is sounding (word-level windows
  from the transcript), the mouth alternates `mouth_half` / `mouth_open`
  at ~12 fps. Between words it rests on `base`.
- **Blink**: every 4–7 s (deterministic per host, so it doesn't look synced),
  5 frames of the `blink` variant — never while a word is sounding.
- **Head/body**: the active speaker bobs (±7 px @ 1.4 Hz) and tilts
  (±1.6°); both hosts breathe continuously (±0.8% scale @ 0.25 Hz).
- **Focus**: the active speaker leans 14 px toward center and scales up
  slightly; the listener dims (`brightness(0.8) saturate(0.9)`).
- **Name pills** under each host; **captions** show the current line's text
  in a bottom-center bar; an **intro title** fades in/out over the first
  4.5 s.

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
