"""Week 9, §2.1 — Cap-weighted vs equal-weighted S&P 500.

Cumulative wealth, log scale, 1928 onward.  The cap-weighted series is
Damodaran's annual S&P 500 total-return column.  The equal-weighted
series is approximated by adding a constant 1.0%/yr to the cap series:
this is consistent with the long-run premium documented by S&P's own
EWI factsheets and academic studies (Plyakha, Uppal, Vilkov 2014;
Bouchey et al. 2012) over multi-decade horizons.  The constant model is
honest about its limits: equal-weight beats by ~1%/yr on average but
loses for stretches (most recently 2017-2024 mega-cap dominance).

Run:
    uv run python course/image/week09_cap_vs_equal.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week09_cap_vs_equal"

# Long-run equal-weight premium over cap-weight, in annual decimal.
# Documented by S&P EWI factsheet (~1.5% over the longest available
# window) and academic literature (~1-2%); we use a conservative 1.0%.
EW_PREMIUM = 0.010

LANG_STRINGS = {
    "en": {
        "title":    "Cap-weighted vs equal-weighted S&P 500, $1 invested in 1928",
        "subtitle": "Same 500 names, two recipes. Equal-weight tilts toward smaller / cheaper members and earns ~1% per year more on average — at the cost of higher turnover and multi-year stretches of underperformance.",
        "xlabel":   "Year",
        "ylabel":   "Cumulative wealth ($, log scale)",
        "cap":      "Cap-weighted (S&P 500)",
        "equal":    "Equal-weighted (~+1%/yr long-run)",
        "ann":      "Geometric ann. nominal return: cap {c:.1%}  ·  equal-weight {e:.1%}",
        "footer":   "Cap series: Damodaran annual data. Equal-weight: cap series + 1.0%/yr constant — a long-run average; multi-year deviations exist (e.g. 2017-2024 mega-cap regime).",
    },
    "hk": {
        "title":    "市值加權 vs 等權重標普 500——1928 年投入 1 美元",
        "subtitle": "同樣的 500 隻股票,兩套配方。等權重偏向較小/較便宜的成分股,長期平均每年多賺約 1%——代價是更高換手率與多年表現落後。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(美元,對數軸)",
        "cap":      "市值加權(標普 500)",
        "equal":    "等權重(長期約多 1%/年)",
        "ann":      "幾何年化名義回報:市值加權 {c:.1%}  ·  等權重 {e:.1%}",
        "footer":   "市值序列:Damodaran 年度數據。等權重:市值序列 + 1.0%/年常數——長期平均值,多年偏離存在(如 2017-2024 巨型科技股主導期)。",
    },
    "tw": {
        "title":    "市值加權 vs 等權重標普 500——1928 年投入 1 美元",
        "subtitle": "同樣的 500 檔股票,兩套配方。等權重偏向較小/較便宜的成分股,長期平均每年多賺約 1%——代價是更高週轉率與多年表現落後。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(美元,對數軸)",
        "cap":      "市值加權(標普 500)",
        "equal":    "等權重(長期約多 1%/年)",
        "ann":      "幾何年化名義報酬:市值加權 {c:.1%}  ·  等權重 {e:.1%}",
        "footer":   "市值序列:Damodaran 年度資料。等權重:市值序列 + 1.0%/年常數——長期平均值,多年偏離存在(如 2017-2024 巨型科技股主導期)。",
    },
    "cn": {
        "title":    "市值加权 vs 等权重标普 500——1928 年投入 1 美元",
        "subtitle": "同样的 500 只股票,两套配方。等权重偏向较小/较便宜的成份股,长期平均每年多赚约 1%——代价是更高换手率与多年表现落后。",
        "xlabel":   "年份",
        "ylabel":   "累计财富(美元,对数轴)",
        "cap":      "市值加权(标普 500)",
        "equal":    "等权重(长期约多 1%/年)",
        "ann":      "几何年化名义回报:市值加权 {c:.1%}  ·  等权重 {e:.1%}",
        "footer":   "市值序列:Damodaran 年度数据。等权重:市值序列 + 1.0%/年常数——长期平均值,多年偏离存在(如 2017-2024 巨型科技股主导期)。",
    },
}


def _series():
    df = damodaran_annual_returns()
    sp = df["SP500"]
    ew = sp + EW_PREMIUM
    cum_cap = (1 + sp).cumprod()
    cum_ew = (1 + ew).cumprod()
    return df.index, cum_cap, cum_ew


def build_fig(s):
    yrs, cum_cap, cum_ew = _series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 5.8))
    style_axes(ax, p)

    ax.plot(yrs, cum_cap, color=p["blue"], linewidth=2.4, label=s["cap"])
    ax.plot(yrs, cum_ew, color=p["accent"], linewidth=2.4, label=s["equal"])

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    n = len(cum_cap)
    ann_c = cum_cap.iloc[-1] ** (1 / n) - 1
    ann_e = cum_ew.iloc[-1] ** (1 / n) - 1

    last_y = yrs[-1]
    ax.text(last_y + 0.6, cum_cap.iloc[-1], f"${cum_cap.iloc[-1]:,.0f}",
            color=p["blue"], fontsize=9, va="center", fontweight="bold")
    ax.text(last_y + 0.6, cum_ew.iloc[-1], f"${cum_ew.iloc[-1]:,.0f}",
            color=p["accent"], fontsize=9, va="center", fontweight="bold")

    ax.text(0, -0.16, s["ann"].format(c=ann_c, e=ann_e),
            transform=ax.transAxes, fontsize=9.5,
            color=p["fg"], fontweight="bold")
    ax.text(0, -0.22, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"], style="italic")

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
