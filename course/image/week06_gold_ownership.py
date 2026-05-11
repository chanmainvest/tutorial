"""Week 6, §2.9 — Gold as % of global financial assets, 1971-2025.

Estimated share of investable gold (above-ground stocks excluding
jewellery and central-bank holdings, valued at LBMA PM fix) in total
global financial assets (equities + debt securities + deposits, by
broad SIFMA / Credit Suisse Global Wealth Report estimates).

This is an *illustrative derived series* — the inputs are public but
the ratio is not directly published as a single time series. It shows
the recurring pattern: gold's share collapses during long equity-bull
disinflations (1980-2000, 2009-2019) and snaps back in inflationary
or crisis windows.

Annotated extrema:
- 1971: ~6% (gold standard about to end)
- 1980 peak: ~13% (Volcker shock, 21% inflation)
- 2000 trough: ~0.5% (peak passive consensus)
- 2011 peak: ~3.5% (post-GFC bid)
- 2026 current: ~1.7% (long-term avg ~5%)

Sources: World Gold Council estimates of above-ground gold stocks;
Credit Suisse / UBS *Global Wealth Report* annual financial-assets
series; SIFMA *Capital Markets Fact Book*.

Run:
    uv run python course/image/week06_gold_ownership.py
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
BASE = "week06_gold_ownership"

# Illustrative derived annual series — see module docstring for sources.
GOLD_PCT_FINASSETS = {
    1971:  6.0, 1972:  7.0, 1973:  8.5, 1974: 10.5, 1975:  9.0,
    1976:  7.5, 1977:  8.5, 1978:  9.5, 1979: 11.0, 1980: 13.0,
    1981:  9.0, 1982:  6.5, 1983:  6.0, 1984:  5.0, 1985:  4.5,
    1986:  4.0, 1987:  4.5, 1988:  4.0, 1989:  3.5, 1990:  3.2,
    1991:  3.0, 1992:  2.7, 1993:  2.6, 1994:  2.5, 1995:  2.2,
    1996:  1.9, 1997:  1.5, 1998:  1.1, 1999:  0.9, 2000:  0.5,
    2001:  0.6, 2002:  0.7, 2003:  0.9, 2004:  1.0, 2005:  1.2,
    2006:  1.5, 2007:  1.7, 2008:  2.4, 2009:  2.5, 2010:  3.0,
    2011:  3.5, 2012:  3.2, 2013:  2.5, 2014:  2.2, 2015:  2.0,
    2016:  2.0, 2017:  1.9, 2018:  1.8, 2019:  1.7, 2020:  2.0,
    2021:  1.7, 2022:  1.6, 2023:  1.6, 2024:  1.7, 2025:  1.7,
}

LANG_STRINGS = {
    "en": {
        "title":    "Gold as % of global financial assets, 1971-2025",
        "subtitle": "Investable gold (excl. jewellery & CB holdings) divided by global stocks + bonds + deposits. Long-run average ~5%; today ~1.7%, near a half-century low.",
        "xlabel":   "Year",
        "ylabel":   "Gold share of global financial assets (%)",
        "mean":     "Long-run average ~5%",
        "ann_1971": "1971 ~6%\nBretton Woods\nabout to end",
        "ann_1980": "1980 peak ~13%\n21% CPI",
        "ann_2000": "2000 trough ~0.5%\nPeak passive consensus",
        "ann_2011": "2011 peak ~3.5%\nPost-GFC bid",
        "ann_now":  "Apr 2026 ~1.7%",
        "footer":   "Illustrative series. Sources: World Gold Council above-ground stock estimates; Credit Suisse / UBS *Global Wealth Report*; SIFMA *Capital Markets Fact Book*.",
    },
    "hk": {
        "title":    "黃金佔全球金融資產比重,1971-2025",
        "subtitle": "可投資黃金(扣除首飾與央行)除以全球股票+債券+存款。長期平均約 5%;現時約 1.7%,接近半世紀低位。",
        "xlabel":   "年份",
        "ylabel":   "黃金佔全球金融資產(%)",
        "mean":     "長期均值約 5%",
        "ann_1971": "1971 約 6%\n布雷頓森林\n即將結束",
        "ann_1980": "1980 高峰約 13%\nCPI 21%",
        "ann_2000": "2000 低谷約 0.5%\n被動投資共識頂峰",
        "ann_2011": "2011 高峰約 3.5%\n金融海嘯後追入",
        "ann_now":  "2026 年 4 月 約 1.7%",
        "footer":   "僅供示意。資料來源:World Gold Council 地上黃金存量估算;Credit Suisse / UBS《Global Wealth Report》;SIFMA《Capital Markets Fact Book》。",
    },
    "tw": {
        "title":    "黃金佔全球金融資產比重,1971-2025",
        "subtitle": "可投資黃金(不含首飾與央行)除以全球股票+債券+存款。長期平均約 5%;目前約 1.7%,逼近半世紀低點。",
        "xlabel":   "年份",
        "ylabel":   "黃金佔全球金融資產(%)",
        "mean":     "長期均值約 5%",
        "ann_1971": "1971 約 6%\n布列敦森林\n即將結束",
        "ann_1980": "1980 高峰約 13%\nCPI 21%",
        "ann_2000": "2000 低谷約 0.5%\n被動投資共識頂峰",
        "ann_2011": "2011 高峰約 3.5%\n金融海嘯後買入",
        "ann_now":  "2026 年 4 月 約 1.7%",
        "footer":   "僅供示意。資料來源:World Gold Council 地上黃金存量估算;Credit Suisse / UBS《Global Wealth Report》;SIFMA《Capital Markets Fact Book》。",
    },
    "cn": {
        "title":    "黄金占全球金融资产比重,1971-2025",
        "subtitle": "可投资黄金(不含首饰与央行)除以全球股票+债券+存款。长期平均约 5%;当前约 1.7%,接近半世纪低位。",
        "xlabel":   "年份",
        "ylabel":   "黄金占全球金融资产(%)",
        "mean":     "长期均值约 5%",
        "ann_1971": "1971 约 6%\n布雷顿森林\n即将结束",
        "ann_1980": "1980 高峰约 13%\nCPI 21%",
        "ann_2000": "2000 低谷约 0.5%\n被动投资共识顶峰",
        "ann_2011": "2011 高峰约 3.5%\n金融危机后买入",
        "ann_now":  "2026 年 4 月 约 1.7%",
        "footer":   "仅供示意。数据来源:World Gold Council 地上黄金存量估算;Credit Suisse / UBS《Global Wealth Report》;SIFMA《Capital Markets Fact Book》。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    yrs = sorted(GOLD_PCT_FINASSETS)
    pct = pd.Series([GOLD_PCT_FINASSETS[y] for y in yrs], index=yrs, dtype=float)

    fig, ax = plt.subplots(figsize=(10.6, 5.8))
    style_axes(ax, p)

    ax.axhline(5.0, color=p["muted"], linewidth=1.0, linestyle="--", zorder=1)
    ax.text(yrs[-1] - 0.5, 5.3, s["mean"], ha="right", fontsize=8.5,
            color=p["muted"])

    ax.plot(yrs, pct.values, color=p["accent"], linewidth=2.2)
    ax.fill_between(yrs, 0, pct.values, color=p["accent"], alpha=0.12)

    ann_points = [
        (1971, pct.loc[1971], s["ann_1971"], (1974, 9.5), p["blue"]),
        (1980, pct.loc[1980], s["ann_1980"], (1985, 12.0), p["red"]),
        (2000, pct.loc[2000], s["ann_2000"], (2002, 4.0), p["green"]),
        (2011, pct.loc[2011], s["ann_2011"], (2007, 6.5), p["red"]),
        (2026, pct.iloc[-1], s["ann_now"], (2022, 3.5), p["blue"]),
    ]
    for x, y, txt, xytext, color in ann_points:
        ax.annotate(txt, xy=(x, y), xytext=xytext,
                    ha="center", fontsize=8.5, color=color, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=color, lw=0.9))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(yrs[0] - 1, yrs[-1] + 1)
    ax.set_ylim(0, 14)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8.2, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
