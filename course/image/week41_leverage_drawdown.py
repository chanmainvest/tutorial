"""Week 41, §2.6 — Expected max drawdown vs leverage over 30 years.

Strategy: 10% annualised arithmetic return, 16% annualised volatility,
GBM with 252 trading days per year. For each leverage L in {1.0, 1.25,
1.5, 2.0, 3.0}, simulate 5,000 thirty-year paths with daily borrow
drag of (L - 1) * 5% / 252 and compute the expected (mean) max
drawdown. Bar chart with non-linear blowup beyond L=1.5.

Run:
    uv run python course/image/week41_leverage_drawdown.py
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
BASE = "week41_leverage_drawdown"

LANG_STRINGS = {
    "en": {
        "title":    "Expected max drawdown over 30 years vs leverage",
        "subtitle": "Strategy: 10% return, 16% vol, weekly GBM, 5% borrow on (L-1) notional. 2,000 paths per leverage.",
        "xlabel":   "Leverage (multiple of bankroll)",
        "ylabel":   "Expected max drawdown (peak to trough)",
        "annot":    "Asymmetric blowup\nbeyond 1.5x",
        "footer":   "DD scales roughly as (1+L) of unlevered DD plus financing drag. Above 1.5x leverage, fat tails dominate the result.",
    },
    "hk": {
        "title":    "三十年期望最大回撚 vs 槓桿",
        "subtitle": "策略:回報 10%、波幅 16%、週度 GBM、(L-1) 名義頭寸 5% 融資成本。每個槓桿 2,000 條路徑。",
        "xlabel":   "槓桿(本金倍數)",
        "ylabel":   "期望最大回撚(前高至谷底)",
        "annot":    "1.5x 之後\n非線性爆煲",
        "footer":   "DD 約為無槓桿 DD 的 (1+L) 倍再加融資拖累。1.5x 以上,肥尾主導結果。",
    },
    "tw": {
        "title":    "三十年期望最大回檔 vs 槓桿",
        "subtitle": "策略:報酬 10%、波動 16%、週度 GBM、(L-1) 名目頭寸 5% 融資成本。每個槓桿 2,000 條路徑。",
        "xlabel":   "槓桿(本金倍數)",
        "ylabel":   "期望最大回檔(前高至谷底)",
        "annot":    "1.5x 之後\n非線性爆倉",
        "footer":   "DD 約為無槓桿 DD 的 (1+L) 倍再加融資拖累。1.5x 以上,肥尾主導結果。",
    },
    "cn": {
        "title":    "三十年期望最大回撚 vs 杠杆",
        "subtitle": "策略:回报 10%、波动 16%、周度 GBM、(L-1) 名义头寸 5% 融资成本。每个杠杆 2,000 条路径。",
        "xlabel":   "杠杆(本金倍数)",
        "ylabel":   "期望最大回撚(前高至谷底)",
        "annot":    "1.5x 之后\n非线性爆仓",
        "footer":   "DD 约为无杠杆 DD 的 (1+L) 倍再加融资拖累。1.5x 以上,肥尾主导结果。",
    },
}

LEVERAGES = [1.0, 1.25, 1.5, 2.0, 3.0]
MU_ANNUAL = 0.10
SIGMA_ANNUAL = 0.16
BORROW_ANNUAL = 0.05
YEARS = 30
STEPS_PER_YEAR = 52  # weekly steps; coarse but stable for max-DD
N_PATHS = 2000
SEED = 42


def _expected_max_drawdown(L: float) -> tuple[float, float]:
    """Return (mean_max_dd, p95_max_dd) as positive fractions for leverage L."""
    rng = np.random.default_rng(SEED + int(L * 100))
    dt = 1.0 / STEPS_PER_YEAR
    n_steps = YEARS * STEPS_PER_YEAR
    # Levered annual drift after borrow drag; vol scales linearly with L.
    annual_drift = L * MU_ANNUAL - (L - 1.0) * BORROW_ANNUAL
    mu_step = annual_drift * dt - 0.5 * (L * SIGMA_ANNUAL) ** 2 * dt
    sig_step = L * SIGMA_ANNUAL * np.sqrt(dt)

    z = rng.standard_normal((N_PATHS, n_steps))
    log_ret = mu_step + sig_step * z
    log_path = np.cumsum(log_ret, axis=1)
    wealth = np.exp(log_path)
    wealth = np.concatenate([np.ones((N_PATHS, 1)), wealth], axis=1)
    running_max = np.maximum.accumulate(wealth, axis=1)
    dd = wealth / running_max - 1.0
    max_dds = -dd.min(axis=1)
    return float(max_dds.mean()), float(np.quantile(max_dds, 0.95))


def build_fig(s):
    means = []
    p95s = []
    for L in LEVERAGES:
        m, p = _expected_max_drawdown(L)
        means.append(m)
        p95s.append(p)

    pal = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, pal)

    x = np.arange(len(LEVERAGES))
    # Colour bars: green/teal/blue for safe, orange/red for blowup.
    bar_colors = [pal["green"], pal["teal"], pal["blue"], pal["orange"], pal["red"]]
    bars = ax.bar(x, [m * 100 for m in means], width=0.62, color=bar_colors,
                  edgecolor=pal["fg"], linewidth=0.8, zorder=3)

    # 95th percentile whiskers (light line caps above mean).
    for xi, m, p in zip(x, means, p95s):
        ax.plot([xi, xi], [m * 100, p * 100], color=pal["fg"], lw=1.0, alpha=0.6, zorder=4)
        ax.plot([xi - 0.15, xi + 0.15], [p * 100, p * 100], color=pal["fg"], lw=1.0, alpha=0.6, zorder=4)

    # Annotate values on bars.
    for xi, m in zip(x, means):
        ax.text(xi, m * 100 + 1.5, f"{m*100:.0f}%", ha="center", va="bottom",
                fontsize=10.5, color=pal["fg"], weight="bold")

    # Asymmetric-blowup callout between 1.5x and 3.0x.
    ax.annotate(
        s["annot"],
        xy=(4, means[4] * 100), xytext=(2.6, means[4] * 100 + 3),
        fontsize=10, color=pal["red"], weight="bold",
        arrowprops=dict(arrowstyle="->", color=pal["red"], lw=1.2),
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff5f5", ec=pal["red"], lw=0.8),
    )

    ax.set_xticks(x)
    ax.set_xticklabels([f"{L:g}x" for L in LEVERAGES], fontsize=10.5)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_ylim(0, max(p95s) * 105)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_yticklabels(["0%", "-20%", "-40%", "-60%", "-80%", "-100%"])

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=9, color=pal["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
