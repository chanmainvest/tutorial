"""Week 7, §2.2 — Rebalancing-method comparison on 60/40 1928-2024.

Four policies on the Damodaran annual dataset:
  - Never rebalance (buy and hold)
  - Annual rebalance
  - Semi-annual rebalance (each annual return split into two equal
    geometric halves; rebalance after each half)
  - 5%-band threshold (annual check; rebalance only if the stock weight
    has drifted >=5pp from the 60% target)

Three side-by-side bar groups: geometric annualised return, realised
volatility (annual), max drawdown.

Run:
    uv run python course/image/week07_method_comparison.py
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
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week07_method_comparison"

TARGET = 0.60
BAND = 0.05  # 5pp absolute band

LANG_STRINGS = {
    "en": {
        "title":    "Rebalancing methods on 60/40, 1928-2024",
        "subtitle": "Geometric annualised return, realised volatility, and max drawdown for four policies. Risk falls; return is essentially flat across the rebalanced policies.",
        "methods":  ["Never", "Annual", "Semi-annual", "5% band"],
        "ret":      "Geo. ann. return",
        "vol":      "Annual volatility",
        "dd":       "Max drawdown",
        "footer":   "Damodaran 1928-2024 annual data. Drawdown computed on annual end-of-year wealth path.",
    },
    "hk": {
        "title":    "60/40 不同再平衡規則:1928-2024",
        "subtitle": "幾何年化回報、實現波幅及最大回撤的對比。再平衡規則之間幾乎沒有回報差,但風險明顯下降。",
        "methods":  ["從不", "每年", "每半年", "5% 帶"],
        "ret":      "幾何年化回報",
        "vol":      "年化波幅",
        "dd":       "最大回撤",
        "footer":   "Damodaran 1928-2024 年度數據,回撤以年末財富路徑計算。",
    },
    "tw": {
        "title":    "60/40 不同再平衡規則:1928-2024",
        "subtitle": "幾何年化報酬、實現波動度及最大回檔的對比。再平衡規則之間幾乎沒有報酬差,但風險明顯下降。",
        "methods":  ["從不", "每年", "每半年", "5% 帶"],
        "ret":      "幾何年化報酬",
        "vol":      "年化波動度",
        "dd":       "最大回檔",
        "footer":   "Damodaran 1928-2024 年度資料,回檔以年末財富路徑計算。",
    },
    "cn": {
        "title":    "60/40 不同再平衡规则:1928-2024",
        "subtitle": "几何年化回报、实现波动率及最大回撤的对比。再平衡规则之间几乎没有回报差,但风险明显下降。",
        "methods":  ["从不", "每年", "每半年", "5% 带"],
        "ret":      "几何年化回报",
        "vol":      "年化波动率",
        "dd":       "最大回撤",
        "footer":   "Damodaran 1928-2024 年度数据,回撤以年末财富路径计算。",
    },
}


def _simulate(sp: np.ndarray, bd: np.ndarray, method: str):
    """Return (port_returns, end_stock_weight) given annual sp/bd returns."""
    n = len(sp)
    s = TARGET
    b = 1 - TARGET
    rets = np.zeros(n)
    if method == "never":
        for i in range(n):
            new_s = s * (1 + sp[i])
            new_b = b * (1 + bd[i])
            tot = new_s + new_b
            rets[i] = tot - 1.0
            s, b = new_s, new_b
            # carry as fractions of *original* dollar-1, so re-express
            tot_val = s + b
            s = s / 1.0  # leave absolute; we only need rets and ratios
            # rebuild as weights normalised to 1 each year for next-year math? No — keep absolute path.
        # rebuild: simulate once more cleanly
        s_v, b_v = TARGET, 1 - TARGET
        rets = []
        for i in range(n):
            s_v *= (1 + sp[i])
            b_v *= (1 + bd[i])
            # Save 1-yr return = total / prev_total - 1
        # use simple total wealth log
        wealth = np.zeros(n + 1)
        wealth[0] = 1.0
        s_v, b_v = TARGET, 1 - TARGET
        for i in range(n):
            s_v *= (1 + sp[i])
            b_v *= (1 + bd[i])
            wealth[i + 1] = s_v + b_v
        rets = wealth[1:] / wealth[:-1] - 1.0
        end_w = s_v / (s_v + b_v)
        return rets, wealth, end_w

    if method == "annual":
        wealth = np.zeros(n + 1)
        wealth[0] = 1.0
        for i in range(n):
            r = TARGET * sp[i] + (1 - TARGET) * bd[i]
            wealth[i + 1] = wealth[i] * (1 + r)
        rets = wealth[1:] / wealth[:-1] - 1.0
        return rets, wealth, TARGET

    if method == "semi":
        # split each annual return into two halves geometrically:
        # (1 + r)^0.5 - 1 each half. Rebalance after each half.
        wealth = np.zeros(n + 1)
        wealth[0] = 1.0
        for i in range(n):
            sp_h = (1 + sp[i]) ** 0.5 - 1
            bd_h = (1 + bd[i]) ** 0.5 - 1
            r1 = TARGET * sp_h + (1 - TARGET) * bd_h
            # second half — rebalance, so identical formula
            r2 = TARGET * sp_h + (1 - TARGET) * bd_h
            wealth[i + 1] = wealth[i] * (1 + r1) * (1 + r2)
        rets = wealth[1:] / wealth[:-1] - 1.0
        return rets, wealth, TARGET

    if method == "band":
        wealth = np.zeros(n + 1)
        wealth[0] = 1.0
        s_v, b_v = TARGET, 1 - TARGET
        end_w = TARGET
        for i in range(n):
            s_v *= (1 + sp[i])
            b_v *= (1 + bd[i])
            tot = s_v + b_v
            w = s_v / tot
            if abs(w - TARGET) >= BAND:
                s_v = tot * TARGET
                b_v = tot * (1 - TARGET)
                w = TARGET
            wealth[i + 1] = tot
            end_w = w
        rets = wealth[1:] / wealth[:-1] - 1.0
        return rets, wealth, end_w

    raise ValueError(method)


def _stats(rets: np.ndarray, wealth: np.ndarray):
    n = len(rets)
    geo = wealth[-1] ** (1 / n) - 1
    vol = float(np.std(rets, ddof=1))
    peaks = np.maximum.accumulate(wealth)
    dd = float((wealth / peaks - 1).min())
    return geo, vol, dd


def _compute_all():
    df = damodaran_annual_returns()
    sp = df["SP500"].to_numpy()
    bd = df["TBond10Y"].to_numpy()
    methods = ["never", "annual", "semi", "band"]
    out = {}
    for m in methods:
        rets, wealth, end_w = _simulate(sp, bd, m)
        geo, vol, dd = _stats(rets, wealth)
        out[m] = (geo, vol, dd, end_w)
    return out


def build_fig(s):
    p = PALETTE_LIGHT
    res = _compute_all()
    methods = ["never", "annual", "semi", "band"]
    geos = [res[m][0] for m in methods]
    vols = [res[m][1] for m in methods]
    dds = [-res[m][2] for m in methods]  # plot magnitude of drawdown

    fig, axes = plt.subplots(1, 3, figsize=(11, 5.4))
    fig.set_facecolor(p["bg"])

    titles = [s["ret"], s["vol"], s["dd"]]
    series = [geos, vols, dds]
    colors = [p["accent"], p["blue"], p["red"]]

    for ax, ttl, vals, col in zip(axes, titles, series, colors):
        style_axes(ax, p)
        bars = ax.bar(s["methods"], vals, color=col, alpha=0.85,
                      edgecolor=p["fg"], linewidth=0.6)
        ax.set_title(ttl, fontsize=11, color=p["fg"], pad=10)
        ax.set_ylim(0, max(vals) * 1.18)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height(), f"{v*100:.1f}%",
                    ha="center", va="bottom", fontsize=9.5,
                    color=p["fg"], fontweight="bold")
        ax.tick_params(axis="x", labelsize=9)

    fig.suptitle(s["title"], fontsize=13, fontweight="bold", x=0.05, ha="left", y=0.985)
    fig.text(0.05, 0.94, s["subtitle"], fontsize=10, color=p["muted"])
    fig.text(0.05, 0.02, s["footer"], fontsize=8.5, color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
