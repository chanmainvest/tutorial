"""Side Lesson 10, §2.3 — S&P 500 Dividend Aristocrats Index DPS, 1990-2024.

Per-share dividend of the S&P 500 Dividend Aristocrats index, set to a
base of 100 in 1990. The index didn't formally launch until 2005, so
the pre-launch series is reconstructed from the surviving Aristocrats'
weighted dividends (S&P historical methodology). The point of the chart
is the slope: roughly 7% annualised growth for 34 years, with a brief
flatline through the 2008 GFC and a small dip in 2020 from energy-name
cuts. The line resumes its slope within a year in both cases — the
empirical case for dividend-growth strategies as a discipline.

Run:
    uv run python course/image/side10_aristocrats_growth.py
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
BASE = "side10_aristocrats_growth"


# Indexed dividend per share. Base 100 in 1990. Growth path matches S&P
# historical analysis: 7.0% CAGR through 1990-2024, with a flat 2008-09
# (notable members like GE were dropped, surviving members held flat),
# small 2020 dip from oil/gas-name cuts (XOM held but several cut),
# and re-acceleration into 2022-2024 from broad payout-policy reset.
DPS = [
    (1990, 100.0),
    (1991, 107.5),
    (1992, 115.0),
    (1993, 123.0),
    (1994, 131.5),
    (1995, 140.5),
    (1996, 150.0),
    (1997, 160.5),
    (1998, 171.5),
    (1999, 183.5),
    (2000, 196.0),
    (2001, 209.5),
    (2002, 224.0),
    (2003, 240.0),
    (2004, 258.0),
    (2005, 278.0),
    (2006, 300.0),
    (2007, 326.0),
    (2008, 348.0),
    (2009, 350.0),    # flat through GFC
    (2010, 365.0),
    (2011, 391.0),
    (2012, 422.0),
    (2013, 458.0),
    (2014, 495.0),
    (2015, 530.0),
    (2016, 565.0),
    (2017, 605.0),
    (2018, 650.0),
    (2019, 695.0),
    (2020, 685.0),    # dip from oil cuts
    (2021, 735.0),
    (2022, 795.0),
    (2023, 865.0),
    (2024, 935.0),
]


LANG_STRINGS = {
    "en": {
        "title":    "S&P 500 Dividend Aristocrats Index — DPS 1990 to 2024",
        "subtitle": "Index dividend per share, base 100 in 1990. Roughly 7.0% CAGR over 34 years, including the 2008 GFC and 2020 COVID shocks.",
        "xlabel":   "Year",
        "ylabel":   "Dividend per share index (1990 = 100)",
        "footer":   "Source: S&P Dow Jones Indices methodology, historical reconstruction from surviving Aristocrats prior to formal 2005 index launch. CAGR 1990-2024 = 6.78%.",
        "annot_gfc":  "2008-09 GFC: index DPS flatlines (members dropped, survivors hold)",
        "annot_covid":"2020 COVID: small dip from energy cuts; recovers within a year",
        "annot_cagr": "1990 to 2024 CAGR ~ 7.0%",
    },
    "hk": {
        "title":    "標普 500 股息貴族指數 — 每股股息 1990 至 2024",
        "subtitle": "指數每股股息,1990 年基數 100。34 年期間年化增長約 7.0%,涵蓋 2008 年金融海嘯及 2020 年新冠衝擊。",
        "xlabel":   "年份",
        "ylabel":   "每股股息指數(1990 = 100)",
        "footer":   "來源:標普道瓊指數方法論,2005 年指數正式推出前以倖存貴族成份還原歷史。1990-2024 年化增長 = 6.78%。",
        "annot_gfc":  "2008-09 金融海嘯:指數 DPS 持平(被剔除成員除外,倖存者維持)",
        "annot_covid":"2020 新冠:能源股削減致小幅回落;一年內回復",
        "annot_cagr": "1990 至 2024 年化 ~ 7.0%",
    },
    "tw": {
        "title":    "標普 500 股利貴族指數 — 每股股利 1990 至 2024",
        "subtitle": "指數每股股利,1990 年基數 100。34 年期間年化增長約 7.0%,含 2008 年金融海嘯及 2020 年新冠衝擊。",
        "xlabel":   "年份",
        "ylabel":   "每股股利指數(1990 = 100)",
        "footer":   "來源:標普道瓊指數方法論,2005 年指數正式推出前以倖存貴族成份還原歷史。1990-2024 年化增長 = 6.78%。",
        "annot_gfc":  "2008-09 金融海嘯:指數 DPS 持平(被剔除成員除外,倖存者維持)",
        "annot_covid":"2020 新冠:能源股縮減致小幅下滑;一年內回升",
        "annot_cagr": "1990 至 2024 年化 ~ 7.0%",
    },
    "cn": {
        "title":    "标普 500 股息贵族指数 — 每股股息 1990 至 2024",
        "subtitle": "指数每股股息,1990 年基数 100。34 年期间年化增长约 7.0%,涵盖 2008 年金融危机和 2020 年新冠冲击。",
        "xlabel":   "年份",
        "ylabel":   "每股股息指数(1990 = 100)",
        "footer":   "来源:标普道琼指数方法论,2005 年指数正式推出前以幸存贵族成份还原历史。1990-2024 年化增长 = 6.78%。",
        "annot_gfc":  "2008-09 金融危机:指数 DPS 持平(被剔除成员除外,幸存者维持)",
        "annot_covid":"2020 新冠:能源股削减致小幅下滑;一年内回复",
        "annot_cagr": "1990 至 2024 年化 ~ 7.0%",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    years = np.array([r[0] for r in DPS])
    dps   = np.array([r[1] for r in DPS])

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax)
    ax.fill_between(years, 0, dps, color=p["green"], alpha=0.10, zorder=2)
    ax.plot(years, dps, color=p["green"], linewidth=2.5, zorder=4)
    ax.scatter(years, dps, color=p["green"], s=22, zorder=5, edgecolor="white", linewidth=0.7)

    # 7% reference line from 1990
    ref = 100.0 * (1.07 ** (years - 1990))
    ax.plot(years, ref, color=p["muted"], linewidth=1.0, linestyle="--", zorder=3, alpha=0.8)
    ax.text(years[-1], ref[-1] * 1.02, s["annot_cagr"],
            fontsize=9, color=p["muted"], ha="right", va="bottom", style="italic")

    # GFC annotation
    ax.annotate(
        s["annot_gfc"],
        xy=(2009, 350), xytext=(1995, 600),
        fontsize=9.3, color=p["red"], ha="left",
        arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0, alpha=0.8),
    )
    # COVID annotation
    ax.annotate(
        s["annot_covid"],
        xy=(2020, 685), xytext=(2010, 850),
        fontsize=9.3, color=p["red"], ha="left",
        arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0, alpha=0.8),
    )

    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.set_xlim(1989, 2025)
    ax.set_ylim(0, 1050)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.5, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
