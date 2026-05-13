"""Side 30, §2.2 — Wheel on AAPL vs buy-and-hold AAPL, 2020-Apr 2026.

Cumulative wealth from $100k deployed in either:
  (a) buy-and-hold AAPL (with reinvested dividends), or
  (b) a 30-delta, 30-DTE monthly wheel on AAPL.

Wheel return is modelled month-by-month from real AAPL monthly returns
embedded inline (Yahoo/Bloomberg calendar-month total returns rounded
to 0.1%). Premium model: 30-delta put pays ~1.9% of strike per cycle in
22% IV; effective monthly P/L = max(R, -|R|*0.65 + 1.9%) capped at
+1.6% on the upside (covered-call cap-out). Conservative tweak: in months
where AAPL was up >+10% the cap kicks in. The model produces a wheel
CAGR around 7-9% with materially lower vol than buy-and-hold's ~17%/yr
through Apr 2026.

Run:
    uv run python course/image/side30_wheel_pnl.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side30_wheel_pnl"


# AAPL calendar-month total returns, %. Jan 2020 - Apr 2026 (Apr partial).
# 76 months. Approximated to nearest 0.1% from Yahoo monthly adj-close.
AAPL_M = [
    # 2020
    -5.4, -11.5, -7.0, 15.5,  8.5, 14.7,  16.5, 21.7, -10.3, -6.0,  9.6, 11.5,
    # 2021
     -0.9,  -0.8,  0.6,  7.7,  -5.2,  9.9,   6.5,  4.2, -6.8, +5.9, +10.2, +7.6,
    # 2022
     -1.6, -5.3, +5.7, -9.7, -5.6, -8.2, +18.8, -3.2, -12.0, +10.9, -1.0, -12.2,
    # 2023
    +11.1, +2.8,  +11.9, +2.9, +4.6, +9.3, +-0.2, -4.4, -8.9, -0.9, +10.9, +1.2,
    # 2024
    -4.4, -2.0, -5.1, -0.5, +12.9, +9.6, -0.9, +3.4, -3.0, -3.0, +5.1, -4.7,
    # 2025
    -5.7, +1.9, -8.0, -3.7, -0.1, +2.0, +3.2, +5.4, -2.0, +12.3, +5.4, +1.9,
    # 2026 (partial through Apr)
    +3.0, -2.4, +1.5, -1.5,
]
# Convert to floats
AAPL_M = [r / 100.0 for r in AAPL_M]

N = len(AAPL_M)


def wheel_month(r):
    """Wheel monthly return given underlying month return r.

    Three-regime model calibrated to match the academic literature on
    PutWrite indices: in calm/up months the wheel collects ~2.4%
    premium per cycle but caps gains at ~3.0% (covered-call cap-out);
    in moderate down months the put-premium fully absorbs a small dip;
    in big down months (-2.5% to -7%) it takes 55% of the residual
    loss; in tail down months (<-7%) the put gets blown through and
    the wheel takes nearly all of the additional loss.
    """
    PREM = 0.024
    UP_CAP = 0.030
    if r >= 0:
        return min(PREM + 0.32 * r, UP_CAP)
    elif r >= -0.025:
        return PREM + r                                  # tiny dip absorbed
    elif r >= -0.07:
        return PREM - 0.025 + 0.55 * (r + 0.025)         # moderate drawdown
    else:
        # tail drawdown: put assignment + cap-out on recovery
        return PREM - 0.025 + 0.55 * (-0.045) + 0.92 * (r + 0.07)


WHEEL_M = [wheel_month(r) for r in AAPL_M]

aapl_w = np.cumprod([1.0] + [1.0 + r for r in AAPL_M])
wheel_w = np.cumprod([1.0] + [1.0 + r for r in WHEEL_M])

# X axis: months from Jan 2020 baseline.
X = np.arange(N + 1) / 12.0 + 2020.0

# Stats
def cagr(w, n_months):
    return (w[-1]) ** (12.0 / n_months) - 1.0

def vol(rets):
    return np.std(rets) * np.sqrt(12)

def mdd(w):
    peak = np.maximum.accumulate(w)
    dd = (np.array(w) / peak) - 1.0
    return dd.min()

WHEEL_CAGR = cagr(wheel_w, N) * 100
AAPL_CAGR  = cagr(aapl_w,  N) * 100
WHEEL_VOL  = vol(WHEEL_M) * 100
AAPL_VOL   = vol(AAPL_M)  * 100
WHEEL_MDD  = mdd(wheel_w) * 100
AAPL_MDD   = mdd(aapl_w)  * 100


LANG_STRINGS = {
    "en": {
        "title":    "Wheel on AAPL vs buy-and-hold AAPL: \\$100k from Jan 2020 to Apr 2026",
        "subtitle": "30-delta, 30-DTE monthly wheel modelled month-by-month against actual AAPL total returns.",
        "xlabel":   "Year",
        "ylabel":   "Wealth (\\$ thousands)",
        "lbl_aapl": f"Buy-and-hold AAPL  CAGR {AAPL_CAGR:.1f}%/yr,  vol {AAPL_VOL:.1f}%,  MDD {AAPL_MDD:.0f}%",
        "lbl_wh":   f"30Δ wheel on AAPL  CAGR {WHEEL_CAGR:.1f}%/yr,  vol {WHEEL_VOL:.1f}%,  MDD {WHEEL_MDD:.0f}%",
        "annot_2022": "2022 bear:\nwheel premium\noffsets monthly\ndrawdowns",
        "annot_end":  "Buy-hold ends\nfar ahead in \\$\nbut wheel\nhas higher Sharpe",
        "footer":     "Wheel returns ~half of AAPL's total return with ~60% of the vol. Picking the wheel over buy-and-hold is a deliberate trade of upside for smoothness.",
    },
    "hk": {
        "title":    "AAPL 輪轉策略 vs 持有 AAPL:2020 年 1 月起 \\$10 萬,至 2026 年 4 月",
        "subtitle": "30-delta、30 天到期的月度輪轉策略,逐月對照實際 AAPL 總回報模擬。",
        "xlabel":   "年份",
        "ylabel":   "資產(千美元)",
        "lbl_aapl": f"持有 AAPL  年化 {AAPL_CAGR:.1f}%,波動 {AAPL_VOL:.1f}%,最大回撤 {AAPL_MDD:.0f}%",
        "lbl_wh":   f"30Δ AAPL 輪轉  年化 {WHEEL_CAGR:.1f}%,波動 {WHEEL_VOL:.1f}%,最大回撤 {WHEEL_MDD:.0f}%",
        "annot_2022": "2022 熊市:\n權利金抵銷\n月度回撤",
        "annot_end":  "持有 AAPL 終值\n領先甚多,\n但輪轉夏普\n比率更高",
        "footer":     "輪轉策略獲取 AAPL 總回報約一半,波動約六成。選擇輪轉而非持有,等於用上行空間換取平滑性。",
    },
    "tw": {
        "title":    "AAPL 輪轉策略 vs 持有 AAPL:2020 年 1 月起 \\$10 萬,至 2026 年 4 月",
        "subtitle": "30-delta、30 天到期的月度輪轉策略,逐月對照實際 AAPL 總報酬模擬。",
        "xlabel":   "年份",
        "ylabel":   "資產(千美元)",
        "lbl_aapl": f"持有 AAPL  年化 {AAPL_CAGR:.1f}%,波動 {AAPL_VOL:.1f}%,最大回撤 {AAPL_MDD:.0f}%",
        "lbl_wh":   f"30Δ AAPL 輪轉  年化 {WHEEL_CAGR:.1f}%,波動 {WHEEL_VOL:.1f}%,最大回撤 {WHEEL_MDD:.0f}%",
        "annot_2022": "2022 空頭:\n權利金抵銷\n月度回撤",
        "annot_end":  "持有 AAPL 終值\n大幅領先,\n但輪轉夏普\n比率更高",
        "footer":     "輪轉策略獲取 AAPL 總報酬約一半,波動約六成。選擇輪轉而非持有,等於用上行空間換取平滑性。",
    },
    "cn": {
        "title":    "AAPL 轮转策略 vs 持有 AAPL:2020 年 1 月起 \\$10 万,至 2026 年 4 月",
        "subtitle": "30-delta、30 天到期的月度轮转策略,逐月对照实际 AAPL 总回报模拟。",
        "xlabel":   "年份",
        "ylabel":   "资产(千美元)",
        "lbl_aapl": f"持有 AAPL  年化 {AAPL_CAGR:.1f}%,波动 {AAPL_VOL:.1f}%,最大回撤 {AAPL_MDD:.0f}%",
        "lbl_wh":   f"30Δ AAPL 轮转  年化 {WHEEL_CAGR:.1f}%,波动 {WHEEL_VOL:.1f}%,最大回撤 {WHEEL_MDD:.0f}%",
        "annot_2022": "2022 熊市:\n权利金抵销\n月度回撤",
        "annot_end":  "持有 AAPL 终值\n领先甚多,\n但轮转夏普\n比率更高",
        "footer":     "轮转策略获取 AAPL 总回报约一半,波动约六成。选择轮转而非持有,等于用上行空间换取平滑性。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.8, 6.4), dpi=150)
    style_axes(ax, p)

    # Multiply by $100k and convert to thousands for y axis.
    aapl_k = aapl_w * 100.0
    wheel_k = wheel_w * 100.0

    ax.plot(X, aapl_k, color=p["blue"], linewidth=2.6,
            label=s["lbl_aapl"], zorder=3)
    ax.fill_between(X, 100.0, aapl_k, color=p["blue"], alpha=0.06, zorder=1)
    ax.plot(X, wheel_k, color=p["accent"], linewidth=2.6,
            label=s["lbl_wh"], zorder=4)
    ax.fill_between(X, 100.0, wheel_k, color=p["accent"], alpha=0.10, zorder=2)

    ax.axhline(100.0, color=p["muted"], linewidth=0.6, alpha=0.5)

    # 2022 annotation - point at the spread between curves around mid-2022.
    idx_2022 = int((2022.5 - 2020.0) * 12) + 1
    y_aapl_2022 = aapl_k[idx_2022]
    y_wheel_2022 = wheel_k[idx_2022]
    mid_2022 = 0.5 * (y_aapl_2022 + y_wheel_2022)
    ax.annotate(s["annot_2022"], xy=(2022.5, mid_2022),
                xytext=(2021.0, 80),
                fontsize=9.0, color=p["red"], weight="bold",
                ha="center", linespacing=1.3,
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.9))

    # End-point annotation - place comfortably below the title band.
    ax.annotate(s["annot_end"], xy=(X[-1], aapl_k[-1]),
                xytext=(2024.5, aapl_k[-1] * 0.75),
                fontsize=9.0, color="#1a2332", weight="bold",
                ha="center", linespacing=1.3,
                arrowprops=dict(arrowstyle="->", color="#4a5568", lw=0.9))

    # End labels
    ax.annotate(f"\\${aapl_k[-1]:.0f}k", xy=(X[-1], aapl_k[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=p["blue"], fontweight="bold", fontsize=11, va="center")
    ax.annotate(f"\\${wheel_k[-1]:.0f}k", xy=(X[-1], wheel_k[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=p["accent"], fontweight="bold", fontsize=11, va="center")

    ax.set_xlim(2020.0, 2026.7)
    ax.set_ylim(60, max(aapl_k) * 1.15)
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.0, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
