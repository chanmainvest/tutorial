"""Week 7, §2.6 — Bessembinder's return-concentration + diversification benefit.

Top panel: stylised histogram of lifetime individual US stock returns
(Bessembinder 1926-2016 dataset) showing the long left tail of losers,
a thick cluster around T-bill returns, and a thin but extreme right
tail of mega-winners.

Bottom panel: Monte Carlo fan chart comparing a single random stock
versus an equal-weight basket of 500 stocks over 30 years, showing how
diversification shrinks the cone of outcomes.

Run:
    uv run python course/image/week07_concentration_vs_diversification.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week07_concentration_vs_diversification"

LANG_STRINGS = {
    "en": {
        "title":    "Most stocks underperform — but the basket captures the winners",
        "subtitle": "Top: lifetime return distribution of individual US stocks (Bessembinder 1926-2016). Bottom: single stock vs 500-stock basket over 30 years.",
        "xlabel_top":   "Lifetime total return (%)",
        "ylabel_top":   "Number of stocks (stylised)",
        "xlabel_bot":   "Years",
        "ylabel_bot":   "Cumulative wealth ($1 start)",
        "mode_lbl":     "Mode: slightly\nnegative return",
        "mean_lbl":     "Mean: positive\n(pulled by right tail)",
        "left_tail":    "~58% underperform\nT-bills over lifetime",
        "right_tail":   "Top 4% create\nall net wealth",
        "single":       "Single random stock\n(wide cone)",
        "basket":       "500-stock basket\n(tight cone)",
        "footer":       "Stylised illustration based on Bessembinder (2018) 'Do Stocks Outperform Treasury Bills?' Not to scale.",
    },
    "hk": {
        "title":    "大多數股票跑輸 — 但組合能捕捉贏家",
        "subtitle": "上:個股終生回報分布(Bessembinder 1926-2016)。下:單一股票 vs 500 股組合,30 年表現。",
        "xlabel_top":   "終生總回報(%)",
        "ylabel_top":   "股票數目(示意)",
        "xlabel_bot":   "年數",
        "ylabel_bot":   "累計財富($1 起)",
        "mode_lbl":     "眾數:略為\n負回報",
        "mean_lbl":     "平均:正數\n(被右尾拉高)",
        "left_tail":    "約 58% 終生\n跑輸國庫券",
        "right_tail":   "頂尖 4% 貢獻\n全部淨財富",
        "single":       "單一隨機股票\n(闊錐)",
        "basket":       "500 股組合\n(窄錐)",
        "footer":       "示意圖,基於 Bessembinder (2018)。並非按比例繪製。",
    },
    "tw": {
        "title":    "大多數個股跑輸 — 但投資組合能捕捉贏家",
        "subtitle": "上:個股終生報酬分布(Bessembinder 1926-2016)。下:單一股票 vs 500 檔組合,30 年表現。",
        "xlabel_top":   "終生總報酬(%)",
        "ylabel_top":   "股票檔數(示意)",
        "xlabel_bot":   "年數",
        "ylabel_bot":   "累計財富($1 起)",
        "mode_lbl":     "眾數:略為\n負報酬",
        "mean_lbl":     "平均:正數\n(被右尾拉高)",
        "left_tail":    "約 58% 終生\n不如國庫券",
        "right_tail":   "頂尖 4% 創造\n全部淨財富",
        "single":       "單一隨機股票\n(寬錐)",
        "basket":       "500 檔組合\n(窄錐)",
        "footer":       "示意圖,基於 Bessembinder (2018)。並非按比例繪製。",
    },
    "cn": {
        "title":    "大多数股票跑输 — 但组合能捕捉赢家",
        "subtitle": "上:个股终身回报分布(Bessembinder 1926-2016)。下:单只股票 vs 500 股组合,30 年表现。",
        "xlabel_top":   "终身总回报(%)",
        "ylabel_top":   "股票数量(示意)",
        "xlabel_bot":   "年数",
        "ylabel_bot":   "累计财富($1 起)",
        "mode_lbl":     "众数:略为\n负回报",
        "mean_lbl":     "均值:正数\n(被右尾拉高)",
        "left_tail":    "约 58% 终身\n跑输国库券",
        "right_tail":   "前 4% 创造\n全部净财富",
        "single":       "单只随机股票\n(宽锥)",
        "basket":       "500 股组合\n(窄锥)",
        "footer":       "示意图,基于 Bessembinder (2018)。并非按比例绘制。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(10.5, 8.5),
        gridspec_kw={"height_ratios": [1, 1], "hspace": 0.42},
    )
    style_axes(ax1, p)
    style_axes(ax2, p)

    # ---- Top panel: Stylised Bessembinder distribution ----
    # Right-skewed distribution with fat left tail and thin right tail
    # Use a mix of two distributions to get the right shape
    rng = np.random.default_rng(42)
    x = np.linspace(-110, 600, 800)

    # Main body: skew-normal centred near -5% with large left mass
    body = skewnorm.pdf(x, a=5, loc=-20, scale=60) * 8000
    # Right tail: thin lognormal-like bump for mega-winners
    right_tail = np.exp(-((x - 200) ** 2) / (2 * 120**2)) * 150
    right_tail2 = np.exp(-((x - 400) ** 2) / (2 * 80**2)) * 40
    y = body + right_tail + right_tail2

    # Colour: left of 0 in red, right in green
    mask_neg = x <= 0
    mask_pos = x > 0
    ax1.fill_between(x[mask_neg], 0, y[mask_neg], color=p["red"], alpha=0.35)
    ax1.fill_between(x[mask_pos], 0, y[mask_pos], color=p["green"], alpha=0.30)
    ax1.plot(x, y, color=p["fg"], linewidth=1.4)

    # Mode line
    mode_idx = np.argmax(y)
    mode_x = x[mode_idx]
    ax1.axvline(mode_x, color=p["red"], linestyle=":", linewidth=1.2, alpha=0.7)
    ax1.text(mode_x - 8, y.max() * 0.92, s["mode_lbl"],
             ha="right", fontsize=8.5, color=p["red"])

    # Mean line (positive)
    mean_x = 45
    ax1.axvline(mean_x, color=p["green"], linestyle="--", linewidth=1.2, alpha=0.7)
    ax1.text(mean_x + 8, y.max() * 0.85, s["mean_lbl"],
             ha="left", fontsize=8.5, color=p["green"])

    # Left tail annotation
    ax1.text(-80, y.max() * 0.45, s["left_tail"],
             ha="center", fontsize=9, color=p["red"], fontweight="bold")

    # Right tail annotation
    ax1.text(350, y.max() * 0.25, s["right_tail"],
             ha="center", fontsize=9, color=p["green"], fontweight="bold")

    ax1.set_xlabel(s["xlabel_top"], fontsize=10)
    ax1.set_ylabel(s["ylabel_top"], fontsize=10)
    ax1.set_xlim(-120, 550)
    ax1.set_yticks([])

    # ---- Bottom panel: Single stock vs basket Monte Carlo ----
    years = np.arange(0, 31)
    n_paths = 200

    # Single stock: mu=10% vol=40% (individual stock vol)
    mu_s, vol_s = 0.07, 0.40
    # Basket of 500: mu=10% vol~15% (market-like)
    mu_b, vol_b = 0.10, 0.15

    single_paths = np.zeros((n_paths, len(years)))
    basket_paths = np.zeros((n_paths, len(years)))
    single_paths[:, 0] = 1.0
    basket_paths[:, 0] = 1.0

    for i in range(n_paths):
        for t in range(1, len(years)):
            single_paths[i, t] = single_paths[i, t-1] * np.exp(
                (mu_s - 0.5 * vol_s**2) + vol_s * rng.standard_normal()
            )
            basket_paths[i, t] = basket_paths[i, t-1] * np.exp(
                (mu_b - 0.5 * vol_b**2) + vol_b * rng.standard_normal()
            )

    # Fan chart for single stock
    for pct in [5, 25, 75, 95]:
        low = np.percentile(single_paths, min(pct, 100-pct), axis=0)
        high = np.percentile(single_paths, max(pct, 100-pct), axis=0)
        ax2.fill_between(years, low, high, color=p["red"], alpha=0.08)

    p50_s = np.median(single_paths, axis=0)
    ax2.plot(years, p50_s, color=p["red"], linewidth=1.8, linestyle="--")

    # Fan chart for basket
    for pct in [5, 25, 75, 95]:
        low = np.percentile(basket_paths, min(pct, 100-pct), axis=0)
        high = np.percentile(basket_paths, max(pct, 100-pct), axis=0)
        ax2.fill_between(years, low, high, color=p["blue"], alpha=0.10)

    p50_b = np.median(basket_paths, axis=0)
    ax2.plot(years, p50_b, color=p["blue"], linewidth=2.0)

    # Labels
    ax2.text(25, np.percentile(single_paths[:, -1], 85),
             s["single"], fontsize=9, color=p["red"], fontweight="bold",
             va="bottom")
    ax2.text(25, np.percentile(basket_paths[:, -1], 75),
             s["basket"], fontsize=9, color=p["blue"], fontweight="bold",
             va="bottom")

    ax2.set_xlabel(s["xlabel_bot"], fontsize=10)
    ax2.set_ylabel(s["ylabel_bot"], fontsize=10)
    ax2.set_yscale("log")
    ax2.set_xlim(0, 30)

    # Title and subtitle
    ax1.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax1.text(0, 1.04, s["subtitle"], transform=ax1.transAxes,
             fontsize=9.5, color=p["muted"])
    ax2.text(0.0, -0.18, s["footer"], transform=ax2.transAxes,
             fontsize=8, color=p["muted"])
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for path in paths:
        print(f"wrote {path}")
