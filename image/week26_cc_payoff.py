"""Week 26, §2.3 - Covered call payoff diagram.

Long 100 shares of XYZ at $100 + sold 1 $110 call at $1.50 with 30
days to expiry. Payoff per package over a stock-price grid from $60
to $140. Marks: breakeven $98.50, max profit +$1,150 (capped at any
S >= $110), downside slope to -$9,850 at S = $0.

Run:
    uv run python course/image/week26_cc_payoff.py
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
BASE = "week26_cc_payoff"

ENTRY = 100.0          # cost basis of the 100 shares
STRIKE = 110.0
PREMIUM = 1.50
CONTRACT = 100


LANG_STRINGS = {
    "en": {
        "title":       "Covered call as a paid limit sell order",
        "subtitle":    "Long 100 XYZ @ $100 + sold $110 call for $1.50 (30 days). Package P&L at expiry.",
        "xlabel":      "XYZ price at expiry ($)",
        "ylabel":      "Package P&L ($)",
        "trace":       "Long stock + short $110 call",
        "trace_stock": "Long stock alone (reference)",
        "be":          "breakeven $98.50",
        "maxp":        "max profit +$1,150 (capped above $110)",
        "maxl":        "max loss -$9,850 (XYZ → $0)",
        "shade_gain":  "in profit",
        "shade_loss":  "in loss",
        "footer":      "Covered call is cushion (~$150), not hedge. Premium income, capped upside, near-stock downside.",
    },
    "hk": {
        "title":       "備兌認購 = 有人付錢的限價賣單",
        "subtitle":    "持有 100 股 XYZ @ $100 + 賣出 $110 認購期權 $1.50(30 日)。組合到期損益。",
        "xlabel":      "XYZ 到期價(美元)",
        "ylabel":      "組合損益(美元)",
        "trace":       "持股 + 賣出 $110 認購",
        "trace_stock": "單純持股(對照)",
        "be":          "打和點 $98.50",
        "maxp":        "最大利潤 +$1,150(超過 $110 後封頂)",
        "maxl":        "最大虧損 -$9,850(XYZ → $0)",
        "shade_gain":  "獲利區",
        "shade_loss":  "虧損區",
        "footer":      "備兌認購是緩衝(~$150),不是對沖。有權利金收入、上行封頂、下行幾乎與持股相同。",
    },
    "tw": {
        "title":       "掩護性買權 = 對方付你錢的限價賣單",
        "subtitle":    "持有 100 股 XYZ @ $100 + 賣出 $110 買權 $1.50(30 天)。組合到期損益。",
        "xlabel":      "XYZ 到期價(美元)",
        "ylabel":      "組合損益(美元)",
        "trace":       "持股 + 賣出 $110 買權",
        "trace_stock": "單純持股(對照)",
        "be":          "損益兩平 $98.50",
        "maxp":        "最大利潤 +$1,150($110 以上封頂)",
        "maxl":        "最大虧損 -$9,850(XYZ → $0)",
        "shade_gain":  "獲利區",
        "shade_loss":  "虧損區",
        "footer":      "掩護性買權是緩衝(~$150),不是避險。有權利金、上行封頂、下行幾乎等同持股。",
    },
    "cn": {
        "title":       "备兑看涨 = 对方付你钱的限价卖单",
        "subtitle":    "持有 100 股 XYZ @ $100 + 卖出 $110 看涨期权 $1.50(30 天)。组合到期损益。",
        "xlabel":      "XYZ 到期价(美元)",
        "ylabel":      "组合损益(美元)",
        "trace":       "持股 + 卖出 $110 看涨",
        "trace_stock": "单纯持股(对照)",
        "be":          "盈亏平衡 $98.50",
        "maxp":        "最大利润 +$1,150($110 以上封顶)",
        "maxl":        "最大亏损 -$9,850(XYZ → $0)",
        "shade_gain":  "获利区",
        "shade_loss":  "亏损区",
        "footer":      "备兑看涨是缓冲(~$150),不是对冲。有权利金、上行封顶、下行几乎等同持股。",
    },
}


def _cc_pnl(s: np.ndarray) -> np.ndarray:
    """Covered-call package P&L: 100*(S-100) + 150 - 100*max(S-110, 0)."""
    stock_pnl = (s - ENTRY) * CONTRACT
    short_call_pnl = PREMIUM * CONTRACT - np.maximum(s - STRIKE, 0.0) * CONTRACT
    return stock_pnl + short_call_pnl


def _stock_only(s: np.ndarray) -> np.ndarray:
    return (s - ENTRY) * CONTRACT


def build_fig(s):
    apply_cjk_font()
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    x = np.linspace(60.0, 140.0, 401)
    pnl = _cc_pnl(x)
    pnl_stock = _stock_only(x)
    breakeven = ENTRY - PREMIUM       # 98.50
    max_profit = (STRIKE - ENTRY + PREMIUM) * CONTRACT  # 1150

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    style_axes(ax, p)

    # Shaded regions for the package
    ax.fill_between(x, pnl, 0, where=(pnl >= 0),
                    color=p["green"], alpha=0.16, linewidth=0,
                    label=s["shade_gain"])
    ax.fill_between(x, pnl, 0, where=(pnl < 0),
                    color=p["red"], alpha=0.16, linewidth=0,
                    label=s["shade_loss"])

    # Stock-only reference (dashed)
    ax.plot(x, pnl_stock, color=p["muted"], linewidth=1.4,
            linestyle="--", alpha=0.85, label=s["trace_stock"])
    # Package
    ax.plot(x, pnl, color=p["blue"], linewidth=2.6, label=s["trace"])

    # Reference lines
    ax.axhline(0, color=p["muted"], linewidth=0.8, alpha=0.6)
    ax.axvline(ENTRY, color=p["muted"], linewidth=0.7,
               linestyle=":", alpha=0.55)
    ax.axvline(STRIKE, color=p["muted"], linewidth=0.7,
               linestyle=":", alpha=0.55)
    ax.axvline(breakeven, color=p["accent"], linewidth=1.0,
               linestyle="--", alpha=0.85)

    # Markers
    ax.scatter([breakeven], [0], s=55, color=p["accent"],
               zorder=5, edgecolor=p["bg"], linewidth=1.2)
    ax.scatter([STRIKE], [max_profit], s=60, color=p["green"],
               zorder=5, edgecolor=p["bg"], linewidth=1.2)

    # Annotations
    ax.annotate(s["be"], xy=(breakeven, 0),
                xytext=(breakeven - 18, -2200),
                fontsize=9.5, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=p["accent"],
                                lw=0.8, alpha=0.7))
    ax.annotate(s["maxp"], xy=(STRIKE + 1, max_profit),
                xytext=(116, 2200),
                fontsize=9.5, color=p["green"], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=p["green"],
                                lw=0.8, alpha=0.7))
    ax.annotate(s["maxl"], xy=(60.5, _cc_pnl(np.array([60.0]))[0]),
                xytext=(62, -3500),
                fontsize=9.5, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=p["red"],
                                lw=0.8, alpha=0.7))
    ax.text(ENTRY + 0.3, -250, "entry \\$100",
            fontsize=8.5, color=p["muted"], style="italic")
    ax.text(STRIKE + 0.3, -250, "strike \\$110",
            fontsize=8.5, color=p["muted"], style="italic")

    ax.set_xlim(60, 140)
    ax.set_ylim(-4200, 4200)
    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_xticks([60, 70, 80, 90, 98.5, 100, 110, 120, 130, 140])
    ax.set_xticklabels(["60", "70", "80", "90", "98.5", "100",
                        "110", "120", "130", "140"])
    ax.set_yticks([-4000, -3000, -2000, -1000, 0, 1150, 3000, 4000])
    ax.set_yticklabels(["-4000", "-3000", "-2000", "-1000", "0",
                        "+1150", "+3000", "+4000"])

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold",
                 color=p["fg"])
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=9, color=p["muted"])

    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
