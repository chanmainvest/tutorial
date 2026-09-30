# Host characters — asset pack & rig plan

Cute cartoonish hosts for the Chanma Investment Tutorial videos, in one
unified modern anime-inspired style (clean cel shading, bold dark
outlines, large expressive eyes with highlight sparkles, soft blush,
flat color fills, warm cream background). Both hosts were drawn with the
same style anchor so they read as one show. Designed 2026-09-29.

## The hosts

- **Horace** (teacher): middle-aged East Asian man, gray-templed hair,
  round glasses, navy cardigan over white shirt. Warm, confident.
- **Stella** (student): young East Asian woman, high ponytail,
  mustard-yellow hoodie. Bright, eager, curious.

## Assets

All in `course/YouTube/assets/`:

| File | Use |
|---|---|
| `characters/horace_base.png` | Horace, neutral (mouth closed) |
| `characters/horace_mouth_half.png` | Horace, lips parted mid-word |
| `characters/horace_mouth_open.png` | Horace, mouth open speaking |
| `characters/horace_blink.png` | Horace, eyes closed (blink) |
| `characters/stella_base.png` | Stella, neutral (mouth closed) |
| `characters/stella_mouth_half.png` | Stella, lips parted mid-word |
| `characters/stella_mouth_open.png` | Stella, mouth open speaking |
| `characters/stella_blink.png` | Stella, eyes closed (blink) |
| `studio_background.png` | 16:9 cozy studio backdrop (bookshelf, plant, lamp) |

Variants were made as image-edits of the base portrait, so pose,
clothing, framing and background stay identical — only the mouth/eyes
change. To add new expressions later, edit the `_base` image the same way.

## Rig plan (Remotion)

Simple 2D "lip-flap" rig — no bone animation needed:

1. **Mouth movement** — swap between `base` / `mouth_half` / `mouth_open`
   per active speaker. Drive it from `week01_why_invest_transcript.json`:
   a word is being spoken inside its `[start, end]` window → cycle
   half → open → half at ~8–10 fps; outside any word → `base`.
   (Cheaper alternative: swap on audio amplitude buckets.)
2. **Blinks** — swap in `*_blink.png` for ~150 ms every 3–6 s (randomized),
   per character independently.
3. **Head movement** — procedural: gentle vertical bob (±6 px, sine ~0.5 Hz)
   while a character speaks; subtle tilt (±2°) on emphasis words.
   Apply to the whole sprite (head and body move as one — reads fine at
   this cartoon style).
4. **Body movement** — slow sway / scale "breathing" (±1.5% scale, ~4 s
   period) on both characters at all times; slight lean-in (translate
   toward center ~10 px) for the active speaker.
5. **Speaker focus** — dim/scale-down the listener slightly
   (brightness 0.85, scale 0.97) while the other speaks; swap on turn
   boundaries from the transcript's `speaker` field.
6. **Layout** — `studio_background.png` full-bleed 16:9; Horace left,
   Stella right; name captions optional.

## Making more characters / expressions

New expression = `media.generate_image` edit of the `<name>_base.png`
with prompt "Change only <feature>: <description>. Keep the exact same
character, face, pose, clothing, art style, framing and background —
everything else pixel-identical." Then drop the PNG into `characters/`
with the `<name>_<expression>.png` naming.

## Transparent cutouts

The portraits above have flat cream backgrounds. `make_cutouts.py`
(edge flood-fill + 1px edge tighten) produces `*_cutout.png` variants
with transparent backgrounds for compositing over the studio backdrop in
the Remotion video. Re-run it after any portrait redraw.
Implementation notes: PIL's `floodfill` must run on a grayscale copy of
the photo (it compares against the seed pixel's own value), and the fill
value must be far from the background luma — fill with 0, not 255,
because cream (~238) is within thresh of 255 and the fill then silently
no-ops.
