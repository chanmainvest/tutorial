"""Side 11, §2.2 — Roth vs. Traditional terminal after-tax wealth.

Two-panel chart.

Left panel: Parity scenarios. For each of four current = retirement
bracket scenarios (12, 22, 32, 37%), compute the after-tax wealth at
age 65 from $7,000/year contributed for 30 years at 7% growth, on an
*equal-after-tax-cost* basis:

  Roth contribution (after tax)         = $7,000
  Trad contribution (pre-tax-equiv)     = $7,000 / (1 - t_now)
  Roth ending after-tax  = $7,000 * FV
  Trad ending after-tax  = $7,000 / (1 - t_now) * FV * (1 - t_ret)

When t_now == t_ret the two are algebraically identical -> equal bars.

Right panel: Divergence scenarios. Fix t_now = 24%; vary t_ret in
{14%, 24%, 34%}. Trad wins when t_ret < t_now, Roth wins when t_ret > t_now.

Run:
    uv run python course/image/side11_roth_vs_trad.py
"""

from __future__ import annotations
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side11_roth_vs_trad"

CONTRIB = 7000.0
YEARS = 30
GROWTH = 0.07
FV_FACTOR = ((1.0 + GROWTH) ** YEARS - 1.0) / GROWTH  # annuity FV factor


def roth_end(t_now):
    # $7,000 after-tax contributed each year, no tax at withdrawal.
    return CONTRIB * FV_FACTOR


def trad_end(t_now, t_ret):
    # Equal after-tax cost: contribute $7,000 / (1 - t_now) pre-tax.
    pretax_contrib = CONTRIB / (1.0 - t_now)
    fv = pretax_contrib * FV_FACTOR
    return fv * (1.0 - t_ret)


PARITY_BRACKETS = [0.12, 0.22, 0.32, 0.37]
DIV_T_NOW = 0.24
DIV_T_RETS = [0.14, 0.24, 0.34]

LANG_STRINGS = {
    "en": {
        "title":    "Roth vs. Traditional - Terminal After-Tax Wealth at Age 65",
        "subtitle": "$7,000/year equal after-tax cost, 30 years, 7% growth. Parity holds when current bracket = retirement bracket.",
        "left_title":  "Parity: current bracket = retirement bracket",
        "right_title": "Divergence: current bracket fixed at 24%",
        "xlabel_left":  "Bracket (current = retirement)",
        "xlabel_right": "Retirement bracket (current = 24%)",
        "ylabel":       "After-tax wealth at 65",
        "label_roth":  "Roth",
        "label_trad":  "Traditional",
        "annot_parity": "Equal in every bracket\n(algebraic parity)",
        "annot_trad_wins": "Trad wins when\nretirement bracket lower",
        "annot_roth_wins": "Roth wins when\nretirement bracket higher",
        "footer": "Roth = (after-tax $) x FV. Traditional = (after-tax $)/(1 - t_now) x FV x (1 - t_ret). Identical when t_now = t_ret.",
    },
    "hk": {
        "title":    "Roth vs 傳統 - 65 歲稅後終值",
        "subtitle": "每年 $7,000 等稅後成本,30 年 7% 增長。當前稅階 = 退休稅階時兩者完全相等。",
        "left_title":  "等同情境:當前稅階 = 退休稅階",
        "right_title": "差異情境:當前稅階固定 24%",
        "xlabel_left":  "稅階(當前 = 退休)",
        "xlabel_right": "退休稅階(當前 = 24%)",
        "ylabel":       "65 歲稅後財富",
        "label_roth":  "Roth",
        "label_trad":  "傳統",
        "annot_parity": "各稅階皆相等\n(代數恆等)",
        "annot_trad_wins": "退休稅階較低時\n傳統勝",
        "annot_roth_wins": "退休稅階較高時\nRoth 勝",
        "footer": "Roth = 稅後元 x FV。傳統 = 稅後元/(1 - t_now) x FV x (1 - t_ret)。當 t_now = t_ret 時相等。",
    },
    "tw": {
        "title":    "Roth vs 傳統 - 65 歲稅後終值",
        "subtitle": "每年 $7,000 等稅後成本,30 年 7% 成長。當前稅階 = 退休稅階時兩者完全相等。",
        "left_title":  "平價情境:當前稅階 = 退休稅階",
        "right_title": "分歧情境:當前稅階固定 24%",
        "xlabel_left":  "稅階(當前 = 退休)",
        "xlabel_right": "退休稅階(當前 = 24%)",
        "ylabel":       "65 歲稅後財富",
        "label_roth":  "Roth",
        "label_trad":  "傳統",
        "annot_parity": "各稅階皆相等\n(代數恆等)",
        "annot_trad_wins": "退休稅階較低時\n傳統勝",
        "annot_roth_wins": "退休稅階較高時\nRoth 勝",
        "footer": "Roth = 稅後元 x FV。傳統 = 稅後元/(1 - t_now) x FV x (1 - t_ret)。當 t_now = t_ret 時相等。",
    },
    "cn": {
        "title":    "Roth vs 传统 - 65 岁税后终值",
        "subtitle": "每年 $7,000 等税后成本,30 年 7% 增长。当前税阶 = 退休税阶时两者完全相等。",
        "left_title":  "平价情境:当前税阶 = 退休税阶",
        "right_title": "分歧情境:当前税阶固定 24%",
        "xlabel_left":  "税阶(当前 = 退休)",
        "xlabel_right": "退休税阶(当前 = 24%)",
        "ylabel":       "65 岁税后财富",
        "label_roth":  "Roth",
        "label_trad":  "传统",
        "annot_parity": "各税阶皆相等\n(代数恒等)",
        "annot_trad_wins": "退休税阶较低时\n传统胜",
        "annot_roth_wins": "退休税阶较高时\nRoth 胜",
        "footer": "Roth = 税后元 x FV。传统 = 税后元/(1 - t_now) x FV x (1 - t_ret)。当 t_now = t_ret 时相等。",
    },
}


