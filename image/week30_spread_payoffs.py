"""Week 30, §2.1 - 2x2 payoff diagrams for the four defined-risk structures.

Bull call spread (debit), bear put spread (debit), iron condor (credit),
and long butterfly (debit) shown at expiry on a single $100-anchored
underlying. Each panel marks max profit, max loss, and breakeven so the
formulas in the markdown can be verified against the picture.

Run:
    uv run python course/image/week30_spread_payoffs.py
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
BASE = "week30_spread_payoffs"


# ---- Payoff helpers (per share, will scale by 100 for per-contract). ----
def _call(s, k):
    return np.maximum(s - k, 0.0)


def _put(s, k):
    return np.maximum(k - s, 0.0)


# Spot anchor for all four panels.
SPOT = 100.0
S = np.linspace(70.0, 130.0, 601)


def _bull_call_spread():
    # Buy 95C at 6.50, sell 105C at 2.50. Debit = 4.00.
    debit = 4.0
    pnl = (_call(S, 95.0) - _call(S, 105.0) - debit) * 100.0
    return {
        "S": S, "pnl": pnl,
        "max_profit": (10.0 - debit) * 100.0,
        "max_loss":   -debit * 100.0,
        "breakeven":  95.0 + debit,
        "k_low": 95.0, "k_high": 105.0,
    }


def _bear_put_spread():
    # Buy 105P at 6.50, sell 95P at 2.50. Debit = 4.00.
    debit = 4.0
    pnl = (_put(S, 105.0) - _put(S, 95.0) - debit) * 100.0
    return {
        "S": S, "pnl": pnl,
        "max_profit": (10.0 - debit) * 100.0,
        "max_loss":   -debit * 100.0,
        "breakeven":  105.0 - debit,
        "k_low": 95.0, "k_high": 105.0,
    }


def _iron_condor():
    # Sell 90P at 1.20, buy 85P at 0.55, sell 110C at 1.05, buy 115C at 0.50.
    # Credit = 1.20 - 0.55 + 1.05 - 0.50 = 1.20.
    credit = 1.20
    pnl = (
        -_put(S, 90.0) + _put(S, 85.0)
        - _call(S, 110.0) + _call(S, 115.0)
        + credit
    ) * 100.0
    return {
        "S": S, "pnl": pnl,
        "max_profit": credit * 100.0,
        "max_loss":   -(5.0 - credit) * 100.0,
        "be_low":  90.0 - credit,
        "be_high": 110.0 + credit,
        "k_short_p": 90.0, "k_long_p": 85.0,
        "k_short_c": 110.0, "k_long_c": 115.0,
    }


def _butterfly():
    # Long $90C at 11.00, short 2 $100C at 5.00, long $110C at 1.20.
    # Debit = 11.00 - 10.00 + 1.20 = 2.20.
    debit = 2.20
    pnl = (
        _call(S, 90.0) - 2.0 * _call(S, 100.0) + _call(S, 110.0) - debit
    ) * 100.0
    return {
        "S": S, "pnl": pnl,
        "max_profit": (10.0 - debit) * 100.0,
        "max_loss":   -debit * 100.0,
        "be_low":  90.0 + debit,
        "be_high": 110.0 - debit,
        "k_low": 90.0, "k_mid": 100.0, "k_high": 110.0,
    }


LANG_STRINGS = {
    "en": {
        "title":   "The four defined-risk option structures at expiry",
        "subtitle":"$100 underlying, 30 DTE, IV~22%. P&L per 1 contract (= 100 shares).",
        "xlabel":  "Underlying price at expiry ($)",
        "ylabel":  "P&L per contract ($)",
        "p1":      "Bull call spread - long $95C, short $105C",
        "p2":      "Bear put spread - long $105P, short $95P",
        "p3":      "Iron condor - 90/85 put + 110/115 call",
        "p4":      "Long butterfly - long $90C, short 2x $100C, long $110C",
        "maxp":    "max profit",
        "maxl":    "max loss",
        "be":      "breakeven",
        "footer":  "Debit structures pay debit, capped profit. Credit structures collect credit, capped loss. Width and credit choose the shape; distance from spot chooses the probability.",
    },
    "hk": {
        "title":   "四種定額風險期權結構到期損益",
        "subtitle":"標的 $100,30 日到期,IV~22%。每張合約(100 股)損益。",
        "xlabel":  "到期標的價(美元)",
        "ylabel":  "每張合約損益(美元)",
        "p1":      "牛市認購差價 - 買 $95C 賣 $105C",
        "p2":      "熊市認沽差價 - 買 $105P 賣 $95P",
        "p3":      "鐵兀鷹 - 90/85 賣權 + 110/115 認購",
        "p4":      "蝴蝶 - 買 $90C 賣 2 張 $100C 買 $110C",
        "maxp":    "最大利潤",
        "maxl":    "最大虧損",
        "be":      "打和點",
        "footer":  "借記結構付權利金、利潤封頂;貸記結構收權利金、虧損封頂。寬度與權利金決定形狀,距現價決定機率。",
    },
    "tw": {
        "title":   "四種定額風險選擇權結構到期損益",
        "subtitle":"標的 $100,30 天到期,IV~22%。每張合約(100 股)損益。",
        "xlabel":  "到期標的價(美元)",
        "ylabel":  "每張合約損益(美元)",
        "p1":      "牛市買權價差 - 買 $95C 賣 $105C",
        "p2":      "熊市賣權價差 - 買 $105P 賣 $95P",
        "p3":      "鐵兀鷹 - 90/85 賣權 + 110/115 買權",
        "p4":      "蝴蝶 - 買 $90C 賣 2 張 $100C 買 $110C",
        "maxp":    "最大利潤",
        "maxl":    "最大虧損",
        "be":      "損益兩平",
        "footer":  "支付型結構付權利金、利潤上限;收取型結構收權利金、虧損上限。寬度與權利金決定形狀,距現價決定機率。",
    },
    "cn": {
        "title":   "四种定额风险期权结构到期损益",
        "subtitle":"标的 $100,30 日到期,IV~22%。每张合约(100 股)损益。",
        "xlabel":  "到期标的价(美元)",
        "ylabel":  "每张合约损益(美元)",
        "p1":      "牛市看涨价差 - 买 $95C 卖 $105C",
        "p2":      "熊市看跌价差 - 买 $105P 卖 $95P",
        "p3":      "铁鹰 - 90/85 卖权 + 110/115 看涨",
        "p4":      "蝶式 - 买 $90C 卖 2 张 $100C 买 $110C",
        "maxp":    "最大利润",
        "maxl":    "最大亏损",
        "be":      "盈亏平衡",
        "footer":  "借记结构付权利金、利润封顶;贷记结构收权利金、亏损封顶。宽度与权利金决定形状,距现价决定概率。",
    },
}


def _draw_panel(ax, p, data, title_text, s, single_be=True):
    x = data["S"]
    y = data["pnl"]
    ax.plot(x, y, color=p["blue"], linewidth=2.4)
    ax.fill_between(x, y, 0, where=(y >= 0),
                    color=p["green"], alpha=0.16, linewidth=0)
    ax.fill_between(x, y, 0, where=(y < 0),
                    color=p["red"], alpha=0.16, linewidth=0)
    ax.axhline(0, color=p["muted"], linewidth=0.7, alpha=0.6)

    # Strike guide lines.
    for k in [data.get("k_low"), data.get("k_high"), data.get("k_mid"),
              data.get("k_short_p"), data.get("k_long_p"),
              data.get("k_short_c"), data.get("k_long_c")]:
        if k is not None:
            ax.axvline(k, color=p["muted"], linewidth=0.6,
                       linestyle=":", alpha=0.5)

    # Marks.
    mp = data["max_profit"]
    ml = data["max_loss"]
    ax.axhline(mp, color=p["green"], linewidth=0.6, linestyle="--", alpha=0.5)
    ax.axhline(ml, color=p["red"],   linewidth=0.6, linestyle="--", alpha=0.5)

    # Annotations.
    ymin, ymax = ax.get_ylim()
    ax.annotate(s["maxp"] + " +\\$" + f"{mp:.0f}",
                xy=(127, mp), xytext=(127, mp),
                fontsize=8.4, color=p["green"], fontweight="bold",
                ha="right", va="bottom")
    ax.annotate(s["maxl"] + " -\\$" + f"{abs(ml):.0f}",
                xy=(73, ml), xytext=(73, ml),
                fontsize=8.4, color=p["red"], fontweight="bold",
                ha="left", va="top")

    if single_be:
        be = data["breakeven"]
        ax.axvline(be, color=p["accent"], linewidth=1.0,
                   linestyle="--", alpha=0.85)
        ax.scatter([be], [0], s=42, color=p["accent"],
                   zorder=5, edgecolor=p["bg"], linewidth=1.0)
        ax.annotate(s["be"] + " \\$" + f"{be:.2f}",
                    xy=(be, 0), xytext=(be + 0.6, ymax * 0.45),
                    fontsize=8.4, color=p["accent"], fontweight="bold")
    else:
        for be in (data["be_low"], data["be_high"]):
            ax.axvline(be, color=p["accent"], linewidth=1.0,
                       linestyle="--", alpha=0.85)
            ax.scatter([be], [0], s=36, color=p["accent"],
                       zorder=5, edgecolor=p["bg"], linewidth=1.0)
        ax.annotate(s["be"] + " \\$" + f"{data['be_low']:.2f} / \\$"
                    + f"{data['be_high']:.2f}",
                    xy=(SPOT, 0), xytext=(SPOT, ymax * 0.55),
                    fontsize=8.2, color=p["accent"], fontweight="bold",
                    ha="center")

    style_axes(ax, p)
    ax.set_title(title_text, fontsize=10.8, fontweight="bold",
                 color=p["fg"], loc="left", pad=6)
    ax.set_xlabel(s["xlabel"], fontsize=9.2, color=p["muted"])
    ax.set_ylabel(s["ylabel"], fontsize=9.2, color=p["muted"])
    ax.set_xlim(70, 130)


def build_fig(s):
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v)
         for k, v in s.items()}

    bcs = _bull_call_spread()
    bps = _bear_put_spread()
    icd = _iron_condor()
    bfly = _butterfly()

    fig, axs = plt.subplots(2, 2, figsize=(13.0, 8.0))
    fig.patch.set_facecolor(p["bg"])

    _draw_panel(axs[0, 0], p, bcs, s["p1"], s, single_be=True)
    _draw_panel(axs[0, 1], p, bps, s["p2"], s, single_be=True)
    _draw_panel(axs[1, 0], p, icd, s["p3"], s, single_be=False)
    _draw_panel(axs[1, 1], p, bfly, s["p4"], s, single_be=False)

    fig.suptitle(s["title"], fontsize=14.5, fontweight="bold",
                 color=p["fg"], x=0.02, ha="left", y=0.985)
    fig.text(0.02, 0.948, s["subtitle"], fontsize=10,
             color=p["muted"], style="italic")
    fig.text(0.5, 0.012, s["footer"], ha="center",
             fontsize=9, color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.035, 1, 0.93])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
