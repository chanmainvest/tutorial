"""Week 43, §2.1 — SPIVA US large-cap underperformance by horizon.

Bar chart of the % of US large-cap active equity funds that
underperformed the S&P 500 over 1y / 3y / 5y / 10y / 15y windows
ending December 2024, per the April 2026 SPIVA scorecard.

Run:
    uv run python course/image/week43_spiva_chart.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week43_spiva_chart"

WINDOWS = ["1y", "3y", "5y", "10y", "15y"]
PCT = [60.0, 75.0, 80.0, 85.0, 90.0]

LANG_STRINGS = {
    "en": {
        "title":    "SPIVA: % of US large-cap active funds underperforming the S&P 500",
        "subtitle": "Net of fees, asset-weighted, survivorship-adjusted. Periods ending December 2024 (April 2026 scorecard).",
        "xlabel":   "Window length",
        "ylabel":   "% of funds underperforming",
        "ann":      "The longer the window, the worse it gets. Fees compound, luck washes out.",
        "ref":      "100% = every active fund loses to the index",
    },
    "hk": {
        "title":    "SPIVA:跑輸標普 500 的美國大型主動基金比例",
        "subtitle": "扣費後、資產加權、已調整存活偏差。截至 2024 年 12 月(2026 年 4 月計分卡)。",
        "xlabel":   "觀察期長度",
        "ylabel":   "跑輸基金比例 %",
        "ann":      "窗口越長,情況越差。費用累積,運氣消散。",
        "ref":      "100% = 全部主動基金都輸給指數",
    },
    "tw": {
        "title":    "SPIVA:跑輸標普 500 的美國大型主動基金比例",
        "subtitle": "扣費後、資產加權、已調整存活偏差。截至 2024 年 12 月(2026 年 4 月計分卡)。",
        "xlabel":   "觀察期長度",
        "ylabel":   "跑輸基金比例 %",
        "ann":      "窗口越長,情況越糟。費用累積,運氣消散。",
        "ref":      "100% = 全部主動基金都輸給指數",
    },
    "cn": {
        "title":    "SPIVA:跑输标普 500 的美国大型主动基金比例",
        "subtitle": "扣费后、资产加权、已调整存活偏差。截至 2024 年 12 月(2026 年 4 月计分卡)。",
        "xlabel":   "观察期长度",
        "ylabel":   "跑输基金比例 %",
        "ann":      "窗口越长,情况越差。费用累积,运气消散。",
        "ref":      "100% = 全部主动基金都输给指数",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.0), dpi=150)
    style_axes(ax, p)

    x = np.arange(len(WINDOWS))
    # Color gradient navy -> red as horizon lengthens
    colors = [p["blue"], "#3b54a3", "#7a3d62", "#a82e3a", p["red"]]
    bars = ax.bar(x, PCT, color=colors, width=0.62, edgecolor=p["bg"], linewidth=1.5)

    # Random-coin reference line at 50%
    ax.axhline(50, color=p["muted"], linestyle="--", linewidth=1.0, alpha=0.7)
    ax.text(len(WINDOWS) - 0.55, 51.5, "50% (coin flip)",
            fontsize=8.6, color=p["muted"], ha="right", style="italic")

    for b, v in zip(bars, PCT):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.5,
                f"{v:.0f}%", ha="center", va="bottom",
                fontsize=12, fontweight="bold", color=p["fg"])

    ax.set_xticks(x)
    ax.set_xticklabels(WINDOWS, fontsize=11)
    ax.set_ylim(0, 100)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold", loc="left")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"], style="italic")
    ax.text(0, -0.16, s["ann"], transform=ax.transAxes,
            fontsize=9.5, color=p["muted"])

    fig.tight_layout(rect=[0, 0, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
