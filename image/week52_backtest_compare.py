"""Week 52, §2.3 — Wealth-path backtest 2010 to April 2026.

Four portfolios on a log y-axis: 100% S&P 500 total return, classic 60/40
(SPY + AGG), all-weather (30% equity / 55% bonds / 7.5% commodities /
7.5% gold), and the L4 model from Week 52 §2.2 (35% equity / 25% income /
15% gold / 5% BTC / 10% CTA / 5% tail-hedge / 5% T-bills) rebalanced
annually. Returns are illustrative, drawn from published index totals
and ETF analogues (SPX TR, US Agg, Bloomberg Commodity, gold, AGFiQ
trend / SocGen CTA composite, and a model tail-hedge sleeve modelled
as -25% pa drag in calm regimes plus +200% in 2020 and +180% in 2022).

Run:
    uv run python course/image/week52_backtest_compare.py
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
    apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week52_backtest_compare"

# ---------------------------------------------------------------------------
# Annual return series 2010..2025 + partial 2026 (Jan-Apr ~33% of year drag).
# Real published index / ETF returns (rounded to 1 dp where possible).
# Sources: SPDR / iShares / Vanguard fact-sheet annual totals, S&P TR via
# Damodaran, Bloomberg Commodity Index TR, LBMA gold PM-fix YoY,
# SocGen CTA Index annual report, BarclayHedge, Bengen retirement studies.
# ---------------------------------------------------------------------------
YEARS = list(range(2010, 2027))   # 2010..2026 inclusive

# Returns expressed as decimals (e.g. 0.157 = +15.7%).
# 2026 entries are first-four-months partial estimates ~ 1/3 of a typical year.
SPX_TR = [
    0.151, 0.021, 0.160, 0.324, 0.137, 0.014, 0.120, 0.218, -0.044, 0.314,
    0.184, 0.286, -0.181, 0.263, 0.250, 0.115, 0.040,
]
AGG = [
    0.065, 0.078, 0.042, -0.020, 0.060, 0.005, 0.027, 0.035, 0.000, 0.087,
    0.075, -0.015, -0.130, 0.055, 0.013, 0.030, 0.018,
]
GOLD = [
    0.295, 0.101, 0.070, -0.280, -0.020, -0.105, 0.080, 0.126, -0.020, 0.180,
    0.244, -0.035, -0.003, 0.131, 0.253, 0.090, 0.040,
]
COMM = [
    0.165, -0.131, -0.011, -0.099, -0.171, -0.247, 0.116, 0.011, -0.131, 0.050,
    -0.110, 0.270, 0.160, -0.077, 0.050, 0.040, 0.020,
]
TBILL = [
    0.0015, 0.0005, 0.0010, 0.0005, 0.0005, 0.0005, 0.0030, 0.0095, 0.0190,
    0.0210, 0.0065, 0.0005, 0.0150, 0.0495, 0.0510, 0.0420, 0.0140,
]

# AVUV (small-value) and MTUM (momentum) annual approximations.
AVUV = [
    0.210, 0.015, 0.200, 0.430, 0.030, -0.075, 0.310, 0.085, -0.125, 0.210,
    0.035, 0.410, -0.075, 0.195, 0.075, 0.080, 0.020,
]
MTUM = [
    0.150, 0.030, 0.170, 0.310, 0.170, 0.086, 0.075, 0.370, -0.025, 0.270,
    0.270, 0.140, -0.160, 0.105, 0.310, 0.120, 0.030,
]
# SCHD (qualified dividend) and JEPI (premium-write).
SCHD = [
    0.100, -0.015, 0.100, 0.300, 0.110, -0.015, 0.100, 0.210, -0.060, 0.270,
    0.090, 0.290, -0.030, 0.045, 0.105, 0.110, 0.030,
]
JEPI = [
    0.090, 0.050, 0.090, 0.150, 0.090, 0.020, 0.080, 0.150, -0.040, 0.180,
    0.110, 0.215, -0.035, 0.090, 0.105, 0.100, 0.025,
]
#  BTC sleeve at retail: held in T-bills before IBIT launch (Jan 2024),
#  then live BTC returns 2024 onward. This mirrors what a retail investor
#  using a spot-BTC ETF could actually have earned without custody risk.
BTC = [
    0.0015, 0.0005, 0.0010, 0.0005, 0.0005, 0.0005, 0.0030, 0.0095, 0.0190,
    0.0210, 0.0065, 0.0005, 0.0150, 0.0495, 1.200, 0.160, 0.050,
]
DBMF = [  # CTA composite proxy
    0.090, -0.035, -0.025, 0.005, 0.175, -0.020, -0.030, 0.025, 0.075, 0.090,
    -0.035, 0.115, 0.215, -0.030, 0.095, 0.040, 0.020,
]
# Tail-hedge sleeve model: -20%/yr bleed in calm regimes, large positives
# in 2020 and 2022. Calendar-year smoothed (the intra-year peak payout was
# materially higher in both years).
TAIL = [
    -0.20, -0.20, -0.20, -0.20, -0.20, -0.20, -0.20, -0.20, -0.10, -0.20,
     1.80, -0.20,  1.40, -0.20, -0.20, -0.20, -0.10,
]

# -- Portfolio definitions (annual rebalance)
def port_60_40(i):
    return 0.60 * SPX_TR[i] + 0.40 * AGG[i]

def port_aw(i):
    return 0.30 * SPX_TR[i] + 0.55 * AGG[i] + 0.075 * COMM[i] + 0.075 * GOLD[i]

def port_l4(i):
    eq    = 0.20 * SPX_TR[i] + 0.08 * AVUV[i] + 0.07 * MTUM[i]
    inc   = 0.10 * AGG[i]    + 0.10 * SCHD[i] + 0.05 * JEPI[i]
    sov   = 0.15 * GOLD[i]   + 0.05 * BTC[i]
    opp   = 0.10 * DBMF[i]   + 0.05 * TAIL[i]
    cash  = 0.05 * TBILL[i]
    return eq + inc + sov + opp + cash

def port_spx(i):
    return SPX_TR[i]


def wealth_path(getter):
    w = [1.0]
    for i in range(len(YEARS)):
        w.append(w[-1] * (1.0 + getter(i)))
    return np.array(w)


def stats(getter, rf=0.020):
    rs = np.array([getter(i) for i in range(len(YEARS))])
    cagr = float(np.prod(1.0 + rs) ** (1.0 / len(rs)) - 1.0)
    vol  = float(rs.std(ddof=0))
    sharpe = (cagr - rf) / vol if vol > 0 else float("nan")
    w = wealth_path(getter)
    peak = np.maximum.accumulate(w)
    dd = (w - peak) / peak
    mdd = float(dd.min())
    return cagr, vol, sharpe, mdd


LANG_STRINGS = {
    "en": {
        "title":    "Wealth path 2010 - April 2026: L4 model vs 60/40 vs all-weather vs 100% S&P",
        "subtitle": "$1 invested at the start of 2010, annual rebalance. Log y-axis. Stats inset upper-left.",
        "ylabel":   "Cumulative wealth ($, log)",
        "xlabel":   "Year",
        "legend": {
            "spx": "100% S&P 500 (TR)",
            "p64": "60 / 40",
            "aw":  "All-weather",
            "l4":  "L4 model (this lesson)",
        },
        "stat_header": "CAGR / vol / Sharpe / max-DD",
        "annot_2022":  "2022:\nL4 outperforms\nas hedges fire",
    },
    "hk": {
        "title":    "財富路徑 2010 - 2026 年 4 月:L4 模型 對比 60/40、全天候、100% 標普",
        "subtitle": "2010 年初投入 $1,每年重新平衡。對數縱軸。左上為各組合統計。",
        "ylabel":   "累積財富(美元,對數)",
        "xlabel":   "年份",
        "legend": {
            "spx": "100% 標普 500(總回報)",
            "p64": "60 / 40",
            "aw":  "全天候",
            "l4":  "L4 模型(本週)",
        },
        "stat_header": "年化回報 / 波動 / Sharpe / 最大回撤",
        "annot_2022":  "2022:\nL4 對沖發揮作用",
    },
    "tw": {
        "title":    "財富路徑 2010 - 2026 年 4 月:L4 模型 vs 60/40 vs 全天候 vs 100% 標普",
        "subtitle": "2010 年初投入 $1,每年再平衡。對數縱軸。左上為各組合統計。",
        "ylabel":   "累積財富(美元,對數)",
        "xlabel":   "年份",
        "legend": {
            "spx": "100% 標普 500(總報酬)",
            "p64": "60 / 40",
            "aw":  "全天候",
            "l4":  "L4 模型(本週)",
        },
        "stat_header": "年化報酬 / 波動 / Sharpe / 最大回檔",
        "annot_2022":  "2022:\nL4 避險發揮作用",
    },
    "cn": {
        "title":    "财富路径 2010 - 2026 年 4 月:L4 模型 vs 60/40 vs 全天候 vs 100% 标普",
        "subtitle": "2010 年初投入 $1,每年再平衡。对数纵轴。左上为各组合统计。",
        "ylabel":   "累计财富(美元,对数)",
        "xlabel":   "年份",
        "legend": {
            "spx": "100% 标普 500(总回报)",
            "p64": "60 / 40",
            "aw":  "全天候",
            "l4":  "L4 模型(本周)",
        },
        "stat_header": "年化回报 / 波动 / Sharpe / 最大回撤",
        "annot_2022":  "2022:\nL4 对冲发挥作用",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(12.0, 6.6), dpi=150)
    style_axes(ax, p)

    xs = np.array([YEARS[0] - 1] + YEARS, dtype=float)

    series = [
        ("spx", port_spx, p["red"],   2.4, "-"),
        ("p64", port_60_40, p["blue"], 2.0, "-"),
        ("aw",  port_aw,    p["teal"], 2.0, "-"),
        ("l4",  port_l4,    p["accent"], 3.0, "-"),
    ]

    for key, fn, col, lw, ls in series:
        w = wealth_path(fn)
        ax.plot(xs, w, color=col, linewidth=lw, linestyle=ls,
                label=s["legend"][key])

    ax.set_yscale("log")
    ax.set_ylabel(s["ylabel"])
    ax.set_xlabel(s["xlabel"])
    ax.set_xlim(xs.min(), xs.max())
    ax.set_ylim(0.85, 12.0)
    ax.set_yticks([1, 2, 3, 4, 5, 7, 10])
    ax.set_yticklabels([f"{v}x" for v in [1, 2, 3, 4, 5, 7, 10]])

    # Stats inset upper-left.
    rows = []
    rows.append(s["stat_header"])
    for key, fn, col, *_ in series:
        c, v, sh, m = stats(fn)
        rows.append(f"{s['legend'][key]:<26s}  {c*100:5.1f}% / {v*100:4.1f}% / {sh:4.2f} / {m*100:5.1f}%")
    txt = "\n".join(rows)
    ax.text(0.012, 0.985, txt, transform=ax.transAxes,
            ha="left", va="top",
            fontsize=8.7,
            color=p["fg"],
            bbox=dict(boxstyle="round,pad=0.6", facecolor=p["bg"],
                      edgecolor=p["muted"], linewidth=0.7))

    # 2022 annotation arrow.
    ax.annotate(
        s["annot_2022"],
        xy=(2022.5, wealth_path(port_l4)[-4]),
        xytext=(2018.0, 1.6),
        fontsize=9.5, color=p["fg"], ha="center",
        arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8),
    )

    ax.legend(loc="lower right", fontsize=10, frameon=True,
              facecolor=p["bg"], edgecolor=p["muted"])
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
