"""Week 28, §2.1 — CSP annualized yield by strike-delta.

Black-Scholes premium for 30-day puts on a synthetic $100 stock at
six target deltas (0.10, 0.16, 0.25, 0.30, 0.40, 0.50). Sigma fixed
at 22%, risk-free 4%. The bar is annualized premium yield on cash
collateral, computed as (premium / strike) * (365 / 30). Shows the
non-linear payoff for moving toward the money: the 50-delta pays
roughly 5-6x the 10-delta in annualized terms but has 5x the
assignment probability.

Run:
    uv run python course/image/week28_csp_yield_curve.py
"""

from __future__ import annotations

import sys
from math import erf, exp, log, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week28_csp_yield_curve"


# Black-Scholes for European put on non-dividend stock.
def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def bs_put(s: float, k: float, r: float, sigma: float, t: float) -> float:
    d1 = (log(s / k) + (r + 0.5 * sigma * sigma) * t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    return k * exp(-r * t) * _norm_cdf(-d2) - s * _norm_cdf(-d1)


def put_delta(s: float, k: float, r: float, sigma: float, t: float) -> float:
    """|delta| of a put = N(-d1). Returns positive number 0..1."""
    d1 = (log(s / k) + (r + 0.5 * sigma * sigma) * t) / (sigma * sqrt(t))
    return _norm_cdf(-d1)


def strike_for_delta(target_delta: float, s: float, r: float, sigma: float, t: float) -> float:
    """Bisect for the strike whose put |delta| equals target_delta."""
    lo, hi = 0.4 * s, s
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        d = put_delta(s, mid, r, sigma, t)
        if d < target_delta:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# Inputs.
S = 100.0
SIGMA = 0.22
R = 0.04
T = 30.0 / 365.0
DELTAS = [0.10, 0.16, 0.25, 0.30, 0.40, 0.50]

ROWS = []
for d in DELTAS:
    k = strike_for_delta(d, S, R, SIGMA, T)
    prem = bs_put(S, k, R, SIGMA, T)
    yield_ann = (prem / k) * (365.0 / 30.0) * 100.0  # percent annualized
    otm_pct = (S - k) / S * 100.0
    ROWS.append({"delta": d, "strike": k, "prem": prem,
                 "yield_ann": yield_ann, "otm_pct": otm_pct})


LANG_STRINGS = {
    "en": {
        "title":    "Cash-secured put: annualized premium yield by strike-delta",
        "subtitle": "30-day puts on a $100 stock, Black-Scholes (sigma=22%, r=4%). Bars show premium-yield only; add ~4% T-bill yield on collateral for total cash yield.",
        "xlabel":   "Target put delta (~ assignment probability)",
        "ylabel":   "Annualized premium yield (%)",
        "footer":   "The 50-delta (ATM) put pays ~6x the 10-delta in premium yield, but has ~5x the assignment probability. Higher yield is not edge; it is risk priced.",
        "bar_label": "{y:.1f}%",
        "strike_label": "K=\\${k:.2f}\n({otm:.1f}% OTM)",
    },
    "hk": {
        "title":    "現金擔保賣權:年化權利金收益率隨 Delta 變化",
        "subtitle": "100 美元股票、30 天賣權,Black-Scholes(σ=22%、r=4%)。柱形只計權利金收益;加上約 4% 的國庫券收益才是現金總收益率。",
        "xlabel":   "目標賣權 Delta(約等於被指派機率)",
        "ylabel":   "年化權利金收益率(%)",
        "footer":   "50-delta(平價)賣權的權利金收益約是 10-delta 的 6 倍,但被指派機率也高出約 5 倍。更高收益不是優勢,是風險的代價。",
        "bar_label": "{y:.1f}%",
        "strike_label": "K=\\${k:.2f}\n(價外 {otm:.1f}%)",
    },
    "tw": {
        "title":    "現金擔保賣權:年化權利金收益率隨 Delta 變化",
        "subtitle": "100 美元股票、30 天賣權,Black-Scholes(σ=22%、r=4%)。柱形只計權利金收益;加上約 4% 的國庫券收益才是現金總收益率。",
        "xlabel":   "目標賣權 Delta(約等於被指派機率)",
        "ylabel":   "年化權利金收益率(%)",
        "footer":   "50-delta(平價)賣權的權利金收益約是 10-delta 的 6 倍,但被指派機率也高出約 5 倍。較高收益不是優勢,而是風險的定價。",
        "bar_label": "{y:.1f}%",
        "strike_label": "K=\\${k:.2f}\n(價外 {otm:.1f}%)",
    },
    "cn": {
        "title":    "现金担保卖权:年化权利金收益率随 Delta 变化",
        "subtitle": "100 美元股票、30 天卖权,Black-Scholes(σ=22%、r=4%)。柱形只计权利金收益;加上约 4% 的国库券收益才是现金总收益率。",
        "xlabel":   "目标卖权 Delta(约等于被指派概率)",
        "ylabel":   "年化权利金收益率(%)",
        "footer":   "50-delta(平价)卖权的权利金收益约为 10-delta 的 6 倍,但被指派概率也高出约 5 倍。更高收益不是优势,而是风险的定价。",
        "bar_label": "{y:.1f}%",
        "strike_label": "K=\\${k:.2f}\n(价外 {otm:.1f}%)",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.6, 6.2))
    style_axes(ax, p)

    deltas = [r["delta"] for r in ROWS]
    yields = [r["yield_ann"] for r in ROWS]
    strikes = [r["strike"] for r in ROWS]
    otms = [r["otm_pct"] for r in ROWS]
    xs = np.arange(len(deltas))

    # Color gradient: low-delta = blue (safer), high-delta = red (risky).
    cmap = [p["blue"], p["teal"], p["accent"], p["orange"], p["red"], p["purple"]]
    bars = ax.bar(xs, yields, color=cmap, edgecolor=p["fg"], linewidth=0.6, width=0.7)

    for i, (bar, y, k, otm) in enumerate(zip(bars, yields, strikes, otms)):
        # Top label: yield.
        ax.text(bar.get_x() + bar.get_width() / 2, y + 0.6,
                s["bar_label"].format(y=y),
                ha="center", va="bottom", fontsize=10.5,
                fontweight="bold", color=p["fg"])
        # Inside-bar label: strike + OTM%.
        lbl = s["strike_label"].format(k=k, otm=otm)
        ax.text(bar.get_x() + bar.get_width() / 2, y * 0.45,
                lbl, ha="center", va="center", fontsize=9,
                color="white", fontweight="bold")

    ax.set_xticks(xs)
    ax.set_xticklabels([f"{int(d*100)}\u0394" for d in deltas])
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, max(yields) * 1.18)
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontweight="bold")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
