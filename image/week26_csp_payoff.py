"""Week 26, §2.2 - Cash-secured put payoff diagram.

Sell 1 XYZ $90 put for $2.00 with 30 days to expiry, fully cash-
secured ($9,000 collateral). Payoff per contract over a stock-price
grid from $60 to $140. Marks: breakeven $88, max profit +$200,
max loss -$8,800 at $0. Visual companion to the SOUL #14 L2 income
sleeve and the limit-order analogy.

Run:
    uv run python course/image/week26_csp_payoff.py
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

OUT_DIR = Path(__file__).parent
BASE = "week26_csp_payoff"

STRIKE = 90.0
PREMIUM = 2.0
CONTRACT = 100  # shares per contract


LANG_STRINGS = {
    "en": {
        "title":       "Cash-secured put as a paid limit buy order",
        "subtitle":    "Sold $90 put on XYZ, $2.00 premium, 30 days. P&L per 1 contract (= 100 shares) at expiry.",
        "xlabel":      "XYZ price at expiry ($)",
        "ylabel":      "P&L per contract ($)",
        "trace":       "Short $90 put P&L",
        "be":          "breakeven $88",
        "maxp":        "max profit +$200",
        "maxl":        "max loss -$8,800 (XYZ → $0)",
        "shade_gain":  "premium kept",
        "shade_loss":  "below breakeven",
        "footer":      "Collateral: $90 x 100 = $9,000 cash reserved. Annualised yield-on-cash if expires worthless: ~27%.",
    },
    "hk": {
        "title":       "現金擔保賣權 = 有人付錢的限價買單",
        "subtitle":    "賣出 XYZ $90 賣權,權利金 $2.00,30 日到期。每張合約(100 股)到期損益。",
        "xlabel":      "XYZ 到期價(美元)",
        "ylabel":      "每張合約損益(美元)",
        "trace":       "賣出 $90 賣權損益",
        "be":          "打和點 $88",
        "maxp":        "最大利潤 +$200",
        "maxl":        "最大虧損 -$8,800(XYZ → $0)",
        "shade_gain":  "全收權利金",
        "shade_loss":  "跌穿打和點",
        "footer":      "擔保金:$90 x 100 = $9,000 現金鎖定。權利金過期作廢時,以擔保金計年化收益 ~27%。",
    },
    "tw": {
        "title":       "現金擔保賣權 = 對方付你錢的限價買單",
        "subtitle":    "賣出 XYZ $90 賣權,權利金 $2.00,30 天到期。每張合約(100 股)到期損益。",
        "xlabel":      "XYZ 到期價(美元)",
        "ylabel":      "每張合約損益(美元)",
        "trace":       "賣出 $90 賣權損益",
        "be":          "損益兩平 $88",
        "maxp":        "最大利潤 +$200",
        "maxl":        "最大虧損 -$8,800(XYZ → $0)",
        "shade_gain":  "全收權利金",
        "shade_loss":  "跌破兩平點",
        "footer":      "擔保金:$90 x 100 = $9,000 現金鎖定。權利金過期作廢時,以擔保金計年化收益約 27%。",
    },
    "cn": {
        "title":       "现金担保卖权 = 对方付你钱的限价买单",
        "subtitle":    "卖出 XYZ $90 卖权,权利金 $2.00,30 天到期。每张合约(100 股)到期损益。",
        "xlabel":      "XYZ 到期价(美元)",
        "ylabel":      "每张合约损益(美元)",
        "trace":       "卖出 $90 卖权损益",
        "be":          "盈亏平衡 $88",
        "maxp":        "最大利润 +$200",
        "maxl":        "最大亏损 -$8,800(XYZ → $0)",
        "shade_gain":  "全收权利金",
        "shade_loss":  "跌破平衡点",
        "footer":      "担保金:$90 x 100 = $9,000 现金锁定。权利金过期作废时,以担保金计年化收益约 27%。",
    },
}


def _short_put_pnl(s: np.ndarray) -> np.ndarray:
    """P&L per contract for a short put at STRIKE with PREMIUM."""
    intrinsic = np.maximum(STRIKE - s, 0.0)
    return (PREMIUM - intrinsic) * CONTRACT


def build_fig(s):
    apply_cjk_font()
    p = PALETTE_LIGHT
    # Escape '$' so matplotlib does not enter mathtext (would break CJK).
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    x = np.linspace(60.0, 140.0, 401)
    pnl = _short_put_pnl(x)
    breakeven = STRIKE - PREMIUM  # 88
    max_profit = PREMIUM * CONTRACT  # 200
    max_loss_at_zero = (PREMIUM - STRIKE) * CONTRACT  # -8800 at S=0

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    style_axes(ax, p)

    # Shaded regions
    ax.fill_between(x, pnl, 0, where=(pnl >= 0),
                    color=p["green"], alpha=0.16, linewidth=0,
                    label=s["shade_gain"])
    ax.fill_between(x, pnl, 0, where=(pnl < 0),
                    color=p["red"], alpha=0.16, linewidth=0,
                    label=s["shade_loss"])
    ax.plot(x, pnl, color=p["blue"], linewidth=2.6, label=s["trace"])

    # Reference lines
    ax.axhline(0, color=p["muted"], linewidth=0.8, alpha=0.6)
    ax.axvline(STRIKE, color=p["muted"], linewidth=0.8,
               linestyle=":", alpha=0.7)
    ax.axvline(breakeven, color=p["accent"], linewidth=1.0,
               linestyle="--", alpha=0.85)

    # Markers
    ax.scatter([breakeven], [0], s=55, color=p["accent"],
               zorder=5, edgecolor=p["bg"], linewidth=1.2)
    ax.scatter([STRIKE], [max_profit], s=55, color=p["green"],
               zorder=5, edgecolor=p["bg"], linewidth=1.2)

    # Annotations
    ax.annotate(s["be"], xy=(breakeven, 0),
                xytext=(breakeven - 12, -1500),
                fontsize=9.5, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=p["accent"],
                                lw=0.8, alpha=0.7))
    ax.annotate(s["maxp"], xy=(STRIKE + 8, max_profit),
                xytext=(STRIKE + 18, 1200),
                fontsize=9.5, color=p["green"], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=p["green"],
                                lw=0.8, alpha=0.7))
    ax.annotate(s["maxl"], xy=(60.5, _short_put_pnl(np.array([60.0]))[0]),
                xytext=(62, -2400),
                fontsize=9.5, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=p["red"],
                                lw=0.8, alpha=0.7))
    ax.text(STRIKE + 0.4, -250, "strike \\$90",
            fontsize=8.5, color=p["muted"], style="italic")

    ax.set_xlim(60, 140)
    ax.set_ylim(-3200, 1500)
    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_xticks([60, 70, 80, 88, 90, 100, 110, 120, 130, 140])
    ax.set_yticks([-3000, -2000, -1000, 0, 200, 1000])
    ax.set_yticklabels(["-3000", "-2000", "-1000", "0", "+200", ""])

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold",
                 color=p["fg"])
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=9, color=p["muted"])

    ax.legend(loc="lower right", frameon=False, fontsize=9.5)
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
