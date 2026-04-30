"""Week 51, §2.6 — Wealth path 1990-Apr 2026: 60/40 vs 50/30/20-CTA vs 100% SP500.

Three lines. SP500 and bond returns are the embedded Damodaran annual
table (TBond10Y for the bond leg). The CTA leg is a *synthetic*
proxy with mu = 6%, sigma = 11%, correlation -0.20 with SP500.
Generated deterministically via a linear conditional model on the
realised SP500 path plus a deterministic LCG-Box-Muller idiosyncratic
component, so the chart is reproducible.

Run:
    uv run python course/image/week51_60_40_with_cta.py
"""

from __future__ import annotations

import math
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
BASE = "week51_60_40_with_cta"

# CTA proxy parameters
MU_CTA = 0.06
SIGMA_CTA = 0.11
RHO = -0.20
SIGMA_SPX = 0.18  # historical realised
MU_SPX = 0.10     # historical realised mean

# Deterministic seed
SEED = 20260429


def _lcg_normals(n: int, seed: int) -> np.ndarray:
    """Deterministic Box-Muller normal samples."""
    a, c, m = 1664525, 1013904223, 2 ** 32
    x = seed & 0xFFFFFFFF
    out = np.zeros(n)
    i = 0
    while i < n:
        x = (a * x + c) % m
        u1 = (x + 1) / (m + 1)
        x = (a * x + c) % m
        u2 = (x + 1) / (m + 1)
        z1 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        z2 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
        out[i] = z1
        if i + 1 < n:
            out[i + 1] = z2
        i += 2
    return out


def _build_returns():
    """Return year array, sp500, bond, cta arrays for 1990 .. 2025-Q1 partial."""
    dam = damodaran_annual_returns()
    years = list(range(1990, 2025))  # 1990..2024 inclusive
    spx = np.array([float(dam.loc[y, "SP500"]) for y in years])
    bnd = np.array([float(dam.loc[y, "TBond10Y"]) for y in years])

    # Synthetic CTA: r_cta = mu + beta*(r_spx - mu_spx) + sqrt(1-rho^2)*sigma_cta*z
    beta = RHO * SIGMA_CTA / SIGMA_SPX
    idio_sigma = math.sqrt(1.0 - RHO * RHO) * SIGMA_CTA
    z = _lcg_normals(len(years), SEED)
    cta = MU_CTA + beta * (spx - MU_SPX) + idio_sigma * z

    # Append 2025 (full year placeholder) and 2026 partial Jan-Apr (4/12).
    # Use realistic-but-illustrative figures.
    spx_2025 = 0.105
    bnd_2025 = 0.040
    z_2025 = _lcg_normals(1, SEED + 1)[0]
    cta_2025 = MU_CTA + beta * (spx_2025 - MU_SPX) + idio_sigma * z_2025

    # 2026 Jan-Apr partial (4 months)
    f = 4.0 / 12.0
    spx_p = 0.045
    bnd_p = 0.018
    cta_p = 0.025

    years.extend([2025, 2026])
    spx = np.concatenate([spx, [spx_2025, spx_p]])
    bnd = np.concatenate([bnd, [bnd_2025, bnd_p]])
    cta = np.concatenate([cta, [cta_2025, cta_p]])

    # Mark partial year via a flag array
    is_partial = np.array([False] * (len(years) - 1) + [True])
    # Rescale partial-year contribution? we keep nominal returns as-is
    # but tag the last point.
    return np.array(years), spx, bnd, cta, is_partial


def _wealth(returns: np.ndarray) -> np.ndarray:
    return np.concatenate([[1.0], np.cumprod(1.0 + returns)])


def _max_drawdown(wealth: np.ndarray) -> float:
    peak = np.maximum.accumulate(wealth)
    return float(np.min(wealth / peak - 1.0))


def _stats(returns: np.ndarray) -> dict:
    n = len(returns)
    cagr = (np.prod(1.0 + returns)) ** (1.0 / n) - 1.0
    vol = float(np.std(returns, ddof=1))
    w = _wealth(returns)
    mdd = _max_drawdown(w)
    return {"cagr": cagr, "vol": vol, "mdd": mdd, "terminal": float(w[-1])}


