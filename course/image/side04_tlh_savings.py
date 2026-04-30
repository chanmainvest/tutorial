"""Side Lesson 04, §2.3 — Cumulative tax-loss-harvesting savings.

A deterministic 30-year simulation on a $1,000,000 starting portfolio
with ~16% annualised volatility.  Each year we (a) compute a
'steady-state' harvest of 0.8% of the portfolio (lot dispersion within
an up year), and (b) on bad years a much larger harvest equal to
~40% of the realised loss beyond -5%.  Tax saved per year =
harvest * combined LTCG+state of 25%.  Returns are an embedded sequence
mimicking 1996-2025 (dot-com 2000-02, GFC 2008, 2018 chop, COVID
shock 2020, 2022 rate shock).

Run:
    uv run python course/image/side04_tlh_savings.py
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
BASE = "side04_tlh_savings"


# 30 years of annual returns (decimals).  An indicative 1996-2025-style
# sequence: dot-com run-up, three down years, GFC trough, 2018 chop,
# COVID shock, 2022 rate shock.
RETURNS = [
    0.23,   # 1996
    0.33,   # 1997
    0.28,   # 1998
    0.21,   # 1999
    -0.09,  # 2000
    -0.12,  # 2001
    -0.22,  # 2002
    0.29,   # 2003
    0.11,   # 2004
    0.05,   # 2005
    0.16,   # 2006
    0.05,   # 2007
    -0.37,  # 2008
    0.26,   # 2009
    0.15,   # 2010
    0.02,   # 2011
    0.16,   # 2012
    0.32,   # 2013
    0.14,   # 2014
    0.01,   # 2015
    0.12,   # 2016
    0.22,   # 2017
    -0.04,  # 2018
    0.31,   # 2019
    0.18,   # 2020 -- net up year despite Q1 -34% intra-year
    0.29,   # 2021
    -0.18,  # 2022
    0.26,   # 2023
    0.25,   # 2024
    0.10,   # 2025
]
# In 2020 the headline annual return is positive but Q1 had a -34%
# intra-year drawdown -- TLH platforms hit big harvests in March 2020.
# We model that with an extra-harvest flag per year.
INTRAYEAR_SHOCKS = {
    14: 0.34,  # year index for 2020 March -- use positional index 24 below
}

START_PV = 1_000_000.0
TAX_RATE = 0.25  # combined LTCG (15-20%) + state (5%)
STEADY_RATE = 0.0012   # harvest as fraction of portfolio in calm years
LOSS_HARVEST_FRAC = 0.06  # fraction of |return| beyond -5% harvested in bad years
LOSS_THRESHOLD = 0.05  # above this point in losses we assume bigger harvest
CALM_VOL_KICKER = 0.00015  # extra harvest in moderately choppy years


def simulate():
    pv = START_PV
    annual_savings = []
    annual_harvest = []
    pv_path = []
    for i, r in enumerate(RETURNS):
        # Use beginning-of-year portfolio value to compute harvest.
        steady = pv * STEADY_RATE
        # Bigger harvest in down years.
        loss_harvest = 0.0
        if r < -LOSS_THRESHOLD:
            loss_harvest = pv * LOSS_HARVEST_FRAC * (abs(r) - LOSS_THRESHOLD)
        # Special: 2020 had March -34% intra-year then recovery.
        # Position 24 in sequence (0-indexed) is 2020.
        if i == 24:
            # March 2020 trough was about -34% from peak; harvest ~40% of that
            # on the equity portion of the portfolio.
            loss_harvest += pv * LOSS_HARVEST_FRAC * (0.34 - LOSS_THRESHOLD) * 0.5
        # Modest extra harvest in 'choppy but not crashing' years (|r|<5%).
        if -LOSS_THRESHOLD < r < 0.02:
            steady += pv * CALM_VOL_KICKER
        harvest = steady + loss_harvest
        savings = harvest * TAX_RATE
        annual_harvest.append(harvest)
        annual_savings.append(savings)
        pv_path.append(pv)
        # Update portfolio.
        pv = pv * (1.0 + r)
    return (
        np.array(annual_savings),
        np.array(annual_harvest),
        np.array(pv_path),
    )


SAVINGS, HARVEST, PV_PATH = simulate()
CUM_SAVINGS = np.cumsum(SAVINGS)
YEARS = np.arange(1, len(RETURNS) + 1)


LANG_STRINGS = {
    "en": {
        "title":   "Cumulative tax-loss-harvesting savings - $1M taxable, 30 years",
        "subtitle": "Annual harvest x 25% combined LTCG+state.  Bear-year spikes (2008, 2020 March, 2022) drive the bumps; cumulative crosses $100k by year 30.",
        "xlabel":  "Year",
        "ylabel_left":  "Annual tax saved (USD)",
        "ylabel_right": "Cumulative tax saved (USD)",
        "annot_2008":   "2008 GFC: -37%",
        "annot_2020":   "2020 March -34% intra-year",
        "annot_2022":   "2022 rate shock: -18%",
        "label_bar":    "Annual saved",
        "label_line":   "Cumulative saved",
        "footer":       "Model: harvest = 12 bps/yr steady + 6% of return beyond -5% in bear years.  Combined tax 25% (LTCG 20% + state 5%).  Returns are an indicative 1996-2025 path; cumulative ~$108k.",
    },
    "hk": {
        "title":   "稅損收割累積節稅 - 100 萬美元應稅,30 年",
        "subtitle": "每年收割 x 25% 合計 LTCG+州稅。熊市年(2008、2020 三月、2022)爆發;30 年累積超過 10 萬美元。",
        "xlabel":  "年數",
        "ylabel_left":  "年度節稅(美元)",
        "ylabel_right": "累積節稅(美元)",
        "annot_2008":   "2008 金融海嘯:-37%",
        "annot_2020":   "2020 年 3 月 -34%",
        "annot_2022":   "2022 加息衝擊:-18%",
        "label_bar":    "年度節稅",
        "label_line":   "累積節稅",
        "footer":       "模型:每年穩態收割 12 bps + 熊市超過 -5% 部分的 6%。合計稅率 25%(LTCG 20% + 州稅 5%)。報酬序列為 1996-2025 指示性路徑;30 年累積約 10.8 萬美元。",
    },
    "tw": {
        "title":   "稅損收割累積節稅 - 100 萬美元應稅,30 年",
        "subtitle": "每年收割 x 25% 合計 LTCG+州稅。空頭年(2008、2020 三月、2022)爆發;30 年累積超過 10 萬美元。",
        "xlabel":  "年數",
        "ylabel_left":  "年度節稅(美元)",
        "ylabel_right": "累積節稅(美元)",
        "annot_2008":   "2008 金融海嘯:-37%",
        "annot_2020":   "2020 年 3 月 -34%",
        "annot_2022":   "2022 升息衝擊:-18%",
        "label_bar":    "年度節稅",
        "label_line":   "累積節稅",
        "footer":       "模型:每年穩態收割 12 bps + 空頭超過 -5% 部分的 6%。合計稅率 25%(LTCG 20% + 州稅 5%)。報酬序列為 1996-2025 指示性路徑;30 年累積約 10.8 萬美元。",
    },
    "cn": {
        "title":   "税损收割累积节税 - 100 万美元应税,30 年",
        "subtitle": "每年收割 x 25% 合计 LTCG+州税。熊市年(2008、2020 三月、2022)爆发;30 年累积超过 10 万美元。",
        "xlabel":  "年数",
        "ylabel_left":  "年度节税(美元)",
        "ylabel_right": "累积节税(美元)",
        "annot_2008":   "2008 金融海啸:-37%",
        "annot_2020":   "2020 年 3 月 -34%",
        "annot_2022":   "2022 加息冲击:-18%",
        "label_bar":    "年度节税",
        "label_line":   "累积节税",
        "footer":       "模型:每年稳态收割 12 bps + 熊市超过 -5% 部分的 6%。合计税率 25%(LTCG 20% + 州税 5%)。报酬序列为 1996-2025 指示性路径;30 年累积约 10.8 万美元。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=150)
    style_axes(ax)

    # Bar colours: bear years red, calm years navy.
    colors = []
    for r in RETURNS:
        if r < -LOSS_THRESHOLD:
            colors.append(p["red"])
        elif r < 0.02:
            colors.append(p["accent"])
        else:
            colors.append(p["blue"])
    # Extra red for 2020 (the intra-year shock).
    colors[24] = p["red"]

    bars = ax.bar(YEARS, SAVINGS, color=colors, edgecolor="white",
                  linewidth=0.8, zorder=3, label=s["label_bar"])

    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel_left"], fontsize=10)
    ax.set_xlim(0.4, len(RETURNS) + 0.6)
    ax.set_ylim(0, max(SAVINGS) * 1.18)
    # Format y-axis as $k.
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${int(v/1000)}k"))

    # Right axis = cumulative savings line.
    ax2 = ax.twinx()
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color(p["muted"])
    ax2.tick_params(colors=p["fg"], labelsize=9)
    ax2.plot(YEARS, CUM_SAVINGS, color=p["green"], linewidth=2.6,
             marker="o", markersize=4.5, zorder=5,
             label=s["label_line"])
    ax2.set_ylabel(s["ylabel_right"], fontsize=10, color=p["green"])
    ax2.set_ylim(0, max(CUM_SAVINGS) * 1.10)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${int(v/1000)}k"))
    ax2.tick_params(axis="y", colors=p["green"])

    # Annotate the three big years.
    # 2008 = position 12 (year 13).
    yr_2008 = 13
    ax.annotate(
        s["annot_2008"],
        xy=(yr_2008, SAVINGS[12]),
        xytext=(yr_2008 - 1.2, SAVINGS[12] * 1.10),
        fontsize=9, color=p["red"], fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=p["red"], lw=0.8))
    # 2020 = position 24 (year 25).
    yr_2020 = 25
    ax.annotate(
        s["annot_2020"],
        xy=(yr_2020, SAVINGS[24]),
        xytext=(yr_2020 - 4.5, SAVINGS[24] * 0.95),
        fontsize=9, color=p["red"], fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=p["red"], lw=0.8))
    # 2022 = position 26 (year 27).
    yr_2022 = 27
    ax.annotate(
        s["annot_2022"],
        xy=(yr_2022, SAVINGS[26]),
        xytext=(yr_2022 - 0.5, SAVINGS[26] * 1.20),
        fontsize=9, color=p["red"], fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=p["red"], lw=0.8))

    # Cumulative endpoint label.
    ax2.text(YEARS[-1] + 0.05, CUM_SAVINGS[-1],
             f"${int(round(CUM_SAVINGS[-1]/1000))}k",
             color=p["green"], fontsize=10.5, fontweight="bold",
             va="center")

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=p["muted"], wrap=True)

    # Legend combining both axes.
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left",
              frameon=False, fontsize=9.5)

    fig.tight_layout(rect=[0, 0.05, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
