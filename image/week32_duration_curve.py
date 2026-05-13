"""Week 32, §2.1 — Macaulay duration as a function of maturity.

Three curves on one panel: zero-coupon (D=N exactly), 5% coupon, and
10% coupon, all priced at par (yield equals coupon for the coupon bonds,
yield = 5% for the zero baseline). Shows that coupon bonds always
sit below the y=x zero-coupon line because intermediate coupons pull
the cash-flow-weighted average forward.

Run:
    uv run python course/image/week32_duration_curve.py
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
BASE = "week32_duration_curve"

LANG_STRINGS = {
    "en": {
        "title":    "Macaulay duration vs. maturity",
        "subtitle": "Zero-coupon bonds sit on the 45-degree line (D=N). Coupon bonds always sag below — coupons pull the weighted average forward.",
        "xlabel":   "Years to maturity (N)",
        "ylabel":   "Macaulay duration (years)",
        "zero":     "Zero-coupon (D = N)",
        "c5":       "5% coupon, semi-annual",
        "c10":      "10% coupon, semi-annual",
        "ann_30y":  "30-yr 5% coupon\nD = {v:.1f} yrs",
        "ann_30z":  "30-yr zero\nD = 30.0 yrs",
        "ref":      "y = N (45-degree)",
    },
    "hk": {
        "title":    "麥考利存續期 vs. 到期年限",
        "subtitle": "零息債券位於 45 度線上(D=N)。附息債券永遠在其下——票息把加權平均期拉前。",
        "xlabel":   "到期年限(N)",
        "ylabel":   "麥考利存續期(年)",
        "zero":     "零息(D = N)",
        "c5":       "5% 票息,每半年付息",
        "c10":      "10% 票息,每半年付息",
        "ann_30y":  "30 年 5% 票息\nD = {v:.1f} 年",
        "ann_30z":  "30 年零息\nD = 30.0 年",
        "ref":      "y = N(45 度線)",
    },
    "tw": {
        "title":    "麥考利存續期 vs. 到期年限",
        "subtitle": "零息債券位於 45 度線上(D=N)。附息債券永遠在其下——票息把加權平均期拉前。",
        "xlabel":   "到期年限(N)",
        "ylabel":   "麥考利存續期(年)",
        "zero":     "零息(D = N)",
        "c5":       "5% 票息,每半年付息",
        "c10":      "10% 票息,每半年付息",
        "ann_30y":  "30 年 5% 票息\nD = {v:.1f} 年",
        "ann_30z":  "30 年零息\nD = 30.0 年",
        "ref":      "y = N(45 度線)",
    },
    "cn": {
        "title":    "麦考利久期 vs. 到期年限",
        "subtitle": "零息债券位于 45 度线上(D=N)。附息债券永远在其下——票息把加权平均期拉前。",
        "xlabel":   "到期年限(N)",
        "ylabel":   "麦考利久期(年)",
        "zero":     "零息(D = N)",
        "c5":       "5% 票息,每半年付息",
        "c10":      "10% 票息,每半年付息",
        "ann_30y":  "30 年 5% 票息\nD = {v:.1f} 年",
        "ann_30z":  "30 年零息\nD = 30.0 年",
        "ref":      "y = N(45 度线)",
    },
}


def macaulay(face: float, coupon: float, N: float, y: float, m: int = 2) -> float:
    """Macaulay duration in years for a coupon bond with semi-annual periods."""
    if N <= 0:
        return 0.0
    n = int(round(m * N))
    if n <= 0:
        return 0.0
    C = face * coupon / m
    r = y / m
    # price
    if abs(r) < 1e-12:
        P = C * n + face
    else:
        P = C * (1 - (1 + r) ** (-n)) / r + face / (1 + r) ** n
    if P <= 0:
        return 0.0
    weighted = 0.0
    for t in range(1, n + 1):
        cf = C + (face if t == n else 0.0)
        weighted += (t / m) * cf / (1 + r) ** t
    return weighted / P


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.4, 5.8))
    style_axes(ax, p)

    # Maturity grid
    Ns = np.linspace(0.5, 30, 60)

    # For coupon bonds, price at par (yield = coupon).
    # Zero-coupon line is just D = N regardless of yield.
    d_zero = Ns.copy()
    d_5 = np.array([macaulay(1000.0, 0.05, n, 0.05, m=2) for n in Ns])
    d_10 = np.array([macaulay(1000.0, 0.10, n, 0.10, m=2) for n in Ns])

    ax.plot(Ns, d_zero, color=p["accent"], linewidth=2.2, label=s["zero"])
    ax.plot(Ns, d_5, color=p["blue"], linewidth=2.0, label=s["c5"])
    ax.plot(Ns, d_10, color=p["red"], linewidth=2.0, label=s["c10"])

    # Light reference line at 45-degree
    ax.plot([0, 30], [0, 30], color=p["muted"], linewidth=0.8,
            linestyle=":", alpha=0.6)

    # Annotate 30-year markers
    d30_5 = float(d_5[-1])
    ax.annotate(s["ann_30y"].format(v=d30_5),
                xy=(30, d30_5), xytext=(22, d30_5 - 5.2),
                ha="center", fontsize=9, color=p["blue"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["blue"], lw=1.0))
    ax.annotate(s["ann_30z"],
                xy=(30, 30), xytext=(20, 28),
                ha="center", fontsize=9, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.0))

    ax.set_xlim(0, 31)
    ax.set_ylim(0, 32)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.legend(loc="upper left", fontsize=9.5, frameon=False)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
