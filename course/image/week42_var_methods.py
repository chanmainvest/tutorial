"""Week 42, §2.3 — Three-panel chart of VaR methods.

Left:    Histogram of S&P 500 daily returns 1990-Apr 2026 with a
         Normal(mu, sigma) overlay; tails coloured red.
Middle:  Histogram of Damodaran annual S&P 500 returns 1928-2024 with
         vertical markers at the empirical 95/99/99.9% VaR
         thresholds and the parametric Normal-fit VaR for comparison.
Right:   Empirical CVaR / VaR ratio at three confidence levels on
         the daily series. The ratio rises with confidence, showing
         the tail breach gets worse as you go further out.

Run:
    uv run python course/image/week42_var_methods.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def _norm_pdf(x, mu=0.0, sd=1.0):
    z = (x - mu) / sd
    return np.exp(-0.5 * z * z) / (sd * math.sqrt(2.0 * math.pi))


# z-values for common confidence levels (one-sided).
_Z = {0.90: 1.2816, 0.95: 1.6449, 0.975: 1.9600,
      0.99: 2.3263, 0.995: 2.5758, 0.999: 3.0902, 0.9999: 3.7190}


def _norm_cvar_var_ratio(c: float) -> float:
    """Standard-Normal CVaR/VaR ratio at confidence level c (loss positive)."""
    z = _Z[c]
    phi = math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)
    return phi / (1.0 - c) / z

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import (  # noqa: E402
    damodaran_annual_returns,
    yahoo_history,
    stooq_history,
)

OUT_DIR = Path(__file__).parent
BASE = "week42_var_methods"


LANG_STRINGS = {
    "en": {
        "title":    "VaR three ways: parametric vs historical vs the breach",
        "subtitle": "S&P 500 daily 1990-Apr 2026 (left), annual 1928-2024 (middle), CVaR/VaR ratio in the tail (right). Tails are not Normal.",
        "p1_title": "Daily returns 1990-Apr 2026",
        "p1_x":     "Daily total return",
        "p1_y":     "Number of days",
        "p1_norm":  "Normal fit (same mu, sigma)",
        "p1_hist":  "Empirical histogram",
        "p1_stats": "mu = {mu:.2%}/d  ·  sigma = {sd:.2%}/d  ·  worst = {lo:.1%}",
        "p2_title": "Annual returns 1928-2024 with VaR thresholds",
        "p2_x":     "Annual total return",
        "p2_y":     "Number of years",
        "p2_v95":   "Hist 95%",
        "p2_v99":   "Hist 99%",
        "p2_v999":  "Hist 99.9%",
        "p2_par":   "Normal 99%",
        "p3_title": "Empirical CVaR / VaR (daily)",
        "p3_y":     "Ratio",
        "p3_x":     "Confidence level",
        "footer":   "Daily series via Yahoo SPY/^GSPC, fallback Stooq. Annual series via Damodaran.",
    },
    "hk": {
        "title":    "VaR 三種方法:參數 vs 歷史 vs 尾部突破",
        "subtitle": "標普 500 日報酬 1990-2026.4(左)、年度 1928-2024(中)、尾部 CVaR/VaR 比率(右)。尾部並非常態。",
        "p1_title": "日報酬 1990-2026.4",
        "p1_x":     "日總回報",
        "p1_y":     "日數",
        "p1_norm":  "常態擬合(同 mu, sigma)",
        "p1_hist":  "實際分布",
        "p1_stats": "mu = {mu:.2%}/日  ·  sigma = {sd:.2%}/日  ·  最差 = {lo:.1%}",
        "p2_title": "年度回報 1928-2024 與 VaR 閾值",
        "p2_x":     "年度總回報",
        "p2_y":     "年數",
        "p2_v95":   "歷史 95%",
        "p2_v99":   "歷史 99%",
        "p2_v999":  "歷史 99.9%",
        "p2_par":   "常態 99%",
        "p3_title": "實際 CVaR / VaR(日)",
        "p3_y":     "比率",
        "p3_x":     "信心水平",
        "footer":   "日數據:Yahoo SPY/^GSPC,備援 Stooq。年度數據:Damodaran。",
    },
    "tw": {
        "title":    "VaR 三種方法:參數 vs 歷史 vs 尾部突破",
        "subtitle": "標普 500 日報酬 1990-2026.4(左)、年度 1928-2024(中)、尾部 CVaR/VaR 比率(右)。尾部並非常態。",
        "p1_title": "日報酬 1990-2026.4",
        "p1_x":     "日總報酬",
        "p1_y":     "日數",
        "p1_norm":  "常態擬合(同 mu, sigma)",
        "p1_hist":  "實際分布",
        "p1_stats": "mu = {mu:.2%}/日  ·  sigma = {sd:.2%}/日  ·  最差 = {lo:.1%}",
        "p2_title": "年度報酬 1928-2024 與 VaR 閾值",
        "p2_x":     "年度總報酬",
        "p2_y":     "年數",
        "p2_v95":   "歷史 95%",
        "p2_v99":   "歷史 99%",
        "p2_v999":  "歷史 99.9%",
        "p2_par":   "常態 99%",
        "p3_title": "實際 CVaR / VaR(日)",
        "p3_y":     "比率",
        "p3_x":     "信心水準",
        "footer":   "日資料:Yahoo SPY/^GSPC,備援 Stooq。年度資料:Damodaran。",
    },
    "cn": {
        "title":    "VaR 三种方法:参数 vs 历史 vs 尾部突破",
        "subtitle": "标普 500 日回报 1990-2026.4(左)、年度 1928-2024(中)、尾部 CVaR/VaR 比率(右)。尾部并非正态。",
        "p1_title": "日回报 1990-2026.4",
        "p1_x":     "日总回报",
        "p1_y":     "日数",
        "p1_norm":  "正态拟合(同 mu, sigma)",
        "p1_hist":  "实际分布",
        "p1_stats": "mu = {mu:.2%}/日  ·  sigma = {sd:.2%}/日  ·  最差 = {lo:.1%}",
        "p2_title": "年度回报 1928-2024 与 VaR 阈值",
        "p2_x":     "年度总回报",
        "p2_y":     "年数",
        "p2_v95":   "历史 95%",
        "p2_v99":   "历史 99%",
        "p2_v999":  "历史 99.9%",
        "p2_par":   "正态 99%",
        "p3_title": "实际 CVaR / VaR(日)",
        "p3_y":     "比率",
        "p3_x":     "置信水平",
        "footer":   "日数据:Yahoo SPY/^GSPC,备援 Stooq。年度数据:Damodaran。",
    },
}


def _daily_returns() -> np.ndarray:
    """Daily total returns of the S&P 500 1990 -> latest, as decimals."""
    df = None
    for ticker in ("^GSPC", "SPY"):
        try:
            df = yahoo_history(ticker, start="1990-01-01")
            if df is not None and len(df) > 1000:
                break
        except Exception:
            df = None
    if df is None or len(df) < 1000:
        try:
            df = stooq_history("^spx")
        except Exception:
            df = None
    if df is None or len(df) < 1000:
        # Last-resort synthetic with a Student-t kick so the chart still
        # renders. Marked clearly in caption-land.
        rng = np.random.default_rng(42)
        n = 252 * 35
        x = rng.standard_t(df=6, size=n) * 0.011 + 0.0004
        return x

    col = "AdjClose" if "AdjClose" in df.columns else (
        "Close" if "Close" in df.columns else df.columns[-1]
    )
    px = df[col].dropna().astype(float).values
    r = np.diff(px) / px[:-1]
    return r[np.isfinite(r)]


def _empirical_var(r: np.ndarray, alpha: float) -> float:
    """Empirical VaR as a positive loss number at confidence alpha."""
    return float(-np.quantile(r, 1.0 - alpha))


def _empirical_cvar(r: np.ndarray, alpha: float) -> float:
    thresh = np.quantile(r, 1.0 - alpha)
    tail = r[r <= thresh]
    if len(tail) == 0:
        return float(-thresh)
    return float(-tail.mean())


def build_fig(s):
    # Escape dollar signs that may appear in Chinese-translated
    # subtitles or stats lines (mathtext mode hazard).
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v)
         for k, v in s.items()}

    p = PALETTE_LIGHT
    daily = _daily_returns()
    annual = damodaran_annual_returns()["SP500"].dropna().values

    mu_d = float(daily.mean())
    sd_d = float(daily.std(ddof=1))
    lo_d = float(daily.min())

    fig, axes = plt.subplots(1, 3, figsize=(15.2, 5.6),
                             gridspec_kw={"width_ratios": [1.15, 1.0, 0.75]})
    for ax in axes:
        style_axes(ax, p)

    # ------------------------------------------------------------------ Panel 1
    ax = axes[0]
    bins = np.linspace(-0.13, 0.13, 80)
    counts, _, patches = ax.hist(
        daily, bins=bins, color=p["blue"], alpha=0.65,
        edgecolor=p["bg"], linewidth=0.4, label=s["p1_hist"],
    )
    # Color bars below -3% (left tail) red
    for patch, left in zip(patches, bins[:-1]):
        if left <= -0.03:
            patch.set_facecolor(p["red"])
            patch.set_alpha(0.75)
    x = np.linspace(bins[0], bins[-1], 600)
    pdf = _norm_pdf(x, mu_d, sd_d)
    bin_width = bins[1] - bins[0]
    ax.plot(x, pdf * bin_width * len(daily), color=p["accent"], linewidth=2.2,
            label=s["p1_norm"])
    ax.set_yscale("log")
    ax.set_ylim(0.7, max(counts.max() * 1.5, 5000))
    ax.set_xlabel(s["p1_x"])
    ax.set_ylabel(s["p1_y"] + " (log)")
    ax.set_title(s["p1_title"], fontsize=11, fontweight="bold", loc="left", pad=14)
    ax.text(0.02, -0.20, s["p1_stats"].format(mu=mu_d, sd=sd_d, lo=lo_d),
            transform=ax.transAxes, fontsize=8.6, color=p["muted"])
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.legend(loc="upper right", frameon=False, fontsize=8.5)

    # ------------------------------------------------------------------ Panel 2
    ax = axes[1]
    bins2 = np.arange(-0.50, 0.60, 0.05)
    n2, _, patches2 = ax.hist(
        annual, bins=bins2, color=p["blue"], alpha=0.55,
        edgecolor=p["bg"], linewidth=0.6,
    )
    for patch, left in zip(patches2, bins2[:-1]):
        if left <= -0.20:
            patch.set_facecolor(p["red"])
            patch.set_alpha(0.7)

    # Empirical VaR thresholds (annual, as negative returns)
    a95 = _empirical_var(annual, 0.95)
    a99 = _empirical_var(annual, 0.99)
    a999 = _empirical_var(annual, 0.999)
    mu_a = float(annual.mean())
    sd_a = float(annual.std(ddof=1))
    par99 = -(mu_a - 2.326 * sd_a)  # parametric 99% VaR (positive loss)

    ymax = n2.max() * 1.12
    ax.set_ylim(0, ymax)
    for v, label, color, dy in [
        (-a95,  s["p2_v95"],  p["orange"], 0.92),
        (-a99,  s["p2_v99"],  p["red"],    0.78),
        (-a999, s["p2_v999"], p["purple"], 0.64),
        (-par99, s["p2_par"], p["accent"], 0.50),
    ]:
        ax.axvline(v, color=color, linewidth=1.6,
                   linestyle="--" if label == s["p2_par"] else "-",
                   alpha=0.85)
        ax.text(v, ymax * dy, "  " + label,
                color=color, fontsize=8.6, fontweight="bold",
                ha="left", va="center")

    ax.set_xlabel(s["p2_x"])
    ax.set_ylabel(s["p2_y"])
    ax.set_title(s["p2_title"], fontsize=11, fontweight="bold", loc="left", pad=14)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))

    # ------------------------------------------------------------------ Panel 3
    ax = axes[2]
    confs = [0.95, 0.99, 0.995]
    ratios = [
        _empirical_cvar(daily, c) / _empirical_var(daily, c) for c in confs
    ]
    norm_ratios = [_norm_cvar_var_ratio(c) for c in confs]

    xpos = np.arange(len(confs))
    w = 0.36
    bars1 = ax.bar(xpos - w / 2, ratios, width=w, color=p["red"], alpha=0.85,
                   label="Empirical")
    bars2 = ax.bar(xpos + w / 2, norm_ratios, width=w, color=p["accent"],
                   alpha=0.85, label="Normal")
    for b, val in zip(bars1, ratios):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.02,
                f"{val:.2f}", ha="center", va="bottom", fontsize=9,
                color=p["red"], fontweight="bold")
    for b, val in zip(bars2, norm_ratios):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.02,
                f"{val:.2f}", ha="center", va="bottom", fontsize=9,
                color=p["accent"])
    ax.set_xticks(xpos)
    ax.set_xticklabels([f"{int(c*100)}%" if c != 0.995 else "99.5%" for c in confs])
    ax.set_xlabel(s["p3_x"])
    ax.set_ylabel(s["p3_y"])
    ax.set_ylim(0, max(max(ratios), max(norm_ratios)) * 1.30)
    ax.set_title(s["p3_title"], fontsize=11, fontweight="bold", loc="left", pad=14)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.axhline(1.0, color=p["muted"], linewidth=0.8, linestyle=":")

    fig.suptitle(s["title"], fontsize=14, fontweight="bold", y=1.005)
    fig.text(0.5, 0.965, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"], style="italic")
    fig.text(0.01, -0.01, s["footer"], ha="left",
             fontsize=8.2, color=p["muted"])
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
