"""Week 23, S2.1 - Realised annualised factor premia 1963-2024.

Bar chart of approximate Fama-French + momentum annualised premia from
the Kenneth French data library (Jul 1963 - Dec 2024). Values are
embedded as constants since the lesson focuses on relative magnitudes,
not exact monthly replication.

Run:
    uv run python course/image/week23_factor_premia.py
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
BASE = "week23_factor_premia"

# Annualised mean premia, Jul 1963 - Dec 2024 (Fama-French + Carhart).
# Values rounded to nearest 10 bps; magnitudes match the canonical
# textbook reference numbers cited in the lesson.
FACTOR_NAMES = ["MKT-RF", "UMD", "HML", "CMA", "RMW", "SMB"]
FACTOR_PREMIA = [0.066, 0.075, 0.038, 0.033, 0.030, 0.024]
# Approximate annualised volatility of each long-short factor.
FACTOR_VOL = [0.155, 0.155, 0.105, 0.070, 0.080, 0.110]


LANG_STRINGS = {
    "en": {
        "title":    "Realised annualised factor premia, 1963-2024",
        "subtitle": "Fama-French + Carhart, US universe, monthly long-short construction. Bars are mean premium; whiskers show +/- 1 ann. std dev.",
        "ylabel":   "Annualised premium",
        "footer":   "Momentum has the largest mean and worst single-year drawdown (-45% in 2009). Size has the smallest premium and is barely distinguishable from zero post-2000.",
        "names":    FACTOR_NAMES,
    },
    "hk": {
        "title":    "已實現的年化因子溢價,1963-2024",
        "subtitle": "Fama-French + Carhart,美股全集,每月多空建構。柱為平均溢價;誤差棒為 +/- 1 個年化標準差。",
        "ylabel":   "年化溢價",
        "footer":   "動量平均最高,但 2009 單年回撚 -45% 也最重。規模溢價最小,2000 年後幾乎與零無異。",
        "names":    ["市場-無風險", "動量", "價值", "投資", "盈利", "規模"],
    },
    "tw": {
        "title":    "已實現的年化因子溢酬,1963-2024",
        "subtitle": "Fama-French + Carhart,美股全集,每月多空建構。柱為平均溢酬;誤差棒為 +/- 1 個年化標準差。",
        "ylabel":   "年化溢酬",
        "footer":   "動量平均最高,但 2009 單年回檔 -45% 也最重。規模溢酬最小,2000 年後幾乎與零無異。",
        "names":    ["市場-無風險", "動量", "價值", "投資", "獲利", "規模"],
    },
    "cn": {
        "title":    "已实现的年化因子溢价,1963-2024",
        "subtitle": "Fama-French + Carhart,美股全集,每月多空构造。柱为平均溢价;误差棒为 +/- 1 个年化标准差。",
        "ylabel":   "年化溢价",
        "footer":   "动量平均最高,但 2009 单年回撚 -45% 也最重。规模溢价最小,2000 年后几乎与零无异。",
        "names":    ["市场-无风险", "动量", "价值", "投资", "盈利", "规模"],
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, p)

    n = len(FACTOR_PREMIA)
    x = np.arange(n)
    colors = [p["accent"], p["red"], p["blue"], p["green"], p["purple"], p["orange"]]
    bars = ax.bar(x, FACTOR_PREMIA, color=colors, edgecolor="none", alpha=0.9, width=0.65)

    # Whiskers: +/- 1 vol (annualised).
    for xi, mu, sigma, c in zip(x, FACTOR_PREMIA, FACTOR_VOL, colors):
        ax.errorbar(xi, mu, yerr=sigma, fmt="none",
                    ecolor=c, alpha=0.55, capsize=8, elinewidth=1.6)

    # Labels above each bar.
    for xi, mu in zip(x, FACTOR_PREMIA):
        ax.text(xi, mu + 0.005, f"{mu*100:.1f}%",
                ha="center", va="bottom", fontsize=11, fontweight="bold", color=p["fg"])

    ax.set_xticks(x)
    ax.set_xticklabels(s["names"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.set_ylim(-0.10, 0.24)
    ax.axhline(0, color=p["fg"], linewidth=0.8)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))

    ax.set_title(s["title"], fontsize=14, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.text(0.06, 0.02, s["footer"], fontsize=9, color=p["muted"])
    fig.tight_layout(rect=[0, 0.05, 1, 0.95])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
