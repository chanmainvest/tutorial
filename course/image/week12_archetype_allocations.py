"""Week 12, §2.3 — Stacked horizontal bar chart of five archetype portfolios.

Each row is one archetype (early career through retired plus a FIRE /
barbell-curious row). The bar is segmented by US stocks, ex-US stocks,
intermediate bonds, TIPS, gold, and cash. Site palette colours.

Run:
    uv run python course/image/week12_archetype_allocations.py
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
BASE = "week12_archetype_allocations"

# Allocation table (US, exUS, bonds, TIPS, gold, cash) - decimals summing to 1.0
ARCHETYPES = [
    ("early",   [0.65, 0.20, 0.05, 0.00, 0.05, 0.05]),
    ("mid",     [0.50, 0.15, 0.20, 0.05, 0.05, 0.05]),
    ("late",    [0.35, 0.10, 0.30, 0.10, 0.10, 0.05]),
    ("retired", [0.25, 0.05, 0.35, 0.15, 0.10, 0.10]),
    ("fire",    [0.40, 0.10, 0.10, 0.05, 0.20, 0.15]),
]

LANG_STRINGS = {
    "en": {
        "title":    "Five archetype starter portfolios",
        "subtitle": "Recommended allocations by life stage and risk profile. Bars sum to 100%.",
        "xlabel":   "Allocation (%)",
        "early":    "Early career",
        "mid":      "Mid career",
        "late":     "Late career",
        "retired":  "Retired",
        "fire":     "FIRE / barbell",
        "us":       "US stocks (VTI)",
        "exus":     "Ex-US (VXUS)",
        "bonds":    "Bonds (BND)",
        "tips":     "TIPS (SCHP)",
        "gold":     "Gold (GLD)",
        "cash":     "Cash (SGOV)",
    },
    "hk": {
        "title":    "五個入門起點組合",
        "subtitle": "依人生階段與風險偏好的建議配置;每行合計 100%。",
        "xlabel":   "配置比例 (%)",
        "early":    "職涯早期",
        "mid":      "職涯中期",
        "late":     "職涯後期",
        "retired":  "退休後",
        "fire":     "FIRE / 槓鈴",
        "us":       "美股 (VTI)",
        "exus":     "美國以外 (VXUS)",
        "bonds":    "債券 (BND)",
        "tips":     "通脹掛鈎債 (SCHP)",
        "gold":     "黃金 (GLD)",
        "cash":     "現金 (SGOV)",
    },
    "tw": {
        "title":    "五個入門起點組合",
        "subtitle": "依人生階段與風險偏好的建議配置;每列合計 100%。",
        "xlabel":   "配置比例 (%)",
        "early":    "職涯早期",
        "mid":      "職涯中期",
        "late":     "職涯後期",
        "retired":  "退休後",
        "fire":     "FIRE / 槓鈴",
        "us":       "美股 (VTI)",
        "exus":     "美國以外 (VXUS)",
        "bonds":    "債券 (BND)",
        "tips":     "通膨連動債 (SCHP)",
        "gold":     "黃金 (GLD)",
        "cash":     "現金 (SGOV)",
    },
    "cn": {
        "title":    "五个入门起点组合",
        "subtitle": "按人生阶段与风险偏好的建议配置;每行合计 100%。",
        "xlabel":   "配置比例 (%)",
        "early":    "职涯早期",
        "mid":      "职涯中期",
        "late":     "职涯后期",
        "retired":  "退休后",
        "fire":     "FIRE / 杠铃",
        "us":       "美股 (VTI)",
        "exus":     "美国以外 (VXUS)",
        "bonds":    "债券 (BND)",
        "tips":     "通胀挂钩债 (SCHP)",
        "gold":     "黄金 (GLD)",
        "cash":     "现金 (SGOV)",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    sleeve_keys   = ["us", "exus", "bonds", "tips", "gold", "cash"]
    sleeve_colors = [p["blue"], p["teal"], p["purple"], p["green"],
                     p["accent"], p["grey"]]

    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    style_axes(ax, p)

    rows = list(reversed(ARCHETYPES))   # plot top-to-bottom
    y_positions = np.arange(len(rows))
    y_labels    = [s[k] for k, _ in rows]

    for i, (_, weights) in enumerate(rows):
        left = 0.0
        for j, w in enumerate(weights):
            pct = w * 100
            ax.barh(i, pct, left=left, color=sleeve_colors[j],
                    edgecolor=p["bg"], linewidth=1.5, height=0.72)
            if pct >= 4.5:
                ax.text(left + pct / 2, i, f"{int(round(pct))}%",
                        ha="center", va="center", color="#ffffff",
                        fontsize=10, fontweight="bold")
            left += pct

    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel(s["xlabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.grid(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0)

    # Legend below
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in sleeve_colors]
    labels  = [s[k] for k in sleeve_keys]
    ax.legend(handles, labels, loc="upper center",
              bbox_to_anchor=(0.5, -0.10), ncol=6, frameon=False,
              fontsize=9.5, handlelength=1.4, handleheight=1.0,
              columnspacing=1.0)

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
