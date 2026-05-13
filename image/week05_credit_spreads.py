"""Week 5, §2.6 — BAA corporate vs 10-year Treasury *realised excess return*, 1928-2024.

Annual excess return = BAACorp total return - TBond10Y total return,
from the Damodaran annual dataset. This is *not* a yield credit
spread (a yield difference quoted in bps that widens upward in
crises). It is the year-by-year realised return differential, which
goes sharply *negative* in credit blow-up years (1932, 1974, 2008,
2020) as defaults reprice and Treasuries rally on flight-to-safety.

Run:
    uv run python course/image/week05_credit_spreads.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week05_credit_spreads"

LANG_STRINGS = {
    "en": {
        "title":    "Corporate bond excess return over Treasuries, 1928-2024",
        "subtitle": "BAA corporate total return minus 10Y Treasury total return, by year. Positive in normal years\n(the realised credit premium); sharply negative in credit blow-ups as defaults reprice and Treasuries rally.",
        "xlabel":   "Year",
        "ylabel":   "BAA - 10Y Treasury annual total return (%)",
        "mean":     "Long-run mean: {m:+.2f}% per year",
        "ann_1932": "1932\nDepression",
        "ann_1974": "1974\nstagflation",
        "ann_2008": "2008\nGFC",
        "ann_2020": "2020\nCOVID",
    },
    "hk": {
        "title":    "公司債對國債超額回報,1928-2024",
        "subtitle": "BAA 公司債總回報減十年期國債總回報(逐年)。正常年份為正(實現信貸溢價);\n危機年份違約重新定價、國債上漲,超額回報急轉為負。",
        "xlabel":   "年份",
        "ylabel":   "BAA - 十年期國債(年度總回報,%)",
        "mean":     "長期平均:每年 {m:+.2f}%",
        "ann_1932": "1932\n大蕭條",
        "ann_1974": "1974\n滯脹",
        "ann_2008": "2008\n金融海嘯",
        "ann_2020": "2020\nCOVID",
    },
    "tw": {
        "title":    "公司債對公債超額報酬,1928-2024",
        "subtitle": "BAA 公司債總報酬減十年期公債總報酬(逐年)。正常年份為正(實現信用溢酬);\n危機年份違約重新定價、公債上漲,超額報酬急轉為負。",
        "xlabel":   "年份",
        "ylabel":   "BAA - 十年期公債(年度總報酬,%)",
        "mean":     "長期平均:每年 {m:+.2f}%",
        "ann_1932": "1932\n大蕭條",
        "ann_1974": "1974\n停滯性通膨",
        "ann_2008": "2008\n金融海嘯",
        "ann_2020": "2020\nCOVID",
    },
    "cn": {
        "title":    "公司债对国债超额回报,1928-2024",
        "subtitle": "BAA 公司债总回报减十年期国债总回报(逐年)。正常年份为正(实现信用溢价);\n危机年份违约重新定价、国债上涨,超额回报急转为负。",
        "xlabel":   "年份",
        "ylabel":   "BAA - 十年期国债(年度总回报,%)",
        "mean":     "长期平均:每年 {m:+.2f}%",
        "ann_1932": "1932\n大萧条",
        "ann_1974": "1974\n滞胀",
        "ann_2008": "2008\n金融危机",
        "ann_2020": "2020\nCOVID",
    },
}


def _series():
    df = damodaran_annual_returns()
    spread = (df["BAACorp"] - df["TBond10Y"]) * 100.0  # to percent
    return df.index.astype(int), spread


def build_fig(s):
    yrs, spread = _series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.4, 5.6))
    style_axes(ax, p)

    colors = [p["green"] if v >= 0 else p["red"] for v in spread.values]
    ax.bar(yrs, spread.values, color=colors, width=0.85, alpha=0.85,
           edgecolor="none")

    mean_v = float(spread.mean())
    ax.axhline(0.0, color=p["muted"], linewidth=0.8)
    ax.axhline(mean_v, color=p["accent"], linewidth=1.2, linestyle="--",
               label=s["mean"].format(m=mean_v))

    # Crisis annotations — text_y is the absolute y for the label
    for yr, key, text_y in [(1932, "ann_1932", -8.0),
                             (1974, "ann_1974", -16.0),
                             (2008, "ann_2008", -32.0),
                             (2020, "ann_2020", -22.0)]:
        v = float(spread.loc[yr])
        ax.annotate(s[key],
                    xy=(yr, v), xytext=(yr, text_y),
                    ha="center", fontsize=8.5, color=p["red"], fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(1927, 2025)
    ax.set_ylim(-38, 40)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=34)
    ax.text(0, 1.03, s["subtitle"], transform=ax.transAxes,
            fontsize=9.5, color=p["muted"], va="bottom")
    ax.legend(loc="lower left", frameon=False, fontsize=10)

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
