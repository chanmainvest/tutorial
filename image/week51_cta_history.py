"""Week 51, §2.3 — SocGen CTA Index annual returns 2000-2024 vs S&P 500.

Two-bar group per year. SocGen CTA Index annual returns approximated
from BarclayHedge / SocGen public reports. S&P 500 total returns from
the embedded Damodaran annual table. Strong CTA years (2008, 2014,
2022) and weak CTA years (2011, 2015, 2018) annotated.

Run:
    uv run python course/image/week51_cta_history.py
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
from scripts.market_data import damodaran_annual_returns  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week51_cta_history"

# SocGen CTA Index annual returns (decimal). Source: SocGen Prime
# Services public CTA Index reports, BarclayHedge supplementals.
# Rounded to single basis point of public-source consensus.
CTA = {
    2000: 0.046,  2001: 0.008,  2002: 0.183,  2003: 0.141,  2004: 0.034,
    2005: 0.017,  2006: 0.035,  2007: 0.080,  2008: 0.131,  2009: -0.041,
    2010: 0.093,  2011: -0.044, 2012: -0.029, 2013: 0.007,  2014: 0.157,
    2015: 0.000,  2016: -0.029, 2017: 0.025,  2018: -0.029, 2019: 0.091,
    2020: 0.019,  2021: 0.086,  2022: 0.205,  2023: -0.038, 2024: 0.045,
}

STRONG_YEARS = (2008, 2014, 2022)
WEAK_YEARS = (2011, 2015, 2018)


LANG_STRINGS = {
    "en": {
        "title":    "SocGen CTA Index vs S&P 500 (total return), 2000-2024",
        "subtitle": "Trend-following pays in extended trending bear markets (2008, 2022) and loses in chop (2011, 2015, 2018). Crisis alpha is the structural pattern.",
        "xlabel":   "Year",
        "ylabel":   "Calendar-year total return",
        "cta":      "SocGen CTA Index",
        "spx":      "S&P 500 (total return)",
        "ann_strong": "STRONG: trend caught it",
        "ann_weak":   "WEAK: chop, no follow-through",
        "footer":   "SocGen CTA Index from public SocGen Prime Services reports. S&P 500 total return from Damodaran histretSP. Rounded to nearest 0.1%.",
    },
    "hk": {
        "title":    "SocGen CTA 指數 vs 標普 500(總回報),2000-2024",
        "subtitle": "趨勢追蹤在持續趨勢的熊市(2008、2022)賺錢,在橫盤(2011、2015、2018)虧錢。Crisis alpha 是結構性圖案。",
        "xlabel":   "年份",
        "ylabel":   "年度總回報",
        "cta":      "SocGen CTA 指數",
        "spx":      "標普 500(總回報)",
        "ann_strong": "強年份:趨勢被捕捉到",
        "ann_weak":   "弱年份:橫盤、無延續",
        "footer":   "SocGen CTA 指數源自 SocGen Prime Services 公開報告。標普 500 總回報源自 Damodaran histretSP。四捨五入至 0.1%。",
    },
    "tw": {
        "title":    "SocGen CTA 指數 vs 標普 500(總報酬),2000-2024",
        "subtitle": "趨勢追蹤在延續性熊市(2008、2022)賺錢,在盤整(2011、2015、2018)虧錢。Crisis alpha 是結構性樣態。",
        "xlabel":   "年份",
        "ylabel":   "年度總報酬",
        "cta":      "SocGen CTA 指數",
        "spx":      "標普 500(總報酬)",
        "ann_strong": "強年份:趨勢被捕捉",
        "ann_weak":   "弱年份:盤整、無延續",
        "footer":   "SocGen CTA 指數源自 SocGen Prime Services 公開報告。標普 500 總報酬源自 Damodaran histretSP。四捨五入至 0.1%。",
    },
    "cn": {
        "title":    "SocGen CTA 指数 vs 标普 500(总回报),2000-2024",
        "subtitle": "趋势跟踪在延续性熊市(2008、2022)赚钱,在震荡市(2011、2015、2018)亏钱。Crisis alpha 是结构性模式。",
        "xlabel":   "年份",
        "ylabel":   "年度总回报",
        "cta":      "SocGen CTA 指数",
        "spx":      "标普 500(总回报)",
        "ann_strong": "强年份:趋势被捕捉",
        "ann_weak":   "弱年份:震荡、无延续",
        "footer":   "SocGen CTA 指数源自 SocGen Prime Services 公开报告。标普 500 总回报源自 Damodaran histretSP。四舍五入至 0.1%。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    dam = damodaran_annual_returns()

    years = sorted(CTA.keys())
    cta_vals = np.array([CTA[y] for y in years])
    spx_vals = np.array([float(dam.loc[y, "SP500"]) for y in years])

    fig, ax = plt.subplots(figsize=(13.0, 6.4), dpi=150)
    style_axes(ax, p)

    x = np.arange(len(years))
    w = 0.40

    cta_colors = []
    spx_colors = []
    for y in years:
        if y in STRONG_YEARS:
            cta_colors.append(p["green"])
            spx_colors.append(p["red"])
        elif y in WEAK_YEARS:
            cta_colors.append(p["red"])
            spx_colors.append(p["muted"])
        else:
            cta_colors.append(p["blue"])
            spx_colors.append(p["muted"])

    ax.bar(x - w / 2, cta_vals, width=w,
           color=cta_colors, edgecolor="white", linewidth=0.6,
           label=s["cta"])
    ax.bar(x + w / 2, spx_vals, width=w,
           color=spx_colors, edgecolor="white", linewidth=0.6, alpha=0.85,
           label=s["spx"])

    ax.axhline(0, color=p["fg"], linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([str(y) for y in years], fontsize=8.5, rotation=45)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_ylabel(s["ylabel"])
    ax.set_xlabel(s["xlabel"])
    ax.set_ylim(-0.45, 0.40)

    # Highlight callouts on strong years (CTA bar value labels).
    for y in STRONG_YEARS:
        i = years.index(y)
        v = cta_vals[i]
        ax.text(i - w / 2, v + 0.012, f"{v:+.0%}",
                ha="center", va="bottom",
                fontsize=9.2, fontweight="bold", color=p["green"])
    for y in WEAK_YEARS:
        i = years.index(y)
        v = cta_vals[i]
        yt = v - 0.012 if v < 0 else v + 0.012
        va = "top" if v < 0 else "bottom"
        ax.text(i - w / 2, yt, f"{v:+.0%}",
                ha="center", va=va,
                fontsize=9.0, fontweight="bold", color=p["red"])

    # Legend boxes for strong/weak callouts.
    ax.annotate(s["ann_strong"], xy=(years.index(2008) - w / 2, 0.131),
                xytext=(years.index(2008) - w / 2 - 1.2, 0.36),
                ha="center", fontsize=9.0, color=p["green"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=0.8))
    ax.annotate(s["ann_weak"], xy=(years.index(2015) - w / 2, 0.0),
                xytext=(years.index(2015) - w / 2 + 1.0, -0.30),
                ha="center", fontsize=9.0, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.8))

    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold", loc="left")
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10.0, color=p["muted"], style="italic")

    ax.legend(loc="upper right", frameon=False, fontsize=10)
    fig.text(0.5, 0.015, s["footer"], ha="center",
             fontsize=8.0, color=p["muted"])

    fig.tight_layout(rect=[0, 0.03, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
