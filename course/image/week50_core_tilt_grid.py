"""Week 50, S2.4 - Core+tilt portfolio grid with ann. return / Sharpe / max-DD.

Six candidate constructions over 2014-Apr 2026:
  P1: 100% VTI                                 (baseline)
  P2: 80% VTI / 20% VTV                        (large-value tilt)
  P3: 80% VTI / 20% MTUM                       (momentum tilt)
  P4: 80% VTI / 20% AVUV                       (small-value+profitability tilt)
  P5: 60% VTI / 10% VTV / 10% MTUM /
      10% QUAL / 10% USMV                      (60/40 multi-factor)
  P6: equal-weight 1/7 across all 7 ETFs       (equal-weight)

For each portfolio we compute:
  - Ann. compound return (CAGR over 12.33 years)
  - Annual std dev (sqrt of variance of annual returns)
  - Sharpe = (CAGR - 0.04) / vol
  - Max drawdown over annual wealth path

Annual returns are reused from week50_factor_etfs_perf.py. AVUV pre-2019
is filled forward with VBR returns (the natural "what to substitute"
choice; small-value ETF as proxy before profitability-screened launch).

Run:
    uv run python course/image/week50_core_tilt_grid.py
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
BASE = "week50_core_tilt_grid"

# Annual returns (decimal). 2014..2026YTD = 13 entries.
RET = {
    "VTI":  [ 0.125, 0.004, 0.127, 0.212,-0.052, 0.310, 0.210, 0.257,-0.195, 0.260, 0.238, 0.105, 0.042],
    "VTV":  [ 0.131,-0.010, 0.173, 0.170,-0.054, 0.265, 0.023, 0.270,-0.023, 0.094, 0.147, 0.082, 0.038],
    "VBR":  [ 0.074,-0.074, 0.245, 0.115,-0.126, 0.226, 0.056, 0.283,-0.107, 0.162, 0.080, 0.105, 0.045],
    "MTUM": [ 0.146, 0.089, 0.046, 0.373,-0.020, 0.259, 0.293, 0.137,-0.174, 0.188, 0.315, 0.080, 0.035],
    "QUAL": [ 0.137, 0.017, 0.121, 0.236,-0.055, 0.337, 0.232, 0.274,-0.194, 0.260, 0.225, 0.115, 0.045],
    "USMV": [ 0.164, 0.052, 0.102, 0.180,-0.014, 0.280,-0.000, 0.242,-0.094, 0.088, 0.135, 0.095, 0.030],
    # AVUV: pre-Sep 2019 filled with VBR (the natural prior small-value proxy).
    "AVUV": [ 0.074,-0.074, 0.245, 0.115,-0.126, 0.226, 0.036, 0.427,-0.054, 0.180, 0.109, 0.120, 0.050],
}
N_YEARS = 13
YEAR_FRAC = [1.0]*12 + [4.0/12.0]   # last entry is Jan-Apr 2026 partial

PORTFOLIOS = [
    # (label_key, weights dict)
    ("P1", {"VTI": 1.00}),
    ("P2", {"VTI": 0.80, "VTV": 0.20}),
    ("P3", {"VTI": 0.80, "MTUM": 0.20}),
    ("P4", {"VTI": 0.80, "AVUV": 0.20}),
    ("P5", {"VTI": 0.60, "VTV": 0.10, "MTUM": 0.10, "QUAL": 0.10, "USMV": 0.10}),
    ("P6", {tk: 1.0/7.0 for tk in ("VTI","VTV","VBR","MTUM","QUAL","USMV","AVUV")}),
]


def portfolio_ann_returns(weights):
    """Weighted-sum annual returns (rebalanced annually)."""
    out = []
    for i in range(N_YEARS):
        r = 0.0
        for tk, w in weights.items():
            r += w * RET[tk][i]
        out.append(r)
    return out


def stats(annual_returns, year_frac):
    """Compute CAGR (using year_frac for partial), vol, Sharpe, MDD over wealth path."""
    cum = 1.0
    wealth = [1.0]
    for r in annual_returns:
        cum *= (1.0 + r)
        wealth.append(cum)
    total_years = sum(year_frac)
    cagr = cum ** (1.0 / total_years) - 1.0
    # Vol: stdev over full-year entries (drop partial 2026).
    full_year_rets = annual_returns[:12]
    vol = float(np.std(full_year_rets, ddof=1))
    rf = 0.04
    sharpe = (cagr - rf) / vol if vol > 0 else float("nan")
    # Max drawdown over wealth path
    peak = wealth[0]
    mdd = 0.0
    for w in wealth:
        if w > peak:
            peak = w
        dd = w / peak - 1.0
        if dd < mdd:
            mdd = dd
    return cagr, vol, sharpe, mdd


# Compute all portfolio stats up front (used by labels & bars).
P_STATS = []
for key, w in PORTFOLIOS:
    annr = portfolio_ann_returns(w)
    cagr, vol, sharpe, mdd = stats(annr, YEAR_FRAC)
    P_STATS.append((key, cagr, vol, sharpe, mdd))


LANG_STRINGS = {
    "en": {
        "title":    "Core + tilt: six portfolios, 2014 - Apr 2026",
        "subtitle": "Annual rebalance to target weights. Sharpe = (CAGR - 4%) / annual std. Max DD over annual wealth path.",
        "panel_a":  "Annualised return (CAGR)",
        "panel_b":  "Sharpe ratio",
        "panel_c":  "Max drawdown",
        "footer":   "AVUV pre-Sep-2019 backfilled with VBR. Multi-factor blend (P5) leads on Sharpe; 80/20 MTUM (P3) leads on raw return; equal-weight (P6) has the smallest drawdown; 100% VTI (P1) the deepest.",
        "labels": {
            "P1": "100% VTI",
            "P2": "80/20\nVTI + VTV",
            "P3": "80/20\nVTI + MTUM",
            "P4": "80/20\nVTI + AVUV",
            "P5": "60/40\nMulti-factor",
            "P6": "1/7 each\nEqual-weight",
        },
    },
    "hk": {
        "title":    "核心 + 傾斜:六個組合,2014 - 2026 年 4 月",
        "subtitle": "每年重新平衡至目標權重。夏普 = (CAGR - 4%) / 年化標準差。最大回撚為年度財富曲線最大跌幅。",
        "panel_a":  "年化複合回報 (CAGR)",
        "panel_b":  "夏普比率",
        "panel_c":  "最大回撚",
        "footer":   "AVUV 於 2019 年 9 月前以 VBR 填補。多因子組合 (P5) 夏普最高；80/20 MTUM (P3) 原始回報最高；等權 (P6) 回撒最淺；100% VTI (P1) 回撒最深。",
        "labels": {
            "P1": "100% VTI",
            "P2": "80/20\nVTI + VTV",
            "P3": "80/20\nVTI + MTUM",
            "P4": "80/20\nVTI + AVUV",
            "P5": "60/40\n多因子",
            "P6": "各 1/7\n等權",
        },
    },
    "tw": {
        "title":    "核心 + 傾斜:六個組合,2014 - 2026 年 4 月",
        "subtitle": "每年重新平衡至目標權重。夏普 = (CAGR - 4%) / 年化標準差。最大回檔為年度財富曲線最大跌幅。",
        "panel_a":  "年化複合報酬 (CAGR)",
        "panel_b":  "夏普比率",
        "panel_c":  "最大回檔",
        "footer":   "AVUV 於 2019 年 9 月前以 VBR 填補。多因子組合 (P5) 夏普最高；80/20 MTUM (P3) 原始報酬最高；等權 (P6) 回檔最淺；100% VTI (P1) 回檔最深。",
        "labels": {
            "P1": "100% VTI",
            "P2": "80/20\nVTI + VTV",
            "P3": "80/20\nVTI + MTUM",
            "P4": "80/20\nVTI + AVUV",
            "P5": "60/40\n多因子",
            "P6": "各 1/7\n等權",
        },
    },
    "cn": {
        "title":    "核心 + 倾斜:六个组合,2014 - 2026 年 4 月",
        "subtitle": "每年再平衡至目标权重。夏普 = (CAGR - 4%) / 年化标准差。最大回撚为年度财富曲线最大跌幅。",
        "panel_a":  "年化复合回报 (CAGR)",
        "panel_b":  "夏普比率",
        "panel_c":  "最大回撚",
        "footer":   "AVUV 在 2019 年 9 月之前以 VBR 填补。多因子组合 (P5) 夏普最高；80/20 MTUM (P3) 原始回报最高；等权 (P6) 回撒最浅；100% VTI (P1) 回撒最深。",
        "labels": {
            "P1": "100% VTI",
            "P2": "80/20\nVTI + VTV",
            "P3": "80/20\nVTI + MTUM",
            "P4": "80/20\nVTI + AVUV",
            "P5": "60/40\n多因子",
            "P6": "各 1/7\n等权",
        },
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.6), dpi=150)
    fig.set_facecolor(p["bg"])

    keys = [k for k, *_ in P_STATS]
    cagrs = [c for _, c, *_ in P_STATS]
    vols  = [v for _, _, v, *_ in P_STATS]
    sharpes = [sh for _, _, _, sh, _ in P_STATS]
    mdds = [m for *_, m in P_STATS]

    labels = [s["labels"][k] for k in keys]
    x = np.arange(len(keys))
    # Highlight winner per metric in accent.
    def colors_for(values, want_max=True):
        idx = int(np.argmax(values)) if want_max else int(np.argmin(values))
        out = [p["blue"]] * len(values)
        out[idx] = p["accent"]
        # Always tint baseline (P1) a different muted shade.
        out[0] = p["grey"]
        if idx != 0:
            out[idx] = p["accent"]
        return out

    # Panel A: CAGR
    ax = axes[0]
    style_axes(ax, p)
    cols = colors_for(cagrs, want_max=True)
    ax.bar(x, cagrs, color=cols, alpha=0.9, width=0.65)
    for xi, v in zip(x, cagrs):
        ax.text(xi, v + 0.003, f"{v*100:.1f}%", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["fg"])
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylim(0, max(cagrs) * 1.18)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))
    ax.set_title(s["panel_a"], fontsize=11.5, fontweight="bold", color=p["fg"], pad=10)

    # Panel B: Sharpe
    ax = axes[1]
    style_axes(ax, p)
    cols = colors_for(sharpes, want_max=True)
    ax.bar(x, sharpes, color=cols, alpha=0.9, width=0.65)
    for xi, v in zip(x, sharpes):
        ax.text(xi, v + 0.015, f"{v:.2f}", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["fg"])
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylim(0, max(sharpes) * 1.20)
    ax.set_title(s["panel_b"], fontsize=11.5, fontweight="bold", color=p["fg"], pad=10)

    # Panel C: MDD (note: mdds are negative; make positive for height, label with sign)
    ax = axes[2]
    style_axes(ax, p)
    mdds_abs = [-m for m in mdds]
    # For MDD, the "winner" is the LEAST drawdown (smallest abs value).
    idx_winner = int(np.argmin(mdds_abs))
    cols = [p["blue"]] * len(mdds_abs)
    cols[0] = p["grey"]
    cols[idx_winner] = p["green"]
    if idx_winner == 0:
        cols[0] = p["green"]
    ax.bar(x, mdds_abs, color=cols, alpha=0.9, width=0.65)
    for xi, v, raw in zip(x, mdds_abs, mdds):
        ax.text(xi, v + 0.005, f"{raw*100:.1f}%", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["fg"])
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylim(0, max(mdds_abs) * 1.22)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"-{v*100:.0f}%"))
    ax.set_title(s["panel_c"], fontsize=11.5, fontweight="bold", color=p["fg"], pad=10)

    fig.suptitle(s["title"], fontsize=14, fontweight="bold", color=p["fg"],
                 x=0.06, y=0.98, ha="left")
    fig.text(0.06, 0.93, s["subtitle"], fontsize=10, color=p["muted"], ha="left")
    fig.text(0.06, 0.02, s["footer"], fontsize=9, color=p["muted"])
    fig.tight_layout(rect=[0, 0.05, 1, 0.90])
    return fig


if __name__ == "__main__":
    # Print stats summary for verification.
    print("Portfolio stats (2014 - Apr 2026):")
    print(f"  {'Key':<4} {'CAGR':>8} {'Vol':>8} {'Sharpe':>8} {'MDD':>8}")
    for key, c, v, sh, m in P_STATS:
        print(f"  {key:<4} {c*100:>7.2f}% {v*100:>7.2f}% {sh:>8.2f} {m*100:>7.1f}%")
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
