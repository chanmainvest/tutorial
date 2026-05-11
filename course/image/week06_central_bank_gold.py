"""Week 6, §2.5 — Central bank net gold purchases, 1971-2025.

Annual net official-sector gold purchases in tonnes. Bars below zero
are net selling years (most of 1990-2009). Bars above zero are net
buying years (every year since 2010). The 2022 record of 1,082 t and
the 2023 follow-up at 1,037 t are annotated.

Secondary line: official-sector gold holdings as a percentage of total
foreign reserves (proxy from World Gold Council annual estimates).

Data sources (annual values, embedded as fallback):
- World Gold Council, *Gold Demand Trends* (annual official sector
  net purchases) and *Gold Reserves by Country* (% of reserves).
- IMF International Financial Statistics (gross reserve composition).

Run:
    uv run python course/image/week06_central_bank_gold.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week06_central_bank_gold"

# Approximate annual central bank net gold purchases in tonnes
# Sources: World Gold Council *Gold Demand Trends* historical tables
# and academic compilations (Bordo & Eichengreen on the 1990s).
# Negative = net selling. Positive = net buying.
CB_NET_PURCHASES = {
    1971:  -50, 1972:  -40, 1973:  -45, 1974:  -55, 1975:  -60,
    1976:  -85, 1977:  -90, 1978: -260, 1979: -544, 1980: -230,
    1981:    0, 1982:  -85, 1983:  -85, 1984:  -85, 1985: -132,
    1986:  -32, 1987:   72, 1988:  -68, 1989: -363, 1990:    0,
    1991:  -85, 1992: -622, 1993:  -464, 1994: -125, 1995: -167,
    1996: -286, 1997: -393, 1998:  -67, 1999: -362, 2000: -474,
    2001: -522, 2002: -549, 2003: -588, 2004: -474, 2005: -663,
    2006: -370, 2007: -484, 2008: -235, 2009:   34, 2010:   77,
    2011:  481, 2012:  569, 2013:  629, 2014:  601, 2015:  580,
    2016:  395, 2017:  379, 2018:  656, 2019:  605, 2020:  255,
    2021:  450, 2022: 1082, 2023: 1037, 2024: 1045, 2025:  920,
}

# Approximate official-sector gold holdings as % of total reserves
# (gross reserves, IMF IFS basis; gold valued at LBMA PM fix).
GOLD_PCT_RESERVES = {
    1971: 35.0, 1975: 32.0, 1980: 50.0, 1985: 22.0, 1990: 15.0,
    1995: 11.0, 2000:  7.0, 2005:  6.0, 2010: 10.0, 2011: 11.5,
    2012: 12.0, 2013: 11.0, 2014: 10.5, 2015: 10.5, 2016: 11.0,
    2017: 11.5, 2018: 11.5, 2019: 12.5, 2020: 13.5, 2021: 13.0,
    2022: 14.5, 2023: 17.0, 2024: 19.5, 2025: 22.0,
}

LANG_STRINGS = {
    "en": {
        "title":    "Central bank net gold purchases, 1971-2025",
        "subtitle": "Annual tonnes (bars). Net sellers 1990-2009; net buyers every year since 2010. Record 1,082 t in 2022 after Russian-FX freeze; line shows gold as % of total official reserves.",
        "xlabel":   "Year",
        "ylabel_l": "Net purchases (tonnes)",
        "ylabel_r": "Gold as % of total reserves",
        "buy":      "Net buying",
        "sell":     "Net selling",
        "pct":      "Gold % of reserves (right axis)",
        "ann_2022": "2022: 1,082 t\n(Russia FX freeze)",
        "ann_browns": "1999 'Brown's Bottom'\nUK sells ~395 t at $282/oz",
        "footer":   "Sources: World Gold Council *Gold Demand Trends* annual tables; IMF International Financial Statistics; academic compilations.",
    },
    "hk": {
        "title":    "全球央行黃金淨購買量,1971-2025",
        "subtitle": "年度噸數(柱)。1990-2009 為淨賣家;2010 起每年都是淨買家。2022 年俄羅斯儲備被凍結後創 1,082 噸紀錄;曲線為黃金佔官方儲備比重。",
        "xlabel":   "年份",
        "ylabel_l": "淨購買量(噸)",
        "ylabel_r": "黃金佔總儲備 %",
        "buy":      "淨買入",
        "sell":     "淨賣出",
        "pct":      "黃金佔儲備比重(右軸)",
        "ann_2022": "2022:1,082 噸\n(俄羅斯外匯被凍)",
        "ann_browns": "1999「Brown 賤賣」\n英國以 282 美元/盎司賣出約 395 噸",
        "footer":   "資料來源:World Gold Council《Gold Demand Trends》年度表、IMF International Financial Statistics、學術彙編。",
    },
    "tw": {
        "title":    "全球央行黃金淨買進量,1971-2025",
        "subtitle": "年度噸數(柱)。1990-2009 為淨賣方;2010 起每年皆為淨買方。2022 年俄羅斯外匯遭凍後創下 1,082 噸紀錄;線為黃金佔官方儲備比重。",
        "xlabel":   "年份",
        "ylabel_l": "淨買進量(噸)",
        "ylabel_r": "黃金佔總儲備 %",
        "buy":      "淨買進",
        "sell":     "淨賣出",
        "pct":      "黃金佔儲備比重(右軸)",
        "ann_2022": "2022:1,082 噸\n(俄羅斯外匯凍結)",
        "ann_browns": "1999「Brown 谷底」\n英國以 282 美元/盎司賣出約 395 噸",
        "footer":   "資料來源:World Gold Council《Gold Demand Trends》年度表、IMF International Financial Statistics、學術彙編。",
    },
    "cn": {
        "title":    "全球央行黄金净购买量,1971-2025",
        "subtitle": "年度吨数(柱)。1990-2009 为净卖方;2010 起每年都是净买方。2022 年俄罗斯储备被冻结后创 1,082 吨纪录;线为黄金占官方储备比重。",
        "xlabel":   "年份",
        "ylabel_l": "净购买量(吨)",
        "ylabel_r": "黄金占总储备 %",
        "buy":      "净买入",
        "sell":     "净卖出",
        "pct":      "黄金占储备比重(右轴)",
        "ann_2022": "2022:1,082 吨\n(俄罗斯外汇冻结)",
        "ann_browns": "1999「Brown 谷底」\n英国以 282 美元/盎司卖出约 395 吨",
        "footer":   "数据来源:World Gold Council《Gold Demand Trends》年度表、IMF International Financial Statistics、学术汇编。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    yrs = sorted(CB_NET_PURCHASES)
    vals = [CB_NET_PURCHASES[y] for y in yrs]

    pct_yrs = sorted(GOLD_PCT_RESERVES)
    pct_vals = [GOLD_PCT_RESERVES[y] for y in pct_yrs]
    pct_series = pd.Series(pct_vals, index=pct_yrs).reindex(range(min(yrs), max(yrs) + 1)).interpolate()

    fig, ax = plt.subplots(figsize=(11.0, 6.2))
    style_axes(ax, p)

    bar_colors = [p["accent"] if v >= 0 else p["grey"] for v in vals]
    ax.bar(yrs, vals, color=bar_colors, alpha=0.85, width=0.85, zorder=2)
    ax.axhline(0, color=p["fg"], linewidth=0.7)
    ax.axvline(2010, color=p["blue"], linewidth=0.6, linestyle="--", alpha=0.6)
    ax.text(2010.2, ax.get_ylim()[1] * 0.05, "2010\nregime\nshift",
            fontsize=8.5, color=p["blue"], va="bottom")

    ax.annotate(s["ann_2022"], xy=(2022, 1082), xytext=(2014, 880),
                ha="center", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0))
    ax.annotate(s["ann_browns"], xy=(1999, -362), xytext=(1986, -680),
                ha="left", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel_l"])
    ax.set_xlim(min(yrs) - 1, max(yrs) + 1)
    ax.set_ylim(-800, 1300)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Right axis: % of reserves
    ax2 = ax.twinx()
    ax2.plot(pct_series.index, pct_series.values, color=p["blue"],
             linewidth=2.0, label=s["pct"])
    ax2.set_ylabel(s["ylabel_r"], color=p["blue"])
    ax2.tick_params(axis="y", colors=p["blue"], labelsize=9)
    ax2.set_ylim(0, 60)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color(p["blue"])

    # Custom legend
    from matplotlib.patches import Patch
    handles = [
        Patch(facecolor=p["accent"], alpha=0.85, label=s["buy"]),
        Patch(facecolor=p["grey"], alpha=0.85, label=s["sell"]),
        plt.Line2D([0], [0], color=p["blue"], linewidth=2.0, label=s["pct"]),
    ]
    ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=9)

    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
