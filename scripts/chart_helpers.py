"""Shared helpers for the tutorial's procedural matplotlib chart scripts.

Every chart-generation script under course/image/ should import the
`apply_cjk_font`, `palette`, and `save_localized_png` helpers from this
module so the four-locale PNG family (en/hk/tw/cn) is rendered with a
consistent style.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

import matplotlib
import matplotlib.pyplot as plt


CJK_FONTS = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC", "PingFang SC",
    "Noto Sans CJK TC", "Noto Sans CJK SC", "SimHei", "Arial Unicode MS",
    "DejaVu Sans",
]

# Site palette — light cream + deep navy, gold accent.
PALETTE_LIGHT = {
    "bg":       "#fdfbf5",
    "fg":       "#1a2332",
    "muted":    "#6b7280",
    "grid":     "#d6d3c4",
    "accent":   "#b8860b",
    "red":      "#b71c1c",
    "blue":     "#0d47a1",
    "green":    "#2e7d32",
    "purple":   "#6a1b9a",
    "orange":   "#e65100",
    "teal":     "#00695c",
    "grey":     "#5a5a5a",
}

LOCALES: tuple[str, ...] = ("en", "hk", "tw", "cn")


def apply_cjk_font() -> None:
    """Configure matplotlib to use a CJK-capable font with English fallback."""
    matplotlib.rcParams["font.sans-serif"] = list(CJK_FONTS)
    matplotlib.rcParams["axes.unicode_minus"] = False


def style_axes(ax, palette: dict | None = None) -> None:
    """Apply cream-and-navy site styling to a matplotlib Axes."""
    p = palette or PALETTE_LIGHT
    ax.set_facecolor(p["bg"])
    ax.figure.set_facecolor(p["bg"])
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(p["muted"])
    ax.tick_params(colors=p["fg"], labelsize=9)
    ax.xaxis.label.set_color(p["fg"])
    ax.yaxis.label.set_color(p["fg"])
    ax.title.set_color(p["fg"])
    ax.grid(True, which="major", color=p["grid"], linewidth=0.6, alpha=0.7)


def save_localized_png(
    fig,
    base: str,
    lang: str,
    out_dir: Path | str,
    dpi: int = 160,
) -> Path:
    """Save the figure as <base>_<lang>.png under out_dir.

    Also writes the canonical <base>.png copy when lang == 'en' so the
    markdown image reference (`image/<base>.png`) resolves with the
    English version as the default.
    """
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    p = out / f"{base}_{lang}.png"
    fig.savefig(p, dpi=dpi, bbox_inches="tight", facecolor=fig.get_facecolor())
    if lang == "en":
        canon = out / f"{base}.png"
        fig.savefig(canon, dpi=dpi, bbox_inches="tight", facecolor=fig.get_facecolor())
    return p


def render_for_all_locales(
    base: str,
    out_dir: Path | str,
    build_fig,            # callable (lang_strings) -> matplotlib.Figure
    lang_strings: dict,   # { "en": {...}, "hk": {...}, ... }
    dpi: int = 160,
) -> list[Path]:
    """Iterate locales, build a fresh figure for each, and write the PNGs."""
    apply_cjk_font()
    paths: list[Path] = []
    for lang in LOCALES:
        if lang not in lang_strings:
            continue
        fig = build_fig(lang_strings[lang])
        paths.append(save_localized_png(fig, base, lang, out_dir, dpi=dpi))
        plt.close(fig)
    return paths
