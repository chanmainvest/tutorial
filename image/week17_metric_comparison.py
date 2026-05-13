"""Week 17, §2.7 — Four metrics x four portfolios bar grid.

For each of {100/0, 60/40, 30/70, 0/100} stock-bond portfolios on
the Damodaran 1928-2024 annual dataset, compute Sharpe, Sortino,
Calmar, and Treynor. Render as a 2x2 bar grid so the rank-order
flips are visible at a glance.

Run:
    uv run python course/image/week17_metric_comparison.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week17_metric_comparison"

LANG_STRINGS = {
    "en": {
        "title":    "Four risk-adjusted metrics x four portfolios, 1928-2024",
        "subtitle": "Damodaran annual returns, S&P 500 + 10-year Treasury, annual rebalance. Same data, four different rankings.",
        "sharpe":   "Sharpe ratio",
        "sortino":  "Sortino ratio",
        "calmar":   "Calmar ratio",
        "treynor":  "Treynor ratio (x100)",
        "ports":    ["100/0", "60/40", "30/70", "0/100"],
        "footer":   "Sharpe favours diversified mixes; Calmar punishes 100/0 for the 1929-32 -82% drawdown; Treynor against S&P-beta is unstable for bond-heavy books.",
    },
    "hk": {
        "title":    "四個風險調整後指標 x 四個組合,1928-2024",
        "subtitle": "Damodaran 年度回報,標普 500 + 十年國債,每年再平衡。同一份數據,四種不同排序。",
        "sharpe":   "夏普比率",
        "sortino":  "索提諾比率",
        "calmar":   "卡馬爾比率",
        "treynor":  "崔諾比率 (x100)",
        "ports":    ["100/0", "60/40", "30/70", "0/100"],
        "footer":   "夏普偏好分散組合;卡馬爾因 1929-32 的 -82% 回撚重罰 100/0;對標普 beta 的崔諾比率,在偏債組合上不穩定。",
    },
    "tw": {
        "title":    "四個風險調整後指標 x 四個組合,1928-2024",
        "subtitle": "Damodaran 年度報酬,標普 500 + 十年公債,每年再平衡。同一份資料,四種不同排序。",
        "sharpe":   "夏普比率",
        "sortino":  "索提諾比率",
        "calmar":   "卡馬爾比率",
        "treynor":  "崔諾比率 (x100)",
        "ports":    ["100/0", "60/40", "30/70", "0/100"],
        "footer":   "夏普偏好分散組合;卡馬爾因 1929-32 的 -82% 回檔重罰 100/0;對標普 beta 的崔諾比率,在偏債組合上不穩定。",
    },
    "cn": {
        "title":    "四个风险调整后指标 x 四个组合,1928-2024",
        "subtitle": "Damodaran 年度回报,标普 500 + 十年国债,每年再平衡。同一份数据,四种不同排序。",
        "sharpe":   "夏普比率",
        "sortino":  "索提诺比率",
        "calmar":   "卡马尔比率",
        "treynor":  "特雷诺比率 (x100)",
        "ports":    ["100/0", "60/40", "30/70", "0/100"],
        "footer":   "夏普偏爱分散组合;卡马尔因 1929-32 的 -82% 回撚重罚 100/0;对标普 beta 的特雷诺,在偏债组合上不稳定。",
    },
}


def _portfolio_metrics(w_stock: float):
    df = damodaran_annual_returns()
    sp = df["SP500"].values
    bd = df["TBond10Y"].values
    rf = df["TBill3M"].values
    r = w_stock * sp + (1 - w_stock) * bd
    excess = r - rf

    # Annual Sharpe
    sharpe = excess.mean() / excess.std(ddof=1) if excess.std(ddof=1) > 0 else np.nan

    # Sortino (downside only, target = 0)
    downside = np.where(r < 0, r, 0.0)
    dd_std = np.sqrt((downside ** 2).sum() / len(downside))
    sortino = excess.mean() / dd_std if dd_std > 0 else np.nan

    # Calmar = annualised geometric return / |max drawdown|
    cum = np.cumprod(1 + r)
    geo = cum[-1] ** (1 / len(r)) - 1
    peak = np.maximum.accumulate(cum)
    dd = cum / peak - 1
    mdd = dd.min()
    calmar = geo / abs(mdd) if mdd < 0 else np.nan

    # Treynor: regress portfolio excess on S&P excess, slope = beta
    sp_excess = sp - rf
    cov = np.cov(excess, sp_excess, ddof=1)
    beta = cov[0, 1] / cov[1, 1] if cov[1, 1] > 0 else np.nan
    treynor = excess.mean() / beta if beta and abs(beta) > 0.05 else np.nan

    return sharpe, sortino, calmar, treynor


def build_fig(s):
    weights = [1.0, 0.6, 0.3, 0.0]
    rows = [_portfolio_metrics(w) for w in weights]
    sharpe_vals = [r[0] for r in rows]
    sortino_vals = [r[1] for r in rows]
    calmar_vals = [r[2] for r in rows]
    treynor_vals = [r[3] * 100 if r[3] is not None and not np.isnan(r[3]) else np.nan for r in rows]

    p = PALETTE_LIGHT
    fig, axes = plt.subplots(2, 2, figsize=(11.5, 7.2))
    fig.patch.set_facecolor(p["bg"])

    panels = [
        (axes[0, 0], sharpe_vals,  s["sharpe"],  p["accent"]),
        (axes[0, 1], sortino_vals, s["sortino"], p["blue"]),
        (axes[1, 0], calmar_vals,  s["calmar"],  p["green"]),
        (axes[1, 1], treynor_vals, s["treynor"], p["red"]),
    ]
    x = np.arange(len(weights))
    for ax, vals, name, col in panels:
        style_axes(ax, p)
        clean = [0 if (v is None or (isinstance(v, float) and np.isnan(v))) else v for v in vals]
        bars = ax.bar(x, clean, color=col, alpha=0.85, edgecolor=col, linewidth=0)
        # Highlight max
        finite_clean = [v for v in clean if isinstance(v, (int, float)) and not np.isnan(v)]
        if finite_clean:
            best_v = max(finite_clean)
            for bar, v in zip(bars, clean):
                if v == best_v:
                    bar.set_edgecolor(p["fg"])
                    bar.set_linewidth(1.6)
        for xi, v_orig in zip(x, vals):
            if v_orig is None or (isinstance(v_orig, float) and np.isnan(v_orig)):
                ax.text(xi, 0.02, "n/a", ha="center", va="bottom",
                        fontsize=9, color=p["muted"])
            else:
                ax.text(xi, v_orig + (0.015 if v_orig >= 0 else -0.04),
                        f"{v_orig:.2f}", ha="center",
                        va="bottom" if v_orig >= 0 else "top",
                        fontsize=9, color=p["fg"], fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(s["ports"], fontsize=9)
        ax.set_title(name, fontsize=11, fontweight="bold", loc="left", pad=8, color=p["fg"])
        ax.axhline(0, color=p["fg"], linewidth=0.7)

    fig.suptitle(s["title"], fontsize=13.5, fontweight="bold", y=0.99, x=0.06, ha="left")
    fig.text(0.06, 0.945, s["subtitle"], fontsize=10, color=p["muted"])
    fig.text(0.06, 0.015, s["footer"], fontsize=9, color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
