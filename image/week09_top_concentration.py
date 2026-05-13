"""Week 9, §2.2 — Top-10 concentration in the S&P 500, April 2026.

Bar chart of the ten largest S&P 500 weights plus an "other 490"
catch-all. Weights are approximate published values rounded to the
nearest 0.1%. The chart annotates the cumulative top-10 share.

Run:
    uv run python course/image/week09_top_concentration.py
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

OUT_DIR = Path(__file__).parent
BASE = "week09_top_concentration"

# Approximate S&P 500 weights, April 2026.  Sourced from published index
# fact sheets; rounded.  The "Other 490" bucket fills to 100%.
TICKERS = [
    ("AAPL",       6.8),
    ("MSFT",       6.4),
    ("NVDA",       5.6),
    ("AMZN",       3.7),
    ("META",       2.7),
    ("GOOGL",      2.0),
    ("GOOG",       1.7),
    ("BRK.B",      1.7),
    ("TSLA",       1.5),
    ("AVGO",       1.5),
]
TOP10_SUM = sum(w for _, w in TICKERS)        # ~33.6
OTHER = 100.0 - TOP10_SUM

LANG_STRINGS = {
    "en": {
        "title":    "S&P 500 — top 10 stocks ~33% of the index, April 2026",
        "subtitle": "Cap-weighting lets winners compound. The cost is concentration: the headline '500 stocks' index behaves like a Mag-7 plus 493 satellites.",
        "ylabel":   "Weight in S&P 500 (%)",
        "other":    "Other 490",
        "annot":    "Top 10 sum: {t:.1f}%   ·   Other 490: {o:.1f}%",
        "footer":   "Approximate published weights, rounded to 0.1%.",
    },
    "hk": {
        "title":    "標普 500——前 10 大成分股約佔 33%,2026 年 4 月",
        "subtitle": "市值加權讓贏家自動複利,代價是集中度。「500 隻股票」實際上像是 Mag-7 加 493 隻衛星股。",
        "ylabel":   "佔標普 500 權重(%)",
        "other":    "其餘 490 隻",
        "annot":    "前 10 合計:{t:.1f}%   ·   其餘 490:{o:.1f}%",
        "footer":   "權重為公開資料,四捨五入至 0.1%。",
    },
    "tw": {
        "title":    "標普 500——前 10 大成分股約佔 33%,2026 年 4 月",
        "subtitle": "市值加權讓贏家自動複利,代價是集中度。「500 檔股票」實際上像 Mag-7 加 493 檔衛星股。",
        "ylabel":   "佔標普 500 權重(%)",
        "other":    "其餘 490 檔",
        "annot":    "前 10 合計:{t:.1f}%   ·   其餘 490:{o:.1f}%",
        "footer":   "權重為公開資料,四捨五入至 0.1%。",
    },
    "cn": {
        "title":    "标普 500——前 10 大成份股约占 33%,2026 年 4 月",
        "subtitle": "市值加权让赢家自动复利,代价是集中度。「500 只股票」实际上像是 Mag-7 加 493 只卫星股。",
        "ylabel":   "占标普 500 权重(%)",
        "other":    "其余 490 只",
        "annot":    "前 10 合计:{t:.1f}%   ·   其余 490:{o:.1f}%",
        "footer":   "权重为公开数据,四舍五入至 0.1%。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    labels = [t for t, _ in TICKERS] + [s["other"]]
    weights = [w for _, w in TICKERS] + [OTHER]
    # Mag-7 highlight = blue, BRK/AVGO = teal, other 490 = muted grey.
    mag7 = {"AAPL", "MSFT", "NVDA", "AMZN", "META", "GOOGL", "GOOG", "TSLA"}
    colors = []
    for t in labels:
        if t == s["other"]:
            colors.append(p["grey"])
        elif t in mag7:
            colors.append(p["blue"])
        else:
            colors.append(p["accent"])

    fig, ax = plt.subplots(figsize=(11, 5.8))
    style_axes(ax, p)

    bars = ax.bar(labels, weights, color=colors, edgecolor=p["bg"], linewidth=0.8)
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Value labels above each bar.
    for bar, w in zip(bars, weights):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.7,
                f"{w:.1f}%",
                ha="center", va="bottom",
                fontsize=9, color=p["fg"], fontweight="bold")

    ax.set_ylim(0, max(weights) * 1.15)
    ax.tick_params(axis="x", labelsize=9.5)

    ax.text(0.5, -0.18,
            s["annot"].format(t=TOP10_SUM, o=OTHER),
            transform=ax.transAxes, ha="center",
            fontsize=10, color=p["fg"], fontweight="bold")
    ax.text(0.5, -0.24, s["footer"], transform=ax.transAxes,
            ha="center", fontsize=8.5, color=p["muted"], style="italic")

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
