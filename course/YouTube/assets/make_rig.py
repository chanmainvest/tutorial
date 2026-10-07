"""Split character portraits into rig layers for the Remotion video.

Produces, per character (1600x1600 RGBA, pixel-aligned):
  <name>_body.png        torso only (head region erased; the collar/hood
                         hides the seam), plus for Stella the ponytail
                         region erased and the shoulder patched
  <name>_head_<variant>.png  head only, extending ~50px past the split
                         line so it overlaps the body (no gap when the
                         head rotates around the neck pivot)
  stella_ponytail.png    Stella's ponytail as its own layer so it can
                         sway on its own pivot at the hair tie

Geometry (1600-canvas px), measured from the portraits:
  Horace: split y=920/995 (body erase / head bottom), pivot (795, 950).
          The black turtleneck collar makes the seam invisible.
  Stella: split y=960/1010, head pivot (770, 985), ponytail pivot
          (865, 155). Ponytail = everything right of a boundary curve
          that follows the tail's left edge, plus the knot at the tie.

Run after make_cutouts.py inputs exist (uses the raw portraits +
the same flood-fill alpha as make_cutouts.cutout, minus the crop).
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

THRESH = 42


def alpha_of(path: str) -> Image.Image:
    """Character alpha mask (L, 1600x1600) via edge flood fill."""
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    corners = [img.getpixel((5, 5)), img.getpixel((w - 6, 5)),
               img.getpixel((5, h - 6)), img.getpixel((w - 6, h - 6))]
    gray = img.convert("RGB").convert("L")
    filled = gray.copy()
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        ImageDraw.floodfill(filled, seed, 0, thresh=THRESH)
    bg_mask = filled.point(lambda v: 255 if v == 0 else 0)
    bg_luma = sum(corners[0][i] * wgt for i, wgt in
                  enumerate((0.299, 0.587, 0.114)))
    near_bg = gray.point(lambda v: 255 if abs(v - bg_luma) < THRESH else 0)
    mask = Image.composite(bg_mask, Image.new("L", (w, h), 0), near_bg)
    char_mask = Image.eval(mask, lambda v: 255 - v)
    return char_mask.filter(ImageFilter.MinFilter(3))


def layer(img: Image.Image, keep: np.ndarray) -> Image.Image:
    """RGBA image keeping only pixels where keep is True (feathered)."""
    m = Image.fromarray((keep * 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(1.2))
    a = np.minimum(np.array(img)[:, :, 3], np.array(m))
    out = img.copy()
    out.putalpha(Image.fromarray(a.astype(np.uint8)))
    return out


def rowsplit(h: int, w: int, y: int) -> np.ndarray:
    k = np.zeros((h, w), dtype=bool)
    k[:y, :] = True
    return k


# ---------------------------------------------------------------- Horace
def build_horace() -> None:
    BODY_ERASE_Y = 920   # body keeps y >= this
    HEAD_BOTTOM_Y = 995  # head keeps y <= this (overlap band hides seam)
    for variant in ("base", "mouth_half", "mouth_open", "blink"):
        src = Image.open(f"characters/horace_{variant}.png").convert("RGBA")
        src.putalpha(alpha_of(f"characters/horace_{variant}.png"))
        h, w = 1600, 1600
        if variant == "base":
            body = layer(src, ~rowsplit(h, w, BODY_ERASE_Y))
            body.save("characters/horace_body.png")
            print("horace_body.png")
        head = layer(src, rowsplit(h, w, HEAD_BOTTOM_Y))
        head.save(f"characters/horace_head_{variant}.png")
        print(f"horace_head_{variant}.png")


# ----------------------------------------------------------------- Stella
# Ponytail boundary: x of the tail's left edge per y (1600-canvas px).
TAIL_PTS = [(60, 905), (250, 965), (400, 1045), (550, 1100), (700, 1150),
            (850, 1205), (1000, 1260), (1150, 1330), (1300, 1405)]
KNOT = (880, 150, 115)  # (x, y, r) hair-tie knot, kept in head AND tail


def tail_mask(h: int, w: int) -> np.ndarray:
    ys = np.array([p[0] for p in TAIL_PTS], dtype=float)
    xs = np.array([p[1] for p in TAIL_PTS], dtype=float)
    yy, xx = np.mgrid[0:h, 0:w]
    edge = np.interp(yy[:, 0], ys, xs)
    m = xx > edge[:, None]
    # The tail ends at the tips (~y 1250); without this cutoff the
    # clamped interp edge would keep eating the torso's right side
    # all the way to the bottom of the canvas.
    m &= yy <= 1310
    knot = (xx - KNOT[0]) ** 2 + (yy - KNOT[1]) ** 2 < KNOT[2] ** 2
    return m | knot


def build_stella() -> None:
    BODY_ERASE_Y = 960
    HEAD_BOTTOM_Y = 1010
    h = w = 1600
    tail = tail_mask(h, w)
    # The tail layer sits UNDER the head, so dilate it ~16px into the
    # head's side of the boundary: the overlap band keeps the seam
    # covered when the tail sways relative to the head. Only dilate in
    # the head zone (y < 1000) — lower down the boundary's left side is
    # hoodie fabric, which must not join the tail layer.
    tail_dil = np.array(
        Image.fromarray((tail * 255).astype(np.uint8)).filter(
            ImageFilter.MaxFilter(49))) > 0
    head_zone = rowsplit(h, w, 1000)
    tail_under = tail | (tail_dil & head_zone)
    for variant in ("base", "mouth_half", "mouth_open", "blink"):
        src = Image.open(f"characters/stella_{variant}.png").convert("RGBA")
        src.putalpha(alpha_of(f"characters/stella_{variant}.png"))
        if variant == "base":
            # ponytail layer
            tail_img = layer(src, tail_under)
            tail_img.save("characters/stella_ponytail.png")
            print("stella_ponytail.png")
            # body: below split line, minus tail; patch the shoulder
            # where the tail hung in front of the hoodie with a smooth
            # local-average fill (no stripes).
            arr = np.array(src)
            body_keep = ~rowsplit(h, w, BODY_ERASE_Y) & ~tail
            body = layer(src, body_keep)
            ba = np.array(body).astype(np.float64)
            solid = (ba[:, :, 3] > 30).astype(np.float64)
            erased = tail & (arr[:, :, 3] > 30) & \
                ~rowsplit(h, w, BODY_ERASE_Y) & (solid < 0.5)
            if erased.any():
                num = np.zeros_like(ba[:, :, :3])
                den = np.zeros((h, w, 1))
                for c in range(3):
                    num[:, :, c] = ba[:, :, c] * solid
                num_img = Image.fromarray(
                    (np.clip(num, 0, 255)).astype(np.uint8))
                den_img = Image.fromarray(
                    (solid * 255).astype(np.uint8))
                blur = ImageFilter.GaussianBlur(45)
                num_b = np.array(num_img.filter(blur)).astype(np.float64)
                den_b = np.array(den_img.filter(blur)).astype(np.float64) / 255.0
                fill = num_b / np.maximum(den_b[:, :, None], 1e-6)
                ba[erased, :3] = fill[erased]
                ba[erased, 3] = 255
            Image.fromarray(ba.astype(np.uint8)).save(
                "characters/stella_body.png")
            print("stella_body.png")
        head = layer(src, rowsplit(h, w, HEAD_BOTTOM_Y) & ~tail)
        # keep the knot in the head too, so no gap opens at the tie
        yy, xx = np.mgrid[0:h, 0:w]
        knot = (xx - KNOT[0]) ** 2 + (yy - KNOT[1]) ** 2 < KNOT[2] ** 2
        head2 = layer(src, (rowsplit(h, w, HEAD_BOTTOM_Y) & ~tail) | knot)
        head2.save(f"characters/stella_head_{variant}.png")
        print(f"stella_head_{variant}.png")


if __name__ == "__main__":
    build_horace()
    build_stella()
