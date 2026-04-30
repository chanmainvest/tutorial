"""Side 21, §2.5 — Effective borrow rates: broker margin vs box spread vs Treasury.

Bar chart of the all-in 5-year financing cost on a $100k loan, expressed
as the effective annual rate, across six structures available to a US
retail investor in April 2026:

    1. Fidelity / Schwab small-balance margin (~12%)
    2. Interactive Brokers Pro small-balance (~6.6%)
    3. Robinhood Gold flat (6.75%)
    4. Interactive Brokers Pro >$1M (~5.6%)
    5. SPX box spread (~4.7%, SOFR + 30-50 bp)
    6. 3-month T-bill (4.30%, the natural floor)

The bars are coloured by who controls the spread (broker discretion vs
market-set), with the Treasury rate drawn as a horizontal reference and
the spread above T-bills called out per bar.

Run:
    uv run python course/image/side21_box_vs_broker.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "side21_box_vs_broker"

LANG_STRINGS = {
    "en": {
        "title":    "Effective borrow rate by structure: $100k, 5-year horizon",
        "subtitle": "April 2026 retail rate card. T-bills 4.30% set the floor; box spreads finance ~40bp above SOFR; brokers stack 200-700bp on top.",
        "xlabel":   "",
        "ylabel":   "Effective annual rate",
        "structures": [
            "Fidelity\nsmall-bal",
            "Schwab\nsmall-bal",
            "Robinhood\nGold (flat)",
            "IB Pro\n$25k-$100k",
            "IB Pro\n$1M+",
            "SPX box\nspread",
            "3M T-bill\n(floor)",
        ],
        "spread_lbl":  "spread vs T-bill",
        "tbill_lbl":   "T-bill 4.30%",
        "annot_box":   "Box spread:\nSection 1256 60/40 tax\nNo margin call on box itself",
        "annot_high":  "Broker margin:\nordinary-income tax\nrules can change overnight",
        "footer":      "Rates as posted Apr 2026. Box-spread financing assumes SPX 12-month box, four legs, settlement at expiry. T-bill is the secondary-market 3-month yield.",
    },
    "hk": {
        "title":    "不同融資結構的有效借款利率(10 萬美元 / 5 年)",
        "subtitle": "2026 年 4 月零售價單。T-bill 4.30% 為底線;box spread 約 SOFR + 40bp;券商再加 200-700bp。",
        "xlabel":   "",
        "ylabel":   "有效年利率",
        "structures": [
            "Fidelity\n小額",
            "Schwab\n小額",
            "Robinhood\nGold(統一)",
            "IB Pro\n$25k-$100k",
            "IB Pro\n$1M 以上",
            "SPX box\nspread",
            "3 月 T-bill\n(底線)",
        ],
        "spread_lbl":  "與 T-bill 之差",
        "tbill_lbl":   "T-bill 4.30%",
        "annot_box":   "Box spread:\n1256 條款 60/40 稅\nbox 本身不會被 call",
        "annot_high":  "券商保證金:\n按一般所得課稅\n規則可一夜變更",
        "footer":      "2026 年 4 月公布利率。Box spread 假設 SPX 12 個月 box,4 條腿,到期結算。T-bill 為 3 月期市場利率。",
    },
    "tw": {
        "title":    "不同融資結構的有效借款利率(10 萬美元 / 5 年)",
        "subtitle": "2026 年 4 月零售價單。T-bill 4.30% 為地板;box spread 約 SOFR + 40bp;券商再加 200-700bp。",
        "xlabel":   "",
        "ylabel":   "有效年利率",
        "structures": [
            "Fidelity\n小額",
            "Schwab\n小額",
            "Robinhood\nGold(均一)",
            "IB Pro\n$25k-$100k",
            "IB Pro\n$1M 以上",
            "SPX box\nspread",
            "3 月 T-bill\n(地板)",
        ],
        "spread_lbl":  "與 T-bill 之差",
        "tbill_lbl":   "T-bill 4.30%",
        "annot_box":   "Box spread:\n1256 條款 60/40 稅\nbox 本身不會被追繳",
        "annot_high":  "券商保證金:\n依一般所得課稅\n規則可一夜變更",
        "footer":      "2026 年 4 月公布利率。Box spread 假設 SPX 12 個月 box,4 條腿,到期結算。T-bill 為 3 月期市場利率。",
    },
    "cn": {
        "title":    "不同融资结构的有效借款利率(10 万美元 / 5 年)",
        "subtitle": "2026 年 4 月零售价单。T-bill 4.30% 为下限;box spread 约 SOFR + 40bp;券商再加 200-700bp。",
        "xlabel":   "",
        "ylabel":   "有效年利率",
        "structures": [
            "Fidelity\n小额",
            "Schwab\n小额",
            "Robinhood\nGold(统一)",
            "IB Pro\n$25k-$100k",
            "IB Pro\n$1M 以上",
            "SPX box\nspread",
            "3 月 T-bill\n(下限)",
        ],
        "spread_lbl":  "与 T-bill 之差",
        "tbill_lbl":   "T-bill 4.30%",
        "annot_box":   "Box spread:\n1256 60/40 税\nbox 本身不会被强平",
        "annot_high":  "券商保证金:\n按普通所得课税\n规则可一夜变更",
        "footer":      "2026 年 4 月公布利率。Box spread 假设 SPX 12 个月 box,4 条腿,到期结算。T-bill 为 3 月期市场利率。",
    },
}

# Effective annual rate per structure (April 2026, retail / posted).
# Order: Fidelity, Schwab, Robinhood, IB-small, IB-large, Box, T-bill.
RATES = [11.075, 11.575, 6.75, 6.08, 5.58, 4.70, 4.30]
TBILL = 4.30


def build_fig(s):
    def _esc(v):
        if isinstance(v, str):
            return v.replace("$", r"\$")
        if isinstance(v, list):
            return [x.replace("$", r"\$") if isinstance(x, str) else x for x in v]
        return v
    s = {k: _esc(v) for k, v in s.items()}
    pal = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(12.0, 6.6), dpi=150)
    style_axes(ax, pal)

    x = np.arange(len(RATES))
    # Color: red for high broker, orange for moderate broker, green for box, grey for T-bill.
    bar_colors = [
        pal["red"], pal["red"], pal["orange"], pal["orange"],
        pal["accent"], pal["green"], pal["muted"],
    ]
    bars = ax.bar(x, RATES, color=bar_colors, edgecolor=pal["fg"],
                  linewidth=0.8, width=0.66, zorder=3)

    # T-bill horizontal floor reference.
    ax.axhline(TBILL, color=pal["muted"], lw=1.0, ls="--", zorder=2)
    ax.text(len(RATES) - 0.5, TBILL + 0.18, s["tbill_lbl"],
            fontsize=9, color=pal["muted"], ha="right", style="italic")

    # Annotate each bar: effective rate + spread above T-bill (in bp).
    for xi, r in zip(x, RATES):
        spread_bp = (r - TBILL) * 100
        ax.text(xi, r + 0.30, f"{r:.2f}%", ha="center", va="bottom",
                fontsize=10.5, color=pal["fg"], weight="bold")
        if spread_bp > 5:
            ax.text(xi, r + 0.95, f"+{int(round(spread_bp))} bp",
                    ha="center", va="bottom", fontsize=8.5, color=pal["muted"])
        else:
            ax.text(xi, r + 0.95, "floor", ha="center", va="bottom",
                    fontsize=8.5, color=pal["muted"], style="italic")

    # Side annotation: box spread advantage.
    ax.annotate(
        s["annot_box"],
        xy=(5, RATES[5]), xytext=(5.2, 9.5),
        fontsize=9, color=pal["green"], weight="bold", ha="left",
        arrowprops=dict(arrowstyle="->", color=pal["green"], lw=0.9),
        bbox=dict(boxstyle="round,pad=0.35", fc="#f0f9f4", ec=pal["green"], lw=0.8),
    )
    # Side annotation: broker margin disadvantage.
    ax.annotate(
        s["annot_high"],
        xy=(0, RATES[0]), xytext=(1.3, 13.3),
        fontsize=9, color=pal["red"], weight="bold", ha="left",
        arrowprops=dict(arrowstyle="->", color=pal["red"], lw=0.9),
        bbox=dict(boxstyle="round,pad=0.35", fc="#fff5f5", ec=pal["red"], lw=0.8),
    )

    ax.set_xticks(x)
    ax.set_xticklabels(s["structures"], fontsize=9.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_ylim(0, 15.5)
    ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14])
    ax.set_yticklabels([f"{v:.0f}%" for v in [0, 2, 4, 6, 8, 10, 12, 14]])
    ax.grid(True, axis="y", alpha=0.25, lw=0.5)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=pal["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
