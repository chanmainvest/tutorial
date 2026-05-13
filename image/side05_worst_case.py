"""Side Lesson 5 - 2008 worst-case lump vs. DCA, 2-panel chart.

Embedded ^GSPC monthly total-return-equivalent for 2008 (Jan to end-Dec).
Source: Yahoo Finance ^GSPC adjusted-close monthly returns. Numbers
match the canonical 2008 calendar reported in every reference text.

Run:
    uv run python course/image/side05_worst_case.py
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
BASE = "side05_worst_case"

# Monthly returns of S&P 500 in 2008 (adjusted close, ^GSPC).
# Jan ... Dec
SP500_2008 = [
    -0.0608, -0.0348, -0.0060,  0.0475,  0.0107, -0.0860,
    -0.0099,  0.0122, -0.0908, -0.1694, -0.0748,  0.0078,
]
# Cumulative product end of year ~ 0.620 -> -38% lump.
# DCA with $10k/month, cash earns 0:
# tranche k invested at start of month k (1..12), grows over remaining months k..12.

MONTH_LABELS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


def _wealth_paths(lump: float = 120000.0, dca_amt: float = 10000.0):
    """Return (lump_curve[0..12], dca_curve[0..12]) — wealth at end of each month."""
    rets = np.array(SP500_2008)
    # Lump: starts at 120k, multiplies by (1+r) each month.
    lump_curve = np.empty(13)
    lump_curve[0] = lump
    for i in range(12):
        lump_curve[i + 1] = lump_curve[i] * (1.0 + rets[i])

    # DCA: invested portion grows; cash portion sits at 0%.
    # invested_value: value of shares already bought. cash_remaining: untouched.
    invested = 0.0
    cash = lump  # set cash = total target, deploy 10k each month-start
    dca_curve = np.empty(13)
    dca_curve[0] = lump  # all cash on day 0
    for i in range(12):
        # At start of month i+1: invest 10k from cash.
        if cash >= dca_amt - 1e-6:
            invested += dca_amt
            cash -= dca_amt
        # Then market moves over month i.
        invested *= (1.0 + rets[i])
        dca_curve[i + 1] = invested + cash
    return lump_curve, dca_curve


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    lump_c, dca_c = _wealth_paths()
    months = np.arange(13)  # 0..12

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4), dpi=150,
                             gridspec_kw={"width_ratios": [1.35, 1.0]})

    # --- LEFT: wealth curves ---
    ax = axes[0]
    style_axes(ax, p)
    ax.plot(months, lump_c / 1000.0, color=p["red"], linewidth=2.6,
            marker="o", markersize=4, label=s["lump_label"])
    ax.plot(months, dca_c / 1000.0, color=p["blue"], linewidth=2.6,
            marker="s", markersize=4, label=s["dca_label"])
    ax.axhline(120, color=p["muted"], linewidth=0.8, linestyle=":")
    ax.set_xticks(months[::2])
    ax.set_xticklabels(["Start"] + MONTH_LABELS[1::2])
    ax.set_xlabel(s["x_left"])
    ax.set_ylabel(s["y_left"])
    ax.set_title(s["title_left"], pad=14, fontsize=12, fontweight="bold", loc="left")
    ax.legend(loc="lower left", frameon=False, fontsize=10)

    # End-of-year annotations
    lump_end_pct = (lump_c[-1] / lump_c[0] - 1) * 100
    dca_end_pct = (dca_c[-1] / 120000 - 1) * 100  # vs total target
    ax.annotate(f"{s['lump_label']}: {lump_end_pct:+.1f}%\n{lump_c[-1]/1000:.1f}k",
                xy=(12, lump_c[-1]/1000), xytext=(8.0, 60),
                fontsize=9.5, color=p["red"], ha="left",
                arrowprops=dict(arrowstyle="-", color=p["red"], lw=0.7))
    ax.annotate(f"{s['dca_label']}: {dca_end_pct:+.1f}%\n{dca_c[-1]/1000:.1f}k",
                xy=(12, dca_c[-1]/1000), xytext=(8.0, 105),
                fontsize=9.5, color=p["blue"], ha="left",
                arrowprops=dict(arrowstyle="-", color=p["blue"], lw=0.7))

    # --- RIGHT: cumulative S&P 500 level (price index) showing where each DCA tranche bought
    ax2 = axes[1]
    style_axes(ax2, p)
    spx = np.empty(13)
    spx[0] = 1.0
    for i in range(12):
        spx[i + 1] = spx[i] * (1.0 + SP500_2008[i])
    ax2.plot(months, spx, color=p["fg"], linewidth=2.0, label=s["spx_label"])
    # Buy markers for DCA at start of each month: tranche bought at price spx[i]
    buy_xs = list(range(12))
    buy_ys = [spx[i] for i in buy_xs]
    ax2.scatter(buy_xs, buy_ys, s=70, color=p["blue"], zorder=5,
                edgecolor=p["bg"], linewidth=1.2, label=s["dca_buys"])
    # Lump buy at month 0
    ax2.scatter([0], [spx[0]], s=140, color=p["red"], marker="*", zorder=6,
                edgecolor=p["bg"], linewidth=1.2, label=s["lump_buy"])

    avg_dca_basis = np.mean(buy_ys)
    ax2.axhline(avg_dca_basis, color=p["blue"], linewidth=0.8, linestyle="--", alpha=0.7)
    ax2.text(11.7, avg_dca_basis, f" {s['avg_basis']}: {avg_dca_basis:.3f}",
             color=p["blue"], fontsize=8.5, va="bottom", ha="right")
    ax2.text(0.2, 1.0, f" {s['lump_basis']}: 1.000",
             color=p["red"], fontsize=8.5, va="bottom")

    ax2.set_xticks(months[::2])
    ax2.set_xticklabels(["Start"] + MONTH_LABELS[1::2])
    ax2.set_xlabel(s["x_right"])
    ax2.set_ylabel(s["y_right"])
    ax2.set_title(s["title_right"], pad=14, fontsize=12, fontweight="bold", loc="left")
    ax2.legend(loc="lower left", frameon=False, fontsize=8.5)

    fig.suptitle(s["title"], fontsize=14, fontweight="bold", y=1.00)
    fig.text(0.5, 0.955, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"])
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    return fig


LANG_STRINGS = {
    "en": {
        "title":    "2008 entry: lump-sum vs. DCA over 12 months",
        "subtitle": "$120k deployed Jan-2 2008. Lump = -38%. DCA ($10k x 12, cash earns 0%) = -19%. Average DCA cost basis ~20% below lump's.",
        "title_left":  "Wealth path through 2008",
        "title_right": "S&P 500 in 2008: where each DCA tranche bought",
        "x_left":  "Months from start",
        "y_left":  "Account value ($k)",
        "x_right": "Months from start",
        "y_right": "S&P 500 (Jan 2 = 1.000)",
        "lump_label": "Lump-sum",
        "dca_label":  "DCA",
        "spx_label":  "S&P 500 path",
        "dca_buys":   "DCA buys (12)",
        "lump_buy":   "Lump buy (1)",
        "avg_basis":  "DCA avg basis",
        "lump_basis": "Lump basis",
    },
    "hk": {
        "title":    "2008 進場:12 個月一筆過 vs 平均成本法",
        "subtitle": "12 萬於 2008 年 1 月 2 日部署。一筆過 = -38%。平均成本法(每月 1 萬,共 12 期,現金 0%)= -19%。平均成本法成本基礎較一筆過低約 20%。",
        "title_left":  "2008 年資產淨值路徑",
        "title_right": "2008 年標普 500:每筆平均成本法買入點",
        "x_left":  "距離起始月份數",
        "y_left":  "帳戶價值(千元)",
        "x_right": "距離起始月份數",
        "y_right": "標普 500(1 月 2 日 = 1.000)",
        "lump_label": "一筆過",
        "dca_label":  "平均成本法",
        "spx_label":  "標普 500 走勢",
        "dca_buys":   "平均成本法買入(12 次)",
        "lump_buy":   "一筆過買入(1 次)",
        "avg_basis":  "平均成本法均價",
        "lump_basis": "一筆過成本",
    },
    "tw": {
        "title":    "2008 進場:12 個月一次投入 vs 定期定額",
        "subtitle": "12 萬於 2008 年 1 月 2 日部署。一次投入 = -38%。定期定額(每月 1 萬,共 12 期,現金 0%)= -19%。定期定額平均成本較一次投入低約 20%。",
        "title_left":  "2008 年資產淨值路徑",
        "title_right": "2008 年標普 500:每筆定期定額買入點",
        "x_left":  "距離起始月份數",
        "y_left":  "帳戶價值(千元)",
        "x_right": "距離起始月份數",
        "y_right": "標普 500(1 月 2 日 = 1.000)",
        "lump_label": "一次投入",
        "dca_label":  "定期定額",
        "spx_label":  "標普 500 走勢",
        "dca_buys":   "定期定額買入(12 次)",
        "lump_buy":   "一次投入買入(1 次)",
        "avg_basis":  "定期定額均價",
        "lump_basis": "一次投入成本",
    },
    "cn": {
        "title":    "2008 进场:12 个月一次性投入 vs 定投",
        "subtitle": "12 万于 2008 年 1 月 2 日部署。一次性 = -38%。定投(每月 1 万,共 12 期,现金 0%)= -19%。定投平均成本较一次性低约 20%。",
        "title_left":  "2008 年资产净值路径",
        "title_right": "2008 年标普 500:每笔定投买入点",
        "x_left":  "距离起始月份数",
        "y_left":  "账户价值(千元)",
        "x_right": "距离起始月份数",
        "y_right": "标普 500(1 月 2 日 = 1.000)",
        "lump_label": "一次性",
        "dca_label":  "定投",
        "spx_label":  "标普 500 走势",
        "dca_buys":   "定投买入(12 次)",
        "lump_buy":   "一次性买入(1 次)",
        "avg_basis":  "定投均价",
        "lump_basis": "一次性成本",
    },
}


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
