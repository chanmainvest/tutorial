"""Side 06, sec 2.4 -- Real annualised returns by asset class, 1970-1982.

Bar chart of approximate real annualised returns during the canonical
US high-inflation regime (CPI averaged 7.8% per year over the window).
Static reference values curated from Damodaran historical series, BLS
CPIAUCSL, GFD historical commodity / gold composites.

Run:
    uv run python course/image/side06_real_returns_inflation.py
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
BASE = "side06_real_returns_inflation"


# Approximate real annualised returns 1970-1982. CPI averaged 7.8%/yr.
# Sources: Damodaran historical (sp500, tbill, tbond), GFD/Kitco (gold),
# Bloomberg Commodity composite predecessors (commodities), Case-Shiller
# real (real estate).
RETS = {
    "sp500":  -0.01,
    "tbill":   0.00,
    "tbond":  -0.03,
    "reits":   0.02,
    "comm":    0.12,
    "gold":    0.18,
}


LANG_STRINGS = {
    "en": {
        "title":    "Real annualised returns by asset class, 1970 - 1982",
        "subtitle": "CPI averaged 7.8% per year over the window. Bonds catastrophic, stocks broke even, gold and commodities carried the period.",
        "xlabel":   "",
        "ylabel":   "Real annualised return",
        "labels":   {
            "sp500":  "S&P 500",
            "tbill":  "T-bills\n(cash)",
            "tbond":  "Long\nTreasuries",
            "reits":  "Real\nestate",
            "comm":   "Broad\ncommodities",
            "gold":   "Gold",
        },
        "annot_loser":  "Long bonds:\n13 yr negative real",
        "annot_winner": "Gold released by\nend of Bretton Woods 1971",
        "footer":       "Sources: Damodaran (SP500/TBill/TBond), Case-Shiller (real estate), BCOM predecessors (commodities), Kitco/GFD (gold). CPI = BLS CPIAUCSL.",
    },
    "hk": {
        "title":    "1970 - 1982 各類資產實質年化回報",
        "subtitle": "期內 CPI 年均 7.8%。債券災難、股票打和、黃金與商品撐起整個年代。",
        "xlabel":   "",
        "ylabel":   "實質年化回報",
        "labels":   {
            "sp500":  "標普 500",
            "tbill":  "短期\n國庫(現金)",
            "tbond":  "長期\n國債",
            "reits":  "房地產",
            "comm":   "商品\n綜合",
            "gold":   "黃金",
        },
        "annot_loser":  "長債:13 年\n持續實質負回報",
        "annot_winner": "1971 年布雷頓\n森林解體釋放黃金",
        "footer":       "資料:Damodaran(標普/短債/長債)、Case-Shiller(地產)、BCOM 前身(商品)、Kitco/GFD(黃金)。CPI = BLS CPIAUCSL。",
    },
    "tw": {
        "title":    "1970 - 1982 各類資產實質年化報酬",
        "subtitle": "期內 CPI 年均 7.8%。債券災難、股票打平、黃金與商品撐起整個年代。",
        "xlabel":   "",
        "ylabel":   "實質年化報酬",
        "labels":   {
            "sp500":  "標普 500",
            "tbill":  "短期\n國庫(現金)",
            "tbond":  "長期\n國債",
            "reits":  "房地產",
            "comm":   "商品\n綜合",
            "gold":   "黃金",
        },
        "annot_loser":  "長債:13 年\n持續實質負報酬",
        "annot_winner": "1971 年布列敦\n森林解體釋放黃金",
        "footer":       "資料:Damodaran(標普/短債/長債)、Case-Shiller(地產)、BCOM 前身(商品)、Kitco/GFD(黃金)。CPI = BLS CPIAUCSL。",
    },
    "cn": {
        "title":    "1970 - 1982 各类资产实质年化回报",
        "subtitle": "期内 CPI 年均 7.8%。债券灾难、股票打平、黄金与商品撑起整个年代。",
        "xlabel":   "",
        "ylabel":   "实质年化回报",
        "labels":   {
            "sp500":  "标普 500",
            "tbill":  "短期\n国库(现金)",
            "tbond":  "长期\n国债",
            "reits":  "房地产",
            "comm":   "商品\n综合",
            "gold":   "黄金",
        },
        "annot_loser":  "长债:13 年\n持续实质负回报",
        "annot_winner": "1971 年布雷顿\n森林解体释放黄金",
        "footer":       "数据:Damodaran(标普/短债/长债)、Case-Shiller(地产)、BCOM 前身(商品)、Kitco/GFD(黄金)。CPI = BLS CPIAUCSL。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    keys = ["sp500", "tbill", "tbond", "reits", "comm", "gold"]
    vals = [RETS[k] for k in keys]
    labs = [s["labels"][k] for k in keys]
    cols = []
    for k, v in zip(keys, vals):
        if v <= -0.005:
            cols.append(p["red"])
        elif v < 0.03:
            cols.append(p["grey"])
        else:
            cols.append(p["green"])

    fig, ax = plt.subplots(figsize=(11.0, 6.0), dpi=150)
    style_axes(ax, p)

    bars = ax.bar(np.arange(len(keys)), vals, color=cols,
                  edgecolor="white", linewidth=1.2, width=0.62)
    ax.axhline(0, color=p["fg"], linewidth=0.9)

    for b, v in zip(bars, vals):
        if v >= 0:
            y = v + 0.006
            va = "bottom"
        else:
            y = v - 0.006
            va = "top"
        ax.text(b.get_x() + b.get_width() / 2, y,
                f"{v:+.0%}", ha="center", va=va,
                fontsize=11, fontweight="bold", color=p["fg"])

    ax.set_xticks(np.arange(len(keys)))
    ax.set_xticklabels(labs, fontsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_ylim(-0.07, 0.22)
    ax.set_ylabel(s["ylabel"])

    # Bracket annotations.
    ax.annotate(s["annot_loser"],
                xy=(2, RETS["tbond"]),
                xytext=(2, -0.062),
                fontsize=9, color=p["red"], ha="center", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.7))
    ax.annotate(s["annot_winner"],
                xy=(5, RETS["gold"]),
                xytext=(4.4, 0.205),
                fontsize=9, color=p["green"], ha="center", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=0.7))

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8.3, color=p["muted"])

    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
