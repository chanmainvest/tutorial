"""Week 13, §2.6 - Hypothetical equity market-neutral vs 60/40, 1990-2024.

Plots cumulative real wealth of two portfolios from 1990 forward:

  1) A hypothetical L/S equity market-neutral fund. Modelled as a
     deterministic compound path with target 4% annualised real return
     and 5% annualised volatility, with a low-amplitude synthetic
     mean-zero seasonal noise component for visual texture (no random
     state — reproducible, illustrative only).

  2) 60/40, US S&P 500 + 10-year Treasury, real (CPI-deflated), annual
     rebalance. Real Damodaran data.

Use for SOUL #5 / #14 framing: market-neutral buys regime independence
at the cost of compounding; 60/40 carries the equity risk premium.

Run:
    uv run python course/image/week13_market_neutral_vs_60_40.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week13_market_neutral_vs_60_40"

START_YEAR = 1990
END_YEAR = 2024


LANG_STRINGS = {
    "en": {
        "title":      "Hypothetical L/S market-neutral vs 60/40 — cumulative real wealth, 1990-2024",
        "subtitle":   "Market-neutral targets 4% real / 5% vol (deterministic compound path, illustrative). 60/40 = 60% S&P 500 + 40% 10y Treasury, real, annual rebalance.",
        "xlabel":     "Year",
        "ylabel":     "Cumulative real wealth ($1 invested in 1990)",
        "mn_label":    "Market-neutral (4% real / 5% vol target)",
        "sf_label":    "60/40 (annual rebalance)",
        "footer":     "Sharpe (real, ann.):  Market-neutral {mn_sharpe:.2f}   ·   60/40 {sf_sharpe:.2f}        CAGR (real):  Market-neutral {mn_cagr:.1%}   ·   60/40 {sf_cagr:.1%}",
        "annot_2008": "2008 GFC: 60/40 -22%",
        "annot_2022": "2022: 60/40 -24% real",
        "annot_mn":   "Market-neutral barely flinches",
    },
    "hk": {
        "title":      "假設股票市場中性策略 vs 60/40 — 累計實質財富,1990-2024",
        "subtitle":   "市場中性目標 4% 實質回報 / 5% 波動率(確定性複利路徑,僅作示意)。60/40 = 60% 標普 500 + 40% 十年期國債,實質、每年再平衡。",
        "xlabel":     "年份",
        "ylabel":     "累計實質財富(1990 年投入 1 美元)",
        "mn_label":    "市場中性(目標 4% 實質 / 5% 波動率)",
        "sf_label":    "60/40(每年再平衡)",
        "footer":     "夏普比率(實質、年化):市場中性 {mn_sharpe:.2f}   ·   60/40 {sf_sharpe:.2f}        年化複合回報(實質):市場中性 {mn_cagr:.1%}   ·   60/40 {sf_cagr:.1%}",
        "annot_2008": "2008 金融危機:60/40 -22%",
        "annot_2022": "2022 年:60/40 實質 -24%",
        "annot_mn":   "市場中性幾乎不受衝擊",
    },
    "tw": {
        "title":      "假設股票市場中性策略 vs 60/40 — 累計實質財富,1990-2024",
        "subtitle":   "市場中性目標 4% 實質報酬 / 5% 波動率(確定性複利路徑,僅供示意)。60/40 = 60% 標普 500 + 40% 十年期公債,實質、每年再平衡。",
        "xlabel":     "年份",
        "ylabel":     "累計實質財富(1990 年投入 1 美元)",
        "mn_label":    "市場中性(目標 4% 實質 / 5% 波動率)",
        "sf_label":    "60/40(每年再平衡)",
        "footer":     "夏普比率(實質、年化):市場中性 {mn_sharpe:.2f}   ·   60/40 {sf_sharpe:.2f}        年化複合報酬(實質):市場中性 {mn_cagr:.1%}   ·   60/40 {sf_cagr:.1%}",
        "annot_2008": "2008 金融危機:60/40 -22%",
        "annot_2022": "2022 年:60/40 實質 -24%",
        "annot_mn":   "市場中性幾乎不受衝擊",
    },
    "cn": {
        "title":      "假设股票市场中性策略 vs 60/40 — 累计实质财富,1990-2024",
        "subtitle":   "市场中性目标 4% 实质回报 / 5% 波动率(确定性复利路径,仅作示意)。60/40 = 60% 标普 500 + 40% 十年期国债,实质、每年再平衡。",
        "xlabel":     "年份",
        "ylabel":     "累计实质财富(1990 年投入 1 美元)",
        "mn_label":    "市场中性(目标 4% 实质 / 5% 波动率)",
        "sf_label":    "60/40(每年再平衡)",
        "footer":     "夏普比率(实质、年化):市场中性 {mn_sharpe:.2f}   ·   60/40 {sf_sharpe:.2f}        年化复合回报(实质):市场中性 {mn_cagr:.1%}   ·   60/40 {sf_cagr:.1%}",
        "annot_2008": "2008 金融危机:60/40 -22%",
        "annot_2022": "2022 年:60/40 实质 -24%",
        "annot_mn":   "市场中性几乎不受冲击",
    },
}


def _series():
    df = damodaran_annual_returns()
    df = df[(df.index >= START_YEAR) & (df.index <= END_YEAR)].copy()
    sp = df["SP500"]
    bd = df["TBond10Y"]
    cpi = df["CPI"]

    rs = (1 + sp) / (1 + cpi) - 1
    rb = (1 + bd) / (1 + cpi) - 1
    sf = 0.6 * rs + 0.4 * rb  # 60/40 real

    # Hypothetical market-neutral: deterministic compounding around target.
    # Use a low-amplitude periodic noise (no RNG -> reproducible).
    # Target: mu_real = 4%, sigma = 5% annual, mean-zero per-year noise.
    n = len(df)
    target_mu = 0.04
    target_sigma = 0.05
    # Two-component periodic "noise" mean-zero, std ~ target_sigma.
    t = np.arange(n)
    noise = (np.sin(2 * math.pi * t / 7.0) +
             np.cos(2 * math.pi * t / 11.0)) / math.sqrt(2.0)  # std ~ 1
    # Re-centre and rescale so empirical std == target_sigma exactly.
    noise = (noise - noise.mean())
    s_emp = noise.std(ddof=0)
    if s_emp > 0:
        noise = noise * (target_sigma / s_emp)
    mn = pd.Series(target_mu + noise, index=df.index)

    cum_mn = (1 + mn).cumprod()
    cum_sf = (1 + sf).cumprod()
    return df.index.values, cum_mn, cum_sf, mn, sf


def _stats(r):
    mu = r.mean()
    sd = r.std(ddof=0)
    sharpe = mu / sd if sd > 0 else float("nan")
    cagr = float((1 + r).prod()) ** (1.0 / len(r)) - 1.0
    return sharpe, cagr


def build_fig(s):
    p = PALETTE_LIGHT
    apply_cjk_font()

    # Escape '$' so matplotlib does not enter mathtext mode (breaks CJK glyphs).
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    yrs, cum_mn, cum_sf, mn, sf = _series()
    mn_sharpe, mn_cagr = _stats(mn)
    sf_sharpe, sf_cagr = _stats(sf)

    fig, ax = plt.subplots(figsize=(11, 5.8), dpi=160)
    style_axes(ax, p)

    ax.plot(yrs, cum_sf.values, color=p["accent"], linewidth=2.4,
            label=s["sf_label"])
    ax.plot(yrs, cum_mn.values, color=p["blue"], linewidth=2.4,
            label=s["mn_label"])

    # End-value labels
    ax.text(yrs[-1] + 0.4, cum_sf.values[-1], f"\\${cum_sf.values[-1]:.2f}",
            color=p["accent"], fontsize=9.5, va="center", fontweight="bold")
    ax.text(yrs[-1] + 0.4, cum_mn.values[-1], f"\\${cum_mn.values[-1]:.2f}",
            color=p["blue"], fontsize=9.5, va="center", fontweight="bold")

    # Highlight 2008 and 2022 troughs in 60/40
    for yr_target, key in [(2008, "annot_2008"), (2022, "annot_2022")]:
        if yr_target in yrs:
            i = list(yrs).index(yr_target)
            ax.scatter([yr_target], [cum_sf.values[i]], color=p["red"],
                       s=42, zorder=5)
            ax.annotate(s[key], xy=(yr_target, cum_sf.values[i]),
                        xytext=(yr_target - 7, cum_sf.values[i] * 0.55),
                        fontsize=8.8, color=p["red"],
                        arrowprops=dict(arrowstyle="->", color=p["red"],
                                        lw=0.8, alpha=0.7))

    # Annotate market-neutral flatness
    mid_year = yrs[len(yrs) // 2]
    mid_val = cum_mn.values[len(yrs) // 2]
    ax.annotate(s["annot_mn"], xy=(mid_year, mid_val),
                xytext=(mid_year - 4, mid_val + 0.6),
                fontsize=9, color=p["blue"],
                arrowprops=dict(arrowstyle="->", color=p["blue"],
                                lw=0.8, alpha=0.7))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left",
                 pad=24, color=p["fg"])
    ax.text(0, 1.025, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"], style="italic")

    ax.legend(loc="upper left", frameon=False, fontsize=10)

    footer = s["footer"].format(
        mn_sharpe=mn_sharpe, sf_sharpe=sf_sharpe,
        mn_cagr=mn_cagr, sf_cagr=sf_cagr,
    )
    fig.text(0.5, 0.012, footer, ha="center", fontsize=9, color=p["muted"])

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
