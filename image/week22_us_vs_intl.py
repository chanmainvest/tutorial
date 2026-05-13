"""Week 22, §2.2 — Cumulative wealth: SPY vs unhedged EAFE vs hedged EAFE.

$1 invested 2000-01-01 through 2024-12-31 in three vehicles:
  SPY  -- US large cap
  EFA  -- iShares MSCI EAFE (unhedged USD)
  HEFA -- iShares MSCI EAFE Hedged (synthetic backfill before HEFA's
          2014 inception by approximating EAFE local-currency returns
          minus a constant ~1% annualised hedge cost)

Annual total returns are embedded inline as approximate constants
sourced from MSCI / S&P / iShares fund factsheets, so the script
renders fully offline.

Run:
    uv run python course/image/week22_us_vs_intl.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week22_us_vs_intl"


# Approximate annual total returns (decimals).
# Sources: SPY total return (S&P 500 TR), MSCI EAFE NR USD (unhedged),
# MSCI EAFE 100% Hedged to USD NR (synthetic local + small hedge drag).
# Values rounded; small inaccuracies are immaterial to the cumulative
# story the chart is meant to tell.
RET = {
    # year: (SPY, EFA_unhedged, HEFA_hedged)
    2000: (-0.091, -0.140, -0.030),
    2001: (-0.119, -0.214, -0.180),
    2002: (-0.221, -0.159, -0.270),  # weak USD helped unhedged
    2003: ( 0.287,  0.386,  0.195),
    2004: ( 0.109,  0.202,  0.130),
    2005: ( 0.049,  0.135,  0.270),  # strong yen/euro -- hedged still solid
    2006: ( 0.158,  0.263,  0.175),
    2007: ( 0.055,  0.112,  0.050),
    2008: (-0.370, -0.434, -0.420),
    2009: ( 0.265,  0.318,  0.230),
    2010: ( 0.151,  0.078,  0.055),
    2011: ( 0.021, -0.121, -0.115),
    2012: ( 0.160,  0.173,  0.175),
    2013: ( 0.324,  0.228,  0.270),
    2014: ( 0.137, -0.049,  0.055),  # USD bid begins -- hedged crushes unhedged
    2015: ( 0.014, -0.008,  0.050),
    2016: ( 0.120,  0.010,  0.030),
    2017: ( 0.218,  0.250,  0.170),
    2018: (-0.044, -0.138, -0.110),
    2019: ( 0.315,  0.220,  0.190),
    2020: ( 0.184,  0.078,  0.055),
    2021: ( 0.287,  0.113,  0.140),
    2022: (-0.181, -0.145, -0.030),  # strong USD year -- hedge wins big
    2023: ( 0.263,  0.182,  0.185),
    2024: ( 0.250,  0.040,  0.110),
}


def _series():
    years = sorted(RET.keys())
    spy = np.array([RET[y][0] for y in years])
    efa = np.array([RET[y][1] for y in years])
    hef = np.array([RET[y][2] for y in years])
    cum_spy = np.concatenate([[1.0], np.cumprod(1 + spy)])
    cum_efa = np.concatenate([[1.0], np.cumprod(1 + efa)])
    cum_hef = np.concatenate([[1.0], np.cumprod(1 + hef)])
    yrs = np.array([years[0] - 1] + years)
    return yrs, cum_spy, cum_efa, cum_hef, spy, efa, hef


LANG_STRINGS = {
    "en": {
        "title":    "$1 invested 2000-2024: SPY vs unhedged EAFE vs hedged EAFE",
        "subtitle": "Same equity asset class, three currency treatments. The gap between unhedged (EFA) and hedged (HEFA) is almost entirely the FX overlay.",
        "xlabel":   "Year-end",
        "ylabel":   "Cumulative wealth ($)",
        "spy":      "SPY (US large cap)",
        "efa":      "EFA -- unhedged EAFE (USD)",
        "hef":      "HEFA -- hedged EAFE (USD)",
        "ann":      "Geometric ann. total return (2000-2024): SPY {s:.1%}  ·  HEFA {h:.1%}  ·  EFA {e:.1%}",
        "footer":   "Annual returns approximated from S&P 500 TR, MSCI EAFE NR USD (unhedged) and MSCI EAFE 100% Hedged USD NR. Hedged series synthesised pre-2014 from local-currency MSCI EAFE less ~1% annualised hedge cost.",
        "note14":   "post-2014\nUSD bid",
        "note25":   "2025\nUSD reset",
    },
    "hk": {
        "title":    "2000-2024 投入 1 美元:SPY vs 未對沖 EAFE vs 對沖 EAFE",
        "subtitle": "同一個股票資產類別,三種貨幣處理。未對沖(EFA)與對沖(HEFA)之間的差距,幾乎全部來自 FX 疊加。",
        "xlabel":   "年底",
        "ylabel":   "累計財富(美元)",
        "spy":      "SPY(美股大型股)",
        "efa":      "EFA──未對沖 EAFE(美元)",
        "hef":      "HEFA──對沖 EAFE(美元)",
        "ann":      "幾何年化總回報(2000-2024):SPY {s:.1%}  ·  HEFA {h:.1%}  ·  EFA {e:.1%}",
        "footer":   "年度回報近似自:標普 500 TR、MSCI EAFE NR USD(未對沖)、MSCI EAFE 100% 對沖 USD NR。2014 年前對沖序列由本地貨幣 MSCI EAFE 減約 1% 年化對沖成本合成。",
        "note14":   "2014 後\n美元買盤",
        "note25":   "2025\n美元重置",
    },
    "tw": {
        "title":    "2000-2024 投入 1 美元:SPY vs 未避險 EAFE vs 避險 EAFE",
        "subtitle": "同一個股票資產類別,三種貨幣處理方式。未避險(EFA)與避險(HEFA)之間的差距,幾乎全部來自 FX 疊加。",
        "xlabel":   "年底",
        "ylabel":   "累計財富(美元)",
        "spy":      "SPY(美股大型股)",
        "efa":      "EFA──未避險 EAFE(美元)",
        "hef":      "HEFA──避險 EAFE(美元)",
        "ann":      "幾何年化總報酬(2000-2024):SPY {s:.1%}  ·  HEFA {h:.1%}  ·  EFA {e:.1%}",
        "footer":   "年度報酬近似自:標普 500 TR、MSCI EAFE NR USD(未避險)、MSCI EAFE 100% 避險 USD NR。2014 年前避險序列由本地貨幣 MSCI EAFE 減約 1% 年化避險成本合成。",
        "note14":   "2014 後\n美元買盤",
        "note25":   "2025\n美元重置",
    },
    "cn": {
        "title":    "2000-2024 投入 1 美元:SPY vs 未对冲 EAFE vs 对冲 EAFE",
        "subtitle": "同一个股票资产类别,三种货币处理。未对冲(EFA)与对冲(HEFA)之间的差距,几乎全部来自 FX 叠加。",
        "xlabel":   "年底",
        "ylabel":   "累计财富(美元)",
        "spy":      "SPY(美股大型股)",
        "efa":      "EFA──未对冲 EAFE(美元)",
        "hef":      "HEFA──对冲 EAFE(美元)",
        "ann":      "几何年化总回报(2000-2024):SPY {s:.1%}  ·  HEFA {h:.1%}  ·  EFA {e:.1%}",
        "footer":   "年度回报近似自:标普 500 TR、MSCI EAFE NR USD(未对冲)、MSCI EAFE 100% 对冲 USD NR。2014 年前对冲序列由本地货币 MSCI EAFE 减约 1% 年化对冲成本合成。",
        "note14":   "2014 后\n美元买盘",
        "note25":   "2025\n美元重置",
    },
}


def build_fig(s):
    yrs, cs, ce, ch, rs, re_, rh = _series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.0, 6.0))
    style_axes(ax, p)

    ax.plot(yrs, cs, color=p["red"],    linewidth=2.4, label=s["spy"])
    ax.plot(yrs, ch, color=p["accent"], linewidth=2.2, label=s["hef"])
    ax.plot(yrs, ce, color=p["blue"],   linewidth=2.2, label=s["efa"])

    # Mark the post-2014 USD-bid era and 2025 reset.
    ax.axvspan(2014, 2024, color=p["muted"], alpha=0.06)
    ax.text(2014.2, 4.3, s["note14"], fontsize=8.5,
            color=p["muted"], style="italic")
    ax.axvline(2025, color=p["accent"], linewidth=0.9,
               linestyle=":", alpha=0.7)

    n = len(rs)
    ann_s = cs[-1] ** (1 / n) - 1
    ann_e = ce[-1] ** (1 / n) - 1
    ann_h = ch[-1] ** (1 / n) - 1

    last_y = yrs[-1]
    for cum, color in [(cs, p["red"]), (ch, p["accent"]), (ce, p["blue"])]:
        ax.text(last_y + 0.25, cum[-1], f"\\${cum[-1]:.2f}",
                color=color, fontsize=9.5, va="center", fontweight="bold")

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.text(0, -0.155, s["ann"].format(s=ann_s, h=ann_h, e=ann_e),
            transform=ax.transAxes, fontsize=9.5,
            color=p["fg"], fontweight="bold")
    ax.text(0, -0.21, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"], style="italic")

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.set_xlim(yrs[0], yrs[-1] + 1)
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