def build_fig(s):
    # Escape $ to avoid matplotlib mathtext mode that breaks CJK glyphs.
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v)
         for k, v in s.items()}
    p = PALETTE_LIGHT
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 6.4), dpi=150,
                                    gridspec_kw={"width_ratios": [1.05, 1.0]})

    # ----- Left panel: parity -----
    n = len(PARITY_BRACKETS)
    x = np.arange(n)
    bw = 0.36
    roth_vals = [roth_end(t) for t in PARITY_BRACKETS]
    trad_vals = [trad_end(t, t) for t in PARITY_BRACKETS]

    axL.bar(x - bw / 2, [v / 1000 for v in roth_vals], bw,
            color=p["blue"], edgecolor=p["fg"], linewidth=0.8,
            label=s["label_roth"], zorder=3)
    axL.bar(x + bw / 2, [v / 1000 for v in trad_vals], bw,
            color=p["accent"], edgecolor=p["fg"], linewidth=0.8,
            label=s["label_trad"], zorder=3)

    # Value labels on top of each bar.
    for xi, v in zip(x - bw / 2, roth_vals):
        axL.text(xi, v / 1000 + 18, f"\\${v/1000:.0f}k", ha="center",
                 va="bottom", fontsize=9, color=p["fg"], weight="bold")
    for xi, v in zip(x + bw / 2, trad_vals):
        axL.text(xi, v / 1000 + 18, f"\\${v/1000:.0f}k", ha="center",
                 va="bottom", fontsize=9, color=p["fg"], weight="bold")

    axL.set_xticks(x)
    axL.set_xticklabels([f"{int(t*100)}%" for t in PARITY_BRACKETS])
    axL.set_xlabel(s["xlabel_left"], fontsize=10.5)
    axL.set_ylabel(s["ylabel"] + " ($k)", fontsize=10.5)
    axL.set_title(s["left_title"], fontsize=12.5, weight="bold", pad=10)
    axL.legend(loc="upper right", frameon=False, fontsize=10)
    style_axes(axL)
    axL.set_ylim(0, max(roth_vals + trad_vals) / 1000 * 1.18)

    # Annotation centred on the chart.
    axL.text(1.5, max(roth_vals) / 1000 * 0.45,
             s["annot_parity"], ha="center", va="center",
             fontsize=10, color=p["green"], weight="bold",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor=p["bg"], edgecolor=p["green"], lw=1.0),
             zorder=10)

    # ----- Right panel: divergence -----
    nR = len(DIV_T_RETS)
    xR = np.arange(nR)
    bwR = 0.36
    roth_R = [roth_end(DIV_T_NOW) for _ in DIV_T_RETS]
    trad_R = [trad_end(DIV_T_NOW, t) for t in DIV_T_RETS]

    axR.bar(xR - bwR / 2, [v / 1000 for v in roth_R], bwR,
            color=p["blue"], edgecolor=p["fg"], linewidth=0.8,
            label=s["label_roth"], zorder=3)
    axR.bar(xR + bwR / 2, [v / 1000 for v in trad_R], bwR,
            color=p["accent"], edgecolor=p["fg"], linewidth=0.8,
            label=s["label_trad"], zorder=3)

    for xi, v in zip(xR - bwR / 2, roth_R):
        axR.text(xi, v / 1000 + 18, f"\\${v/1000:.0f}k", ha="center",
                 va="bottom", fontsize=9, color=p["fg"], weight="bold")
    for xi, v in zip(xR + bwR / 2, trad_R):
        axR.text(xi, v / 1000 + 18, f"\\${v/1000:.0f}k", ha="center",
                 va="bottom", fontsize=9, color=p["fg"], weight="bold")

    axR.set_xticks(xR)
    axR.set_xticklabels([f"{int(t*100)}%" for t in DIV_T_RETS])
    axR.set_xlabel(s["xlabel_right"], fontsize=10.5)
    axR.set_ylabel(s["ylabel"] + " ($k)", fontsize=10.5)
    axR.set_title(s["right_title"], fontsize=12.5, weight="bold", pad=10)
    axR.legend(loc="upper right", frameon=False, fontsize=10,
               bbox_to_anchor=(1.0, 1.04))
    style_axes(axR)
    axR.set_ylim(0, max(roth_R + trad_R) / 1000 * 1.32)

    # Highlight winning side per group with text below the higher bar tip.
    ymax = max(roth_R + trad_R) / 1000
    axR.text(0.0, trad_R[0] / 1000 + 60,
             s["annot_trad_wins"], ha="center", va="bottom",
             fontsize=8.8, color=p["accent"], weight="bold")
    axR.text(2.0, roth_R[2] / 1000 + 60,
             s["annot_roth_wins"], ha="center", va="bottom",
             fontsize=8.8, color=p["blue"], weight="bold")

    fig.suptitle(s["title"], fontsize=15, weight="bold", y=0.995,
                 color=p["fg"])
    fig.text(0.5, 0.945, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.4,
             color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
