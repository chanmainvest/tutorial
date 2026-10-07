# Host characters — asset pack & rig plan

Cute cartoonish hosts for the Chanma Investment Tutorial videos, in one
unified modern anime-inspired style (clean cel shading, bold dark
outlines, large expressive eyes with highlight sparkles, soft blush,
flat color fills, warm cream background). Both hosts were drawn with the
same style anchor so they read as one show. Designed 2026-09-29.

## The hosts

- **Horace** (teacher): middle-aged East Asian man, all-black hair
  (redesigned 2026-10-06: no more gray temples), sporty Oakley-style
  glasses with a black frame, black turtleneck like Steve Jobs.
  Warm, confident.
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

## Rig (Remotion) — layered, head separate from body

`make_rig.py` splits each portrait into pixel-aligned 1600×1600
layers (same flood-fill alpha as the cutouts, no bbox crop):

| File | Use |
|---|---|
| `characters/<name>_body.png` | Torso only (head erased; collar/hood hides the seam). Never moves. |
| `characters/<name>_head_<variant>.png` | Head only, 4 mouth/blink variants, extends ~50 px past the split for overlap |
| `characters/stella_ponytail.png` | Stella's ponytail as its own layer (dilated ~24 px under the head so the seam never opens) |

Pivots (1600-canvas px): Horace neck (795, 950) — the turtleneck
collar makes the seam invisible; Stella neck (770, 985), ponytail
tie (865, 155). Stella's body layer has the ponytail region erased
and the shoulder patched with a local-average fill.

Motion (see `remotion/src/Character.tsx`):

1. **Mouth** — head sprite swaps base/half/open from the precomputed
   per-frame loudness envelope of the real audio, gated on speaker
   turns.
2. **Head** — only the head moves: gentle nods/tilts pivoting at the
   neck while speaking, amplitude scaled by loudness; near-still
   idle sway while listening. Body and name pill never move.
3. **Ponytail** — nested in the head group (inherits head motion)
   plus its own lagged pendulum sway at the tie.
4. **Blinks** — blink head sprite ~130 ms every ~3.5–5.5 s per host,
   speaking or not (skipped only mid wide-open mouth).
5. **Focus** — listener dims; hosts shrink to 85% while a diagram
   is on screen.

## Making more characters / expressions

New expression = `media.generate_image` edit of the `<name>_base.png`
with prompt "Change only <feature>: <description>. Keep the exact same
character, face, pose, clothing, art style, framing and background —
everything else pixel-identical." Then drop the PNG into `characters/`
with the `<name>_<expression>.png` naming.

## Transparent cutouts

The portraits above have flat cream backgrounds. `make_cutouts.py`
(edge flood-fill + 1px edge tighten) produces `*_cutout.png` variants
with transparent backgrounds. (The Remotion video itself now
composites the `make_rig.py` layers above instead; the cutouts remain
handy for thumbnails/stills.) Re-run after any portrait redraw.
Implementation notes: PIL's `floodfill` must run on a grayscale copy of
the photo (it compares against the seed pixel's own value), and the fill
value must be far from the background luma — fill with 0, not 255,
because cream (~238) is within thresh of 255 and the fill then silently
no-ops.
