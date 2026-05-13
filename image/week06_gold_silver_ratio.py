"""Week 6, §2.7 — Gold/silver ratio, 1968-2026.

Annual-average ratio of gold price to silver price (USD/oz). Long-run
average around 65:1; flagged extrema:
- Jan 1980: ~17:1 (Hunt brothers silver squeeze)
- 1991: ~100:1 (post-bullion crisis)
- Apr 2011: ~32:1 (precious-metals euphoria)
- Mar 2020: ~125:1 (COVID liquidation, all-time high)
- Apr 2026: ~80:1 (current)

Sources (annual averages, embedded as fallback):
- Gold: LBMA London PM fix (FRED GOLDAMGBD228NLBM).
- Silver: LBMA silver fix / Kitco / USGS Mineral Yearbook.

Run:
    uv run python course/image/week06_gold_silver_ratio.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from week06_gold_real import GOLD_FALLBACK  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week06_gold_silver_ratio"

# Annual-average silver price, USD/oz (Kitco / USGS / LBMA fix).
SILVER_FALLBACK = {
    1968:  2.14, 1969:  1.79, 1970:  1.77, 1971:  1.55, 1972:  1.69,
    1973:  2.56, 1974:  4.71, 1975:  4.42, 1976:  4.35, 1977:  4.62,
    1978:  5.40, 1979: 11.09, 1980: 20.98, 1981: 10.52, 1982:  7.95,
    1983: 11.44, 1984:  8.14, 1985:  6.14, 1986:  5.47, 1987:  7.01,
    1988:  6.53, 1989:  5.50, 1990:  4.83, 1991:  4.04, 1992:  3.94,
    1993:  4.31, 1994:  5.28, 1995:  5.20, 1996:  5.20, 1997:  4.91,
    1998:  5.55, 1999:  5.22, 2000:  4.95, 2001:  4.39, 2002:  4.60,
    2003:  4.88, 2004:  6.66, 2005:  7.32, 2006: 11.55, 2007: 13.38,
    2008: 14.99, 2009: 14.67, 2010: 20.19, 2011: 35.12, 2012: 31.15,
    2013: 23.79, 2014: 19.08, 2015: 15.68, 2016: 17.14, 2017: 17.05,
    2018: 15.71, 2019: 16.21, 2020: 20.55, 2021: 25.14, 2022: 21.73,
    2023: 23.35, 2024: 28.27, 2025: 32.50, 2026: 35.30,
}

LANG_STRINGS = {
    "en": {
        "title":    "Gold/silver ratio, 1968-2026",
        "subtitle": "Annual average. Long-run mean ~65:1 (dashed). Below 30 historically marked silver tops; above 100 has marked precious-metals lows.",
        "xlabel":   "Year",
        "ylabel":   "Gold price / silver price (oz per oz)",
        "mean":     "Long-run mean ~65:1",
        "ann_1980": "1980 ~16:1\nHunt squeeze",
        "ann_1991": "1991 ~96:1\nPost-bullion crisis",
        "ann_2011": "2011 ~32:1\nPM euphoria",
        "ann_2020": "Mar 2020 ~125:1\nCOVID liquidation",
        "ann_now":  "Apr 2026 ~80:1",
        "footer":   "Sources: LBMA gold PM fix (FRED GOLDAMGBD228NLBM); LBMA silver fix / Kitco / USGS Mineral Yearbook.",
    },
    "hk": {
        "title":    "金銀比價,1968-2026",
        "subtitle": "年平均。長期均值約 65:1(虛線)。低於 30 歷來是白銀頂;高於 100 則是貴金屬底。",
        "xlabel":   "年份",
        "ylabel":   "黃金價格 / 白銀價格(每盎司)",
        "mean":     "長期均值約 65:1",
        "ann_1980": "1980 約 16:1\n亨特軋空",
        "ann_1991": "1991 約 96:1\n金條危機後",
        "ann_2011": "2011 約 32:1\n貴金屬熱潮",
        "ann_2020": "2020 年 3 月 約 125:1\n新冠拋售",
        "ann_now":  "2026 年 4 月 約 80:1",
        "footer":   "資料來源:LBMA 黃金下午定盤(FRED GOLDAMGBD228NLBM);LBMA 白銀定盤 / Kitco / USGS《Mineral Yearbook》。",
    },
    "tw": {
        "title":    "金銀比價,1968-2026",
        "subtitle": "年平均。長期均值約 65:1(虛線)。低於 30 歷史上是白銀頭部;高於 100 則是貴金屬底部。",
        "xlabel":   "年份",
        "ylabel":   "黃金價格 / 白銀價格(每盎司)",
        "mean":     "長期均值約 65:1",
        "ann_1980": "1980 約 16:1\n亨特軋空",
        "ann_1991": "1991 約 96:1\n金條危機後",
        "ann_2011": "2011 約 32:1\n貴金屬熱潮",
        "ann_2020": "2020 年 3 月 約 125:1\n新冠拋售",
        "ann_now":  "2026 年 4 月 約 80:1",
        "footer":   "資料來源:LBMA 黃金午盤(FRED GOLDAMGBD228NLBM);LBMA 白銀定盤 / Kitco / USGS《Mineral Yearbook》。",
    },
    "cn": {
        "title":    "金银比价,1968-2026",
        "subtitle": "年平均。长期均值约 65:1(虚线)。低于 30 历史上是白银顶部;高于 100 则是贵金属底部。",
        "xlabel":   "年份",
        "ylabel":   "黄金价格 / 白银价格(每盎司)",
        "mean":     "长期均值约 65:1",
        "ann_1980": "1980 约 16:1\n亨特挤空",
        "ann_1991": "1991 约 96:1\n金条危机后",
        "ann_2011": "2011 约 32:1\n贵金属热潮",
        "ann_2020": "2020 年 3 月 约 125:1\n新冠抛售",
        "ann_now":  "2026 年 4 月 约 80:1",
        "footer":   "数据来源:LBMA 黄金下午定盘(FRED GOLDAMGBD228NLBM);LBMA 白银定盘 / Kitco / USGS《Mineral Yearbook》。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    yrs = sorted(set(GOLD_FALLBACK) & set(SILVER_FALLBACK))
    gold = pd.Series([float(GOLD_FALLBACK[y]) for y in yrs], index=yrs)
    silver = pd.Series([float(SILVER_FALLBACK[y]) for y in yrs], index=yrs)
    ratio = gold / silver

    fig, ax = plt.subplots(figsize=(10.6, 6.0))
    style_axes(ax, p)

    ax.fill_between(ratio.index, 30, 100, color=p["grid"], alpha=0.25, zorder=0)
    ax.axhline(65, color=p["muted"], linewidth=1.0, linestyle="--", zorder=1)
    ax.text(ratio.index.max() - 0.5, 67, s["mean"], ha="right", fontsize=8.5,
            color=p["muted"])

    ax.plot(ratio.index, ratio.values, color=p["accent"], linewidth=2.0)
    ax.fill_between(ratio.index, 0, ratio.values, color=p["accent"], alpha=0.10)

    # Annotations at key extrema (use annual-average values)
    ann_points = [
        (1980, ratio.loc[1980], s["ann_1980"], (1980 - 5, ratio.loc[1980] - 30), p["green"]),
        (1991, ratio.loc[1991], s["ann_1991"], (1995, ratio.loc[1991] + 18), p["red"]),
        (2011, ratio.loc[2011], s["ann_2011"], (2003, ratio.loc[2011] - 28), p["green"]),
        (2020, ratio.loc[2020], s["ann_2020"], (2014, ratio.loc[2020] + 22), p["red"]),
        (2026, ratio.iloc[-1], s["ann_now"], (2024, ratio.iloc[-1] + 18), p["blue"]),
    ]
    for x, y, txt, xytext, color in ann_points:
        ax.annotate(txt, xy=(x, y), xytext=xytext,
                    ha="center", fontsize=8.5, color=color, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=color, lw=0.9))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(ratio.index.min() - 1, ratio.index.max() + 1)
    ax.set_ylim(0, max(ratio.max() * 1.1, 130))
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
