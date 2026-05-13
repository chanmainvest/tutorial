"""Week 4, §2.3 — Rolling 36-month stock-bond correlation.

Damodaran annual data only goes year-by-year, so we use a rolling
window over annual returns. Window = 8 years for stability.

Run:
    uv run python course/image/week04_stock_bond_corr.py
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
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week04_stock_bond_corr"
WINDOW = 8

LANG_STRINGS = {
    "en": {
        "title":    f"Rolling {WINDOW}-year correlation: US stocks vs 10-year Treasury",
        "subtitle": "Annual returns, 1928-2024 (Damodaran). The correlation flipped negative in the late 1990s and snapped positive again in 2022.",
        "xlabel":   "Year (window end)",
        "ylabel":   f"Rolling {WINDOW}-year correlation",
        "ann_pos":  "Inflation regime\n(stocks & bonds fall together)",
        "ann_neg":  "Growth/recession regime\n(bonds hedge stocks)",
        "ann_2022": "2022:\nregime break",
    },
    "hk": {
        "title":    f"美國股票與十年期國債的滾動 {WINDOW} 年相關性",
        "subtitle": "年度回報,1928-2024(Damodaran)。相關性在 1990 年代末轉負,2022 年又突然轉正。",
        "xlabel":   "年份(窗口末年)",
        "ylabel":   f"滾動 {WINDOW} 年相關性",
        "ann_pos":  "通脹主導期\n(股債齊跌)",
        "ann_neg":  "增長/衰退主導期\n(債券對沖股票)",
        "ann_2022": "2022 年:\n體制斷裂",
    },
    "tw": {
        "title":    f"美國股票與十年期公債的滾動 {WINDOW} 年相關性",
        "subtitle": "年度報酬,1928-2024(Damodaran)。相關性在 1990 年代末轉負,2022 年又突然轉正。",
        "xlabel":   "年份(窗口末年)",
        "ylabel":   f"滾動 {WINDOW} 年相關性",
        "ann_pos":  "通膨主導期\n(股債齊跌)",
        "ann_neg":  "成長/衰退主導期\n(公債對沖股票)",
        "ann_2022": "2022 年:\n體制斷裂",
    },
    "cn": {
        "title":    f"美国股票与十年期国债的滚动 {WINDOW} 年相关性",
        "subtitle": "年度回报,1928-2024(Damodaran)。相关性在 1990 年代末转负,2022 年又突然转正。",
        "xlabel":   "年份(窗口末年)",
        "ylabel":   f"滚动 {WINDOW} 年相关性",
        "ann_pos":  "通胀主导期\n(股债齐跌)",
        "ann_neg":  "增长/衰退主导期\n(国债对冲股票)",
        "ann_2022": "2022 年:\n体制断裂",
    },
}


def _corr():
    df = damodaran_annual_returns()
    return df["SP500"].rolling(WINDOW).corr(df["TBond10Y"]).dropna()


def build_fig(s):
    c = _corr()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    style_axes(ax, p)

    # Color fills
    ax.fill_between(c.index, c.values, 0, where=(c.values >= 0),
                    color=p["red"], alpha=0.25, interpolate=True)
    ax.fill_between(c.index, c.values, 0, where=(c.values < 0),
                    color=p["blue"], alpha=0.25, interpolate=True)
    ax.plot(c.index, c.values, color=p["fg"], linewidth=1.6)
    ax.axhline(0, color=p["fg"], linewidth=0.8)

    ax.text(1955, 0.55, s["ann_pos"], color=p["red"], fontsize=9.5,
            ha="center", va="center", fontweight="bold")
    ax.text(2008, -0.55, s["ann_neg"], color=p["blue"], fontsize=9.5,
            ha="center", va="center", fontweight="bold")
    last_yr = c.index[-1]
    last_v = float(c.iloc[-1])
    ax.annotate(s["ann_2022"], xy=(last_yr, last_v), xytext=(last_yr - 8, 0.65),
                fontsize=9, color=p["red"],
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.8))

    ax.set_ylim(-0.85, 0.95)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
