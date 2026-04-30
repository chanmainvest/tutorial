"""Week 3, §2.2 — Histogram of S&P 500 annual total returns 1928–2024.

Uses the embedded Damodaran annual dataset from scripts.market_data.
Overlays a normal distribution with the same mean and standard
deviation to highlight the empirical fat tails.

Run:
    uv run python course/image/week03_return_distribution.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week03_return_distribution"

LANG_STRINGS = {
    "en": {
        "title":    "S&P 500 annual total returns, 1928–2024",
        "subtitle": "Empirical histogram with same-mean normal curve overlaid. Markets have fat tails.",
        "xlabel":   "Annual total return",
        "ylabel":   "Number of years",
        "norm_lbl": "Normal distribution (same μ and σ)",
        "hist_lbl": "Actual annual returns (Damodaran)",
        "stats":    "Mean: {mu:.1%}  ·  Std dev: {sd:.1%}  ·  Worst: {lo:.1%}  ·  Best: {hi:.1%}",
        "annot1":   "1931:\n{v1:.0%}",
        "annot2":   "2008:\n{v2:.0%}",
        "annot3":   "1933:\n+{v3:.0%}",
    },
    "hk": {
        "title":    "標普 500 年度總回報,1928–2024",
        "subtitle": "實際分布直方圖,疊加同均值同標準差的常態曲線。市場有肥尾。",
        "xlabel":   "年度總回報",
        "ylabel":   "年數",
        "norm_lbl": "常態分布(同 μ 同 σ)",
        "hist_lbl": "實際年度回報(Damodaran)",
        "stats":    "均值:{mu:.1%}  ·  標準差:{sd:.1%}  ·  最差:{lo:.1%}  ·  最佳:{hi:.1%}",
        "annot1":   "1931 年:\n{v1:.0%}",
        "annot2":   "2008 年:\n{v2:.0%}",
        "annot3":   "1933 年:\n+{v3:.0%}",
    },
    "tw": {
        "title":    "標普 500 年度總報酬,1928–2024",
        "subtitle": "實際分布直方圖,疊加同均值同標準差的常態曲線。市場有肥尾。",
        "xlabel":   "年度總報酬",
        "ylabel":   "年數",
        "norm_lbl": "常態分布(同 μ 同 σ)",
        "hist_lbl": "實際年度報酬(Damodaran)",
        "stats":    "均值:{mu:.1%}  ·  標準差:{sd:.1%}  ·  最差:{lo:.1%}  ·  最佳:{hi:.1%}",
        "annot1":   "1931 年:\n{v1:.0%}",
        "annot2":   "2008 年:\n{v2:.0%}",
        "annot3":   "1933 年:\n+{v3:.0%}",
    },
    "cn": {
        "title":    "标普 500 年度总回报,1928–2024",
        "subtitle": "实际分布直方图,叠加同均值同标准差的正态曲线。市场有肥尾。",
        "xlabel":   "年度总回报",
        "ylabel":   "年数",
        "norm_lbl": "正态分布(同 μ 同 σ)",
        "hist_lbl": "实际年度回报(Damodaran)",
        "stats":    "均值:{mu:.1%}  ·  标准差:{sd:.1%}  ·  最差:{lo:.1%}  ·  最佳:{hi:.1%}",
        "annot1":   "1931 年:\n{v1:.0%}",
        "annot2":   "2008 年:\n{v2:.0%}",
        "annot3":   "1933 年:\n+{v3:.0%}",
    },
}


def _data():
    df = damodaran_annual_returns()
    sp = df["SP500"].dropna()
    return sp


def build_fig(s):
    sp = _data()
    mu = float(sp.mean())
    sd = float(sp.std(ddof=1))
    lo = float(sp.min())
    hi = float(sp.max())
    v_1931 = float(sp.loc[1931]) if 1931 in sp.index else lo
    v_2008 = float(sp.loc[2008]) if 2008 in sp.index else lo
    v_1933 = float(sp.loc[1933]) if 1933 in sp.index else hi

    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10, 5.6))
    style_axes(ax, p)

    bins = np.arange(-0.50, 0.60, 0.05)
    n, _, patches = ax.hist(
        sp.values, bins=bins, color=p["blue"], alpha=0.65,
        edgecolor=p["bg"], linewidth=0.8, label=s["hist_lbl"],
    )
    # Color tail bins red
    for patch, left in zip(patches, bins[:-1]):
        if left <= -0.30 or left >= 0.40:
            patch.set_facecolor(p["red"])
            patch.set_alpha(0.7)

    # Normal curve overlay (scaled to histogram area)
    x = np.linspace(bins[0], bins[-1], 400)
    pdf = norm.pdf(x, mu, sd)
    bin_width = bins[1] - bins[0]
    ax.plot(x, pdf * bin_width * len(sp), color=p["accent"], linewidth=2.2,
            label=s["norm_lbl"])

    ax.axvline(mu, color=p["fg"], linewidth=1.0, linestyle=":", alpha=0.7)
    ax.text(mu, ax.get_ylim()[1] * 0.95, f"μ = {mu:.1%}",
            ha="center", va="top", fontsize=9, color=p["fg"])

    # Annotate extremes
    ax.annotate(s["annot1"].format(v1=v_1931), xy=(v_1931, 1), xytext=(-0.43, 7),
                fontsize=9, color=p["red"],
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.8))
    ax.annotate(s["annot2"].format(v2=v_2008), xy=(v_2008, 1), xytext=(-0.20, 9),
                fontsize=9, color=p["red"],
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.8))
    ax.annotate(s["annot3"].format(v3=v_1933), xy=(v_1933, 1), xytext=(0.43, 7),
                fontsize=9, color=p["green"],
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=0.8))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0.0, -0.18,
            s["stats"].format(mu=mu, sd=sd, lo=lo, hi=hi),
            transform=ax.transAxes, fontsize=9, color=p["muted"])
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
