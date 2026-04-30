"""Week 22, §2.1 — DXY (US Dollar Index) 1985 to April 2026.

Quarterly DXY (ICE basket: EUR 57.6, JPY 13.6, GBP 11.9, CAD 9.1,
SEK 4.2, CHF 3.6) embedded inline as approximate quarter-end values.
We optionally overlay the FRED broad-trade-weighted dollar
(DTWEXBGS, 2006+) but the chart is fully renderable offline.

Five regime markers annotated: 1985 Plaza Accord (peak ~165),
2002 USD peak (~120), 2008 trough (~71), post-2014 structural USD
bid, and the 2025 policy-driven reset.

Run:
    uv run python course/image/week22_dxy_decade.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week22_dxy_decade"


# Quarter-end DXY values, approximate. Source: ICE / Bloomberg /
# St. Louis Fed (DTWEXM legacy, then DTWEXAFEGS as proxy where DXY
# itself isn't on FRED). Rounded to whole points; precise tick is
# not the point of the chart.
DXY = {
    # year: [Q1, Q2, Q3, Q4]
    1985: [158, 145, 132, 124],
    1986: [120, 113, 109, 105],
    1987: [101, 96,  98,  91],
    1988: [88,  92,  98,  92],
    1989: [98, 100, 100,  94],
    1990: [89,  86,  82,  84],
    1991: [89,  93,  90,  85],
    1992: [86,  84,  79,  82],
    1993: [88,  88,  91,  92],
    1994: [89,  86,  85,  88],
    1995: [86,  85,  82,  85],
    1996: [86,  87,  88,  87],
    1997: [91,  93,  98,  99],
    1998: [99,  98,  98,  93],
    1999: [99,  98, 100, 102],
    2000: [105,107, 113, 109],
    2001: [115,116, 116, 117],
    2002: [118,107, 108, 102],
    2003: [99,  94,  93,  87],
    2004: [88,  88,  87,  81],
    2005: [82,  89,  89,  91],
    2006: [89,  86,  86,  84],
    2007: [83,  82,  78,  76],
    2008: [72,  73,  77,  82],
    2009: [85,  80,  77,  78],
    2010: [81,  86,  79,  79],
    2011: [76,  75,  79,  80],
    2012: [79,  82,  80,  80],
    2013: [83,  83,  80,  80],
    2014: [80,  80,  86,  90],
    2015: [98,  96,  96,  98],
    2016: [95,  96,  95, 102],
    2017: [100, 96,  93,  92],
    2018: [89,  95,  95,  96],
    2019: [97,  96,  99,  96],
    2020: [99,  97,  94,  90],
    2021: [93,  92,  94,  96],
    2022: [98, 105, 112, 104],
    2023: [102,103, 106, 101],
    2024: [104,106, 100, 108],
    2025: [109, 99,  96,  97],   # 2025 policy reset visible
    2026: [95,   None, None, None],   # April 2026 reading only
}


def _build_series():
    rows = []
    for year, qs in DXY.items():
        for qi, v in enumerate(qs):
            if v is None:
                continue
            month = qi * 3 + 3   # Mar, Jun, Sep, Dec
            rows.append((pd.Timestamp(year, month, 28), v))
    df = pd.DataFrame(rows, columns=["date", "dxy"]).set_index("date")
    return df


LANG_STRINGS = {
    "en": {
        "title":    "DXY -- US Dollar Index, 1985 to April 2026",
        "subtitle": "Quarter-end levels of the ICE DXY basket: EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%. Two-thirds of it is the euro.",
        "ylabel":   "DXY level",
        "xlabel":   "Year",
        "plaza":    "1985 Plaza Accord:\nG5 coordinates USD weakening",
        "peak2002": "2002 USD peak ~120:\nend of dot-com inflows",
        "trough08": "2008 trough ~71:\nFed cuts to zero",
        "bid2014":  "Post-2014 structural USD bid:\nshale + reserve status + Fed",
        "reset25":  "2025 policy reset:\ntariff regime + admin shift",
        "footer":   "Source: ICE DXY quarterly closes (approximate). The DXY does not include CNY, MXN, INR, KRW or any emerging-market currency.",
    },
    "hk": {
        "title":    "DXY──美元指數,1985 至 2026 年 4 月",
        "subtitle": "ICE DXY 一籃子季末水平:歐元 57.6%、日圓 13.6%、英鎊 11.9%、加元 9.1%、瑞典克朗 4.2%、瑞郎 3.6%。三分之二其實就是歐元。",
        "ylabel":   "DXY 水平",
        "xlabel":   "年份",
        "plaza":    "1985 廣場協議:\nG5 協調美元貶值",
        "peak2002": "2002 美元高峰 ~120:\n網絡熱資金見頂",
        "trough08": "2008 低點 ~71:\n聯儲減息至零",
        "bid2014":  "2014 後結構性美元買盤:\n頁岩 + 儲備地位 + 聯儲",
        "reset25":  "2025 政策重置:\n關稅制度 + 政權交替",
        "footer":   "資料:ICE DXY 季末(近似值)。DXY 不包含人民幣、墨西哥披索、印度盧比、韓圜或任何新興市場貨幣。",
    },
    "tw": {
        "title":    "DXY──美元指數,1985 至 2026 年 4 月",
        "subtitle": "ICE DXY 一籃子季末水準:歐元 57.6%、日圓 13.6%、英鎊 11.9%、加元 9.1%、瑞典克朗 4.2%、瑞郎 3.6%。三分之二其實就是歐元。",
        "ylabel":   "DXY 水準",
        "xlabel":   "年份",
        "plaza":    "1985 廣場協議:\nG5 協調美元走弱",
        "peak2002": "2002 美元高點 ~120:\n網路熱資金見頂",
        "trough08": "2008 低點 ~71:\n聯準會降息至零",
        "bid2014":  "2014 後結構性美元買盤:\n頁岩 + 儲備地位 + 聯準會",
        "reset25":  "2025 政策重置:\n關稅制度 + 政權交替",
        "footer":   "資料:ICE DXY 季末(近似值)。DXY 不含人民幣、墨西哥披索、印度盧比、韓圜或任何新興市場貨幣。",
    },
    "cn": {
        "title":    "DXY──美元指数,1985 至 2026 年 4 月",
        "subtitle": "ICE DXY 一篮子季末水平:欧元 57.6%、日元 13.6%、英镑 11.9%、加元 9.1%、瑞典克朗 4.2%、瑞郎 3.6%。三分之二其实就是欧元。",
        "ylabel":   "DXY 水平",
        "xlabel":   "年份",
        "plaza":    "1985 广场协议:\nG5 协调美元贬值",
        "peak2002": "2002 美元高点 ~120:\n互联网热资金见顶",
        "trough08": "2008 低点 ~71:\n美联储降息至零",
        "bid2014":  "2014 后结构性美元买盘:\n页岩 + 储备地位 + 美联储",
        "reset25":  "2025 政策重置:\n关税制度 + 政权交替",
        "footer":   "数据:ICE DXY 季末(近似值)。DXY 不包含人民币、墨西哥比索、印度卢比、韩圆或任何新兴市场货币。",
    },
}


def build_fig(s):
    df = _build_series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.5, 6.0))
    style_axes(ax, p)

    ax.plot(df.index, df["dxy"], color=p["blue"], linewidth=1.8)
    ax.fill_between(df.index, 70, df["dxy"], color=p["blue"], alpha=0.07)

    # Long-run mean band
    mean_lvl = float(df["dxy"].mean())
    ax.axhline(mean_lvl, color=p["muted"], linewidth=0.9, linestyle=":")
    ax.text(df.index[2], mean_lvl + 1.2, f"~{mean_lvl:.0f} long-run mean",
            color=p["muted"], fontsize=8.5, style="italic")

    # Annotations -- five regime markers.
    annots = [
        (pd.Timestamp(1985, 3, 28), 158, s["plaza"],     p["red"],     ( 22, -38)),
        (pd.Timestamp(2002, 3, 28), 118, s["peak2002"],  p["orange"],  (-90,  26)),
        (pd.Timestamp(2008, 3, 28),  72, s["trough08"],  p["green"],   (-150, 42)),
        (pd.Timestamp(2015, 12, 28), 98, s["bid2014"],   p["purple"],  (-180, 50)),
        (pd.Timestamp(2025, 3, 28), 109, s["reset25"],   p["accent"],  ( -50, -50)),
    ]
    for x, y, txt, col, off in annots:
        ax.plot(x, y, "o", color=col, markersize=7, zorder=5)
        ax.annotate(
            txt, xy=(x, y), xytext=off, textcoords="offset points",
            fontsize=8.5, color=col, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=col, lw=0.9, alpha=0.85),
            bbox=dict(boxstyle="round,pad=0.3", facecolor=p["bg"],
                      edgecolor=col, alpha=0.92),
        )

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(65, 175)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=42)
    ax.text(0, 1.025, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"], style="italic")

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
