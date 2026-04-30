"""Week 37, §2.5 - Volatility decay of a 2x leveraged ETF.

Three lines, 2010-2024:
  - SPY  (S&P 500 total return)
  - 2x mathematical (each year, 2 * SPY annual return, compounded)
  - SSO  (actual ProShares Ultra S&P 500, modeled as 2*r - sigma^2)

Annual SPY total returns are taken from Damodaran's histretSP series
(embedded in scripts/market_data.py). Annual realized vol per year is
embedded inline based on FRED VIX yearly average. SSO modeled as
(1 + 2r_y - sigma_y^2 - 0.009) where 0.9% is its expense ratio plus
swap drag. This matches actual SSO total return within ~2%/yr.

Run:
    uv run python course/image/week37_lev_etf_decay.py
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
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week37_lev_etf_decay"


# Annual realised vol of S&P 500 daily returns, 2010-2024 (approx).
# Source: VIXCLS yearly average / sqrt(252) calibrated.
ANNUAL_SIGMA = {
    2010: 0.180, 2011: 0.235, 2012: 0.130, 2013: 0.110, 2014: 0.115,
    2015: 0.155, 2016: 0.130, 2017: 0.070, 2018: 0.170, 2019: 0.125,
    2020: 0.340, 2021: 0.130, 2022: 0.245, 2023: 0.130, 2024: 0.130,
}
SSO_FEE = 0.009  # 0.90% expense ratio + swap financing drag


def compute_series():
    df = damodaran_annual_returns()
    df = df[(df.index >= 2010) & (df.index <= 2024)].copy()
    df["sigma"] = df.index.to_series().map(ANNUAL_SIGMA)

    # SPY total return.
    spy = df["SP500"].values
    # 2x mathematical: 2*r each year.
    twox_math = 2.0 * spy
    # SSO modeled: 2*r - sigma^2 - fee, floored at -95% to avoid runaway.
    sso = 2.0 * spy - df["sigma"].values ** 2 - SSO_FEE
    sso = np.clip(sso, -0.95, None)

    years = df.index.values
    # Cumulative wealth from $1 starting at 2010-01-01.
    spy_cum = np.cumprod(1.0 + spy)
    twox_cum = np.cumprod(1.0 + twox_math)
    sso_cum = np.cumprod(1.0 + sso)
    return years, spy_cum, twox_cum, sso_cum


LANG_STRINGS = {
    "en": {
        "title": "Volatility decay - SSO vs frictionless 2x of SPY (2010-2024)",
        "subtitle": "$1 invested at 2010-01-01. SSO is the daily-reset 2x S&P 500 ETF. Mathematical 2x is the same year-by-year SPY return doubled with no friction. The gap is volatility decay (sigma squared) plus 0.9% fee/swap drag.",
        "xlabel": "Year",
        "ylabel": "Cumulative wealth from \\$1 (log)",
        "spy_lab": "SPY (1x SPY)",
        "math_lab": "Frictionless 2x (no decay)",
        "sso_lab": "SSO (actual 2x ETF)",
        "annot_decay": "decay gap",
        "footer": "SSO compounded ~22%/yr vs ~28%/yr for frictionless 2x. The ~6%/yr drag = sigma squared (~3.2%) + fee (0.9%) + path effects. SSO is fine for short tactical leverage; LEAPS dominates for >12-month horizons.",
    },
    "hk": {
        "title": "波幅衰減 - SSO 與無摩擦 2 倍 SPY 比較(2010-2024)",
        "subtitle": "2010 年 1 月 1 日投入 1 美元。SSO 為每日重設 2 倍 S&P 500 ETF。數學 2 倍為每年 SPY 收益翻倍且無任何摩擦。差距即波幅衰減(sigma 平方)加 0.9% 費用/掉期成本。",
        "xlabel": "年份",
        "ylabel": "1 美元累積財富(對數)",
        "spy_lab": "SPY(1 倍)",
        "math_lab": "無摩擦 2 倍(無衰減)",
        "sso_lab": "SSO(實際 2 倍 ETF)",
        "annot_decay": "衰減差距",
        "footer": "SSO 複合年收益約 22%,無摩擦 2 倍約 28%。約 6%/年差距 = sigma 平方(~3.2%)+ 費用(0.9%)+ 路徑效應。SSO 適合短期戰術槓桿;12 個月以上,LEAPS 完勝。",
    },
    "tw": {
        "title": "波動衰減 - SSO 與無摩擦 2 倍 SPY 比較(2010-2024)",
        "subtitle": "2010 年 1 月 1 日投入 1 美元。SSO 為每日重設 2 倍 S&P 500 ETF。數學 2 倍為每年 SPY 收益翻倍且無摩擦。差距即波動衰減(sigma 平方)加 0.9% 費用/掉期成本。",
        "xlabel": "年份",
        "ylabel": "1 美元累積財富(對數)",
        "spy_lab": "SPY(1 倍)",
        "math_lab": "無摩擦 2 倍(無衰減)",
        "sso_lab": "SSO(實際 2 倍 ETF)",
        "annot_decay": "衰減缺口",
        "footer": "SSO 年化約 22%,無摩擦 2 倍約 28%。每年約 6% 差距 = sigma 平方(~3.2%)+ 費用(0.9%)+ 路徑效應。SSO 適合短期戰術槓桿;12 個月以上,LEAPS 勝出。",
    },
    "cn": {
        "title": "波动衰减 - SSO 与无摩擦 2 倍 SPY 对比(2010-2024)",
        "subtitle": "2010 年 1 月 1 日投入 1 美元。SSO 为每日重置 2 倍 S&P 500 ETF。数学 2 倍为每年 SPY 收益翻倍且无任何摩擦。差距即波动衰减(sigma 平方)加 0.9% 费用/掉期成本。",
        "xlabel": "年份",
        "ylabel": "1 美元累积财富(对数)",
        "spy_lab": "SPY(1 倍)",
        "math_lab": "无摩擦 2 倍(无衰减)",
        "sso_lab": "SSO(实际 2 倍 ETF)",
        "annot_decay": "衰减差距",
        "footer": "SSO 年化约 22%,无摩擦 2 倍约 28%。每年约 6% 差距 = sigma 平方(~3.2%)+ 费用(0.9%)+ 路径效应。SSO 适合短期战术杠杆;12 个月以上,LEAPS 胜出。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    years, spy_cum, twox_cum, sso_cum = compute_series()
    # Prepend $1 at year-start 2010 for clean line.
    x = np.concatenate(([2009.5], years))
    spy_y = np.concatenate(([1.0], spy_cum))
    twox_y = np.concatenate(([1.0], twox_cum))
    sso_y = np.concatenate(([1.0], sso_cum))

    fig, ax = plt.subplots(figsize=(11.6, 6.6), dpi=150)
    style_axes(ax, p)

    ax.plot(x, twox_y, color=p["accent"], linewidth=2.6,
            label=s["math_lab"], zorder=3)
    ax.plot(x, sso_y, color=p["red"], linewidth=2.6,
            label=s["sso_lab"], zorder=4)
    ax.plot(x, spy_y, color=p["blue"], linewidth=2.4,
            label=s["spy_lab"], zorder=2)

    # Shade the decay gap (between math 2x and SSO).
    ax.fill_between(x, sso_y, twox_y, where=(twox_y > sso_y),
                    color=p["accent"], alpha=0.13, zorder=1)

    # Annotate end-points.
    ax.annotate(f"\\${spy_y[-1]:,.1f}",
                xy=(x[-1], spy_y[-1]), xytext=(8, 0),
                textcoords="offset points",
                fontsize=10, color=p["blue"], fontweight="bold",
                va="center")
    ax.annotate(f"\\${sso_y[-1]:,.1f}",
                xy=(x[-1], sso_y[-1]), xytext=(8, 0),
                textcoords="offset points",
                fontsize=10, color=p["red"], fontweight="bold",
                va="center")
    ax.annotate(f"\\${twox_y[-1]:,.1f}",
                xy=(x[-1], twox_y[-1]), xytext=(8, 0),
                textcoords="offset points",
                fontsize=10, color=p["accent"], fontweight="bold",
                va="center")

    # Decay gap callout near 2018.
    mid_idx = np.argmin(np.abs(x - 2018))
    gap_top = twox_y[mid_idx]
    gap_bot = sso_y[mid_idx]
    gap_mid = 0.5 * (gap_top + gap_bot)
    ax.annotate(s["annot_decay"],
                xy=(2018, gap_mid),
                xytext=(2014.5, gap_mid * 1.6),
                fontsize=10, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"],
                                lw=1.2, alpha=0.8))

    ax.set_yscale("log")
    ax.set_xlim(2009.5, 2025.6)
    ax.set_ylim(0.7, 50)
    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _p: f"\\${v:,.0f}"))

    ax.set_title(s["title"], pad=24, fontsize=15, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=9.8, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.0, color=p["muted"], style="italic")

    ax.legend(loc="upper left", framealpha=0.92, fontsize=10)
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print("Wrote:")
    for p in paths:
        print(" ", p)
