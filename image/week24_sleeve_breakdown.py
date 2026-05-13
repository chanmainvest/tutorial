"""Week 24, §2.3 — Stacked horizontal bar of five archetype multi-strategy portfolios.

Five archetypes (conservative, moderate, aggressive, institutional,
FIRE/barbell), each shown as a 100% horizontal bar segmented by
beta / factor / alpha / cash. Site-palette colours.

Run:
    uv run python course/image/week24_sleeve_breakdown.py
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
BASE = "week24_sleeve_breakdown"

# (key, [beta, factor, alpha, cash]) — must sum to 1.0
ARCHETYPES = [
    ("conservative",  [0.90, 0.00, 0.00, 0.10]),
    ("moderate",      [0.80, 0.10, 0.05, 0.05]),
    ("aggressive",    [0.65, 0.15, 0.15, 0.05]),
    ("institutional", [0.70, 0.15, 0.13, 0.02]),
    ("fire",          [0.70, 0.05, 0.10, 0.15]),
]

LANG_STRINGS = {
    "en": {
        "title":         "Five archetype multi-strategy portfolios",
        "subtitle":      "Each row is one archetype's sleeve breakdown. Bars sum to 100%. SOUL #1 — alpha is rare; most retail should sit on the conservative row.",
        "xlabel":        "Allocation (%)",
        "conservative":  "Conservative",
        "moderate":      "Moderate (retail default)",
        "aggressive":    "Aggressive",
        "institutional": "Institutional (Yale-style)",
        "fire":          "FIRE / barbell",
        "beta":          "Beta (VTI + BND)",
        "factor":        "Smart beta / factor",
        "alpha":         "Alpha (market-neutral)",
        "cash":          "Cash (SGOV / T-bills)",
    },
    "hk": {
        "title":         "五個多策略原型組合",
        "subtitle":      "每行是一個原型的板塊拆分,合計 100%。SOUL #1 — alpha 稀有,大多數零售投資者應留在最保守那一行。",
        "xlabel":        "配置比例 (%)",
        "conservative":  "保守型",
        "moderate":      "中庸型(零售預設)",
        "aggressive":    "進取型",
        "institutional": "機構型(耶魯式)",
        "fire":          "FIRE / 槓鈴",
        "beta":          "Beta(VTI + BND)",
        "factor":        "Smart beta / 因子",
        "alpha":         "Alpha(市場中性)",
        "cash":          "現金(SGOV / 國庫券)",
    },
    "tw": {
        "title":         "五個多策略原型組合",
        "subtitle":      "每列是一個原型的板塊拆分,合計 100%。SOUL #1 — alpha 稀有,多數零售投資者應停留在最保守那一列。",
        "xlabel":        "配置比例 (%)",
        "conservative":  "保守型",
        "moderate":      "中庸型(零售預設)",
        "aggressive":    "積極型",
        "institutional": "機構型(耶魯式)",
        "fire":          "FIRE / 槓鈴",
        "beta":          "Beta(VTI + BND)",
        "factor":        "Smart beta / 因子",
        "alpha":         "Alpha(市場中性)",
        "cash":          "現金(SGOV / 國庫券)",
    },
    "cn": {
        "title":         "五个多策略原型组合",
        "subtitle":      "每行是一个原型的板块拆分,合计 100%。SOUL #1 — alpha 稀有,多数零售投资者应留在最保守那一行。",
        "xlabel":        "配置比例 (%)",
        "conservative":  "保守型",
        "moderate":      "中庸型(零售默认)",
        "aggressive":    "进取型",
        "institutional": "机构型(耶鲁式)",
        "fire":          "FIRE / 杠铃",
        "beta":          "Beta(VTI + BND)",
        "factor":        "Smart beta / 因子",
        "alpha":         "Alpha(市场中性)",
        "cash":          "现金(SGOV / 国库券)",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    sleeve_keys   = ["beta", "factor", "alpha", "cash"]
    sleeve_colors = [p["blue"], p["accent"], p["green"], p["grey"]]

    fig, ax = plt.subplots(figsize=(11, 5.6))
    style_axes(ax, p)

    rows = list(reversed(ARCHETYPES))   # plot top-to-bottom
    y_positions = np.arange(len(rows))
    y_labels    = [s[k] for k, _ in rows]

    for i, (_, weights) in enumerate(rows):
        left = 0.0
        for j, w in enumerate(weights):
            if w <= 0:
                continue
            ax.barh(i, w * 100, left=left, color=sleeve_colors[j],
                    edgecolor=p["bg"], linewidth=1.2,
                    label=s[sleeve_keys[j]] if i == 0 else None)
            if w >= 0.04:
                ax.text(left + w * 100 / 2, i, f"{int(round(w * 100))}%",
                        ha="center", va="center",
                        color="white", fontsize=9.5, fontweight="bold")
            left += w * 100

    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=10.5)
    ax.set_xlim(0, 100)
    ax.set_xlabel(s["xlabel"])
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])

    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.22),
              ncol=4, frameon=False, fontsize=10)

    fig.tight_layout(rect=[0, 0.05, 1, 0.95])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
