"""Week 46, §2.4 — Histogram of 1000 random-strategy in-sample Sharpe ratios
under the null (true SR = 0), with theoretical density overlaid and the
SR=2, SR=3 thresholds marked.

For T=252 daily observations and true SR=0, the SE of the annualised
estimated Sharpe is approximately 1.0. So out of 1000 random strategies,
about 25 will clear SR>2 and about 3 will clear SR>3 by pure chance.

Run:
    uv run python course/image/week46_deflated_sharpe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week46_deflated_sharpe"

N_STRAT = 1000
T_DAYS = 252
DAILY_VOL = 0.01  # 1% daily vol -> ~16% annualised, irrelevant since SR is scale-free

LANG_STRINGS = {
    "en": {
        "title":    "1000 random strategies, true Sharpe = 0",
        "subtitle": "Histogram of in-sample annualised Sharpe ratios. Each bar to the right of SR=2 is a strategy with literally zero alpha that nonetheless tested above the conventional threshold.",
        "xlabel":   "In-sample annualised Sharpe ratio",
        "ylabel":   "Number of strategies (out of 1000)",
        "footer":   "Simulation: each of 1000 strategies generates 252 daily noise returns. SR=mean/std * sqrt(252). Theoretical density (smooth curve) is N(0, 1) approximately. ~25 random strategies clear SR>2 by chance; ~3 clear SR>3.",
        "thr2":     "SR = 2.0\n~25 strategies",
        "thr3":     "SR = 3.0\n~3 strategies",
        "null":     "Null density (zero true SR)",
        "obs":      "Observed (1000 trials)",
    },
    "hk": {
        "title":    "1000 個隨機策略,真實夏普 = 0",
        "subtitle": "1000 個隨機策略的樣本內年化夏普比直方圖。SR=2 右邊的每根柱代表一個真實 alpha 為零、卻測試出傳統門檻以上的策略。",
        "xlabel":   "樣本內年化夏普比",
        "ylabel":   "策略數量(共 1000)",
        "footer":   "模擬:每個策略生成 252 個每日噪聲回報。SR = 均值/標準差 * sqrt(252)。理論密度近似 N(0, 1)。約 25 個策略意外越過 SR>2;約 3 個越過 SR>3。",
        "thr2":     "SR = 2.0\n~25 個策略",
        "thr3":     "SR = 3.0\n~3 個策略",
        "null":     "虛無分佈(真實 SR = 0)",
        "obs":      "觀測值(1000 次試驗)",
    },
    "tw": {
        "title":    "1000 個隨機策略,真實夏普 = 0",
        "subtitle": "1000 個隨機策略的樣本內年化夏普比直方圖。SR=2 右邊的每根柱代表一個真實 alpha 為零、卻測試出傳統門檻以上的策略。",
        "xlabel":   "樣本內年化夏普比",
        "ylabel":   "策略數量(共 1000)",
        "footer":   "模擬:每個策略生成 252 個每日噪聲報酬。SR = 均值/標準差 * sqrt(252)。理論密度近似 N(0, 1)。約 25 個策略意外越過 SR>2;約 3 個越過 SR>3。",
        "thr2":     "SR = 2.0\n~25 個策略",
        "thr3":     "SR = 3.0\n~3 個策略",
        "null":     "虛無分布(真實 SR = 0)",
        "obs":      "觀測值(1000 次試驗)",
    },
    "cn": {
        "title":    "1000 个随机策略,真实夏普 = 0",
        "subtitle": "1000 个随机策略的样本内年化夏普比直方图。SR=2 右边的每根柱代表一个真实 alpha 为零、却测出传统门槛以上的策略。",
        "xlabel":   "样本内年化夏普比",
        "ylabel":   "策略数量(共 1000)",
        "footer":   "模拟:每个策略生成 252 个每日噪声回报。SR = 均值/标准差 * sqrt(252)。理论密度近似 N(0, 1)。约 25 个策略意外越过 SR>2;约 3 个越过 SR>3。",
        "thr2":     "SR = 2.0\n~25 个策略",
        "thr3":     "SR = 3.0\n~3 个策略",
        "null":     "虚无分布(真实 SR = 0)",
        "obs":      "观测值(1000 次试验)",
    },
}


def _simulate_sharpes(seed=20260429):
    rng = np.random.default_rng(seed)
    # Each row = one strategy with T_DAYS daily returns N(0, vol).
    rets = rng.normal(0.0, DAILY_VOL, size=(N_STRAT, T_DAYS))
    mu = rets.mean(axis=1)
    sd = rets.std(axis=1, ddof=1)
    daily_sr = mu / sd
    annual_sr = daily_sr * np.sqrt(T_DAYS)
    return annual_sr


def build_fig(s):
    p = PALETTE_LIGHT
    sharpes = _simulate_sharpes()

    fig, ax = plt.subplots(figsize=(11.2, 6.2), dpi=160)
    style_axes(ax, p)

    bins = np.arange(-3.5, 3.6, 0.2)
    counts, _, patches = ax.hist(
        sharpes, bins=bins, color=p["blue"], alpha=0.78,
        edgecolor=p["bg"], linewidth=0.8, label=s["obs"],
    )

    # Color tail bins (>2) in red.
    for patch, edge in zip(patches, bins[:-1]):
        if edge >= 2.0:
            patch.set_facecolor(p["red"])
        elif edge >= 1.0:
            patch.set_facecolor(p["accent"])

    # Theoretical N(0,1) density scaled to histogram total area.
    bin_width = bins[1] - bins[0]
    xs = np.linspace(-3.5, 3.5, 400)
    pdf = (1.0 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * xs ** 2)
    pdf_count = pdf * N_STRAT * bin_width
    ax.plot(xs, pdf_count, color=p["fg"], linewidth=2.0,
            label=s["null"])

    # Threshold lines
    n_above_2 = int((sharpes > 2.0).sum())
    n_above_3 = int((sharpes > 3.0).sum())

    ax.axvline(2.0, color=p["red"], linestyle="--", linewidth=1.4, alpha=0.85)
    ax.axvline(3.0, color=p["purple"], linestyle="--", linewidth=1.4, alpha=0.85)

    ymax = counts.max() * 1.20
    ax.set_ylim(0, ymax)

    # Annotation boxes for thresholds
    text_y = ymax * 0.78
    txt2 = s["thr2"].replace("~25", f"{n_above_2}")
    txt3 = s["thr3"].replace("~3", f"{n_above_3}")
    ax.annotate(
        txt2, xy=(2.0, ymax * 0.55), xytext=(2.55, text_y),
        fontsize=9.5, color=p["red"], fontweight="bold",
        ha="left", va="top",
        arrowprops=dict(arrowstyle="-", color=p["red"], lw=0.8, alpha=0.6),
    )
    ax.annotate(
        txt3, xy=(3.0, ymax * 0.20), xytext=(3.05, ymax * 0.45),
        fontsize=9.5, color=p["purple"], fontweight="bold",
        ha="left", va="top",
        arrowprops=dict(arrowstyle="-", color=p["purple"], lw=0.8, alpha=0.6),
    )

    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_xlim(-3.5, 3.8)
    ax.legend(loc="upper left", fontsize=9.5, frameon=False)

    ax.set_title(s["title"], pad=24, fontsize=14.5, weight="bold",
                 color=p["fg"], loc="left")
    fig.text(0.06, 0.93, s["subtitle"], ha="left",
             fontsize=10, color=p["muted"], style="italic")
    fig.text(0.06, 0.015, s["footer"], fontsize=8.8, color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
