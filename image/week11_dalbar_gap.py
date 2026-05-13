"""Week 11, §2.1 — The Dalbar gap: fund return vs investor return.

Bar chart over three trailing windows ending December 2024
(10y, 20y, 30y). The fund (or S&P 500) bar is taller than the
average equity-fund-investor bar in every window. The shaded
gap is pure behaviour: sequence-of-flows, panic exits, and
chasing last year's winner.

Numbers are representative long-run DALBAR QAIB figures
(for teaching). They are not refit each year.

Run:
    uv run python course/image/week11_dalbar_gap.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week11_dalbar_gap"

# Trailing-window annualised returns ending Dec 2024 (representative
# DALBAR QAIB long-run values; teaching figures, not refit yearly).
WINDOWS = ["10y", "20y", "30y"]
SP500   = [0.120, 0.099, 0.102]   # fund / S&P 500
INVESTOR = [0.080, 0.060, 0.068]  # average equity-fund investor

LANG_STRINGS = {
    "en": {
        "title":    "The Dalbar gap: fund return vs investor return",
        "subtitle": "Average S&P 500 / equity fund return vs the dollar-weighted return of the average investor in those funds. Trailing windows ending December 2024.",
        "xlabel":   "Trailing window",
        "ylabel":   "Annualised return",
        "fund":     "S&P 500 / fund",
        "investor": "Avg fund investor",
        "gap":      "behaviour gap",
        "footer":   "Behaviour costs ~3-4 pp / yr. Compounded 30y, that turns ~10x wealth into ~4x.",
    },
    "hk": {
        "title":    "Dalbar 落差:基金回報 vs 投資者回報",
        "subtitle": "平均標普 500 / 股票型基金回報 vs 該等基金的平均投資者按金額加權回報。截至 2024 年 12 月的滾動窗口。",
        "xlabel":   "滾動窗口",
        "ylabel":   "年化回報",
        "fund":     "標普 500 / 基金",
        "investor": "平均基金投資者",
        "gap":      "行為落差",
        "footer":   "行為每年蝕約 3-4 個百分點。複利 30 年,把約 10 倍財富變成約 4 倍。",
    },
    "tw": {
        "title":    "Dalbar 落差:基金報酬 vs 投資人報酬",
        "subtitle": "平均標普 500 / 股票型基金報酬 vs 該等基金的平均投資人按金額加權報酬。截至 2024 年 12 月的滾動窗口。",
        "xlabel":   "滾動窗口",
        "ylabel":   "年化報酬",
        "fund":     "標普 500 / 基金",
        "investor": "平均基金投資人",
        "gap":      "行為落差",
        "footer":   "行為每年損失約 3-4 個百分點。複利 30 年,把約 10 倍財富變成約 4 倍。",
    },
    "cn": {
        "title":    "Dalbar 落差:基金回报 vs 投资者回报",
        "subtitle": "平均标普 500 / 股票型基金回报 vs 该等基金的平均投资者按金额加权回报。截至 2024 年 12 月的滚动窗口。",
        "xlabel":   "滚动窗口",
        "ylabel":   "年化回报",
        "fund":     "标普 500 / 基金",
        "investor": "平均基金投资者",
        "gap":      "行为落差",
        "footer":   "行为每年损失约 3-4 个百分点。复利 30 年,把约 10 倍财富变成约 4 倍。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.5, 6.0), dpi=150)
    style_axes(ax, p)

    x = np.arange(len(WINDOWS))
    w = 0.36

    bars_f = ax.bar(x - w / 2, SP500,    width=w, color=p["accent"],
                    label=s["fund"], edgecolor="none")
    bars_i = ax.bar(x + w / 2, INVESTOR, width=w, color=p["blue"],
                    label=s["investor"], edgecolor="none")

    # Shade the gap with a translucent overlay above the investor bar
    for xi, fr, ir in zip(x, SP500, INVESTOR):
        ax.add_patch(plt.Rectangle(
            (xi - w / 2, ir), w, fr - ir,
            facecolor=p["red"], alpha=0.18, edgecolor=p["red"],
            linewidth=0.8, hatch="///",
        ))
        # Gap label
        gap = fr - ir
        ax.annotate(
            f"-{gap*100:.1f} pp",
            xy=(xi, (fr + ir) / 2),
            ha="center", va="center",
            fontsize=10, fontweight="bold",
            color=p["red"],
        )

    # Value labels on each bar
    for bar, val in zip(bars_f, SP500):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.003,
                f"{val*100:.1f}%", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["accent"])
    for bar, val in zip(bars_i, INVESTOR):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.003,
                f"{val*100:.1f}%", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["blue"])

    # Custom legend with gap entry
    gap_patch = plt.Rectangle((0, 0), 1, 1,
                              facecolor=p["red"], alpha=0.18,
                              edgecolor=p["red"], hatch="///",
                              label=s["gap"])
    handles, labels = ax.get_legend_handles_labels()
    handles.append(gap_patch)
    labels.append(s["gap"])
    ax.legend(handles, labels, loc="upper right", frameon=False, fontsize=10)

    ax.set_xticks(x)
    ax.set_xticklabels(WINDOWS)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, max(SP500) * 1.22)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))

    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.04, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["muted"], style="italic")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
