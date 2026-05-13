"""Week 37, §2.1 - Capital required for $10k SPY exposure across instruments.

Five-bar comparison: shares, 0.90D 12mo LEAPS, 0.70D 6mo call, 0.30D 3mo
call, SSO 2x ETF. Each bar splits into capital deployed (solid) and freed
cash earning T-bills (orange shaded extension). Premium values come from
Black-Scholes at SPY=$520, sigma=19%, r=4.3%, dividend yield=1.3%, scaled
to $10,000 of underlying exposure.

Run:
    uv run python course/image/week37_replacement_capital.py
"""

from __future__ import annotations

import math
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
BASE = "week37_replacement_capital"


SQRT_2PI = math.sqrt(2.0 * math.pi)


def _Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bsm_call(S, K, T, sigma, r, q=0.0):
    sqrtT = math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    price = S * math.exp(-q * T) * _Phi(d1) - K * math.exp(-r * T) * _Phi(d2)
    delta = math.exp(-q * T) * _Phi(d1)
    return price, delta


def premium_per_10k(S, K, T, sigma, r, q):
    """Option premium scaled to $10,000 of underlying exposure."""
    price, _ = bsm_call(S, K, T, sigma, r, q)
    # Per $1 of exposure: price / S. Scale to $10k.
    return price / S * 10000.0


# Market anchors (April 2026).
SPY_PX = 520.0
TBILL = 0.043
SIGMA = 0.19
RFREE = 0.043
DIV_YIELD = 0.013

# Five instruments: each is (label_key, capital, color_key, freed_cash, holding_yrs)
def compute_bars():
    # Shares: $10,000 deployed, no freed cash.
    cap_shares = 10000.0
    freed_shares = 0.0

    # 90D LEAPS, K=0.80*S, T=1yr, premium per $10k exposure.
    cap_leaps90 = premium_per_10k(SPY_PX, 0.80 * SPY_PX, 1.00, SIGMA, RFREE, DIV_YIELD)
    freed_leaps90 = 10000.0 - cap_leaps90

    # 70D 6mo call, K=0.92*S, T=0.5yr.
    cap_call70 = premium_per_10k(SPY_PX, 0.92 * SPY_PX, 0.50, SIGMA, RFREE, DIV_YIELD)
    freed_call70 = 10000.0 - cap_call70

    # 30D 3mo call, K=1.06*S, T=0.25yr.
    cap_call30 = premium_per_10k(SPY_PX, 1.06 * SPY_PX, 0.25, SIGMA, RFREE, DIV_YIELD)
    freed_call30 = 10000.0 - cap_call30

    # SSO 2x: half the capital ($5,000) gets you $10,000 exposure.
    cap_sso = 5000.0
    freed_sso = 5000.0

    return [
        ("shares",   cap_shares,   freed_shares,   1.00),
        ("leaps90",  cap_leaps90,  freed_leaps90,  1.00),
        ("call70",   cap_call70,   freed_call70,   0.50),
        ("call30",   cap_call30,   freed_call30,   0.25),
        ("sso",      cap_sso,      freed_sso,      1.00),
    ]


