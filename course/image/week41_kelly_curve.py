"""Week 41, §2.1 — Kelly fraction f* vs win rate p across 5 payoff ratios.

For binary win/lose bets, full Kelly is f* = (b p - q) / b. We plot
f* clamped at zero (no-bet region) for b in {1, 2, 3, 0.5, 1/3} —
i.e. risk:reward 1:1, 1:2, 1:3, 2:1, 3:1. Annotates the typical
equity-edge zone (p~0.52, b=1, f*~4%).

Run:
    uv run python course/image/week41_kelly_curve.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week41_kelly_curve"

LANG_STRINGS = {
    "en": {
        "title":    "Kelly fraction f* vs win rate, 5 payoff ratios",
        "subtitle": "Full Kelly = (b p - q) / b for binary bets. The typical equity-edge zone (p~52%, b=1) lands at f*~4%.",
        "xlabel":   "Win rate p",
        "ylabel":   "Full Kelly fraction f*",
        "ratios":   ["3:1 (b=3)", "2:1 (b=2)", "1:1 (b=1)", "1:2 (b=0.5)", "1:3 (b=0.33)"],
        "zone":     "Typical equity edge\np~52%, b=1\nf*~4%",
        "footer":   "Above 2 f* the geometric growth rate is zero. Quarter-Kelly is the retail default to absorb edge-estimate uncertainty.",
    },
    "hk": {
        "title":    "Kelly 比率 f* 對勝率,五個賠率",
        "subtitle": "二元下注的全 Kelly = (b p - q) / b。典型股票邊緣區(p~52%,b=1)落在 f*~4%。",
        "xlabel":   "勝率 p",
        "ylabel":   "全 Kelly 比率 f*",
        "ratios":   ["3:1 (b=3)", "2:1 (b=2)", "1:1 (b=1)", "1:2 (b=0.5)", "1:3 (b=0.33)"],
        "zone":     "典型股票邊緣\np~52%、b=1\nf*~4%",
        "footer":   "超過 2 f* 幾何增長率為零。零售預設用四分一 Kelly 以吸收邊緣估計不確定性。",
    },
    "tw": {
        "title":    "Kelly 比率 f* 對勝率,五個賠率",
        "subtitle": "二元下注的全 Kelly = (b p - q) / b。典型股票邊緣區(p~52%,b=1)落在 f*~4%。",
        "xlabel":   "勝率 p",
        "ylabel":   "全 Kelly 比率 f*",
        "ratios":   ["3:1 (b=3)", "2:1 (b=2)", "1:1 (b=1)", "1:2 (b=0.5)", "1:3 (b=0.33)"],
        "zone":     "典型股票邊緣\np~52%、b=1\nf*~4%",
        "footer":   "超過 2 f* 幾何成長率為零。散戶預設用四分之一 Kelly 以吸收邊緣估計不確定性。",
    },
    "cn": {
        "title":    "Kelly 比率 f* 对胜率,五个赔率",
        "subtitle": "二元下注的全 Kelly = (b p - q) / b。典型股票边缘区(p~52%,b=1)落在 f*~4%。",
        "xlabel":   "胜率 p",
        "ylabel":   "全 Kelly 比率 f*",
        "ratios":   ["3:1 (b=3)", "2:1 (b=2)", "1:1 (b=1)", "1:2 (b=0.5)", "1:3 (b=0.33)"],
        "zone":     "典型股票边缘\np~52%、b=1\nf*~4%",
        "footer":   "超过 2 f* 几何增长率为零。零售默认用四分之一 Kelly 以吸收边缘估计不确定性。",
    },
}


def _kelly(p: np.ndarray, b: float) -> np.ndarray:
    q = 1.0 - p
    f = (b * p - q) / b
    return np.clip(f, 0.0, None)


def build_fig(s):
    p_grid = np.linspace(0.30, 0.80, 401)
    bs = [3.0, 2.0, 1.0, 0.5, 1.0 / 3.0]
    pal = PALETTE_LIGHT

    colors = [pal["green"], pal["teal"], pal["blue"], pal["orange"], pal["red"]]
    widths = [1.8, 1.8, 2.6, 1.8, 1.8]

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, pal)

    for b, label, c, lw in zip(bs, s["ratios"], colors, widths):
        f = _kelly(p_grid, b)
        ax.plot(p_grid, f * 100.0, color=c, linewidth=lw, label=label)

    # Equity-edge zone marker: p=0.52, b=1
    eq_p = 0.52
    eq_f = _kelly(np.array([eq_p]), 1.0)[0] * 100.0
    ax.scatter([eq_p], [eq_f], s=120, color=pal["accent"], zorder=5,
               edgecolors=pal["fg"], linewidths=1.2)
    ax.annotate(
        s["zone"],
        xy=(eq_p, eq_f), xytext=(eq_p + 0.08, eq_f + 14),
        fontsize=9.5, color=pal["fg"],
        arrowprops=dict(arrowstyle="-", color=pal["accent"], lw=1.0),
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff8dc", ec=pal["accent"], lw=0.8),
    )

    # Quarter-Kelly horizontal reference
    ax.axhline(eq_f * 0.25, color=pal["muted"], linestyle=":", linewidth=1.0, alpha=0.7)
    ax.text(0.305, eq_f * 0.25 + 0.6, "1/4 Kelly = " + f"{eq_f*0.25:.1f}%",
            fontsize=8.5, color=pal["muted"])

    ax.set_xlim(0.30, 0.80)
    ax.set_ylim(0, 70)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"] + " (%)", fontsize=10.5)
    ax.legend(loc="upper left", frameon=False, fontsize=9)

    # Format x as percent
    ax.set_xticks([0.30, 0.40, 0.50, 0.55, 0.60, 0.70, 0.80])
    ax.set_xticklabels(["30%", "40%", "50%", "55%", "60%", "70%", "80%"])

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=9, color=pal["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
