"""Week 16, §2.3 — Heatmap of yearly returns by SPDR sector ETF, 2010-2024.

Each cell is the calendar-year total return for that sector's SPDR ETF.
Color is rank within the year: deepest green = year's best sector,
deepest red = year's worst. Numbers in cells are the actual percent.

Returns are publicly-available approximate annual total returns from
SPDR sector ETF factsheets (rounded to one decimal). XLRE began
trading in October 2015 (carved out of XLF); XLC began in June 2018
(carved out of XLK and XLY). Pre-launch cells are blank.

Run:
    uv run python course/image/week16_sector_winners.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week16_sector_winners"

# ---------------------------------------------------------------------------
# Annual total returns (%), SPDR sector ETFs + SPY, 2010-2024.
# Source: SPDR / SSGA factsheets and public total-return calculators.
# Values rounded to one decimal. None = ETF not yet launched in that year.
# ---------------------------------------------------------------------------
YEARS = list(range(2010, 2025))

SECTORS = ["XLY", "XLC", "XLK", "XLI", "XLF", "XLB", "XLE",
           "XLRE", "XLV", "XLP", "XLU"]   # cyclical -> defensive top to bottom

# year -> dict of {ticker: pct return}
RETURNS: dict[int, dict[str, float | None]] = {
    2010: {"XLY": 27.7, "XLP": 14.1, "XLE": 21.7, "XLF": 12.0, "XLV": 4.4,
           "XLI": 26.8, "XLB": 22.5, "XLRE": None, "XLK": 11.7,
           "XLC": None, "XLU": 5.6,  "SPY": 15.1},
    2011: {"XLY": 6.1,  "XLP": 14.0, "XLE": 2.8,  "XLF": -17.3, "XLV": 12.7,
           "XLI": -0.6, "XLB": -9.7, "XLRE": None, "XLK": 2.6,
           "XLC": None, "XLU": 19.9, "SPY": 2.1},
    2012: {"XLY": 23.9, "XLP": 10.8, "XLE": 4.8,  "XLF": 28.8, "XLV": 17.9,
           "XLI": 15.4, "XLB": 15.0, "XLRE": None, "XLK": 14.8,
           "XLC": None, "XLU": 1.3,  "SPY": 16.0},
    2013: {"XLY": 43.1, "XLP": 26.1, "XLE": 25.1, "XLF": 35.5, "XLV": 41.4,
           "XLI": 40.6, "XLB": 25.6, "XLRE": None, "XLK": 26.2,
           "XLC": None, "XLU": 13.2, "SPY": 32.3},
    2014: {"XLY": 9.7,  "XLP": 16.0, "XLE": -8.7, "XLF": 15.0, "XLV": 25.3,
           "XLI": 9.8,  "XLB": 7.4,  "XLRE": None, "XLK": 17.9,
           "XLC": None, "XLU": 28.7, "SPY": 13.5},
    2015: {"XLY": 10.0, "XLP": 6.9,  "XLE": -21.5,"XLF": -1.5, "XLV": 6.9,
           "XLI": -4.0, "XLB": -8.3, "XLRE": 2.5, "XLK": 5.5,
           "XLC": None, "XLU": -4.8, "SPY": 1.4},
    2016: {"XLY": 6.0,  "XLP": 5.4,  "XLE": 27.4, "XLF": 22.8, "XLV": -2.7,
           "XLI": 18.9, "XLB": 16.7, "XLRE": 6.6, "XLK": 14.8,
           "XLC": None, "XLU": 16.3, "SPY": 12.0},
    2017: {"XLY": 22.9, "XLP": 13.5, "XLE": -1.0, "XLF": 22.2, "XLV": 22.1,
           "XLI": 23.3, "XLB": 23.8, "XLRE": 10.8, "XLK": 33.9,
           "XLC": None, "XLU": 12.1, "SPY": 21.7},
    2018: {"XLY": 0.1,  "XLP": -8.4, "XLE": -18.2,"XLF": -13.0, "XLV": 6.5,
           "XLI": -13.3,"XLB": -14.7,"XLRE": -2.0, "XLK": -1.6,
           "XLC": -16.0,"XLU": 4.1,  "SPY": -4.6},
    2019: {"XLY": 27.9, "XLP": 27.6, "XLE": 11.8, "XLF": 32.1, "XLV": 20.5,
           "XLI": 29.4, "XLB": 24.6, "XLRE": 29.0, "XLK": 50.3,
           "XLC": 32.7, "XLU": 26.4, "SPY": 31.2},
    2020: {"XLY": 33.3, "XLP": 10.1, "XLE": -32.6,"XLF": -1.7, "XLV": 13.5,
           "XLI": 10.9, "XLB": 20.5, "XLRE": -2.2, "XLK": 43.6,
           "XLC": 26.9, "XLU": 0.5,  "SPY": 18.4},
    2021: {"XLY": 24.4, "XLP": 18.6, "XLE": 53.3, "XLF": 35.0, "XLV": 26.0,
           "XLI": 21.1, "XLB": 27.3, "XLRE": 46.2, "XLK": 34.5,
           "XLC": 15.6, "XLU": 17.7, "SPY": 28.7},
    2022: {"XLY": -36.2,"XLP": -0.6, "XLE": 64.2, "XLF": -10.5,"XLV": -1.9,
           "XLI": -5.5, "XLB": -12.3,"XLRE": -26.2,"XLK": -27.7,
           "XLC": -37.6,"XLU": 1.6,  "SPY": -18.2},
    2023: {"XLY": 42.4, "XLP": 0.5,  "XLE": -1.3, "XLF": 12.0, "XLV": 2.1,
           "XLI": 18.1, "XLB": 12.6, "XLRE": 12.3, "XLK": 56.1,
           "XLC": 55.8, "XLU": -7.1, "SPY": 26.2},
    2024: {"XLY": 30.1, "XLP": 14.6, "XLE": 5.7,  "XLF": 30.6, "XLV": 2.6,
           "XLI": 17.5, "XLB": 0.0,  "XLRE": 5.2,  "XLK": 21.6,
           "XLC": 38.9, "XLU": 23.4, "SPY": 25.0},
}

LANG_STRINGS = {
    "en": {
        "title":    "SPDR sector ETFs — annual total return, 2010-2024",
        "subtitle": "Each cell shaded by rank within that year (green = best, red = worst). The cycle map is a tendency; the catalysts are the year.",
        "spy":      "SPY",
        "footer":   "Source: SPDR factsheets, public total-return data. XLRE launched Oct 2015 (carved from XLF); XLC launched Jun 2018 (carved from XLK + XLY).",
    },
    "hk": {
        "title":    "SPDR 行業 ETF — 年度總回報,2010-2024",
        "subtitle": "每格依該年內排名上色(綠=最佳、紅=最差)。週期地圖是趨勢,但催化劑才是當年主題。",
        "spy":      "SPY",
        "footer":   "資料:SPDR 簡介、公開總回報資料。XLRE 於 2015 年 10 月推出(從 XLF 拆出);XLC 於 2018 年 6 月推出(從 XLK + XLY 拆出)。",
    },
    "tw": {
        "title":    "SPDR 行業 ETF — 年度總報酬,2010-2024",
        "subtitle": "每格依該年內排名上色(綠=最佳、紅=最差)。週期地圖是趨勢,但催化劑才是當年主題。",
        "spy":      "SPY",
        "footer":   "資料:SPDR 簡介、公開總報酬資料。XLRE 於 2015 年 10 月推出(從 XLF 拆出);XLC 於 2018 年 6 月推出(從 XLK + XLY 拆出)。",
    },
    "cn": {
        "title":    "SPDR 行业 ETF — 年度总回报,2010-2024",
        "subtitle": "每格按该年内排名上色(绿=最佳、红=最差)。周期地图是趋势,但催化剂才是当年主题。",
        "spy":      "SPY",
        "footer":   "资料:SPDR 简介、公开总回报数据。XLRE 于 2015 年 10 月推出(从 XLF 拆出);XLC 于 2018 年 6 月推出(从 XLK + XLY 拆出)。",
    },
}


def _rank_cmap():
    return LinearSegmentedColormap.from_list(
        "rg", ["#b71c1c", "#e57373", "#f5f0e0", "#81c784", "#2e7d32"],
        N=256,
    )


def build_fig(s):
    p = PALETTE_LIGHT
    rows = SECTORS + ["SPY"]
    n_rows = len(rows)
    n_cols = len(YEARS)

    fig, ax = plt.subplots(figsize=(13.4, 6.8), dpi=150)
    style_axes(ax, p)
    ax.set_facecolor(p["bg"])
    fig.set_facecolor(p["bg"])

    cmap = _rank_cmap()

    for j, yr in enumerate(YEARS):
        # Rank ALL non-None entries (incl SPY) within the year
        items = [(r, RETURNS[yr].get(r)) for r in rows]
        valid = [(r, v) for r, v in items if v is not None]
        # rank: 0 (worst) -> 1 (best)
        sorted_vals = sorted(v for _, v in valid)
        for i, (r, v) in enumerate(items):
            x0 = j
            y0 = n_rows - 1 - i
            if v is None:
                ax.add_patch(Rectangle(
                    (x0, y0), 1, 1,
                    facecolor=p["grid"], edgecolor=p["bg"], linewidth=1.4,
                    alpha=0.35,
                ))
                continue
            # rank position 0..1
            rank = sorted_vals.index(v)
            t = rank / max(1, len(sorted_vals) - 1)
            face = cmap(t)
            edge = p["bg"]
            lw = 1.4
            if r == "SPY":
                edge = p["accent"]
                lw = 2.2
            ax.add_patch(Rectangle(
                (x0, y0), 1, 1,
                facecolor=face, edgecolor=edge, linewidth=lw,
            ))
            # annotate
            txt = f"{v:+.0f}" if abs(v) >= 10 else f"{v:+.1f}"
            txt = txt.replace("+0", "0").replace("-0.0", "0.0")
            # readable text color: black on light cells, white on extreme
            tcol = "#1a2332" if 0.18 < t < 0.85 else "#ffffff"
            ax.text(x0 + 0.5, y0 + 0.5, txt,
                    ha="center", va="center",
                    fontsize=8.4, fontweight="bold", color=tcol)

    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.set_xticks([j + 0.5 for j in range(n_cols)])
    ax.set_xticklabels([str(y) for y in YEARS], fontsize=9)
    ax.set_yticks([n_rows - 1 - i + 0.5 for i in range(n_rows)])
    ax.set_yticklabels(rows, fontsize=9.5, fontweight="bold")
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(length=0)
    ax.grid(False)

    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold",
                 loc="left", color=p["fg"])
    fig.text(0.13, 0.93, s["subtitle"], fontsize=10, color=p["muted"],
             style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.2,
             color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"wrote {BASE}.png and locale variants to {OUT_DIR}")
