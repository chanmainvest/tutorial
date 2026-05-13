"""Week 47, §2.3 — Tail-hedge payoff in a -30% crash scenario.

$100,000 in SPY plus a $1,000 quarterly tail-hedge sleeve allocated to
deep-OTM SPY puts. The sleeve is modelled as ~5 contracts of 90-day
SPY puts struck at 15% OTM (strike $440 with spot $520, premium $2.10,
~5 contracts = $1050 spend). Payoff is the put intrinsic value at
expiry minus the premium paid; portfolio P&L is unhedged stock P&L
plus hedge sleeve P&L.

The chart shows two lines vs. the SPY return at expiry: the
unhedged $100k (straight diagonal) and the hedged total (kinked
upward by the convex put payout below the strike).

Run:
    uv run python course/image/week47_tail_hedge_payoff.py
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
BASE = "week47_tail_hedge_payoff"

# ----- scenario parameters -----
NAV = 100_000.0          # base portfolio value (all SPY)
SPOT = 520.0             # SPY spot
STRIKE = 440.0           # put strike (~15% OTM)
PREMIUM = 2.10           # per-share BSM put premium at sigma=0.19, r=0.043, q=0.013, T=0.25
N_CONTRACTS = 5          # 5 contracts -> 500 shares notional, $1050 spend
HEDGE_SPEND = N_CONTRACTS * 100 * PREMIUM   # ~ $1050
SHARES = NAV / SPOT       # ~192.3 shares of SPY

LANG_STRINGS = {
    "en": {
        "title": "Tail-hedge payoff: \\$100k SPY + \\$1k OTM puts in a crash",
        "subtitle": "5 SPY 90-DTE puts struck \\$440 (~15% OTM), \\$2.10 premium each. Hedged P&L kinks upward below strike.",
        "xlabel": "SPY return at expiry",
        "ylabel": "Total portfolio P&L (\\$)",
        "unh": "Unhedged \\$100k SPY",
        "hed": "Hedged: \\$100k SPY + 5 puts",
        "scen": "Crash scenarios",
        "annot_30": "-30%: unhedged -\\$30k\nhedged ~ flat",
        "annot_50": "-50%: hedge\npays out ~\\$50k",
    },
    "hk": {
        "title": "尾部對沖損益:\\$10萬標普 + \\$1k OTM 認沽",
        "subtitle": "5 張 90DTE SPY 認沽,行使價 \\$440(15% OTM),每張權利金 \\$2.10。對沖後損益在行使價下方折升。",
        "xlabel": "到期 SPY 回報",
        "ylabel": "組合總損益 (\\$)",
        "unh": "無對沖 \\$10 萬 SPY",
        "hed": "對沖:\\$10 萬 SPY + 5 張認沽",
        "scen": "崩盤情境",
        "annot_30": "-30%:無對沖 -\\$3 萬\n對沖後約打和",
        "annot_50": "-50%:對沖\n派出 ~\\$5 萬",
    },
    "tw": {
        "title": "尾部對沖損益:\\$10萬標普 + \\$1k OTM 賣權",
        "subtitle": "5 張 90DTE SPY 賣權,履約價 \\$440(15% OTM),每張權利金 \\$2.10。對沖後損益在履約價下方折升。",
        "xlabel": "到期 SPY 報酬",
        "ylabel": "組合總損益 (\\$)",
        "unh": "未避險 \\$10 萬 SPY",
        "hed": "避險:\\$10 萬 SPY + 5 張賣權",
        "scen": "崩盤情境",
        "annot_30": "-30%:未避險 -\\$3 萬\n避險後約打平",
        "annot_50": "-50%:避險\n支付 ~\\$5 萬",
    },
    "cn": {
        "title": "尾部对冲损益:\\$10万标普 + \\$1k OTM 看跌",
        "subtitle": "5 张 90DTE SPY 看跌,行权价 \\$440(15% OTM),每张权利金 \\$2.10。对冲后损益在行权价下方折升。",
        "xlabel": "到期 SPY 回报",
        "ylabel": "组合总损益 (\\$)",
        "unh": "无对冲 \\$10 万 SPY",
        "hed": "对冲:\\$10 万 SPY + 5 张看跌",
        "scen": "崩盘情境",
        "annot_30": "-30%:无对冲 -\\$3 万\n对冲后约打平",
        "annot_50": "-50%:对冲\n派出 ~\\$5 万",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    rets = np.linspace(-0.55, 0.20, 401)
    spy_at_exp = SPOT * (1.0 + rets)

    # Stock P&L per share = (S_T - S_0); times shares
    stock_pnl = SHARES * (spy_at_exp - SPOT)
    # Put intrinsic at expiry per share = max(K - S_T, 0); times notional shares.
    put_intr = np.maximum(STRIKE - spy_at_exp, 0.0)
    hedge_pnl = N_CONTRACTS * 100 * put_intr - HEDGE_SPEND
    total_hedged = stock_pnl + hedge_pnl

    fig, ax = plt.subplots(figsize=(11, 6.0), dpi=150)
    style_axes(ax, p)

    # Zero line.
    ax.axhline(0, color=p["fg"], linewidth=0.8, zorder=2)

    # Unhedged: dashed muted.
    ax.plot(rets, stock_pnl, color=p["red"], linewidth=2.2,
            linestyle="--", label=s["unh"], zorder=3)
    # Hedged: heavy navy.
    ax.plot(rets, total_hedged, color=p["blue"], linewidth=3.0,
            label=s["hed"], zorder=4)

    # Scenario verticals.
    for r, lab in [(-0.10, "-10%"), (-0.20, "-20%"),
                   (-0.30, "-30%"), (-0.50, "-50%")]:
        ax.axvline(r, color=p["muted"], linewidth=0.8,
                   linestyle=":", alpha=0.6, zorder=1)
        ax.text(r, ax.get_ylim()[1] if False else 25_000, lab,
                color=p["muted"], fontsize=8.5, ha="center",
                va="bottom", zorder=2)

    # Annotations at -30% and -50%.
    idx_30 = np.argmin(np.abs(rets - (-0.30)))
    idx_50 = np.argmin(np.abs(rets - (-0.50)))
    ax.annotate(s["annot_30"],
                xy=(-0.30, total_hedged[idx_30]),
                xytext=(-0.34, -42_000),
                fontsize=9, color=p["fg"], ha="center",
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))
    ax.annotate(s["annot_50"],
                xy=(-0.50, total_hedged[idx_50]),
                xytext=(-0.42, 30_000),
                fontsize=9, color=p["fg"], ha="center",
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(-0.55, 0.20)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda v, _: f"-${abs(v)/1000:.0f}k" if v < 0 else f"${v/1000:.0f}k"))
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
