"""Side Lesson 28 - Monte Carlo wealth fan, 1000 paths x 30 years.

Starts at $1M, no contributions, 7% annual expected return, 15% annual
volatility, monthly steps. Plots all 1000 paths faintly plus the
5/25/50/75/95 percentile bands as shaded regions. Deterministic seed
so the chart is reproducible.

Run:
    uv run python course/image/side28_mc_fan.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side28_mc_fan"

# --- Simulation parameters ---
W0 = 1_000_000.0
MU_A = 0.07          # annual expected return
SIG_A = 0.15         # annual volatility
T_YEARS = 30
STEPS_PER_YEAR = 12
N_PATHS = 1000
SEED = 20260429


def _simulate():
    rng = np.random.default_rng(SEED)
    n_steps = T_YEARS * STEPS_PER_YEAR
    mu_m = MU_A / STEPS_PER_YEAR
    sig_m = SIG_A / np.sqrt(STEPS_PER_YEAR)
    # Arithmetic monthly Normal returns clipped at -50% to avoid <=-100%.
    rets = rng.normal(mu_m, sig_m, size=(N_PATHS, n_steps))
    rets = np.clip(rets, -0.5, None)
    growth = np.cumprod(1.0 + rets, axis=1)
    paths = W0 * np.concatenate([np.ones((N_PATHS, 1)), growth], axis=1)
    # Convert to years
    years = np.arange(n_steps + 1) / STEPS_PER_YEAR
    return years, paths


LANG_STRINGS = {
    "en": {
        "title":    "Monte Carlo wealth fan: $1M, 30-year horizon, 7% / 15% return-vol",
        "subtitle": "1,000 simulated paths. Bands = 5/25/50/75/95 percentiles. No contributions or withdrawals.",
        "xlabel":   "Years from start",
        "ylabel":   "Account value (USD)",
        "legend":   {
            "p5_95": "5-95 percentile band",
            "p25_75": "25-75 percentile band",
            "median": "Median path",
            "paths": "Individual paths (faint)",
        },
        "annot_med":  "Median ${med}M",
        "annot_p5":   "P5 ${p5}M",
        "annot_p95":  "P95 ${p95}M",
        "footer":     "Parametric Normal MC: monthly steps, mu/12 mean, sigma/sqrt(12) stdev. Seed=20260429.",
    },
    "hk": {
        "title":    "蒙特卡羅財富扇形圖:100 萬美元,30 年期,7% / 15% 回報-波幅",
        "subtitle": "1,000 條模擬路徑。色帶 = 5/25/50/75/95 百分位數。無供款或提取。",
        "xlabel":   "起始後年數",
        "ylabel":   "戶口價值(美元)",
        "legend":   {
            "p5_95": "5-95 百分位帶",
            "p25_75": "25-75 百分位帶",
            "median": "中位路徑",
            "paths": "個別路徑(淡色)",
        },
        "annot_med":  "中位 ${med}M",
        "annot_p5":   "P5 ${p5}M",
        "annot_p95":  "P95 ${p95}M",
        "footer":     "參數常態 MC:月度步長,均值 mu/12,標準差 sigma/sqrt(12)。種子 20260429。",
    },
    "tw": {
        "title":    "蒙地卡羅財富扇形圖:100 萬美元,30 年期,7% / 15% 報酬-波動",
        "subtitle": "1,000 條模擬路徑。色帶 = 5/25/50/75/95 百分位數。無提撥或提領。",
        "xlabel":   "起始後年數",
        "ylabel":   "帳戶價值(美元)",
        "legend":   {
            "p5_95": "5-95 百分位帶",
            "p25_75": "25-75 百分位帶",
            "median": "中位路徑",
            "paths": "個別路徑(淡色)",
        },
        "annot_med":  "中位 ${med}M",
        "annot_p5":   "P5 ${p5}M",
        "annot_p95":  "P95 ${p95}M",
        "footer":     "參數常態 MC:月度步長,平均 mu/12,標準差 sigma/sqrt(12)。種子 20260429。",
    },
    "cn": {
        "title":    "蒙特卡洛财富扇形图:100 万美元,30 年期,7% / 15% 回报-波动",
        "subtitle": "1,000 条模拟路径。色带 = 5/25/50/75/95 百分位数。无供款或提取。",
        "xlabel":   "起始后年数",
        "ylabel":   "账户价值(美元)",
        "legend":   {
            "p5_95": "5-95 百分位带",
            "p25_75": "25-75 百分位带",
            "median": "中位路径",
            "paths": "个别路径(淡色)",
        },
        "annot_med":  "中位 ${med}M",
        "annot_p5":   "P5 ${p5}M",
        "annot_p95":  "P95 ${p95}M",
        "footer":     "参数正态 MC:月度步长,均值 mu/12,标准差 sigma/sqrt(12)。种子 20260429。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    years, paths = _simulate()

    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax, p)

    # Faint individual paths (subset for legibility)
    show_n = 100
    idx = np.linspace(0, N_PATHS - 1, show_n).astype(int)
    for i in idx:
        ax.plot(years, paths[i] / 1e6, color=p["muted"], linewidth=0.4, alpha=0.18)

    # Percentiles
    p5 = np.percentile(paths, 5, axis=0) / 1e6
    p25 = np.percentile(paths, 25, axis=0) / 1e6
    p50 = np.percentile(paths, 50, axis=0) / 1e6
    p75 = np.percentile(paths, 75, axis=0) / 1e6
    p95 = np.percentile(paths, 95, axis=0) / 1e6

    ax.fill_between(years, p5, p95, color=p["blue"], alpha=0.13,
                    label=s["legend"]["p5_95"])
    ax.fill_between(years, p25, p75, color=p["blue"], alpha=0.28,
                    label=s["legend"]["p25_75"])
    ax.plot(years, p50, color=p["accent"], linewidth=2.4,
            label=s["legend"]["median"])

    # Bound lines
    ax.plot(years, p5, color=p["red"], linewidth=1.0, alpha=0.7)
    ax.plot(years, p95, color=p["green"], linewidth=1.0, alpha=0.7)

    # Annotations at year 30
    end_p5, end_p50, end_p95 = float(p5[-1]), float(p50[-1]), float(p95[-1])
    ax.annotate(s["annot_p95"].format(p95=f"{end_p95:.1f}"),
                xy=(T_YEARS, end_p95), xytext=(T_YEARS - 0.5, end_p95 * 1.05),
                ha="right", va="bottom", color=p["green"], fontsize=10,
                weight="bold")
    ax.annotate(s["annot_med"].format(med=f"{end_p50:.1f}"),
                xy=(T_YEARS, end_p50), xytext=(T_YEARS - 0.5, end_p50 * 1.10),
                ha="right", va="bottom", color=p["accent"], fontsize=10,
                weight="bold")
    ax.annotate(s["annot_p5"].format(p5=f"{end_p5:.1f}"),
                xy=(T_YEARS, end_p5), xytext=(T_YEARS - 0.5, end_p5 * 0.85),
                ha="right", va="top", color=p["red"], fontsize=10,
                weight="bold")

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"], color=p["fg"])
    ax.set_ylabel(s["ylabel"] + " (M, log scale)", color=p["fg"])
    ax.set_xlim(0, T_YEARS)
    ax.set_ylim(0.5, 60)
    ax.set_yticks([0.5, 1, 2, 5, 10, 20, 50])
    ax.set_yticklabels(["0.5M", "1M", "2M", "5M", "10M", "20M", "50M"])

    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold", color=p["fg"])
    fig.text(0.5, 0.93, s["subtitle"], ha="center", fontsize=10.5,
             color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.5,
             color=p["muted"], style="italic")

    leg = ax.legend(loc="upper left", fontsize=9, framealpha=0.92)
    leg.get_frame().set_edgecolor(p["grid"])

    fig.tight_layout(rect=[0, 0.03, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}.png + 4 locale variants to {OUT_DIR}")
