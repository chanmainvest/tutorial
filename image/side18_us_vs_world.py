"""Side 18, §2.2 -- Wealth path of $1: SPY vs EFA vs EEM, 1990-Apr 2026.

Three regimes shaded on the chart:
  1990-1999  US dominance (SPY ~+18%/yr)
  2000-2009  International dominance (the textbook's case for VXUS)
  2010-2024  US dominance, hard (the regime in living memory)

Annual returns embedded inline as approximate constants from S&P 500 TR,
MSCI EAFE NR USD, and MSCI EM NR USD.  EEM the ETF launched 2003 and
EFA launched 2001; pre-inception years use the underlying MSCI index
returns (which is what the ETFs track).  Approximate first-3-months
2026 added at the tail.

Run:
    uv run python course/image/side18_us_vs_world.py
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
BASE = "side18_us_vs_world"


# Approximate annual total returns (decimals).
# year: (SPY=SP500TR, EFA=MSCI_EAFE_NR_USD, EEM=MSCI_EM_NR_USD)
# Sources: Damodaran SP500 TR, MSCI factsheets.
# 2026 row is partial (Q1 only) -- approximate Apr month-end.
RET = {
    1990: (-0.031, -0.232, -0.106),
    1991: ( 0.305,  0.122,  0.594),
    1992: ( 0.076, -0.119,  0.114),
    1993: ( 0.101,  0.328,  0.748),
    1994: ( 0.013,  0.078, -0.072),
    1995: ( 0.376,  0.114, -0.052),
    1996: ( 0.230,  0.061,  0.061),
    1997: ( 0.334,  0.018, -0.117),
    1998: ( 0.286,  0.200, -0.252),
    1999: ( 0.210,  0.270,  0.665),
    2000: (-0.091, -0.140, -0.305),
    2001: (-0.119, -0.214, -0.025),
    2002: (-0.221, -0.159, -0.060),
    2003: ( 0.287,  0.386,  0.561),
    2004: ( 0.109,  0.202,  0.260),
    2005: ( 0.049,  0.135,  0.342),
    2006: ( 0.158,  0.263,  0.323),
    2007: ( 0.055,  0.112,  0.395),
    2008: (-0.370, -0.434, -0.534),
    2009: ( 0.265,  0.318,  0.789),
    2010: ( 0.151,  0.078,  0.188),
    2011: ( 0.021, -0.121, -0.183),
    2012: ( 0.160,  0.173,  0.183),
    2013: ( 0.324,  0.228, -0.026),
    2014: ( 0.137, -0.049, -0.022),
    2015: ( 0.014, -0.008, -0.149),
    2016: ( 0.120,  0.010,  0.114),
    2017: ( 0.218,  0.250,  0.373),
    2018: (-0.044, -0.138, -0.144),
    2019: ( 0.315,  0.220,  0.184),
    2020: ( 0.184,  0.078,  0.183),
    2021: ( 0.287,  0.113, -0.025),
    2022: (-0.181, -0.145, -0.200),
    2023: ( 0.263,  0.182,  0.099),
    2024: ( 0.250,  0.040,  0.080),
    2025: ( 0.220,  0.180,  0.150),
    2026: ( 0.030, -0.005,  0.010),  # YTD through April 2026 approx
}


def _series():
    years = sorted(RET.keys())
    spy = np.array([RET[y][0] for y in years])
    efa = np.array([RET[y][1] for y in years])
    eem = np.array([RET[y][2] for y in years])
    cum_spy = np.concatenate([[1.0], np.cumprod(1 + spy)])
    cum_efa = np.concatenate([[1.0], np.cumprod(1 + efa)])
    cum_eem = np.concatenate([[1.0], np.cumprod(1 + eem)])
    yrs = np.array([years[0] - 1] + years)
    return yrs, cum_spy, cum_efa, cum_eem


LANG_STRINGS = {
    "en": {
        "title":    "$1 invested 1990-Apr 2026: SPY vs EFA (EAFE) vs EEM (Emerging)",
        "subtitle": "Three regimes. The 2000s favoured ex-US; the 1990s and 2010s did not. The 2010-2024 gap is the largest in modern data.",
        "xlabel":   "Year-end",
        "ylabel":   "Cumulative wealth ($, log scale)",
        "spy":      "SPY -- US large cap",
        "efa":      "EFA -- developed ex-US",
        "eem":      "EEM -- emerging markets",
        "ann":      "Geometric ann. total return: SPY {s:.1%}  EFA {e:.1%}  EEM {m:.1%}",
        "footer":   "Sources: Damodaran SP500 TR, MSCI EAFE NR USD, MSCI EM NR USD. ETF tickers used as labels; pre-2001/2003 inception years use the underlying MSCI index. 2026 partial (Q1).",
        "reg1":     "1990-1999\nUS dominance",
        "reg2":     "2000-2009\nlost decade",
        "reg3":     "2010-Apr 2026\nUS dominance, hard",
    },
    "hk": {
        "title":    "1990-2026 年 4 月投入 1 美元:SPY vs EFA(EAFE)vs EEM(新興)",
        "subtitle": "三個體制。2000 年代利於非美;1990 與 2010 年代則不然。2010-2024 差距是現代數據中最大的。",
        "xlabel":   "年底",
        "ylabel":   "累計財富(美元,對數軸)",
        "spy":      "SPY──美股大型股",
        "efa":      "EFA──已開發市場除美",
        "eem":      "EEM──新興市場",
        "ann":      "幾何年化總回報:SPY {s:.1%}  EFA {e:.1%}  EEM {m:.1%}",
        "footer":   "資料:Damodaran 標普 TR、MSCI EAFE NR USD、MSCI EM NR USD。標籤使用 ETF 代號;2001/2003 成立前年份使用底層 MSCI 指數。2026 為 Q1 部分數據。",
        "reg1":     "1990-1999\n美國領先",
        "reg2":     "2000-2009\n失落十年",
        "reg3":     "2010-2026 年 4 月\n美國強勢領先",
    },
    "tw": {
        "title":    "1990-2026 年 4 月投入 1 美元:SPY vs EFA(EAFE)vs EEM(新興)",
        "subtitle": "三個體制。2000 年代利於非美;1990 與 2010 年代則不然。2010-2024 差距是現代資料中最大的。",
        "xlabel":   "年底",
        "ylabel":   "累計財富(美元,對數軸)",
        "spy":      "SPY──美股大型股",
        "efa":      "EFA──已開發市場除美",
        "eem":      "EEM──新興市場",
        "ann":      "幾何年化總報酬:SPY {s:.1%}  EFA {e:.1%}  EEM {m:.1%}",
        "footer":   "資料:Damodaran 標普 TR、MSCI EAFE NR USD、MSCI EM NR USD。標籤使用 ETF 代號;2001/2003 成立前年份使用底層 MSCI 指數。2026 為 Q1 部分數據。",
        "reg1":     "1990-1999\n美國領先",
        "reg2":     "2000-2009\n失落十年",
        "reg3":     "2010-2026 年 4 月\n美國強勢領先",
    },
    "cn": {
        "title":    "1990-2026 年 4 月投入 1 美元:SPY vs EFA(EAFE)vs EEM(新兴)",
        "subtitle": "三个体制。2000 年代利于非美;1990 与 2010 年代则不然。2010-2024 差距是现代数据中最大的。",
        "xlabel":   "年底",
        "ylabel":   "累计财富(美元,对数轴)",
        "spy":      "SPY──美股大型股",
        "efa":      "EFA──发达市场除美",
        "eem":      "EEM──新兴市场",
        "ann":      "几何年化总回报:SPY {s:.1%}  EFA {e:.1%}  EEM {m:.1%}",
        "footer":   "资料:Damodaran 标普 TR、MSCI EAFE NR USD、MSCI EM NR USD。标签使用 ETF 代号;2001/2003 成立前年份使用底层 MSCI 指数。2026 为 Q1 部分数据。",
        "reg1":     "1990-1999\n美国领先",
        "reg2":     "2000-2009\n失落十年",
        "reg3":     "2010-2026 年 4 月\n美国强势领先",
    },
}


def build_fig(s):
    yrs, cs, ce, cm = _series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.0, 6.2))
    style_axes(ax, p)

    # Regime bands.
    ax.axvspan(1989, 1999, color=p["red"], alpha=0.05)
    ax.axvspan(1999, 2009, color=p["blue"], alpha=0.05)
    ax.axvspan(2009, 2026, color=p["red"], alpha=0.06)

    ax.plot(yrs, cs, color=p["red"],    linewidth=2.6, label=s["spy"])
    ax.plot(yrs, ce, color=p["blue"],   linewidth=2.0, label=s["efa"])
    ax.plot(yrs, cm, color=p["accent"], linewidth=2.0, label=s["eem"])

    ax.set_yscale("log")

    last_y = yrs[-1]
    for cum, color in [(cs, p["red"]), (ce, p["blue"]), (cm, p["accent"])]:
        ax.text(last_y + 0.4, cum[-1], f"\\${cum[-1]:.2f}",
                color=color, fontsize=9.5, va="center", fontweight="bold")

    # Regime annotations
    ax.text(1994.5, 0.35, s["reg1"], fontsize=8.5, color=p["muted"],
            ha="center", style="italic")
    ax.text(2004,   0.35, s["reg2"], fontsize=8.5, color=p["muted"],
            ha="center", style="italic")
    ax.text(2017.5, 0.35, s["reg3"], fontsize=8.5, color=p["muted"],
            ha="center", style="italic")

    n = len(yrs) - 1
    ann_s = cs[-1] ** (1 / n) - 1
    ann_e = ce[-1] ** (1 / n) - 1
    ann_m = cm[-1] ** (1 / n) - 1

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24, color=p["fg"])
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.text(0, -0.155, s["ann"].format(s=ann_s, e=ann_e, m=ann_m),
            transform=ax.transAxes, fontsize=9.5,
            color=p["fg"], fontweight="bold")
    ax.text(0, -0.21, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"], style="italic")

    ax.set_ylim(0.3, 50)
    ax.set_xlim(yrs[0], yrs[-1] + 1)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
