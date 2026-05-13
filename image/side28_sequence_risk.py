"""Side Lesson 28 - Sequence-of-returns risk: same mean, two orderings.

Two retirees, both starting with $1M, both withdrawing $40k/yr (4% rule),
both experiencing the SAME 30 annual returns but in opposite orderings.

Sequence A: bad first decade (avg -5%/yr), then 20y of +13%/yr -> ruins
            around year 24.
Sequence B: reversed - 20y of +13%/yr first, then bad decade -5% at end
            -> finishes with multi-million-dollar wealth.

Both have arithmetic mean return = 7.0% over 30 years.

Run:
    uv run python course/image/side28_sequence_risk.py
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
BASE = "side28_sequence_risk"

W0 = 1_000_000.0
WITHDRAWAL = 40_000.0  # per year, start-of-year

# Bad-decade returns (avg -5%/yr) and good-decades returns (+13%/yr).
BAD_DECADE = [-0.20, -0.10, -0.05, 0.00, 0.05, -0.08, 0.02, 0.08, -0.05, 0.03]
# 20 years averaging +13%
GOOD_TWENTY = [0.18, 0.10, 0.15, 0.08, 0.20, 0.05, 0.18, 0.12, 0.16, 0.09,
               0.14, 0.20, 0.06, 0.18, 0.10, 0.15, 0.13, 0.17, 0.11, 0.15]
# Sequence A: bad first 10y, good 20y
SEQ_A = BAD_DECADE + GOOD_TWENTY
# Sequence B: good 20y first, then bad 10y at end
SEQ_B = GOOD_TWENTY + BAD_DECADE

assert abs(np.mean(SEQ_A) - np.mean(SEQ_B)) < 1e-12, "Means must match"


def _path(returns, w0=W0, wd=WITHDRAWAL):
    """Withdraw at start of year, then grow by returns[t]."""
    w = [w0]
    for r in returns:
        cur = w[-1]
        if cur <= 0:
            w.append(0.0)
            continue
        after_wd = cur - wd
        if after_wd <= 0:
            w.append(0.0)
            continue
        w.append(after_wd * (1 + r))
    return np.array(w)


LANG_STRINGS = {
    "en": {
        "title":    "Sequence-of-returns risk: same 7% average, opposite orderings",
        "subtitle": "Both retirees: $1M start, $40k/yr withdrawal, identical 30 returns. Order alone produces ruin vs. dynastic wealth.",
        "xlabel":   "Years into retirement",
        "ylabel":   "Account value (USD millions)",
        "seq_a":    "Sequence A: bad decade first",
        "seq_b":    "Sequence B: bad decade last",
        "ruin":     "Sequence A: ruin year {y}",
        "endb":     "Sequence B: ${v}M ending wealth",
        "panelA":   "PANEL A - WEALTH PATH",
        "panelB":   "PANEL B - ANNUAL RETURNS",
        "yr_label": "Year",
        "ret_label":"Return %",
        "footer":   "Identical 30-year arithmetic-mean return. Same withdrawals. Calendar order alone destroys one and enriches the other.",
        "mean_box": "Mean return = 7.0% (both)",
    },
    "hk": {
        "title":    "回報順序風險:相同 7% 平均,相反排序",
        "subtitle": "兩位退休者:100 萬起點,每年提取 4 萬,30 個年度回報完全相同。順序就能造成破產 vs 家族財富。",
        "xlabel":   "退休後年數",
        "ylabel":   "戶口價值(百萬美元)",
        "seq_a":    "序列 A:壞十年在前",
        "seq_b":    "序列 B:壞十年在後",
        "ruin":     "序列 A:第 {y} 年破產",
        "endb":     "序列 B:終值 ${v}M",
        "panelA":   "面板 A - 財富走勢",
        "panelB":   "面板 B - 年度回報",
        "yr_label": "年份",
        "ret_label":"回報 %",
        "footer":   "30 年算術平均回報相同,提款相同。日曆順序就足以毀掉一個並豐富另一個。",
        "mean_box": "平均回報 = 7.0%(兩者)",
    },
    "tw": {
        "title":    "報酬順序風險:相同 7% 平均,相反排序",
        "subtitle": "兩位退休者:100 萬起點,每年提領 4 萬,30 個年度報酬完全相同。順序就能造成破產 vs 家族財富。",
        "xlabel":   "退休後年數",
        "ylabel":   "帳戶價值(百萬美元)",
        "seq_a":    "序列 A:壞十年在前",
        "seq_b":    "序列 B:壞十年在後",
        "ruin":     "序列 A:第 {y} 年破產",
        "endb":     "序列 B:終值 ${v}M",
        "panelA":   "面板 A - 財富走勢",
        "panelB":   "面板 B - 年度報酬",
        "yr_label": "年份",
        "ret_label":"報酬 %",
        "footer":   "30 年算術平均報酬相同,提領相同。日曆順序就足以毀掉一個並豐富另一個。",
        "mean_box": "平均報酬 = 7.0%(兩者)",
    },
    "cn": {
        "title":    "回报顺序风险:相同 7% 平均,相反排序",
        "subtitle": "两位退休者:100 万起点,每年提取 4 万,30 个年度回报完全相同。顺序就能造成破产 vs 家族财富。",
        "xlabel":   "退休后年数",
        "ylabel":   "账户价值(百万美元)",
        "seq_a":    "序列 A:坏十年在前",
        "seq_b":    "序列 B:坏十年在后",
        "ruin":     "序列 A:第 {y} 年破产",
        "endb":     "序列 B:终值 ${v}M",
        "panelA":   "面板 A - 财富走势",
        "panelB":   "面板 B - 年度回报",
        "yr_label": "年份",
        "ret_label":"回报 %",
        "footer":   "30 年算术平均回报相同,提款相同。日历顺序就足以毁掉一个并丰富另一个。",
        "mean_box": "平均回报 = 7.0%(两者)",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    path_a = _path(SEQ_A) / 1e6
    path_b = _path(SEQ_B) / 1e6
    years = np.arange(len(path_a))

    # Find ruin year for A (first index where balance hits 0)
    zero_idx = np.where(path_a <= 1e-6)[0]
    ruin_year = int(zero_idx[0]) if len(zero_idx) > 0 else None
    end_b = float(path_b[-1])

    fig, (axT, axB) = plt.subplots(
        2, 1, figsize=(11, 7.6), dpi=150,
        gridspec_kw={"height_ratios": [2.2, 1.0]},
    )
    style_axes(axT, p)
    style_axes(axB, p)

    # ---- Top panel: wealth paths ----
    axT.plot(years, path_a, color=p["red"], linewidth=2.6, label=s["seq_a"])
    axT.plot(years, path_b, color=p["green"], linewidth=2.6, label=s["seq_b"])
    axT.axhline(W0 / 1e6, color=p["muted"], linewidth=0.8, linestyle=":", alpha=0.6)
    axT.fill_between(years, path_a, 0, color=p["red"], alpha=0.10)

    if ruin_year is not None:
        axT.scatter([ruin_year], [0], color=p["red"], s=80, zorder=5, marker="X")
        axT.annotate(
            s["ruin"].format(y=ruin_year),
            xy=(ruin_year, 0), xytext=(ruin_year - 1, 1.5),
            ha="right", color=p["red"], fontsize=10.5, weight="bold",
            arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.2),
        )
    axT.annotate(
        s["endb"].format(v=f"{end_b:.1f}"),
        xy=(len(years) - 1, end_b),
        xytext=(len(years) - 6, end_b + 1.2),
        ha="right", color=p["green"], fontsize=10.5, weight="bold",
        arrowprops=dict(arrowstyle="->", color=p["green"], lw=1.2),
    )

    # Mean-return box
    axT.text(0.02, 0.97, s["mean_box"], transform=axT.transAxes,
             ha="left", va="top", fontsize=10, color=p["fg"], weight="bold",
             bbox=dict(boxstyle="round,pad=0.35", facecolor=p["bg"],
                       edgecolor=p["accent"], linewidth=1.2))

    axT.set_xlim(0, len(years) - 1)
    axT.set_ylim(0, max(path_b.max() * 1.1, 9))
    axT.set_ylabel(s["ylabel"], color=p["fg"])
    axT.set_xlabel("")
    axT.set_title(s["panelA"], loc="left", fontsize=10.5, color=p["muted"], pad=4)
    leg = axT.legend(loc="upper left", bbox_to_anchor=(0.02, 0.90), fontsize=10)
    leg.get_frame().set_edgecolor(p["grid"])

    # ---- Bottom panel: annual returns bars ----
    yrs_b = np.arange(1, 31)
    bw = 0.4
    axB.bar(yrs_b - bw / 2, [r * 100 for r in SEQ_A], width=bw, color=p["red"],
            alpha=0.8, label=s["seq_a"])
    axB.bar(yrs_b + bw / 2, [r * 100 for r in SEQ_B], width=bw, color=p["green"],
            alpha=0.8, label=s["seq_b"])
    axB.axhline(0, color=p["muted"], linewidth=0.8)
    axB.axhline(7.0, color=p["accent"], linewidth=1.0, linestyle="--", alpha=0.7)
    axB.text(30.4, 7.0, "7%", color=p["accent"], fontsize=9, va="center")
    axB.set_xlim(0, 31)
    axB.set_ylim(-25, 25)
    axB.set_xlabel(s["xlabel"], color=p["fg"])
    axB.set_ylabel(s["ret_label"], color=p["fg"])
    axB.set_title(s["panelB"], loc="left", fontsize=10.5, color=p["muted"], pad=4)

    fig.suptitle(s["title"], y=0.98, fontsize=14, weight="bold", color=p["fg"])
    fig.text(0.5, 0.935, s["subtitle"], ha="center", fontsize=10.5,
             color="#4a5568", style="italic")
    fig.text(0.5, 0.015, s["footer"], ha="center", fontsize=8.5,
             color=p["muted"], style="italic")

    fig.tight_layout(rect=[0, 0.03, 1, 0.91])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}.png + 4 locale variants to {OUT_DIR}")
