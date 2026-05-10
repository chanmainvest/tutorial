"""Week 5, end-of-§4 — static fallback chart for the bond-pricer interactive.

Plots the price-yield curve for a 4% semi-annual-coupon bond at three
maturities (2y, 10y, 30y), so the markdown is self-contained when the
interactive demo can't render. Demonstrates duration (slope at par) and
convexity (curvature) visually.

Run:
    uv run python course/image/week05_price_yield.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week05_price_yield"

LANG_STRINGS = {
    "en": {
        "title":    "Bond price vs market yield, 4% semi-annual coupon",
        "subtitle": "All three cross at par (100) when yield = coupon. Longer maturity = steeper slope (more duration) and more bow (more convexity).",
        "xlabel":   "Market yield (%)",
        "ylabel":   "Price (% of face)",
        "label_2":  "2-year",
        "label_10": "10-year",
        "label_30": "30-year",
        "par_note": "Par (100) at yield = 4%",
    },
    "hk": {
        "title":    "債券價格對市場孳息率,4% 半年付息",
        "subtitle": "孳息率等於票面息率時三條線都在面值(100)交叉。期限越長,斜率越陡(存續期越大),弧度越大(凸性越強)。",
        "xlabel":   "市場孳息率(%)",
        "ylabel":   "價格(面值百分比)",
        "label_2":  "2 年期",
        "label_10": "10 年期",
        "label_30": "30 年期",
        "par_note": "孳息率 4% 時為面值(100)",
    },
    "tw": {
        "title":    "債券價格對市場殖利率,4% 半年付息",
        "subtitle": "殖利率等於票面利率時三條線都在面值(100)交叉。期限越長,斜率越陡(存續期越大),弧度越大(凸性越強)。",
        "xlabel":   "市場殖利率(%)",
        "ylabel":   "價格(面值百分比)",
        "label_2":  "2 年期",
        "label_10": "10 年期",
        "label_30": "30 年期",
        "par_note": "殖利率 4% 時為面值(100)",
    },
    "cn": {
        "title":    "债券价格对市场收益率,4% 半年付息",
        "subtitle": "收益率等于票面利率时三条线都在面值(100)交叉。期限越长,斜率越陡(久期越大),弧度越大(凸性越强)。",
        "xlabel":   "市场收益率(%)",
        "ylabel":   "价格(面值百分比)",
        "label_2":  "2 年期",
        "label_10": "10 年期",
        "label_30": "30 年期",
        "par_note": "收益率 4% 时为面值(100)",
    },
}


def bond_price(face: float, coupon_rate: float, n_years: float,
               y: np.ndarray, m: int = 2) -> np.ndarray:
    """Closed-form vanilla bond price as a percent of face."""
    c = face * coupon_rate / m
    n = int(round(n_years * m))
    yp = y / m
    # Avoid divide-by-zero at y = 0
    pv_coupons = np.where(
        yp == 0,
        c * n,
        c * (1.0 - (1.0 + yp) ** (-n)) / yp,
    )
    pv_face = face / (1.0 + yp) ** n
    return (pv_coupons + pv_face) / face * 100.0  # as percent of face


def build_fig(s):
    p = PALETTE_LIGHT
    yields = np.linspace(0.001, 0.15, 400)

    p2  = bond_price(1000.0, 0.04,  2.0, yields)
    p10 = bond_price(1000.0, 0.04, 10.0, yields)
    p30 = bond_price(1000.0, 0.04, 30.0, yields)

    fig, ax = plt.subplots(figsize=(10.4, 5.6))
    style_axes(ax, p)

    ax.plot(yields * 100, p2,  color=p["green"],  linewidth=2.2, label=s["label_2"])
    ax.plot(yields * 100, p10, color=p["blue"],   linewidth=2.2, label=s["label_10"])
    ax.plot(yields * 100, p30, color=p["red"],    linewidth=2.4, label=s["label_30"])

    # Mark par at y = 4%
    ax.axhline(100.0, color=p["muted"], linewidth=0.7, linestyle=":")
    ax.axvline(4.0,   color=p["muted"], linewidth=0.7, linestyle=":")
    ax.scatter([4.0], [100.0], color=p["accent"], s=44, zorder=5)
    ax.annotate(s["par_note"],
                xy=(4.0, 100.0), xytext=(5.5, 145.0),
                fontsize=9.5, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.0))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(0, 15)
    ax.set_ylim(20, 230)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.legend(loc="upper right", frameon=False, fontsize=10)

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
