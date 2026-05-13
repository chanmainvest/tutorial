"""Week 27, §2.1 — Covered-call premium yield by strike.

Black-Scholes call premium for a $100 stock, 30 DTE, sigma=22%, r=4%.
Plot premium / strike for strikes 90 to 130 in $1 steps. Mark the
50-, 30-, 16-, and 10-delta strikes. The bend at ~110 is the lesson.

Run:
    uv run python course/image/week27_strike_yield.py
"""

from __future__ import annotations
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week27_strike_yield"

S = 100.0
SIGMA = 0.22
R = 0.04
T = 30.0 / 365.0


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_call(s: float, k: float, r: float, sigma: float, t: float) -> tuple[float, float]:
    """Return (premium, delta) for a European call."""
    if t <= 0:
        intrinsic = max(0.0, s - k)
        delta = 1.0 if s > k else 0.0
        return intrinsic, delta
    d1 = (math.log(s / k) + (r + 0.5 * sigma * sigma) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    prem = s * _norm_cdf(d1) - k * math.exp(-r * t) * _norm_cdf(d2)
    delta = _norm_cdf(d1)
    return prem, delta


def strike_for_delta(target: float) -> tuple[float, float, float]:
    """Find K such that BS call delta == target. Returns (K, premium, delta)."""
    lo, hi = S * 0.7, S * 1.6
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        _, d = bs_call(S, mid, R, SIGMA, T)
        if d > target:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    prem, d = bs_call(S, k, R, SIGMA, T)
    return k, prem, d


LANG_STRINGS = {
    "en": {
        "title": "Covered-call premium yield by strike",
        "subtitle": r"\$100 stock, 30 DTE, sigma=22%, r=4% — premium / strike, by Black-Scholes",
        "xlabel": "Strike (% of spot)",
        "ylabel": "Premium / strike  (per 30 days)",
        "tag_50": "50-delta (ATM)",
        "tag_30": "30-delta — standard income strike",
        "tag_16": "16-delta — 1 sigma out, conservative",
        "tag_10": "10-delta — 2 sigma out, lottery",
        "footer": "The bend past 110% of spot is where extra strike width stops paying you premium.",
    },
    "hk": {
        "title": "備兌認購期權:不同行使價的權利金收益率",
        "subtitle": r"\$100 股票,30 DTE,σ=22%,r=4% — 權利金 / 行使價(Black-Scholes)",
        "xlabel": "行使價(現價百分比)",
        "ylabel": "權利金 / 行使價(30 天)",
        "tag_50": "50-delta(ATM)",
        "tag_30": "30-delta — 收入寫單標準",
        "tag_16": "16-delta — 1σ 外,保守選擇",
        "tag_10": "10-delta — 2σ 外,彩票",
        "footer": "超過現價 110% 之後的彎位:再向外推已經幾乎不再給你補貼。",
    },
    "tw": {
        "title": "備兌買權權利金收益率與履約價",
        "subtitle": r"\$100 股票,30 DTE,σ=22%,r=4% — 權利金 / 履約價(Black-Scholes)",
        "xlabel": "履約價(現價百分比)",
        "ylabel": "權利金 / 履約價(30 天)",
        "tag_50": "50-delta(ATM)",
        "tag_30": "30-delta — 收益寫單標準",
        "tag_16": "16-delta — 1σ 外,保守",
        "tag_10": "10-delta — 2σ 外,樂透",
        "footer": "超過現價 110% 後曲線變平:再外推幾乎收不到額外權利金。",
    },
    "cn": {
        "title": "备兑看涨期权:不同执行价的权利金收益率",
        "subtitle": r"\$100 股票,30 DTE,σ=22%,r=4% — 权利金 / 执行价(Black-Scholes)",
        "xlabel": "执行价(现价百分比)",
        "ylabel": "权利金 / 执行价(30 天)",
        "tag_50": "50-delta(ATM)",
        "tag_30": "30-delta — 收益写单标准",
        "tag_16": "16-delta — 1σ 外,保守",
        "tag_10": "10-delta — 2σ 外,彩票",
        "footer": "现价 110% 之后曲线变平:再向外推几乎收不到额外补偿。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    strikes = np.arange(90.0, 131.0, 0.5)
    yields = []
    for k in strikes:
        prem, _ = bs_call(S, k, R, SIGMA, T)
        yields.append(prem / k)
    yields = np.array(yields)

    deltas = [(0.50, p["red"]), (0.30, p["accent"]), (0.16, p["blue"]), (0.10, p["purple"])]
    tags = {0.50: s["tag_50"], 0.30: s["tag_30"], 0.16: s["tag_16"], 0.10: s["tag_10"]}
    points = []
    for tgt, col in deltas:
        k, prem, d = strike_for_delta(tgt)
        points.append((tgt, k, prem, d, col))

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax)
    ax.plot(strikes, yields * 100.0, color=p["fg"], linewidth=2.4, zorder=3)
    ax.fill_between(strikes, 0, yields * 100.0, color=p["accent"], alpha=0.10, zorder=1)

    for tgt, k, prem, d, col in points:
        y_pct = (prem / k) * 100.0
        ax.scatter([k], [y_pct], color=col, s=70, zorder=5, edgecolor=p["bg"], linewidth=1.8)
        ax.annotate(
            f"{tags[tgt]}\nK={k:.1f}, prem={prem:.2f}\n{y_pct:.2f}% / 30d",
            xy=(k, y_pct),
            xytext=(k + 4, y_pct + 0.55),
            fontsize=8.6, color=col, weight="bold",
            arrowprops=dict(arrowstyle="-", color=col, lw=0.9, alpha=0.7),
        )

    ax.axvline(S, color=p["muted"], linewidth=0.8, linestyle=":", alpha=0.7)
    ax.set_xlim(89, 132)
    ax.set_ylim(0, max(yields) * 100.0 * 1.18)
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.0, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
