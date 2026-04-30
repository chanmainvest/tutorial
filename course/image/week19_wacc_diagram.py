"""Week 19, §2.3 — WACC schematic: low-leverage tech vs. high-leverage utility.

Two example firms, identical formula, very different blended cost of
capital. Stacked horizontal bars show each weighted contribution
(equity component + post-tax debt component), and a totals bar
shows the resulting WACC.

Tech (low leverage):
    E/V = 90%, rE = 11%, D/V = 10%, rD = 5%, t = 25%
    WACC = 0.90 * 11% + 0.10 * 5% * 0.75 = 9.90% + 0.375% = 10.275%

Utility (high leverage):
    E/V = 50%, rE = 8%, D/V = 50%, rD = 5%, t = 25%
    WACC = 0.50 * 8% + 0.50 * 5% * 0.75 = 4.00% + 1.875% = 5.875%

Run:
    uv run python course/image/week19_wacc_diagram.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week19_wacc_diagram"


FIRMS = [
    # (key, E/V, rE, D/V, rD, tax)
    ("tech",    0.90, 0.11, 0.10, 0.05, 0.25),
    ("utility", 0.50, 0.08, 0.50, 0.05, 0.25),
]


def _components(ev, re, dv, rd, t):
    eq = ev * re
    dt = dv * rd * (1 - t)
    return eq, dt, eq + dt


LANG_STRINGS = {
    "en": {
        "title":    "WACC = E/V * rE + D/V * rD * (1 - t)",
        "subtitle": "Same formula, two very different firms. The utility's heavier debt and lower equity risk produce a much lower blended cost of capital.",
        "xlabel":   "Weighted contribution (% per year)",
        "tech":     "Low-leverage tech\nE/V 90%, rE 11%\nD/V 10%, rD 5%, t 25%",
        "utility":  "High-leverage utility\nE/V 50%, rE 8%\nD/V 50%, rD 5%, t 25%",
        "eq_lab":   "Equity component (E/V * rE)",
        "dt_lab":   "Post-tax debt component (D/V * rD * (1-t))",
        "tot_lab":  "Total WACC",
        "footer":   "Tech WACC = 9.90% + 0.38% = 10.28%   |   Utility WACC = 4.00% + 1.88% = 5.88%   |   Project hurdle is the WACC, not the cost of equity.",
    },
    "hk": {
        "title":    "WACC = E/V x rE + D/V x rD x (1 - t)",
        "subtitle": "同一條公式,兩家迥異的公司。公用事業負債較高、權益風險較低,加權平均資金成本明顯更低。",
        "xlabel":   "加權貢獻(每年 %)",
        "tech":     "低槓桿科技股\nE/V 90%、rE 11%\nD/V 10%、rD 5%、稅 25%",
        "utility":  "高槓桿公用股\nE/V 50%、rE 8%\nD/V 50%、rD 5%、稅 25%",
        "eq_lab":   "股權部分(E/V x rE)",
        "dt_lab":   "稅後債務部分(D/V x rD x (1-t))",
        "tot_lab":  "總 WACC",
        "footer":   "科技 WACC = 9.90% + 0.38% = 10.28%   |   公用 WACC = 4.00% + 1.88% = 5.88%   |   投資項目的門檻是 WACC,不是 rE。",
    },
    "tw": {
        "title":    "WACC = E/V x rE + D/V x rD x (1 - t)",
        "subtitle": "同一條公式,兩家迥異的公司。公用事業負債較高、權益風險較低,加權平均資金成本明顯更低。",
        "xlabel":   "加權貢獻(每年 %)",
        "tech":     "低槓桿科技股\nE/V 90%、rE 11%\nD/V 10%、rD 5%、稅 25%",
        "utility":  "高槓桿公用股\nE/V 50%、rE 8%\nD/V 50%、rD 5%、稅 25%",
        "eq_lab":   "股權部分(E/V x rE)",
        "dt_lab":   "稅後債務部分(D/V x rD x (1-t))",
        "tot_lab":  "總 WACC",
        "footer":   "科技 WACC = 9.90% + 0.38% = 10.28%   |   公用 WACC = 4.00% + 1.88% = 5.88%   |   投資專案的門檻是 WACC,不是 rE。",
    },
    "cn": {
        "title":    "WACC = E/V x rE + D/V x rD x (1 - t)",
        "subtitle": "同一条公式,两家迥异的公司。公用事业负债较高、权益风险较低,加权平均资金成本明显更低。",
        "xlabel":   "加权贡献(每年 %)",
        "tech":     "低杠杆科技股\nE/V 90%、rE 11%\nD/V 10%、rD 5%、税 25%",
        "utility":  "高杠杆公用股\nE/V 50%、rE 8%\nD/V 50%、rD 5%、税 25%",
        "eq_lab":   "股权部分(E/V x rE)",
        "dt_lab":   "税后债务部分(D/V x rD x (1-t))",
        "tot_lab":  "总 WACC",
        "footer":   "科技 WACC = 9.90% + 0.38% = 10.28%   |   公用 WACC = 4.00% + 1.88% = 5.88%   |   投资项目的门槛是 WACC,不是 rE。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.2, 6.0))
    style_axes(ax, p)

    # Two firms x two stacked rows: stacked component bar + total bar
    # Y positions: tech components at y=4.0, tech total at 3.0
    #              utility components at 1.5, utility total at 0.5
    rows = []
    for offset_idx, (key, ev, re, dv, rd, t) in enumerate(FIRMS):
        eq, dt, tot = _components(ev, re, dv, rd, t)
        # tech is offset_idx=0 -> place at top (higher y)
        y_comp = 3.5 - offset_idx * 2.5
        y_tot = y_comp - 1.0
        rows.append((key, y_comp, y_tot, eq * 100, dt * 100, tot * 100))

    # Plot stacked component bars
    for key, y_comp, y_tot, eq, dt, tot in rows:
        ax.barh(y_comp, eq, color=p["blue"], height=0.55,
                edgecolor=p["blue"], alpha=0.92)
        ax.barh(y_comp, dt, left=eq, color=p["accent"], height=0.55,
                edgecolor=p["accent"], alpha=0.92)
        # Component value labels
        ax.text(eq / 2, y_comp, f"{eq:.2f}%", va="center", ha="center",
                color="white", fontsize=10, fontweight="bold")
        if dt > 0.25:
            ax.text(eq + dt / 2, y_comp, f"{dt:.2f}%",
                    va="center", ha="center",
                    color="white", fontsize=9, fontweight="bold")
        else:
            ax.text(eq + dt + 0.25, y_comp, f"{dt:.2f}%",
                    va="center", ha="left",
                    color=p["accent"], fontsize=9, fontweight="bold")
        # Total bar
        ax.barh(y_tot, tot, color=p["green"], height=0.55,
                edgecolor=p["green"], alpha=0.92)
        ax.text(tot + 0.2, y_tot, f"WACC {tot:.2f}%",
                va="center", ha="left",
                color=p["green"], fontsize=11, fontweight="bold")

    # Y-axis labels: each firm gets a left label spanning its two rows
    ytick_positions = []
    ytick_labels = []
    for key, y_comp, y_tot, *_ in rows:
        ytick_positions.append(y_comp)
        ytick_labels.append(s[key])
        ytick_positions.append(y_tot)
        ytick_labels.append(s["tot_lab"])

    ax.set_yticks(ytick_positions)
    ax.set_yticklabels(ytick_labels, fontsize=9)
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_xlim(0, 13.5)
    ax.set_ylim(-0.4, 4.4)

    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.04, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Legend (manual rectangles via proxy artists)
    from matplotlib.patches import Patch
    legend_handles = [
        Patch(facecolor=p["blue"], label=s["eq_lab"]),
        Patch(facecolor=p["accent"], label=s["dt_lab"]),
        Patch(facecolor=p["green"], label=s["tot_lab"]),
    ]
    ax.legend(handles=legend_handles, loc="lower right",
              frameon=False, fontsize=9)

    ax.text(0, -0.18, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["muted"])

    fig.tight_layout(rect=[0, 0.03, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
