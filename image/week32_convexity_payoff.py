"""Week 32, §2.4 — Bond price vs. yield with duration and convexity overlays.

Plots a 30-year, 5%-coupon bond at a current yield of 5% (par). Three
lines: the true price-yield curve, the linear duration approximation,
and the duration-plus-convexity quadratic. Highlights the asymmetric
upside that positive convexity provides on rate moves.

Run:
    uv run python course/image/week32_convexity_payoff.py
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

OUT_DIR = Path(__file__).parent
BASE = "week32_convexity_payoff"

LANG_STRINGS = {
    "en": {
        "title":    "Price vs. yield: duration is the slope, convexity is the curve",
        "subtitle": "30-year, 5% coupon, current yield 5%. Linear duration undershoots both upside and downside. Convexity nails the curve out to ~+/-200 bps.",
        "xlabel":   "Yield (%)",
        "ylabel":   "Price (% of face)",
        "exact":    "Exact price (true curve)",
        "linear":   "Linear duration only",
        "quad":     "Duration + convexity",
        "now":      "Current\ny = 5.0%, P = 100",
        "ann_up":   "Rally -200 bps:\nexact +33.0\nlinear +30.4\nquad +33.5",
        "ann_dn":   "Sell-off +200 bps:\nexact -27.7\nlinear -30.4\nquad -27.3",
        "asym":     "Asymmetric upside = positive convexity",
    },
    "hk": {
        "title":    "價格 vs. 孳息率:存續期是斜率,凸性是曲度",
        "subtitle": "30 年期、5% 票息、目前孳息率 5%。線性存續期低估上下方;加上凸性,在約 +/-200 基點內幾乎吻合。",
        "xlabel":   "孳息率(%)",
        "ylabel":   "價格(面值 %)",
        "exact":    "實際價格(真實曲線)",
        "linear":   "僅線性存續期",
        "quad":     "存續期 + 凸性",
        "now":      "目前\ny = 5.0%、P = 100",
        "ann_up":   "下跌 200 基點:\n實際 +33.0\n線性 +30.4\n二次 +33.5",
        "ann_dn":   "上升 200 基點:\n實際 -27.7\n線性 -30.4\n二次 -27.3",
        "asym":     "上下不對稱 = 凸性正",
    },
    "tw": {
        "title":    "價格 vs. 殖利率:存續期是斜率,凸性是曲度",
        "subtitle": "30 年期、5% 票息、目前殖利率 5%。線性存續期低估上下方;加上凸性,在約 +/-200 基點內幾乎吻合。",
        "xlabel":   "殖利率(%)",
        "ylabel":   "價格(面值 %)",
        "exact":    "實際價格(真實曲線)",
        "linear":   "僅線性存續期",
        "quad":     "存續期 + 凸性",
        "now":      "目前\ny = 5.0%、P = 100",
        "ann_up":   "下跌 200 基點:\n實際 +33.0\n線性 +30.4\n二次 +33.5",
        "ann_dn":   "上升 200 基點:\n實際 -27.7\n線性 -30.4\n二次 -27.3",
        "asym":     "上下不對稱 = 凸性為正",
    },
    "cn": {
        "title":    "价格 vs. 收益率:久期是斜率,凸性是曲度",
        "subtitle": "30 年期、5% 票息、当前收益率 5%。线性久期低估上下方;加上凸性,在约 +/-200 基点内几乎吻合。",
        "xlabel":   "收益率(%)",
        "ylabel":   "价格(面值 %)",
        "exact":    "实际价格(真实曲线)",
        "linear":   "仅线性久期",
        "quad":     "久期 + 凸性",
        "now":      "当前\ny = 5.0%、P = 100",
        "ann_up":   "下跌 200 基点:\n实际 +33.0\n线性 +30.4\n二次 +33.5",
        "ann_dn":   "上升 200 基点:\n实际 -27.7\n线性 -30.4\n二次 -27.3",
        "asym":     "上下不对称 = 凸性为正",
    },
}


def bond_price(face: float, coupon: float, N: float, y: float, m: int = 2) -> float:
    n = int(round(m * N))
    C = face * coupon / m
    r = y / m
    if abs(r) < 1e-12:
        return C * n + face
    return C * (1 - (1 + r) ** (-n)) / r + face / (1 + r) ** n


def macaulay(face, coupon, N, y, m=2):
    n = int(round(m * N))
    C = face * coupon / m
    r = y / m
    P = bond_price(face, coupon, N, y, m)
    if P <= 0:
        return 0.0
    w = 0.0
    for t in range(1, n + 1):
        cf = C + (face if t == n else 0.0)
        w += (t / m) * cf / (1 + r) ** t
    return w / P


def convexity(face, coupon, N, y, m=2):
    n = int(round(m * N))
    C = face * coupon / m
    r = y / m
    P = bond_price(face, coupon, N, y, m)
    if P <= 0:
        return 0.0
    cx = 0.0
    for t in range(1, n + 1):
        cf = C + (face if t == n else 0.0)
        cx += (t / m) * (t / m + 1.0 / m) * cf / (1 + r) ** (t + 2)
    return cx / P


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.4, 5.8))
    style_axes(ax, p)

    face = 100.0
    coupon = 0.05
    N = 30.0
    y0 = 0.05  # 5%
    P0 = bond_price(face, coupon, N, y0)
    D_mac = macaulay(face, coupon, N, y0)
    D_mod = D_mac / (1 + y0 / 2)
    C = convexity(face, coupon, N, y0)

    # Yield grid 0.5% to 12%
    ys = np.linspace(0.005, 0.12, 240)
    exact = np.array([bond_price(face, coupon, N, yi) for yi in ys])
    dy = ys - y0
    linear = P0 * (1 - D_mod * dy)
    quad = P0 * (1 - D_mod * dy + 0.5 * C * dy ** 2)

    ax.plot(ys * 100, exact, color=p["blue"], linewidth=2.4, label=s["exact"])
    ax.plot(ys * 100, linear, color=p["orange"], linewidth=1.6,
            linestyle="--", label=s["linear"])
    ax.plot(ys * 100, quad, color=p["green"], linewidth=1.8,
            linestyle="-.", label=s["quad"])

    # Current point
    ax.scatter([y0 * 100], [P0], s=70, color=p["accent"],
               zorder=5, edgecolors="white", linewidths=1.5)
    ax.annotate(s["now"], xy=(y0 * 100, P0), xytext=(y0 * 100 + 0.6, P0 + 14),
                fontsize=9, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.0))

    # Annotations for 200 bps moves
    ax.axvline(3.0, color=p["muted"], linewidth=0.7,
               linestyle=":", alpha=0.5)
    ax.axvline(7.0, color=p["muted"], linewidth=0.7,
               linestyle=":", alpha=0.5)
    P_up = bond_price(face, coupon, N, 0.03)
    P_dn = bond_price(face, coupon, N, 0.07)

    ax.annotate(s["ann_up"], xy=(3.0, P_up), xytext=(1.8, 105),
                fontsize=8.5, color=p["green"], ha="left",
                bbox=dict(boxstyle="round,pad=0.3", fc=p["bg"],
                          ec=p["grid"], lw=0.6))
    ax.annotate(s["ann_dn"], xy=(7.0, P_dn), xytext=(8.5, 90),
                fontsize=8.5, color=p["red"], ha="left",
                bbox=dict(boxstyle="round,pad=0.3", fc=p["bg"],
                          ec=p["grid"], lw=0.6))

    # Asymmetry text
    ax.text(0.55, 0.06, s["asym"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], style="italic")

    ax.set_xlim(0, 12)
    ax.set_ylim(35, 165)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.legend(loc="upper right", fontsize=9.5, frameon=False)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
