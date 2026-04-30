"""Week 21, §2.6 — Fed model spread, 1962 to April 2026.

Spread = S&P 500 cyclically-adjusted earnings yield (1/CAPE) MINUS
the 10-year Treasury yield (FRED DGS10, annual average). Approximate
annual values embedded inline so the chart renders offline.

Run:
    uv run python course/image/week21_fed_model.py
"""

from __future__ import annotations

import sys
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
BASE = "week21_fed_model"


# (year, CAPE, 10y_yield_pct).  CAPE from Shiller; 10y from FRED DGS10
# annual average. Both rounded to 0.1; April 2026 is the trailing reading.
ROWS = [
    (1962, 17.5, 3.95), (1963, 19.1, 4.00), (1964, 21.1, 4.19),
    (1965, 23.0, 4.28), (1966, 19.3, 4.93), (1967, 21.6, 5.07),
    (1968, 21.6, 5.65), (1969, 17.6, 6.67), (1970, 16.4, 7.35),
    (1971, 17.7, 6.16), (1972, 18.7, 6.21), (1973, 13.5, 6.84),
    (1974, 8.3,  7.56), (1975, 11.2, 7.99), (1976, 11.7, 7.61),
    (1977, 9.3,  7.42), (1978, 9.2,  8.41), (1979, 9.3,  9.43),
    (1980, 8.8,  11.43), (1981, 7.4,  13.92), (1982, 9.7,  13.01),
    (1983, 11.7, 11.10), (1984, 10.3, 12.46), (1985, 13.7, 10.62),
    (1986, 16.2, 7.67), (1987, 15.7, 8.39), (1988, 14.4, 8.85),
    (1989, 17.7, 8.49), (1990, 15.0, 8.55), (1991, 19.5, 7.86),
    (1992, 20.4, 7.01), (1993, 21.4, 5.87), (1994, 20.4, 7.09),
    (1995, 24.6, 6.57), (1996, 27.7, 6.44), (1997, 32.9, 6.35),
    (1998, 40.6, 5.26), (1999, 44.2, 5.65), (2000, 36.4, 6.03),
    (2001, 28.3, 5.02), (2002, 22.7, 4.61), (2003, 26.5, 4.01),
    (2004, 27.5, 4.27), (2005, 26.5, 4.29), (2006, 27.0, 4.80),
    (2007, 26.4, 4.63), (2008, 15.2, 3.66), (2009, 20.3, 3.26),
    (2010, 22.1, 3.22), (2011, 21.2, 2.78), (2012, 22.4, 1.80),
    (2013, 25.4, 2.35), (2014, 27.0, 2.54), (2015, 26.0, 2.14),
    (2016, 28.1, 1.84), (2017, 32.4, 2.33), (2018, 28.4, 2.91),
    (2019, 30.3, 2.14), (2020, 33.5, 0.89), (2021, 38.6, 1.45),
    (2022, 28.3, 2.95), (2023, 31.0, 3.96), (2024, 35.1, 4.21),
    (2025, 36.5, 4.15), (2026, 36.0, 4.05),  # April 2026
]

YEARS = [r[0] for r in ROWS]
EYIELD = [100.0 / r[1] for r in ROWS]            # % earnings yield
TYIELD = [r[2] for r in ROWS]                     # % 10y yield
SPREAD = [e - t for e, t in zip(EYIELD, TYIELD)]  # percentage points


