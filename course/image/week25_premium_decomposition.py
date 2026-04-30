"""Week 25, §2.4 - Premium decomposition for a 30-day call.

Black-Scholes premium of a European call at K=$100, sigma=20%, r=4%,
T=30 days, plotted against spot S in [50, 150]. The chart shades the
intrinsic-value floor (max(S-K, 0)) and the time-value bump that sits
on top, making concrete why ATM options carry the most time value.

Run:
    uv run python course/image/week25_premium_decomposition.py
"""

from __future__ import annotations

import sys
from math import erf, log, sqrt
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

OUT_DIR = Path(__file__).parent
BASE = "week25_premium_decomposition"

K = 100.0          # strike
SIGMA = 0.20       # implied vol (annualised)
R = 0.04           # risk-free rate
T = 30.0 / 365.0   # 30 days


def _norm_cdf(x: np.ndarray) -> np.ndarray:
    return 0.5 * (1.0 + np.vectorize(erf)(x / sqrt(2.0)))


def bs_call(S, K, r, sigma, T):
    """Black-Scholes call price (no dividends). Vectorised in S."""
    S = np.asarray(S, dtype=float)
    eps = 1e-12
    sqrtT = sqrt(max(T, eps))
    d1 = (np.log(np.maximum(S, eps) / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    return S * _norm_cdf(d1) - K * np.exp(-r * T) * _norm_cdf(d2)


LANG_STRINGS = {
    "en": {
        "title":      "Premium = intrinsic value + time value",
        "subtitle":   "30-day call, strike $100, sigma 20%, r 4%. Time value peaks at the strike, tapers to ~0 at the wings.",
        "xlabel":     "Spot price S ($)",
        "ylabel":     "Per-share value ($)",
        "lbl_total":      "Total premium (Black-Scholes)",
        "lbl_intrinsic":  "Intrinsic value = max(S - K, 0)",
        "lbl_time":       "Time value (everything above intrinsic)",
        "ann_strike":     "strike K = $100",
        "ann_peak":       "time value peaks ATM",
        "footer":         "Black-Scholes call, K=$100, sigma=20%, r=4%, T=30/365. Premium decomposes into the deterministic max(S-K, 0) plus a wasting time-value wrapper.",
    },
    "hk": {
        "title":      "權利金 = 內在價值 + 時間價值",
        "subtitle":   "30 日認購期權,行使價 $100、波動率 20%、利率 4%。時間價值在行使價附近最高,兩翼接近零。",
        "xlabel":     "現貨價 S(美元)",
        "ylabel":     "每股價值(美元)",
        "lbl_total":      "總權利金(Black-Scholes)",
        "lbl_intrinsic":  "內在價值 = max(S - K, 0)",
        "lbl_time":       "時間價值(內在以上的部分)",
        "ann_strike":     "行使價 K = $100",
        "ann_peak":       "ATM 時間價值最高",
        "footer":         "Black-Scholes 認購期權,K=$100、sigma=20%、r=4%、T=30/365。權利金可拆為確定的 max(S-K, 0) 加一層會逐日衰減的時間價值。",
    },
    "tw": {
        "title":      "權利金 = 內含價值 + 時間價值",
        "subtitle":   "30 日買權,履約價 $100、波動率 20%、利率 4%。時間價值在履約價附近最高,兩翼趨近於零。",
        "xlabel":     "現貨價 S(美元)",
        "ylabel":     "每股價值(美元)",
        "lbl_total":      "總權利金(Black-Scholes)",
        "lbl_intrinsic":  "內含價值 = max(S - K, 0)",
        "lbl_time":       "時間價值(內含以上的部分)",
        "ann_strike":     "履約價 K = $100",
        "ann_peak":       "ATM 時間價值最高",
        "footer":         "Black-Scholes 買權,K=$100、sigma=20%、r=4%、T=30/365。權利金可拆為確定的 max(S-K, 0) 加一層會逐日衰減的時間價值。",
    },
    "cn": {
        "title":      "权利金 = 内在价值 + 时间价值",
        "subtitle":   "30 日看涨期权,行权价 $100、波动率 20%、利率 4%。时间价值在行权价附近最高,两翼趋近于零。",
        "xlabel":     "现货价 S(美元)",
        "ylabel":     "每股价值(美元)",
        "lbl_total":      "总权利金(Black-Scholes)",
        "lbl_intrinsic":  "内在价值 = max(S - K, 0)",
        "lbl_time":       "时间价值(内在以上的部分)",
        "ann_strike":     "行权价 K = $100",
        "ann_peak":       "ATM 时间价值最高",
        "footer":         "Black-Scholes 看涨期权,K=$100、sigma=20%、r=4%、T=30/365。权利金可拆为确定的 max(S-K, 0) 加一层会逐日衰减的时间价值。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    apply_cjk_font()

    # Escape '$' so matplotlib does not treat as mathtext (breaks CJK).
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    S = np.linspace(50.0, 150.0, 401)
    intrinsic = np.maximum(S - K, 0.0)
    total = bs_call(S, K, R, SIGMA, T)
    time_val = np.maximum(total - intrinsic, 0.0)

    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=160)
    style_axes(ax, p)

    # Shaded intrinsic value (from 0 up to intrinsic).
    ax.fill_between(S, 0.0, intrinsic, color=p["blue"], alpha=0.20,
                    linewidth=0, label=s["lbl_intrinsic"])
    # Shaded time value (from intrinsic up to total).
    ax.fill_between(S, intrinsic, total, color=p["accent"], alpha=0.30,
                    linewidth=0, label=s["lbl_time"])

    # Lines
    ax.plot(S, intrinsic, color=p["blue"], linewidth=1.6, linestyle="--", alpha=0.9)
    ax.plot(S, total, color=p["fg"], linewidth=2.4, label=s["lbl_total"])

    # Strike marker.
    ax.axvline(K, color=p["muted"], linewidth=0.9, linestyle=":", alpha=0.8)
    ax.annotate(s["ann_strike"], xy=(K, 0.5), xytext=(K + 1.5, 1.2),
                fontsize=9, color=p["muted"])

    # ATM peak callout — point to top of time-value bump near K.
    atm_idx = int(np.argmin(np.abs(S - K)))
    atm_total = total[atm_idx]
    atm_intr = intrinsic[atm_idx]
    mid_y = 0.5 * (atm_total + atm_intr)
    ax.annotate(s["ann_peak"], xy=(K, mid_y), xytext=(K + 14, mid_y + 6),
                fontsize=9.5, color=p["accent"],
                arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.8))

    ax.set_xlim(50, 150)
    ax.set_ylim(0, max(total.max() * 1.15, intrinsic.max() * 1.05))
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)

    ax.set_xticks([50, 75, 100, 125, 150])

    leg = ax.legend(loc="upper left", fontsize=9.5, frameon=True,
                    facecolor=p["bg"], edgecolor=p["grid"])
    for t in leg.get_texts():
        t.set_color(p["fg"])

    fig.suptitle(s["title"], fontsize=15, fontweight="bold",
                 color=p["fg"], y=0.985)
    fig.text(0.5, 0.945, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.015, s["footer"], ha="center", fontsize=8.5,
             color=p["muted"])

    fig.tight_layout(rect=[0, 0.035, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
