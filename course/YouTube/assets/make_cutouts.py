"""Remove the flat cream studio background from character portraits.

Flood-fills from the image edges with a tolerance, so only the
connected background region is removed (enclosed light areas like eye
sparkles are preserved). Then tightens the alpha edge by 1px to kill
the halo fringe.
"""
import sys
from PIL import Image, ImageDraw, ImageFilter

def cutout(src: str, dst: str, thresh: int = 42) -> None:
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    # Sample background color from corners
    corners = [img.getpixel((5, 5)), img.getpixel((w - 6, 5)),
               img.getpixel((5, h - 6)), img.getpixel((w - 6, h - 6))]
    bg = tuple(sum(c[i] for c in corners) // 4 for i in range(3))
    print(f"{src}: bg sample {bg}")

    # Flood fill on a grayscale copy of the SOURCE photo: floodfill fills
    # the connected region whose pixels are within `thresh` of the seed
    # pixel's own value (the cream background at the corners), so it must
    # run on the photo, not on a blank mask. Enclosed light areas (eye
    # sparkles) are untouched because they aren't connected to the edges.
    gray = img.convert("RGB").convert("L")
    # NOTE: fill with 0, not 255 — the cream background (luma ~238) is
    # within `thresh` of 255, which makes floodfill think the seed is
    # already filled and return immediately.
    filled = gray.copy()
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        ImageDraw.floodfill(filled, seed, 0, thresh=thresh)
    bg_mask = filled.point(lambda v: 255 if v == 0 else 0)
    # Guard against the fill leaking through a narrow gap into the
    # character: keep only filled pixels that are actually near the
    # background color.
    bg_luma = sum(corners[0][i] * w_ for i, w_ in
                  enumerate((0.299, 0.587, 0.114)))
    near_bg = gray.point(lambda v: 255 if abs(v - bg_luma) < thresh else 0)
    mask = Image.composite(bg_mask, Image.new("L", (w, h), 0), near_bg)
    # Invert: character = 255
    char_mask = Image.eval(mask, lambda v: 255 - v)
    # Tighten edge by 1px to remove halo
    char_mask = char_mask.filter(ImageFilter.MinFilter(3))

    r, g, b, _ = img.split()
    out = Image.merge("RGBA", (r, g, b, char_mask))
    # Crop to content bbox with small padding
    bbox = char_mask.getbbox()
    if bbox:
        pad = 8
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        out = out.crop(bbox)
    out.save(dst)
    print(f"  -> {dst} {out.size}")

if __name__ == "__main__":
    for name in ["horace_base", "horace_mouth_half", "horace_mouth_open",
                 "horace_blink", "stella_base", "stella_mouth_half",
                 "stella_mouth_open", "stella_blink"]:
        cutout(f"characters/{name}.png", f"characters/{name}_cutout.png")
