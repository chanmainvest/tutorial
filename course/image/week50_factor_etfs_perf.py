"""Week 50, S2.1 - Factor ETF cumulative performance 2014-Apr 2026.

Cumulative growth of $1 in seven retail factor ETFs from Jan 2014 through
end-Apr 2026. AVUV is filled forward at 1.0 prior to its Sep-2019 launch
so the line starts when investable.

Annual total returns are embedded as approximate industry-source values.
The lesson focuses on relative shape (single-factor regime risk +
post-decay magnitudes) rather than tick-by-tick replication.

Run:
    uv run python course/image/week50_factor_etfs_perf.py
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
BASE = "week50_factor_etfs_perf"

# Approximate annual total returns (decimal). 2026 entry = Jan-Apr partial.
# AVUV before 2019 = NaN (line starts Sep 2019; we model it from year-end
# 2019 forward). We use "n/a" sentinel = None to mark pre-launch years.
TICKERS = ["VTI", "VTV", "VBR", "MTUM", "QUAL", "USMV", "AVUV"]
YEARS = list(range(2014, 2027))  # 2014..2026
RETURNS = {
    #         2014   2015   2016   2017   2018   2019   2020   2021   2022   2023   2024   2025   2026YTD
    "VTI":  [ 0.125, 0.004, 0.127, 0.212,-0.052, 0.310, 0.210, 0.257,-0.195, 0.260, 0.238, 0.105, 0.042],
    "VTV":  [ 0.131,-0.010, 0.173, 0.170,-0.054, 0.265, 0.023, 0.270,-0.023, 0.094, 0.147, 0.082, 0.038],
    "VBR":  [ 0.074,-0.074, 0.245, 0.115,-0.126, 0.226, 0.056, 0.283,-0.107, 0.162, 0.080, 0.105, 0.045],
    "MTUM": [ 0.146, 0.089, 0.046, 0.373,-0.020, 0.259, 0.293, 0.137,-0.174, 0.188, 0.315, 0.080, 0.035],
    "QUAL": [ 0.137, 0.017, 0.121, 0.236,-0.055, 0.337, 0.232, 0.274,-0.194, 0.260, 0.225, 0.115, 0.045],
    "USMV": [ 0.164, 0.052, 0.102, 0.180,-0.014, 0.280,-0.000, 0.242,-0.094, 0.088, 0.135, 0.095, 0.030],
    # AVUV launched Sep 2019; pre-2019 = None. 2019 partial Sep-Dec ~= 4%.
    "AVUV": [ None,  None,  None,  None,  None,  0.040, 0.036, 0.427,-0.054, 0.180, 0.109, 0.120, 0.050],
}

# Drawing palette: VTI black, others factor-coded.
P = PALETTE_LIGHT
COLORS = {
    "VTI":  P["fg"],
    "VTV":  P["blue"],
    "VBR":  P["teal"],
    "MTUM": P["red"],
    "QUAL": P["purple"],
    "USMV": P["green"],
    "AVUV": P["accent"],
}
LINESTYLES = {
    "VTI":  "-",
    "VTV":  "-",
    "VBR":  "--",
    "MTUM": "-",
    "QUAL": "-",
    "USMV": "-",
    "AVUV": "-",
}
WIDTHS = {
    "VTI":  2.6,
    "VTV":  1.6,
    "VBR":  1.6,
    "MTUM": 1.8,
    "QUAL": 1.8,
    "USMV": 1.8,
    "AVUV": 2.2,
}


def cum_path(rets):
    """Compound annual returns into a wealth path. Skip None entries (pre-launch)."""
    out = []
    cum = 1.0
    started = False
    for r in rets:
        if r is None:
            out.append(None)
            continue
        if not started:
            cum = 1.0
            out.append(cum)
            started = True
        cum *= (1.0 + r)
        if started and len(out) > 0 and out[-1] is None:
            # already appended starting 1.0 above? handled.
            pass
        out.append(cum)
    # The above logic over-shoots by one; rebuild cleanly.
    out = []
    cum = 1.0
    started = False
    for r in rets:
        if r is None:
            out.append(None)
            continue
        cum *= (1.0 + r)
        out.append(cum)
        started = True
    return out


LANG_STRINGS = {
    "en": {
        "title":    "Cumulative growth of $1, seven factor ETFs, 2014 - Apr 2026",
        "subtitle": "VTI core (black) vs. value, momentum, quality, low-vol, small-value tilts. AVUV starts Sep 2019.",
        "ylabel":   "Wealth ($)",
        "footer":   "Annual total returns compounded from approximate end-of-year values. AVUV pre-launch line absent. Single-factor tilts beat or trail the core in regime-dependent runs of multiple years.",
        "tickers":  TICKERS,
    },
    "hk": {
        "title":    "$1 在七隻因子 ETF 中的累計增長,2014 - 2026 年 4 月",
        "subtitle": "VTI 核心(黑線)對價值、動量、品質、低波、小型價值的傾斜。AVUV 於 2019 年 9 月才上市。",
        "ylabel":   "財富(美元)",
        "footer":   "由近似年末總回報複利累計。AVUV 上市前無數據。單因子傾斜對核心的相對表現受多年期的階段性影響。",
        "tickers":  TICKERS,
    },
    "tw": {
        "title":    "$1 在七檔因子 ETF 中的累計成長,2014 - 2026 年 4 月",
        "subtitle": "VTI 核心(黑線)對價值、動量、品質、低波、小型價值的傾斜。AVUV 於 2019 年 9 月才上市。",
        "ylabel":   "財富(美元)",
        "footer":   "由近似年末總報酬複利累計。AVUV 上市前無數據。單因子傾斜相對核心表現受多年期階段影響。",
        "tickers":  TICKERS,
    },
    "cn": {
        "title":    "$1 在七只因子 ETF 中的累计增长,2014 - 2026 年 4 月",
        "subtitle": "VTI 核心(黑线)对价值、动量、质量、低波、小型价值的倾斜。AVUV 于 2019 年 9 月才上市。",
        "ylabel":   "财富(美元)",
        "footer":   "由近似年末总回报复利累计。AVUV 上市前无数据。单因子倾斜对核心的相对表现受多年期阶段性影响。",
        "tickers":  TICKERS,
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax, p)

    # x-axis: each year's end. 2014 entry = end-2014; we anchor at Jan 1 2014 = 1.0.
    # So x = [2014, 2014.99, 2015.99, ..., 2026.33] roughly.
    # Simpler: x_i = year_end fractional (year+1).
    # Anchor start at 2014.0 with wealth 1.0.
    x_anchor = [2014.0]
    for y in YEARS[:-1]:
        x_anchor.append(y + 1.0)  # 2015..2026 (12 year-end ticks)
    x_anchor.append(2026.0 + 4.0/12.0)  # 2026 partial = end-Apr 2026
    # x_anchor length should be len(YEARS)+1 = 14.

    for tk in TICKERS:
        rets = RETURNS[tk]
        # Build wealth path; pre-launch entries -> None.
        ys = [None] * len(x_anchor)
        cum = 1.0
        started_idx = None
        # Find first non-None index.
        for i, r in enumerate(rets):
            if r is not None:
                started_idx = i
                break
        if started_idx is None:
            continue
        # Anchor wealth=1.0 at x[started_idx] (the start of that year).
        ys[started_idx] = 1.0
        cum = 1.0
        for j in range(started_idx, len(rets)):
            r = rets[j]
            if r is None:
                continue
            cum *= (1.0 + r)
            ys[j + 1] = cum  # value at end of that year goes into next x slot.
        xs_plot = [x_anchor[i] for i, v in enumerate(ys) if v is not None]
        ys_plot = [v for v in ys if v is not None]
        ax.plot(xs_plot, ys_plot,
                color=COLORS[tk], linestyle=LINESTYLES[tk],
                linewidth=WIDTHS[tk], label=tk, alpha=0.92)

        # End label
        ax.text(xs_plot[-1] + 0.05, ys_plot[-1], tk,
                fontsize=9.5, fontweight="bold", color=COLORS[tk],
                va="center", ha="left")

    ax.set_xlim(2013.8, 2027.6)
    ax.set_ylim(0.85, 4.6)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.axhline(1.0, color=p["muted"], linewidth=0.7, alpha=0.5)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:.1f}"))

    ax.set_title(s["title"], fontsize=14, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.text(0.06, 0.02, s["footer"], fontsize=8.8, color=p["muted"])
    fig.tight_layout(rect=[0, 0.05, 1, 0.95])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
