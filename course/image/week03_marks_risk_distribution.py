"""Week 3, §2.9 — Howard Marks's risk-distribution diagram.

The textbook capital-market line plots a single expected return at each
risk level. Marks's reframing replaces each point with a probability
*distribution* of returns — narrow at low risk, progressively wider and
more left-skewed as risk rises. Higher risk does not promise higher
return; it promises a wider range of possible returns, including a real
left tail of much-worse outcomes.

Run:
    uv run python course/image/week03_marks_risk_distribution.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week03_marks_risk_distribution"

LANG_STRINGS = {
    "en": {
        "title":    "Howard Marks: risk is a distribution, not a point",
        "subtitle": "Higher risk does not promise higher return. It promises a wider range — with a real left tail.",
        "xlabel":   "Risk (volatility)",
        "ylabel":   "Return",
        "cml":      "Textbook capital-market line",
        "labels":   ["T-bills", "IG bonds", "Broad equity", "Small cap / EM", "Single stock", "Venture / spec"],
        "annot":    "Each vertical band is the\nprobability distribution of\nrealised returns at that risk level.",
        "tail_lbl": "Left tail extends\nto large losses",
        "footer":   "Schematic. Distribution shape and width are illustrative, not fitted.",
    },
    "hk": {
        "title":    "霍華・馬克斯:風險是一個分布,不是一個點",
        "subtitle": "更高風險不保證更高回報,只保證回報範圍更闊 — 連帶真實存在的左尾。",
        "xlabel":   "風險(波動率)",
        "ylabel":   "回報",
        "cml":      "教科書資本市場線",
        "labels":   ["國庫券", "投資級債", "大盤股", "小型股/新興市場", "個股", "創投/投機"],
        "annot":    "每條垂直分布代表\n該風險水平下實際\n回報的機率分布。",
        "tail_lbl": "左尾延伸至\n重大虧損",
        "footer":   "示意圖。分布形狀及寬度為示例,非實際擬合。",
    },
    "tw": {
        "title":    "霍華・馬克斯:風險是一個分布,不是一個點",
        "subtitle": "更高風險不保證更高報酬,只保證報酬範圍更寬 — 包含真實存在的左尾。",
        "xlabel":   "風險(波動率)",
        "ylabel":   "報酬",
        "cml":      "教科書資本市場線",
        "labels":   ["國庫券", "投資級債", "大型股", "小型股/新興市場", "個股", "創投/投機"],
        "annot":    "每條垂直分布代表\n該風險水準下實際\n報酬的機率分布。",
        "tail_lbl": "左尾延伸至\n重大虧損",
        "footer":   "示意圖。分布形狀及寬度為示例,非實際擬合。",
    },
    "cn": {
        "title":    "霍华德・马克斯:风险是一个分布,不是一个点",
        "subtitle": "更高风险不保证更高回报,只保证回报范围更宽 — 并伴随真实存在的左尾。",
        "xlabel":   "风险(波动率)",
        "ylabel":   "回报",
        "cml":      "教科书资本市场线",
        "labels":   ["国库券", "投资级债", "大盘股", "小盘股/新兴市场", "个股", "创投/投机"],
        "annot":    "每条垂直分布代表\n该风险水平下实际\n回报的概率分布。",
        "tail_lbl": "左尾延伸至\n重大亏损",
        "footer":   "示意图。分布形状及宽度为示例,非实际拟合。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10, 6.0))
    style_axes(ax, p)

    # Six asset classes along the risk axis.
    xs = np.array([1.0, 5.0, 16.0, 25.0, 35.0, 60.0])  # risk (vol %)
    rs = np.array([3.5, 5.5, 9.0, 11.0, 12.0, 13.5])   # expected return %

    # Capital-market line through (0, rf) and last point.
    rf = 3.5
    line_x = np.linspace(0, 70, 100)
    line_y = rf + (rs[-1] - rf) / xs[-1] * line_x
    ax.plot(line_x, line_y, color=p["muted"], linewidth=1.4,
            linestyle="--", label=s["cml"])

    # For each risk level, draw a vertical skew-normal distribution.
    # Width grows with risk; left skew increases with risk.
    y_grid = np.linspace(-30, 35, 400)
    for i, (x, r) in enumerate(zip(xs, rs)):
        # std grows with risk; skew (negative => left tail) grows with risk
        sd = max(0.6, x * 0.55)
        a = -1.0 * (i / 2.0)  # increasingly left-skewed
        # location chosen so the *mean* sits near r
        # skewnorm mean = loc + scale * delta * sqrt(2/pi); compensate
        delta = a / np.sqrt(1 + a * a)
        loc = r - sd * delta * np.sqrt(2 / np.pi)
        pdf = skewnorm.pdf(y_grid, a, loc=loc, scale=sd)
        # Scale horizontally so all distributions have similar visual width
        width_scale = 4.5
        pdf_scaled = pdf / pdf.max() * width_scale

        # Color: low risk = blue, high risk = red-ish
        t = i / (len(xs) - 1)
        color = (
            0.05 + 0.65 * t,
            0.18 + 0.10 * (1 - t),
            0.55 - 0.45 * t,
        )

        ax.fill_betweenx(y_grid, x - pdf_scaled, x + pdf_scaled,
                         color=color, alpha=0.55, linewidth=0)
        ax.plot([x - pdf_scaled[200], x + pdf_scaled[200]], [y_grid[200]] * 2,
                color=color, linewidth=0)

        # Mean dot
        ax.plot(x, r, "o", color=p["fg"], markersize=4, zorder=5)
        # Asset class label below x-axis
        ax.text(x, -34, s["labels"][i], ha="center", va="top",
                fontsize=9, color=p["fg"])

    # Annotate the rightmost distribution's left tail
    ax.annotate(
        s["tail_lbl"],
        xy=(xs[-1] - 4.0, -22),
        xytext=(xs[-1] - 22, -28),
        fontsize=9, color=p["red"],
        arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.9),
    )

    # General annotation explaining the diagram
    ax.text(2, 30, s["annot"], fontsize=9, color=p["muted"],
            va="top", ha="left")

    ax.set_xlim(-3, 72)
    ax.set_ylim(-35, 35)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0.0, -0.20, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"])
    ax.set_xticks([])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for path in paths:
        print(f"wrote {path}")