LANG_STRINGS = {
    "en": {
        "title":    "Fed model spread: earnings yield minus 10-yr Treasury, 1962-Apr 2026",
        "subtitle": "Earnings yield = 1 / Shiller CAPE. Treasury yield = FRED DGS10 annual average. Negative = stocks expensive vs bonds. April 2026 reads near -1pp.",
        "xlabel":   "Year",
        "ylabel":   "Spread (percentage points)",
        "label_2000": "2000 inversion\n(stocks expensive)",
        "label_1970s": "1970s deep negative\n(bonds yielded more)",
        "label_2009": "2009 peak\n(low rates, rebuilt earnings yield)",
        "label_2026": "Apr 2026 ~ -1pp",
        "footer":   "Use as one cross-asset thermometer, not a verdict. The signal breaks down when inflation is the dominant variable (1970s).",
    },
    "hk": {
        "title":    "聯儲模型利差:盈利收益率減十年期國債,1962 - 2026 年 4 月",
        "subtitle": "盈利收益率 = 1 / 席勒 CAPE。十年期收益率 = FRED DGS10 年均。負值 = 股票相對債券貴。2026 年 4 月約 -1 個百分點。",
        "xlabel":   "年份",
        "ylabel":   "利差(百分點)",
        "label_2000": "2000 倒掛\n(股票貴)",
        "label_1970s": "1970 年代深度負值\n(債券收益更高)",
        "label_2009": "2009 高峰\n(低息+盈利收益率回升)",
        "label_2026": "2026 年 4 月約 -1pp",
        "footer":   "視為一個跨資產溫度計,而非結論。當通脹主導時(1970 年代),這個訊號會失效。",
    },
    "tw": {
        "title":    "聯準會模型利差:盈餘收益率減十年期公債,1962 - 2026 年 4 月",
        "subtitle": "盈餘收益率 = 1 / 席勒 CAPE。十年期收益率 = FRED DGS10 年均。負值 = 股票相對債券貴。2026 年 4 月約 -1 個百分點。",
        "xlabel":   "年份",
        "ylabel":   "利差(百分點)",
        "label_2000": "2000 倒掛\n(股票貴)",
        "label_1970s": "1970 年代深度負值\n(公債收益更高)",
        "label_2009": "2009 高峰\n(低利率+盈餘收益率回升)",
        "label_2026": "2026 年 4 月約 -1pp",
        "footer":   "視為一個跨資產溫度計,而非結論。當通膨主導時(1970 年代),這個訊號會失效。",
    },
    "cn": {
        "title":    "美联储模型利差:盈利收益率减十年期国债,1962 - 2026 年 4 月",
        "subtitle": "盈利收益率 = 1 / 席勒 CAPE。十年期收益率 = FRED DGS10 年均。负值 = 股票相对债券贵。2026 年 4 月约 -1 个百分点。",
        "xlabel":   "年份",
        "ylabel":   "利差(百分点)",
        "label_2000": "2000 倒挂\n(股票贵)",
        "label_1970s": "1970 年代深度负值\n(债券收益更高)",
        "label_2009": "2009 高峰\n(低息+盈利收益率回升)",
        "label_2026": "2026 年 4 月约 -1pp",
        "footer":   "视为一个跨资产温度计,而非结论。当通胀主导时(1970 年代),这个信号会失效。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.6, 6.0))
    style_axes(ax, p)

    yrs = np.array(YEARS)
    sp = np.array(SPREAD)

    # Fill positive (green) and negative (red) regions.
    ax.fill_between(yrs, 0, sp, where=sp >= 0,
                    color=p["green"], alpha=0.22, interpolate=True)
    ax.fill_between(yrs, 0, sp, where=sp < 0,
                    color=p["red"], alpha=0.22, interpolate=True)
    ax.plot(yrs, sp, color=p["fg"], linewidth=1.7)

    ax.axhline(0, color=p["muted"], linewidth=0.9)

    # Annotations.
    # 1970s deep negative (use 1981 as anchor).
    idx81 = YEARS.index(1981)
    ax.annotate(s["label_1970s"],
                xy=(1981, sp[idx81]), xytext=(1965, -8.0),
                fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"],
                                connectionstyle="arc3,rad=-0.15"))

    # 2000 inversion.
    idx00 = YEARS.index(2000)
    ax.annotate(s["label_2000"],
                xy=(2000, sp[idx00]), xytext=(1992, -5.5),
                fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"],
                                connectionstyle="arc3,rad=0.2"))

    # 2009 peak.
    idx09 = YEARS.index(2009)
    ax.annotate(s["label_2009"],
                xy=(2009, sp[idx09]), xytext=(2009, sp[idx09] + 2.5),
                fontsize=9, color=p["green"], fontweight="bold",
                ha="center",
                arrowprops=dict(arrowstyle="->", color=p["green"]))

    # April 2026 marker.
    idx26 = YEARS.index(2026)
    ax.plot(2026, sp[idx26], "o", color=p["accent"], markersize=7, zorder=5)
    ax.annotate(s["label_2026"],
                xy=(2026, sp[idx26]), xytext=(2018, 4.5),
                fontsize=9, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"]))

    ax.set_xlim(1960, 2030)
    ax.set_ylim(-10, 7)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13.5, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontweight="bold")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
