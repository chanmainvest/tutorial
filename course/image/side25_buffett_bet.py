"""Side 25, sec 2.3 -- Buffett-Protege bet 2008-2017 wealth path.

$1 invested Jan 1 2008 in:
  - Vanguard S&P 500 Admiral (VFIAX) -- Buffett's pick
  - Protege Partners' basket of 5 funds-of-hedge-funds (avg) -- Protege's pick

Annual returns embedded inline from the public Berkshire 2017 annual
letter ("The Bet" appendix). Final cumulative: SPX +125.8% / FoFs +36.3%.

Run:
    uv run python course/image/side25_buffett_bet.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side25_buffett_bet"

# From Berkshire 2017 annual letter, Appendix on "The Bet" (p.11-13).
# FoFs annual = average across 5 FoFs picked by Protege Partners.
DATA = [
#   year   SPX     FoFs
    (2008, -0.371, -0.238),
    (2009,  0.265,  0.157),
    (2010,  0.151,  0.085),
    (2011,  0.021,  -0.039),
    (2012,  0.160,  0.067),
    (2013,  0.323,  0.117),
    (2014,  0.137,  0.052),
    (2015,  0.014,  0.018),
    (2016,  0.120,  0.022),
    (2017,  0.218,  0.063),
]


LANG_STRINGS = {
    "en": {
        "title":    "The Buffett-Protege Bet, 2008-2017: $1 -> ?",
        "subtitle": "S&P 500 vs basket of 5 funds-of-hedge-funds. SPX returned 3.5x what the FoFs returned.",
        "xlabel":   "Year",
        "ylabel":   "Wealth from $1 invested Jan 2008",
        "lbl_spx":  "Vanguard S&P 500 (Buffett's pick)",
        "lbl_fof":  "Protege FoF basket (Protege's pick)",
        "ann_2008": "2008: SPX -37%, FoFs -24%",
        "ann_end_spx": "$2.26 (+125.8%, 8.5%/yr)",
        "ann_end_fof": "$1.36 (+36.3%, 3.2%/yr)",
        "ann_gap":  "Fee stack: 2/20 underlying + 1/10 FoF = ~5%/yr alpha needed to break even.\nThe FoFs delivered roughly that gross. The fee stack ate it.",
        "footer":   "Source: Berkshire Hathaway 2017 Annual Letter, Appendix on 'The Bet'. FoFs picked by Protege Partners. SP500 = Vanguard 500 Admiral (VFIAX).",
    },
    "hk": {
        "title":    "巴菲特-Protege 賭局,2008-2017:$1 變多少?",
        "subtitle": "標普 500 對戰 5 隻對沖基金中基金的組合。標普回報是 FoF 的 3.5 倍。",
        "xlabel":   "年份",
        "ylabel":   "2008 年 1 月起投入 1 美元的累積財富",
        "lbl_spx":  "Vanguard 標普 500(巴菲特一方)",
        "lbl_fof":  "Protege FoF 組合(Protege 一方)",
        "ann_2008": "2008 年:標普 -37%、FoF -24%",
        "ann_end_spx": "$2.26(+125.8%,年化 8.5%)",
        "ann_end_fof": "$1.36(+36.3%,年化 3.2%)",
        "ann_gap":  "費用堆疊:底層 2/20 + FoF 1/10,需要約 5%/年 alpha 才剛好打平。\nFoF 大概有這個毛 alpha。費用堆疊把它全吃光了。",
        "footer":   "資料來源:Berkshire Hathaway 2017 年報「The Bet」附錄。FoF 由 Protege Partners 選擇。標普 500 = VFIAX。",
    },
    "tw": {
        "title":    "巴菲特-Protege 賭局,2008-2017:$1 變多少?",
        "subtitle": "標普 500 對戰 5 檔避險基金中基金的組合。標普報酬是 FoF 的 3.5 倍。",
        "xlabel":   "年份",
        "ylabel":   "2008 年 1 月起投入 1 美元的累積財富",
        "lbl_spx":  "Vanguard 標普 500(巴菲特一方)",
        "lbl_fof":  "Protege FoF 組合(Protege 一方)",
        "ann_2008": "2008 年:標普 -37%、FoF -24%",
        "ann_end_spx": "$2.26(+125.8%,年化 8.5%)",
        "ann_end_fof": "$1.36(+36.3%,年化 3.2%)",
        "ann_gap":  "費用堆疊:底層 2/20 + FoF 1/10,需要約 5%/年 alpha 才剛好打平。\nFoF 大概有這個毛 alpha。費用堆疊把它全吃光了。",
        "footer":   "資料來源:Berkshire Hathaway 2017 年報「The Bet」附錄。FoF 由 Protege Partners 選擇。標普 500 = VFIAX。",
    },
    "cn": {
        "title":    "巴菲特-Protege 赌局,2008-2017:$1 变多少?",
        "subtitle": "标普 500 对战 5 只对冲基金中基金的组合。标普回报是 FoF 的 3.5 倍。",
        "xlabel":   "年份",
        "ylabel":   "2008 年 1 月起投入 1 美元的累计财富",
        "lbl_spx":  "Vanguard 标普 500(巴菲特一方)",
        "lbl_fof":  "Protege FoF 组合(Protege 一方)",
        "ann_2008": "2008 年:标普 -37%、FoF -24%",
        "ann_end_spx": "$2.26(+125.8%,年化 8.5%)",
        "ann_end_fof": "$1.36(+36.3%,年化 3.2%)",
        "ann_gap":  "费用堆叠:底层 2/20 + FoF 1/10,需要约 5%/年 alpha 才刚好打平。\nFoF 大概有这个毛 alpha。费用堆叠把它全吃光了。",
        "footer":   "资料来源:Berkshire Hathaway 2017 年报「The Bet」附录。FoF 由 Protege Partners 选择。标普 500 = VFIAX。",
    },
}


def _build_paths():
    spx = [1.0]
    fof = [1.0]
    years = [2007]
    for y, s, f in DATA:
        spx.append(spx[-1] * (1 + s))
        fof.append(fof[-1] * (1 + f))
        years.append(y)
    return np.array(years), np.array(spx), np.array(fof)


def build_fig(s):
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    x, spx, fof = _build_paths()

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax, p)

    # Lines
    ax.plot(x, spx, color=p["accent"], linewidth=2.8,
            marker="o", markersize=5, label=s["lbl_spx"])
    ax.plot(x, fof, color=p["red"], linewidth=2.4,
            marker="s", markersize=4.5, label=s["lbl_fof"])

    # Shade gap between curves after 2008
    ax.fill_between(x, spx, fof, where=(spx >= fof),
                    color=p["accent"], alpha=0.10, interpolate=True)

    # Endpoint annotations
    ax.annotate(s["ann_end_spx"],
                xy=(x[-1], spx[-1]),
                xytext=(x[-1] - 3.0, spx[-1] + 0.25),
                fontsize=10, fontweight="bold", color=p["accent"],
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=0.9))
    ax.annotate(s["ann_end_fof"],
                xy=(x[-1], fof[-1]),
                xytext=(x[-1] - 3.0, fof[-1] - 0.42),
                fontsize=10, fontweight="bold", color=p["red"],
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.9))

    # 2008 callout
    ax.annotate(s["ann_2008"],
                xy=(2008, spx[1]),
                xytext=(2008.4, 0.15),
                fontsize=9, color=p["muted"],
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.7))

    # Mid-chart fee callout
    ax.text(2010.5, 1.85, s["ann_gap"],
            fontsize=9, color=p["fg"], style="italic",
            bbox=dict(boxstyle="round,pad=0.5",
                      facecolor=p["bg"], edgecolor=p["grid"], linewidth=0.8))

    ax.axhline(1.0, color=p["muted"], linestyle="--", linewidth=0.8, alpha=0.6)

    ax.set_xlim(2007.4, 2018.0)
    ax.set_ylim(0.5, 2.7)
    ax.set_xticks(list(range(2008, 2018)))
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=p["muted"], style="italic")

    ax.legend(loc="upper left", frameon=True, fontsize=10,
              facecolor=p["bg"], edgecolor=p["grid"])
    ax.grid(True, color=p["grid"], linewidth=0.6, alpha=0.7)

    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