LANG_STRINGS = {
    "en": {
        "title":    "Wealth path 1990-Apr 2026: adding 20% CTA shrinks the drawdown",
        "subtitle": "100% SP500 vs 60/40 vs 50/30/20 (50% SP500 / 30% bonds / 20% synthetic CTA proxy: mu=6%, sigma=11%, corr=-0.2 with SP500). Bond leg = Damodaran TBond10Y.",
        "xlabel":   "Year",
        "ylabel":   "Growth of $1 (log scale)",
        "spx":      "100% S&P 500",
        "p60":      "60% S&P / 40% bonds",
        "p50":      "50% S&P / 30% bonds / 20% CTA",
        "footer":   "SP500 and bond returns from Damodaran histretSP. CTA proxy generated deterministically (LCG-Box-Muller seed 20260429). 2025 and 2026 partial-year figures are illustrative.",
        "stat_cagr": "CAGR",
        "stat_vol":  "Vol",
        "stat_mdd":  "Max DD",
    },
    "hk": {
        "title":    "1990-2026/4 財富路徑:加入 20% CTA 縮小回撚",
        "subtitle": "100% 標普 vs 60/40 vs 50/30/20(50% 標普 / 30% 債券 / 20% 合成 CTA 代理:mu=6%、sigma=11%、與標普相關 -0.2)。債券來源:Damodaran TBond10Y。",
        "xlabel":   "年份",
        "ylabel":   "1 美元成長(對數刻度)",
        "spx":      "100% 標普 500",
        "p60":      "60% 標普 / 40% 債券",
        "p50":      "50% 標普 / 30% 債券 / 20% CTA",
        "footer":   "標普與債券來源:Damodaran histretSP。CTA 代理由 LCG-Box-Muller 確定性生成(seed 20260429)。2025 與 2026 部分年度為示意。",
        "stat_cagr": "年化",
        "stat_vol":  "波動率",
        "stat_mdd":  "最大回撚",
    },
    "tw": {
        "title":    "1990-2026/4 財富路徑:加入 20% CTA 縮小回檔",
        "subtitle": "100% 標普 vs 60/40 vs 50/30/20(50% 標普 / 30% 債券 / 20% 合成 CTA 代理:mu=6%、sigma=11%、與標普相關 -0.2)。債券來源:Damodaran TBond10Y。",
        "xlabel":   "年份",
        "ylabel":   "1 美元成長(對數刻度)",
        "spx":      "100% 標普 500",
        "p60":      "60% 標普 / 40% 債券",
        "p50":      "50% 標普 / 30% 債券 / 20% CTA",
        "footer":   "標普與債券來源:Damodaran histretSP。CTA 代理由 LCG-Box-Muller 確定性生成(seed 20260429)。2025 與 2026 部分年度為示意。",
        "stat_cagr": "年化",
        "stat_vol":  "波動率",
        "stat_mdd":  "最大回檔",
    },
    "cn": {
        "title":    "1990-2026/4 财富路径:加入 20% CTA 缩小回撤",
        "subtitle": "100% 标普 vs 60/40 vs 50/30/20(50% 标普 / 30% 债券 / 20% 合成 CTA 代理:mu=6%、sigma=11%、与标普相关 -0.2)。债券来源:Damodaran TBond10Y。",
        "xlabel":   "年份",
        "ylabel":   "1 美元成长(对数刻度)",
        "spx":      "100% 标普 500",
        "p60":      "60% 标普 / 40% 债券",
        "p50":      "50% 标普 / 30% 债券 / 20% CTA",
        "footer":   "标普与债券来源:Damodaran histretSP。CTA 代理由 LCG-Box-Muller 确定性生成(seed 20260429)。2025 与 2026 部分年度为示意。",
        "stat_cagr": "年化",
        "stat_vol":  "波动率",
        "stat_mdd":  "最大回撤",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    years, spx, bnd, cta, _ = _build_returns()

    r_spx = spx
    r_60 = 0.60 * spx + 0.40 * bnd
    r_50 = 0.50 * spx + 0.30 * bnd + 0.20 * cta

    w_spx = _wealth(r_spx)
    w_60 = _wealth(r_60)
    w_50 = _wealth(r_50)

    # X-axis: include initial point at year start (years[0]) ... years[-1]+(0 or 1)
    x = np.concatenate([[years[0]], years + 1])
    # Last year is partial 2026 (Jan-Apr) -> use 2026.33 instead of 2027
    x = x.astype(float)
    x[-1] = 2026.33

    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=150)
    style_axes(ax, p)

    ax.plot(x, w_spx, color=p["red"],   linewidth=2.0, label=s["spx"])
    ax.plot(x, w_60,  color=p["blue"],  linewidth=2.0, label=s["p60"])
    ax.plot(x, w_50,  color=p["green"], linewidth=2.6, label=s["p50"])

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold", loc="left")
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10.0, color=p["muted"], style="italic")

    # Endpoint labels.
    def end_label(y_arr, color, name_short):
        ax.text(x[-1] + 0.3, y_arr[-1], f"{name_short}\n${y_arr[-1]:.1f}",
                color=color, fontsize=9.5, fontweight="bold",
                va="center")
    end_label(w_spx, p["red"], "SP500")
    end_label(w_60,  p["blue"], "60/40")
    end_label(w_50,  p["green"], "50/30/20")

    # Stats box (use full-year returns only, exclude partial 2026 to keep CAGR honest).
    full = slice(0, -1)
    st_spx = _stats(r_spx[full])
    st_60 = _stats(r_60[full])
    st_50 = _stats(r_50[full])

    txt = (
        f"               {s['stat_cagr']:>6}   {s['stat_vol']:>6}   {s['stat_mdd']:>7}\n"
        f"100% SP500   {st_spx['cagr']*100:>5.1f}%  {st_spx['vol']*100:>5.1f}%  {st_spx['mdd']*100:>6.1f}%\n"
        f"60/40        {st_60['cagr']*100:>5.1f}%  {st_60['vol']*100:>5.1f}%  {st_60['mdd']*100:>6.1f}%\n"
        f"50/30/20+CTA {st_50['cagr']*100:>5.1f}%  {st_50['vol']*100:>5.1f}%  {st_50['mdd']*100:>6.1f}%"
    )
    ax.text(0.02, 0.98, txt, transform=ax.transAxes,
            fontsize=8.8,
            color=p["fg"], va="top", ha="left",
            bbox=dict(facecolor=p["bg"], edgecolor=p["grid"],
                      boxstyle="round,pad=0.5", linewidth=0.8))

    ax.legend(loc="lower right", frameon=False, fontsize=10)
    ax.set_xlim(years[0] - 0.5, x[-1] + 4.5)
    fig.text(0.5, 0.015, s["footer"], ha="center",
             fontsize=8.0, color=p["muted"])
    fig.tight_layout(rect=[0, 0.03, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
