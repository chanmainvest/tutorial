"""Week 15, §2.5 — Four-tranche donut.

Donut chart of the SOUL #13 four-tranche book at retail scale:
Growth 40%, Income 30%, Store-of-Value 20%, Opportunistic 10%.
Each segment annotated with vehicles and dollar amount on a $100k book.

Run:
    uv run python course/image/week15_four_tranches.py
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
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week15_four_tranches"


LANG_STRINGS = {
    "en": {
        "title":    "The four-tranche book — retail scale",
        "subtitle": "SOUL #13 framework, unlevered, applied to a $100,000 account. Annual rebalance.",
        "growth":   "Growth",
        "income":   "Income",
        "sov":      "Store-of-value",
        "opp":      "Opportunistic",
        "g_sub":    "VTI · SPY · QUAL\n40% = \\$40,000",
        "i_sub":    "IEF · LQD · GOVT\n30% = \\$30,000",
        "s_sub":    "GLD · IAU · SCHP\n20% = \\$20,000",
        "o_sub":    "BIL · SGOV · options\n10% = \\$10,000",
        "centre":   "$100,000\nbook",
        "footer":   "Income tranche reduced from 1996 Bridgewater template (~55%) to 30% post-2022. Store-of-value increased from ~7% to 20%.",
    },
    "hk": {
        "title":    "四層資產組合 — 散戶版",
        "subtitle": "SOUL #13 框架,不加槓桿,套用至 10 萬美元帳戶。每年再平衡。",
        "growth":   "增長層",
        "income":   "收益層",
        "sov":      "保值層",
        "opp":      "機會層",
        "g_sub":    "VTI · SPY · QUAL\n40% = \\$40,000",
        "i_sub":    "IEF · LQD · GOVT\n30% = \\$30,000",
        "s_sub":    "GLD · IAU · SCHP\n20% = \\$20,000",
        "o_sub":    "BIL · SGOV · 期權\n10% = \\$10,000",
        "centre":   "$100,000\n組合",
        "footer":   "收益層由 1996 年橋水模板的 ~55% 下調至 30%(2022 年後);保值層由 ~7% 上調至 20%。",
    },
    "tw": {
        "title":    "四層資產組合 — 散戶版",
        "subtitle": "SOUL #13 框架,不加槓桿,套用至 10 萬美元帳戶。每年再平衡。",
        "growth":   "成長層",
        "income":   "收益層",
        "sov":      "保值層",
        "opp":      "機會層",
        "g_sub":    "VTI · SPY · QUAL\n40% = \\$40,000",
        "i_sub":    "IEF · LQD · GOVT\n30% = \\$30,000",
        "s_sub":    "GLD · IAU · SCHP\n20% = \\$20,000",
        "o_sub":    "BIL · SGOV · 選擇權\n10% = \\$10,000",
        "centre":   "$100,000\n組合",
        "footer":   "收益層由 1996 年橋水模板的 ~55% 下調至 30%(2022 年後);保值層由 ~7% 上調至 20%。",
    },
    "cn": {
        "title":    "四层资产组合 — 散户版",
        "subtitle": "SOUL #13 框架,不加杠杆,套用至 10 万美元账户。每年再平衡。",
        "growth":   "增长层",
        "income":   "收益层",
        "sov":      "保值层",
        "opp":      "机会层",
        "g_sub":    "VTI · SPY · QUAL\n40% = \\$40,000",
        "i_sub":    "IEF · LQD · GOVT\n30% = \\$30,000",
        "s_sub":    "GLD · IAU · SCHP\n20% = \\$20,000",
        "o_sub":    "BIL · SGOV · 期权\n10% = \\$10,000",
        "centre":   "$100,000\n组合",
        "footer":   "收益层由 1996 年桥水模板的 ~55% 下调至 30%(2022 年后);保值层由 ~7% 上调至 20%。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    weights = [40, 30, 20, 10]
    colors = [p["red"], p["blue"], p["accent"], p["green"]]
    labels = [s["growth"], s["income"], s["sov"], s["opp"]]
    sublabels = [s["g_sub"], s["i_sub"], s["s_sub"], s["o_sub"]]

    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    ax.set_facecolor(p["bg"])

    wedges, _ = ax.pie(
        weights, colors=colors, startangle=90, counterclock=False,
        wedgeprops=dict(width=0.42, edgecolor=p["bg"], linewidth=3),
    )

    # Centre text
    ax.text(0, 0, s["centre"], ha="center", va="center",
            fontsize=14, color=p["fg"], weight="bold")

    # Outer labels at wedge midpoints
    for i, w in enumerate(wedges):
        ang = (w.theta1 + w.theta2) / 2.0
        x = 1.18 * np.cos(np.deg2rad(ang))
        y = 1.18 * np.sin(np.deg2rad(ang))
        ha = "left" if x >= 0 else "right"
        ax.annotate(
            f"{labels[i]}  {weights[i]}%",
            xy=(np.cos(np.deg2rad(ang)) * 0.79, np.sin(np.deg2rad(ang)) * 0.79),
            xytext=(x, y),
            ha=ha, va="center",
            fontsize=11.5, fontweight="bold", color=colors[i],
            arrowprops=dict(arrowstyle="-", color=colors[i], lw=1.0),
        )
        # Sub-label below the main label
        ax.text(x, y - 0.16, sublabels[i],
                ha=ha, va="top", fontsize=9, color=p["muted"])

    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.suptitle(s["title"], fontsize=15, fontweight="bold", y=0.97)
    fig.text(0.5, 0.92, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.04, s["footer"], ha="center",
             fontsize=9, color=p["muted"])

    fig.tight_layout(rect=[0, 0.06, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
