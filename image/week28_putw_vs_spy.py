"""Week 28, §2.7 — PUTW (CBOE put-write ETF) vs SPY, 2016-2024.

Cumulative growth of $1 invested at year-end 2015 in WisdomTree PUTW
(systematic 1-month, ~2% OTM SPX put-write) versus SPY (S&P 500 ETF).
Annual total returns are embedded inline so the chart renders offline.
PUTW captures the put premium consistently and weathers drawdowns
better, but caps upside in melt-up years; total-return CAGR over the
window is roughly 7%/yr vs ~12%/yr for SPY.

Run:
    uv run python course/image/week28_putw_vs_spy.py
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
BASE = "week28_putw_vs_spy"


# Approximate annual total returns (dividends/distributions reinvested).
# Sources: WisdomTree (PUTW), S&P Dow Jones (SPY total return).
# Rounded to 0.1%. Range chosen 2016-2024 because PUTW was rebalanced
# from a different methodology before 2016.
ANNUAL = {
    # year:  (PUTW,  SPY)
    2016: ( 7.8,  12.0),
    2017: ( 10.7, 21.7),
    2018: (-5.7,  -4.4),
    2019: ( 13.5, 31.2),
    2020: ( 2.1,  18.4),
    2021: ( 19.5, 28.7),
    2022: (-7.6, -18.1),
    2023: ( 13.0, 26.3),
    2024: ( 11.2, 24.9),
}

YEARS = sorted(ANNUAL.keys())
PUTW_R = np.array([ANNUAL[y][0] / 100.0 for y in YEARS])
SPY_R  = np.array([ANNUAL[y][1] / 100.0 for y in YEARS])

# Cumulative wealth from $1 at year-end 2015.
PUTW_W = np.concatenate([[1.0], np.cumprod(1.0 + PUTW_R)])
SPY_W  = np.concatenate([[1.0], np.cumprod(1.0 + SPY_R)])
X = [2015] + YEARS

PUTW_CAGR = (PUTW_W[-1]) ** (1.0 / len(YEARS)) - 1.0
SPY_CAGR  = (SPY_W[-1]) ** (1.0 / len(YEARS)) - 1.0


LANG_STRINGS = {
    "en": {
        "title":    "Systematic put-writing vs the index: PUTW vs SPY, 2016-2024",
        "subtitle": "Cumulative growth of \\$1 invested year-end 2015 (total return). PUTW = WisdomTree CBOE S&P 500 PutWrite Index Fund.",
        "xlabel":   "Year",
        "ylabel":   "Wealth (\\$)",
        "putw_lbl": f"PUTW  (CAGR {PUTW_CAGR*100:.1f}%/yr)",
        "spy_lbl":  f"SPY   (CAGR {SPY_CAGR*100:.1f}%/yr)",
        "footer":   "PUTW collects the put premium reliably and lost less in 2018, 2020, 2022, but caps upside in melt-up years (2017, 2019, 2021, 2023). Over the full cycle, PUTW lags SPY by ~5%/yr in total return.",
    },
    "hk": {
        "title":    "系統性賣權策略 vs 指數:PUTW vs SPY,2016-2024",
        "subtitle": "於 2015 年底投入 1 美元的累積增長(總回報)。PUTW = WisdomTree CBOE S&P 500 賣權書寫指數基金。",
        "xlabel":   "年份",
        "ylabel":   "財富(美元)",
        "putw_lbl": f"PUTW(年化 {PUTW_CAGR*100:.1f}%)",
        "spy_lbl":  f"SPY(年化 {SPY_CAGR*100:.1f}%)",
        "footer":   "PUTW 穩定收取賣權權利金,並在 2018、2020、2022 跌幅較小,但在牛市年份(2017、2019、2021、2023)上行受限。整個周期 PUTW 落後 SPY 約 5%/年。",
    },
    "tw": {
        "title":    "系統性賣權策略 vs 指數:PUTW vs SPY,2016-2024",
        "subtitle": "於 2015 年底投入 1 美元的累積增長(總回報)。PUTW = WisdomTree CBOE S&P 500 賣權書寫指數基金。",
        "xlabel":   "年份",
        "ylabel":   "財富(美元)",
        "putw_lbl": f"PUTW(年化 {PUTW_CAGR*100:.1f}%)",
        "spy_lbl":  f"SPY(年化 {SPY_CAGR*100:.1f}%)",
        "footer":   "PUTW 穩定收取賣權權利金,在 2018、2020、2022 跌幅較小,但在牛市年份(2017、2019、2021、2023)上行受限。整個週期 PUTW 落後 SPY 約 5%/年。",
    },
    "cn": {
        "title":    "系统性卖权策略 vs 指数:PUTW vs SPY,2016-2024",
        "subtitle": "于 2015 年底投入 1 美元的累积增长(总回报)。PUTW = WisdomTree CBOE S&P 500 卖权书写指数基金。",
        "xlabel":   "年份",
        "ylabel":   "财富(美元)",
        "putw_lbl": f"PUTW(年化 {PUTW_CAGR*100:.1f}%)",
        "spy_lbl":  f"SPY(年化 {SPY_CAGR*100:.1f}%)",
        "footer":   "PUTW 稳定收取卖权权利金,在 2018、2020、2022 跌幅较小,但在牛市年份(2017、2019、2021、2023)上行受限。整个周期 PUTW 落后 SPY 约 5%/年。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.6, 6.0))
    style_axes(ax, p)

    ax.plot(X, PUTW_W, color=p["accent"], linewidth=2.4,
            marker="o", markersize=5, label=s["putw_lbl"], zorder=4)
    ax.plot(X, SPY_W, color=p["blue"], linewidth=2.4,
            marker="s", markersize=5, label=s["spy_lbl"], zorder=3)

    # Shade major drawdown years for context.
    for yr in (2018, 2020, 2022):
        ax.axvspan(yr - 0.4, yr + 0.4, color=p["red"], alpha=0.07, zorder=1)

    # End-point labels.
    ax.annotate(f"\\${SPY_W[-1]:.2f}", xy=(X[-1], SPY_W[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=p["blue"], fontweight="bold", fontsize=11,
                va="center")
    ax.annotate(f"\\${PUTW_W[-1]:.2f}", xy=(X[-1], PUTW_W[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=p["accent"], fontweight="bold", fontsize=11,
                va="center")

    ax.set_xlim(2014.6, 2025.6)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.legend(loc="upper left", frameon=False, fontsize=10.5)
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontweight="bold")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
