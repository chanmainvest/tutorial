"""Week 43, §2.2 — Top-quartile fund persistence transition matrix.

Visual heatmap of the empirical 5-year-to-5-year quartile transition
matrix for US large-cap active equity funds, drawn from S&P's
Persistence Scorecard. Highlights that top-quartile-to-top-quartile
persistence is ~15% versus the 25% random baseline.

Run:
    uv run python course/image/week43_persistence_table.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week43_persistence_table"

# Empirical 4x4 transition matrix (rows = window-1 quartile,
# cols = window-2 quartile). Each row sums to 100%. Numbers are
# representative of multi-vintage averages from SPIVA Persistence.
# Diagonal is barely above 25%; top-quartile->top-quartile is 15%.
MATRIX = np.array([
    [15, 22, 26, 27],   # was Top      -> below random
    [22, 24, 26, 22],   # was Q2
    [26, 26, 25, 23],   # was Q3
    [27, 24, 22, 27],   # was Bottom -> mild bottom-stays-bottom
], dtype=float)
# Each row = approx 90 (because some funds die / merge)
DEATH = np.array([10, 6, 0, 0], dtype=float)  # Mortality column (informational)

LANG_STRINGS = {
    "en": {
        "title":    "5-year quartile persistence — US large-cap active funds",
        "subtitle": "Empirical transition: rows = quartile in window 1, columns = quartile in window 2. Random baseline = 25%.",
        "xlabel":   "Quartile in next 5 years",
        "ylabel":   "Quartile in first 5 years",
        "row_top":  "Top",
        "row_q2":   "Q2",
        "row_q3":   "Q3",
        "row_bot":  "Bottom",
        "col_top":  "Top",
        "col_q2":   "Q2",
        "col_q3":   "Q3",
        "col_bot":  "Bottom",
        "ann":      "Top quartile -> top quartile = 15% (below random 25%). Buying last cycle's winner is mildly anti-predictive.",
        "ref_label": "Random = 25%",
    },
    "hk": {
        "title":    "5 年分位數續航 — 美國大型主動基金",
        "subtitle": "實證轉移矩陣:行 = 第一個 5 年分位數,列 = 第二個 5 年分位數。隨機基準 = 25%。",
        "xlabel":   "下一個 5 年分位數",
        "ylabel":   "首個 5 年分位數",
        "row_top":  "頂",
        "row_q2":   "Q2",
        "row_q3":   "Q3",
        "row_bot":  "底",
        "col_top":  "頂",
        "col_q2":   "Q2",
        "col_q3":   "Q3",
        "col_bot":  "底",
        "ann":      "頂端 -> 頂端 = 15%(低於隨機 25%)。追逐上一週期贏家有輕微反向預測效應。",
        "ref_label": "隨機 = 25%",
    },
    "tw": {
        "title":    "5 年分位數續航 — 美國大型主動基金",
        "subtitle": "實證轉移矩陣:列 = 首個 5 年分位數,欄 = 次個 5 年分位數。隨機基準 = 25%。",
        "xlabel":   "次個 5 年分位數",
        "ylabel":   "首個 5 年分位數",
        "row_top":  "頂",
        "row_q2":   "Q2",
        "row_q3":   "Q3",
        "row_bot":  "底",
        "col_top":  "頂",
        "col_q2":   "Q2",
        "col_q3":   "Q3",
        "col_bot":  "底",
        "ann":      "頂端 -> 頂端 = 15%(低於隨機 25%)。追逐上一週期贏家有輕微反向預測效應。",
        "ref_label": "隨機 = 25%",
    },
    "cn": {
        "title":    "5 年分位续航 — 美国大型主动基金",
        "subtitle": "实证转移矩阵:行 = 第一个 5 年分位,列 = 第二个 5 年分位。随机基准 = 25%。",
        "xlabel":   "下一个 5 年分位",
        "ylabel":   "首个 5 年分位",
        "row_top":  "顶",
        "row_q2":   "Q2",
        "row_q3":   "Q3",
        "row_bot":  "底",
        "col_top":  "顶",
        "col_q2":   "Q2",
        "col_q3":   "Q3",
        "col_bot":  "底",
        "ann":      "顶 -> 顶 = 15%(低于随机 25%)。追逐上一周期赢家有轻微反向预测效应。",
        "ref_label": "随机 = 25%",
    },
}


def _color_for(v):
    """Map cell value to a heatmap color: 0 -> bg, 25 -> neutral, >25 -> red, <25 -> blue tint."""
    p = PALETTE_LIGHT
    if v >= 25:
        # Above random: warm red gradient
        t = min(1.0, (v - 25) / 15.0)
        # Blend bg toward red
        return _blend(p["bg"], p["red"], 0.15 + 0.55 * t)
    else:
        # Below random: cool blue gradient
        t = min(1.0, (25 - v) / 15.0)
        return _blend(p["bg"], p["blue"], 0.15 + 0.55 * t)


def _blend(c1, c2, t):
    def _hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    r1, g1, b1 = _hex_to_rgb(c1)
    r2, g2, b2 = _hex_to_rgb(c2)
    return (r1 + (r2 - r1) * t, g1 + (g2 - g1) * t, b1 + (b2 - b1) * t)


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.5, 6.4), dpi=150)
    style_axes(ax, p)
    ax.grid(False)

    rows = [s["row_top"], s["row_q2"], s["row_q3"], s["row_bot"]]
    cols = [s["col_top"], s["col_q2"], s["col_q3"], s["col_bot"]]

    n = 4
    for i in range(n):
        for j in range(n):
            v = MATRIX[i, j]
            ax.add_patch(plt.Rectangle((j, n - 1 - i), 1, 1,
                                       facecolor=_color_for(v),
                                       edgecolor=p["bg"], linewidth=2))
            # Highlight top-left (was Top -> still Top)
            if i == 0 and j == 0:
                ax.add_patch(plt.Rectangle((j, n - 1 - i), 1, 1,
                                           fill=False,
                                           edgecolor=p["accent"], linewidth=3.0,
                                           zorder=5))
            ax.text(j + 0.5, n - 1 - i + 0.5, f"{v:.0f}%",
                    ha="center", va="center",
                    fontsize=15 if (i == 0 and j == 0) else 13,
                    fontweight="bold" if (i == 0 and j == 0) else "normal",
                    color=p["fg"])

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([0.5 + k for k in range(n)])
    ax.set_xticklabels(cols, fontsize=11)
    ax.set_yticks([0.5 + k for k in range(n)])
    ax.set_yticklabels(rows[::-1], fontsize=11)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold", loc="left")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"], style="italic")
    ax.text(0, -0.13, s["ann"], transform=ax.transAxes,
            fontsize=9.5, color=p["muted"])

    # Reference legend strip on the right
    ref_x = n + 0.15
    ax.text(ref_x, n - 0.3, s["ref_label"],
            fontsize=9, color=p["muted"], style="italic")
    # color-bar style markers
    for k, v in enumerate([10, 15, 20, 25, 30, 35]):
        ax.add_patch(plt.Rectangle((ref_x, n - 1.0 - k * 0.5), 0.35, 0.42,
                                   facecolor=_color_for(v),
                                   edgecolor=p["muted"], linewidth=0.6))
        ax.text(ref_x + 0.45, n - 1.0 - k * 0.5 + 0.21, f"{v}%",
                fontsize=8.4, color=p["muted"], va="center")
    ax.set_xlim(0, n + 1.15)

    fig.tight_layout(rect=[0, 0, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
