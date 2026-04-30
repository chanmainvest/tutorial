"""Side 17, sec 2.2 -- schematic FOMC dot plot recreation.

A stylised version of the FOMC Summary of Economic Projections dot plot
showing 16 anonymous participant projections per year for 2026, 2027,
2028, and the longer run. Dots cluster around 3.625% / 3.0% / 2.75% /
2.875%. Median highlighted as a horizontal mark.

Run:
    uv run python course/image/side17_dot_plot.py
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
    save_localized_png,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side17_dot_plot"


# 16 dots per column. Hand-arranged on a 25-bp grid (0.25%) to look like
# a real FOMC dot plot. Each list is sorted ascending; medians chosen so
# they sit on a 1/8-step inside the cluster.
DOTS = {
    "2026": [3.125, 3.375, 3.375, 3.625, 3.625, 3.625, 3.625, 3.625,
             3.625, 3.625, 3.875, 3.875, 3.875, 4.125, 4.125, 4.375],
    "2027": [2.375, 2.625, 2.625, 2.875, 2.875, 3.000, 3.000, 3.125,
             3.125, 3.125, 3.375, 3.375, 3.375, 3.625, 3.875, 4.125],
    "2028": [2.125, 2.375, 2.375, 2.625, 2.625, 2.625, 2.875, 2.875,
             2.875, 2.875, 3.000, 3.125, 3.125, 3.375, 3.625, 4.125],
    "Long-run": [2.375, 2.500, 2.500, 2.625, 2.625, 2.750, 2.750, 2.875,
                 2.875, 2.875, 3.000, 3.000, 3.125, 3.125, 3.250, 3.500],
}
COL_X = {"2026": 1, "2027": 2, "2028": 3, "Long-run": 4}


LANG_STRINGS = {
    "en": {
        "title":    "FOMC dot plot - schematic, March 2026 SEP-style",
        "subtitle": "16 anonymous participant projections of appropriate Fed funds rate at year-end. Median highlighted in gold; central tendency shaded.",
        "xlabel":   "Projection horizon",
        "ylabel":   "Fed funds rate (% year-end)",
        "x_lab":    {"2026": "2026", "2027": "2027",
                     "2028": "2028", "Long-run": "Longer run"},
        "median":   "median",
        "ct":       "central tendency (drop top 3 / bottom 3)",
        "neutral":  "Implied neutral cluster: 2.75-3.00%",
        "footer":   "Schematic recreation, not the official chart. Dots are stylised. Source design: Federal Reserve Board SEP, March meeting style.",
    },
    "hk": {
        "title":    "FOMC 點陣圖 - 示意圖,2026 年 3 月 SEP 風格",
        "subtitle": "16 位參與者匿名給出年末聯邦基金利率合適水平。中位數金色標示;中心區段陰影顯示。",
        "xlabel":   "預測年期",
        "ylabel":   "聯邦基金利率(年末 %)",
        "x_lab":    {"2026": "2026", "2027": "2027",
                     "2028": "2028", "Long-run": "長期"},
        "median":   "中位數",
        "ct":       "中心區段(剔除最高 3 個/最低 3 個)",
        "neutral":  "隱含中性利率區:2.75-3.00%",
        "footer":   "示意重繪,非官方圖。圓點為示意。設計來源:聯儲局 SEP 三月會議格式。",
    },
    "tw": {
        "title":    "FOMC 點陣圖 - 示意圖,2026 年 3 月 SEP 樣式",
        "subtitle": "16 位委員匿名提交年末聯邦資金利率合適水平。中位數金色標示;中心區段陰影顯示。",
        "xlabel":   "預測年期",
        "ylabel":   "聯邦資金利率(年末 %)",
        "x_lab":    {"2026": "2026", "2027": "2027",
                     "2028": "2028", "Long-run": "長期"},
        "median":   "中位數",
        "ct":       "中心區段(去除最高 3 個/最低 3 個)",
        "neutral":  "隱含中性利率區:2.75-3.00%",
        "footer":   "示意重繪,非官方圖。圓點為示意。設計來源:聯準會 SEP 三月會議樣式。",
    },
    "cn": {
        "title":    "FOMC 点阵图 - 示意图,2026 年 3 月 SEP 风格",
        "subtitle": "16 位参与者匿名给出年末联邦基金利率合适水平。中位数金色标示;中心区间阴影显示。",
        "xlabel":   "预测期",
        "ylabel":   "联邦基金利率(年末 %)",
        "x_lab":    {"2026": "2026", "2027": "2027",
                     "2028": "2028", "Long-run": "长期"},
        "median":   "中位数",
        "ct":       "中心区间(剔除最高 3 个/最低 3 个)",
        "neutral":  "隐含中性利率区:2.75-3.00%",
        "footer":   "示意重绘,非官方图。圆点为示意。设计来源:美联储 SEP 三月会议格式。",
    },
}


def _stagger(values):
    """Spread duplicate y-values horizontally a tiny bit so dots don't overlap."""
    counts: dict[float, int] = {}
    out: list[tuple[float, float]] = []
    for v in values:
        n = counts.get(v, 0)
        counts[v] = n + 1
        out.append((v, n))
    # final pass to centre stagger around 0
    final = []
    for v, n in out:
        total = counts[v]
        # spread offsets symmetric around 0 with step 0.06
        idx = n - (total - 1) / 2.0
        final.append((v, idx * 0.07))
    return final


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.4, 6.6), dpi=150)
    style_axes(ax, p)

    cols = ["2026", "2027", "2028", "Long-run"]
    x_centres = [COL_X[c] for c in cols]

    for col in cols:
        x = COL_X[col]
        vals = DOTS[col]
        median = float(np.median(vals))
        # central tendency = drop top-3 / bottom-3
        sorted_vals = sorted(vals)
        ct_lo = sorted_vals[3]
        ct_hi = sorted_vals[-4]
        # shaded central tendency
        ax.add_patch(plt.Rectangle((x - 0.32, ct_lo), 0.64, ct_hi - ct_lo,
                                   facecolor=p["blue"], alpha=0.10,
                                   edgecolor="none", zorder=1))
        # dots
        for v, dx in _stagger(vals):
            ax.plot(x + dx, v, "o", color=p["blue"],
                    markerfacecolor=p["blue"], markeredgecolor=p["bg"],
                    markeredgewidth=0.8, markersize=10.5, alpha=0.85,
                    zorder=3)
        # median bar
        ax.plot([x - 0.36, x + 0.36], [median, median],
                color=p["accent"], linewidth=3.0, solid_capstyle="round",
                zorder=4)
        ax.text(x + 0.40, median, f"{median:.2f}%",
                color=p["accent"], fontsize=9, fontweight="bold",
                va="center")

    # Neutral band 2.75-3.00%
    ax.axhspan(2.75, 3.00, color=p["green"], alpha=0.10)
    ax.text(0.55, 2.875, s["neutral"],
            color=p["green"], fontsize=8.6, fontweight="bold",
            ha="left", va="center")

    # Vertical column separators (faint)
    for x in x_centres[:-1]:
        ax.axvline(x + 0.5, color=p["grid"], linewidth=0.6,
                   linestyle=":", alpha=0.6)

    # legend dummy items
    ax.plot([], [], "o", color=p["blue"], markersize=10,
            markerfacecolor=p["blue"], markeredgecolor=p["bg"],
            label=f"participant ({s['median']} = " + s['median'] + ")")
    # build legend manually with two entries
    h_dot = plt.Line2D([], [], marker="o", linestyle="None",
                       color=p["blue"], markerfacecolor=p["blue"],
                       markeredgecolor=p["bg"], markersize=10,
                       label="participant")
    h_med = plt.Line2D([], [], color=p["accent"], linewidth=3.0,
                       label=s["median"])
    h_ct = plt.Rectangle((0, 0), 1, 1, facecolor=p["blue"],
                         alpha=0.18, label=s["ct"])
    ax.legend(handles=[h_dot, h_med, h_ct],
              loc="upper right", fontsize=9, frameon=False)

    ax.set_xticks(x_centres)
    ax.set_xticklabels([s["x_lab"][c] for c in cols])
    ax.set_xlim(0.45, 4.55)
    ax.set_ylim(1.6, 4.8)
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.12, s["footer"], transform=ax.transAxes,
            fontsize=8.4, color=p["muted"])

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = []
    for lang in ("en", "hk", "tw", "cn"):
        fig = build_fig(LANG_STRINGS[lang])
        paths.append(save_localized_png(fig, BASE, lang, OUT_DIR, dpi=160))
        plt.close(fig)
    for pth in paths:
        print(f"wrote {pth}")
