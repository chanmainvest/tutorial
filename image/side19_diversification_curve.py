"""Side 19, Sec 2.1 — Portfolio volatility as a function of N for four
correlation regimes (rho = 0, 0.3, 0.5, 0.7).

Single-asset vol fixed at sigma = 16% (long-run US large-cap). For each
rho, plot sigma_p(N) = sigma * sqrt(1/N + (1 - 1/N)*rho) for N=1..50.
Dotted horizontal asymptotes at sigma*sqrt(rho) make the diversification
floor visible.

Run:
    uv run python course/image/side19_diversification_curve.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side19_diversification_curve"

SIGMA = 0.16  # 16% per-asset annual vol
RHOS = [0.0, 0.3, 0.5, 0.7]


def _vol_curve(rho: float, ns: np.ndarray) -> np.ndarray:
    return SIGMA * np.sqrt(1.0 / ns + (1.0 - 1.0 / ns) * rho)


LANG_STRINGS = {
    "en": {
        "title":    "Diversification curve: portfolio vol vs N at four correlation regimes",
        "subtitle": "Per-asset vol = 16%. Equal weights. Curve = sigma * sqrt(1/N + (1-1/N) * rho). Floor = sigma * sqrt(rho).",
        "xlabel":   "Number of assets (N)",
        "ylabel":   "Portfolio volatility (annualised)",
        "legend":   ["rho = 0.0  (independent)", "rho = 0.3", "rho = 0.5", "rho = 0.7"],
        "floor":    "Floor = {pct:.1f}%",
        "ann_uncorr": "Independent assets:\nvol -> 0 as N grows",
        "ann_floor":  "At rho=0.5, more assets\nstop helping past ~25",
        "footer":   "The off-diagonal of the covariance matrix puts a hard floor on portfolio vol. Pairwise correlation, not name count, is the binding constraint.",
    },
    "hk": {
        "title":    "分散曲線:四個相關性情境下的組合波動率 vs N",
        "subtitle": "單一資產波動 = 16%。等權重。曲線 = sigma * sqrt(1/N + (1-1/N) * rho)。下限 = sigma * sqrt(rho)。",
        "xlabel":   "資產數目(N)",
        "ylabel":   "組合波動率(年化)",
        "legend":   ["rho = 0.0(獨立)", "rho = 0.3", "rho = 0.5", "rho = 0.7"],
        "floor":    "下限 = {pct:.1f}%",
        "ann_uncorr": "獨立資產:\nN 增加,vol -> 0",
        "ann_floor":  "rho=0.5 時,加多資產\n超過 25 隻已無幫助",
        "footer":   "協方差矩陣的非對角項目為組合波動設下硬性下限。決定因素是資產間的相關性,而非持倉數目。",
    },
    "tw": {
        "title":    "分散曲線:四種相關性情境下的組合波動率 vs N",
        "subtitle": "單一資產波動 = 16%。等權重。曲線 = sigma * sqrt(1/N + (1-1/N) * rho)。下限 = sigma * sqrt(rho)。",
        "xlabel":   "資產數目(N)",
        "ylabel":   "組合波動率(年化)",
        "legend":   ["rho = 0.0(獨立)", "rho = 0.3", "rho = 0.5", "rho = 0.7"],
        "floor":    "下限 = {pct:.1f}%",
        "ann_uncorr": "獨立資產:\nN 增加,vol -> 0",
        "ann_floor":  "rho=0.5 時,增加資產\n超過 25 檔已無助益",
        "footer":   "共變異矩陣的非對角項目為組合波動設下硬性下限。關鍵是資產間的相關性,而非持股數量。",
    },
    "cn": {
        "title":    "分散曲线:四种相关性情境下的组合波动率 vs N",
        "subtitle": "单一资产波动 = 16%。等权重。曲线 = sigma * sqrt(1/N + (1-1/N) * rho)。下限 = sigma * sqrt(rho)。",
        "xlabel":   "资产数目(N)",
        "ylabel":   "组合波动率(年化)",
        "legend":   ["rho = 0.0(独立)", "rho = 0.3", "rho = 0.5", "rho = 0.7"],
        "floor":    "下限 = {pct:.1f}%",
        "ann_uncorr": "独立资产:\nN 增加,vol -> 0",
        "ann_floor":  "rho=0.5 时,加多资产\n超过 25 只已无帮助",
        "footer":   "协方差矩阵的非对角项目为组合波动设下硬性下限。决定因素是资产间的相关性,而非持仓数目。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)

    ns = np.arange(1, 51)
    colors = [PALETTE_LIGHT["blue"], PALETTE_LIGHT["green"],
              PALETTE_LIGHT["accent"], PALETTE_LIGHT["red"]]
    for rho, color, label in zip(RHOS, colors, s["legend"]):
        y = _vol_curve(rho, ns) * 100.0
        ax.plot(ns, y, color=color, linewidth=2.4, label=label, zorder=3)
        # Floor as dotted horizontal at sigma*sqrt(rho).
        if rho > 0:
            floor = SIGMA * np.sqrt(rho) * 100.0
            ax.axhline(floor, color=color, linestyle=":",
                       linewidth=1.0, alpha=0.55, zorder=2)
            ax.text(50.6, floor, s["floor"].format(pct=floor),
                    color=color, fontsize=8.5, va="center", ha="left")

    # Annotation: independent assets -> 0
    ax.annotate(
        s["ann_uncorr"],
        xy=(45, _vol_curve(0.0, np.array([45]))[0] * 100.0),
        xytext=(28, 1.2),
        fontsize=9, color=PALETTE_LIGHT["blue"],
        ha="center", va="bottom",
        arrowprops=dict(arrowstyle="->", color=PALETTE_LIGHT["blue"],
                        lw=0.9, alpha=0.7),
    )
    # Annotation: floor in action
    ax.annotate(
        s["ann_floor"],
        xy=(25, _vol_curve(0.5, np.array([25]))[0] * 100.0),
        xytext=(8, 14.3),
        fontsize=9, color=PALETTE_LIGHT["accent"],
        ha="left", va="center",
        arrowprops=dict(arrowstyle="->", color=PALETTE_LIGHT["accent"],
                        lw=0.9, alpha=0.7),
    )

    ax.set_xlim(0.5, 55)
    ax.set_ylim(0, 17.5)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0f}%"))
    ax.legend(loc="upper right", framealpha=0.9, fontsize=9.5)

    style_axes(ax)
    ax.set_title(s["title"], pad=24, fontsize=14.5, weight="bold")
    fig.text(0.5, 0.935, s["subtitle"], ha="center",
             fontsize=10, color=PALETTE_LIGHT["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=PALETTE_LIGHT["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