LANG_STRINGS = {
    "en": {
        "title": "Capital required for \\$10,000 of SPY exposure",
        "subtitle": "April 2026 anchors: SPY=\\$520, sigma=19%, r=4.3%, q=1.3%. Solid = capital deployed. Shaded = freed cash earning T-bills (4.3%) over the holding period.",
        "ylabel": "Capital deployed (\\$)",
        "labels": ["100 shares\nof SPY",
                   "0.90D LEAPS\n12-month, K=80%",
                   "0.70D call\n6-month, K=92%",
                   "0.30D call\n3-month, K=106%",
                   "SSO 2x ETF\n(half-capital)"],
        "cap_lab": "Capital",
        "freed_lab": "Freed cash earning T-bills",
        "footer": "Stock replacement = the 0.90D LEAPS bar. Same notional exposure as 100 shares for ~25% of the capital, with 75% earning the risk-free rate.",
    },
    "hk": {
        "title": "取得 1 萬美元 SPY 風險敞口的所需資金",
        "subtitle": "2026 年 4 月基準:SPY=520 美元,sigma=19%,r=4.3%,q=1.3%。實心 = 已投入資金。橙色 = 未動用現金以國庫券利率(4.3%)生息至到期。",
        "ylabel": "投入資金(美元)",
        "labels": ["100 股\nSPY",
                   "0.90D LEAPS\n12 個月,K=80%",
                   "0.70D 認購\n6 個月,K=92%",
                   "0.30D 認購\n3 個月,K=106%",
                   "SSO 2 倍 ETF\n(一半資金)"],
        "cap_lab": "已投入資金",
        "freed_lab": "未動用現金的國庫券收益",
        "footer": "股票替代 = 0.90D LEAPS 那條柱。與 100 股相同的名義敞口,只需約 25% 資金,其餘 75% 賺取無風險利率。",
    },
    "tw": {
        "title": "取得 1 萬美元 SPY 部位所需資金",
        "subtitle": "2026 年 4 月基準:SPY=520 美元,sigma=19%,r=4.3%,q=1.3%。實心 = 投入資金。橙色 = 未動用現金以國庫券利率(4.3%)生息至到期。",
        "ylabel": "投入資金(美元)",
        "labels": ["100 股\nSPY",
                   "0.90D LEAPS\n12 個月,K=80%",
                   "0.70D 買權\n6 個月,K=92%",
                   "0.30D 買權\n3 個月,K=106%",
                   "SSO 2 倍 ETF\n(半額資金)"],
        "cap_lab": "投入資金",
        "freed_lab": "未動用現金的國庫券收益",
        "footer": "股票替代 = 0.90D LEAPS 這根柱。與 100 股相同的名義敞口,只需約 25% 資金,其餘 75% 賺取無風險利率。",
    },
    "cn": {
        "title": "获得 1 万美元 SPY 风险敞口所需资金",
        "subtitle": "2026 年 4 月基准:SPY=520 美元,sigma=19%,r=4.3%,q=1.3%。实心 = 已投入资金。橙色 = 闲置现金以国库券利率(4.3%)生息至到期。",
        "ylabel": "投入资金(美元)",
        "labels": ["100 股\nSPY",
                   "0.90D LEAPS\n12 个月,K=80%",
                   "0.70D 看涨\n6 个月,K=92%",
                   "0.30D 看涨\n3 个月,K=106%",
                   "SSO 2 倍 ETF\n(半额资金)"],
        "cap_lab": "已投入资金",
        "freed_lab": "闲置现金的国库券收益",
        "footer": "股票替代 = 0.90D LEAPS 这根柱。与 100 股相同的名义敞口,只需约 25% 资金,其余 75% 赚取无风险利率。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    bars = compute_bars()
    n = len(bars)
    x = np.arange(n)
    cap_vals = np.array([b[1] for b in bars])
    freed_vals = np.array([b[2] for b in bars])
    holding = np.array([b[3] for b in bars])
    # Treasury yield earned over the holding period (simple).
    tbill_earnings = freed_vals * TBILL * holding

    fig, ax = plt.subplots(figsize=(11.4, 6.6), dpi=150)
    style_axes(ax, p)

    bar_colors = [p["blue"], p["green"], p["accent"], p["red"], p["purple"]]
    # Capital portion (solid).
    ax.bar(x, cap_vals, color=bar_colors, width=0.62,
           edgecolor=p["fg"], linewidth=0.8, label=s["cap_lab"], zorder=3)
    # Freed cash portion stacked on top, lighter shade.
    ax.bar(x, freed_vals, bottom=cap_vals, color=p["orange"],
           alpha=0.32, width=0.62, edgecolor=p["orange"], linewidth=0.8,
           hatch="///", label=s["freed_lab"], zorder=2)

    # Annotate capital + tbill earned.
    for i, (cap, fr, t) in enumerate(zip(cap_vals, freed_vals, tbill_earnings)):
        ax.text(i, cap / 2.0, f"\\${cap:,.0f}", ha="center", va="center",
                fontsize=10.5, fontweight="bold", color="white")
        if fr > 50:
            ax.text(i, cap + fr / 2.0,
                    f"\\${fr:,.0f}\n+\\${t:,.0f}", ha="center", va="center",
                    fontsize=8.7, color=p["fg"])

    ax.set_xticks(x)
    ax.set_xticklabels(s["labels"], fontsize=9.7)
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylim(0, 11000)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _p: f"\\${v:,.0f}"))

    # Reference dashed line at $10,000 (full notional).
    ax.axhline(10000.0, color=p["muted"], linestyle="--", linewidth=0.9, alpha=0.7, zorder=1)

    ax.set_title(s["title"], pad=24, fontsize=15, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.2, color=p["muted"], style="italic")

    ax.legend(loc="upper right", framealpha=0.92, fontsize=9.5)
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print("Wrote:")
    for p in paths:
        print(" ", p)
