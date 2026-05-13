"""Week 48, §2.3 — Wealth comparison: Buffer ETF vs DIY replication, 5y.

Two products with identical pre-fee buffered economics. ETF: 0.79%
expense ratio + 0.12% bid-ask drag = 0.91%/yr cost. DIY: 0.20% slippage
on a 4-leg roll once per year, amortised as ~0.05%/yr (most slippage is
realised at roll only). Starting balance $100k, gross buffered return
6.0%/yr (typical 1y outcome on a 15-buffer / 18-cap series in a normal
year), 5-year horizon.

Run:
    uv run python course/image/week48_diy_vs_etf.py
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
BASE = "week48_diy_vs_etf"

START = 100_000.0
GROSS = 0.060          # buffered gross return / yr
ETF_FEE = 0.0091       # 0.79% ER + 0.12% spread
DIY_FEE = 0.0005       # ~5bps/yr amortised slippage
YEARS = 5

years = np.arange(0, YEARS + 1)
etf_path = START * (1.0 + GROSS - ETF_FEE) ** years
diy_path = START * (1.0 + GROSS - DIY_FEE) ** years
gross_path = START * (1.0 + GROSS) ** years


LANG_STRINGS = {
    "en": {
        "title": "Buffer ETF vs DIY 4-leg replication: \\$100k over 5 years",
        "subtitle": "Same gross buffered economics (6.0%/yr). ETF 91 bps/yr fee + spread; DIY ~5 bps/yr slippage.",
        "xlabel": "Year",
        "ylabel": "Wealth (\\$)",
        "etf": "Buffer ETF (BUFR-class, 0.91% / yr)",
        "diy": "DIY 4-leg SPX (~0.05% / yr)",
        "gross": "Gross buffered (no fees, reference)",
        "gap_label": "Convenience tax: \\$%d gap at year 5",
        "callout": "Difference: \\$%d at end-Y5 = %.1f%% of starting capital",
    },
    "hk": {
        "title": "緩衝 ETF vs DIY 四腿複製:5 年 \\$10 萬",
        "subtitle": "相同緩衝毛回報(6.0%/年)。ETF 91 基點/年 費率 + 點差;DIY ~5 基點/年 滑價。",
        "xlabel": "年份",
        "ylabel": "財富 (\\$)",
        "etf": "緩衝 ETF (BUFR 類, 0.91% / 年)",
        "diy": "DIY 4 腿 SPX (~0.05% / 年)",
        "gross": "緩衝毛回報(無費用,參考)",
        "gap_label": "便利稅:第 5 年差距 \\$%d",
        "callout": "差距:第 5 年 \\$%d = 起始資本 %.1f%%",
    },
    "tw": {
        "title": "緩衝 ETF vs DIY 四腳複製:5 年 \\$10 萬",
        "subtitle": "相同緩衝毛報酬(6.0%/年)。ETF 91 基點/年 費用 + 價差;DIY ~5 基點/年 滑價。",
        "xlabel": "年份",
        "ylabel": "財富 (\\$)",
        "etf": "緩衝 ETF (BUFR 類, 0.91% / 年)",
        "diy": "DIY 4 腳 SPX (~0.05% / 年)",
        "gross": "緩衝毛報酬(無費用,參考)",
        "gap_label": "便利稅:第 5 年差距 \\$%d",
        "callout": "差距:第 5 年 \\$%d = 起始資金 %.1f%%",
    },
    "cn": {
        "title": "缓冲 ETF vs DIY 四腿复制:5 年 \\$10 万",
        "subtitle": "相同缓冲毛回报(6.0%/年)。ETF 91 基点/年 费率 + 点差;DIY ~5 基点/年 滑价。",
        "xlabel": "年份",
        "ylabel": "财富 (\\$)",
        "etf": "缓冲 ETF (BUFR 类, 0.91% / 年)",
        "diy": "DIY 4 腿 SPX (~0.05% / 年)",
        "gross": "缓冲毛回报(无费用,参考)",
        "gap_label": "便利税:第 5 年差距 \\$%d",
        "callout": "差距:第 5 年 \\$%d = 起始资本 %.1f%%",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, p)

    width = 0.36
    x = np.arange(YEARS + 1)

    # Reference gross line behind bars.
    ax.plot(x, gross_path, color=p["muted"], linewidth=1.4,
            linestyle=":", marker="o", markersize=4,
            label=s["gross"], zorder=2)

    bars_etf = ax.bar(x - width/2, etf_path, width=width,
                      color=p["red"], alpha=0.85, label=s["etf"], zorder=3)
    bars_diy = ax.bar(x + width/2, diy_path, width=width,
                      color=p["blue"], alpha=0.85, label=s["diy"], zorder=3)

    # Endpoint annotations.
    ax.text(x[-1] - width/2, etf_path[-1] + 1500,
            f"${etf_path[-1]/1000:.1f}k",
            ha="center", va="bottom", fontsize=9,
            color=p["red"], fontweight="bold")
    ax.text(x[-1] + width/2, diy_path[-1] + 1500,
            f"${diy_path[-1]/1000:.1f}k",
            ha="center", va="bottom", fontsize=9,
            color=p["blue"], fontweight="bold")

    # Gap callout box at year 5.
    gap = diy_path[-1] - etf_path[-1]
    pct = gap / START * 100.0
    ax.annotate(
        s["callout"] % (int(round(gap)), pct),
        xy=(x[-1], (etf_path[-1] + diy_path[-1]) / 2),
        xytext=(x[-1] - 2.4, 110_000),
        fontsize=10, color=p["fg"], ha="left",
        bbox=dict(boxstyle="round,pad=0.45", fc=p["bg"],
                  ec=p["accent"], lw=1.2),
        arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.0),
    )

    ax.set_xticks(x)
    ax.set_xticklabels([f"Y{i}" for i in x])
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda v, _: f"${v/1000:.0f}k"))
    ax.set_ylim(95_000, 140_000)
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
