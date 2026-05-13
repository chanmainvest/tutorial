"""Week 47, §2.4 — 2008 calendar returns: SP500, 60/40, Agg, SocGen CTA.

Bar chart contrasting how four strategies fared in 2008. The SocGen
CTA Index (the industry composite for managed-futures trend-followers)
returned roughly +14.1% — the only equity-correlated risk strategy
that meaningfully gained in a year stocks lost more than a third of
their value.

Run:
    uv run python course/image/week47_cta_2008.py
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
BASE = "week47_cta_2008"

# 2008 calendar-year returns (sources: S&P TR via Damodaran; 60/40 = 0.6*SPX_TR + 0.4*BarcAgg;
# Agg = Bloomberg US Aggregate Bond Index; SocGen CTA Index annual report).
RETS = {
    "sp500":  -0.370,
    "sixty40": -0.220,
    "agg":     +0.052,
    "cta":     +0.141,
}

LANG_STRINGS = {
    "en": {
        "title":   "2008 calendar returns: only CTAs were paid by the trend",
        "subtitle": "S&P -37.0% (TR), 60/40 -22.0%, Bloomberg Agg +5.2%, SocGen CTA Index +14.1%.",
        "xlabel":  "",
        "ylabel":  "2008 total return",
        "labels":  {
            "sp500":   "S&P 500\n(total return)",
            "sixty40": "60 / 40\nstock-bond",
            "agg":     "Bloomberg\nAgg Bond",
            "cta":     "SocGen\nCTA Index",
        },
        "annot_cta": "+14.1%\nthe only +ve strategy\nin a year stocks lost a third",
    },
    "hk": {
        "title":   "2008 年度回報:只有 CTA 被趨勢支付",
        "subtitle": "標普 -37.0% (總回報),60/40 -22.0%,Bloomberg Agg +5.2%,SocGen CTA 指數 +14.1%。",
        "xlabel":  "",
        "ylabel":  "2008 全年回報",
        "labels":  {
            "sp500":   "標普 500\n(總回報)",
            "sixty40": "60 / 40\n股債組合",
            "agg":     "Bloomberg\nAgg 債券",
            "cta":     "SocGen\nCTA 指數",
        },
        "annot_cta": "+14.1%\n股市跌三分一一年中\n唯一正回報策略",
    },
    "tw": {
        "title":   "2008 年度報酬:僅 CTA 被趨勢支付",
        "subtitle": "標普 -37.0%(總報酬),60/40 -22.0%,Bloomberg Agg +5.2%,SocGen CTA 指數 +14.1%。",
        "xlabel":  "",
        "ylabel":  "2008 全年報酬",
        "labels":  {
            "sp500":   "標普 500\n(總報酬)",
            "sixty40": "60 / 40\n股債組合",
            "agg":     "Bloomberg\nAgg 債券",
            "cta":     "SocGen\nCTA 指數",
        },
        "annot_cta": "+14.1%\n股市跌三分之一那年\n唯一正報酬策略",
    },
    "cn": {
        "title":   "2008 年度回报:只有 CTA 被趋势支付",
        "subtitle": "标普 -37.0%(总回报),60/40 -22.0%,Bloomberg Agg +5.2%,SocGen CTA 指数 +14.1%。",
        "xlabel":  "",
        "ylabel":  "2008 全年回报",
        "labels":  {
            "sp500":   "标普 500\n(总回报)",
            "sixty40": "60 / 40\n股债组合",
            "agg":     "Bloomberg\nAgg 债券",
            "cta":     "SocGen\nCTA 指数",
        },
        "annot_cta": "+14.1%\n股市跌三分一那一年\n唯一正回报策略",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    keys = ["sp500", "sixty40", "agg", "cta"]
    vals = [RETS[k] for k in keys]
    labs = [s["labels"][k] for k in keys]
    cols = [p["red"], p["red"], p["blue"], p["green"]]

    fig, ax = plt.subplots(figsize=(10, 6.0), dpi=150)
    style_axes(ax, p)

    bars = ax.bar(np.arange(len(keys)), vals, color=cols,
                  edgecolor="white", linewidth=1.2, width=0.62)
    ax.axhline(0, color=p["fg"], linewidth=0.9)

    for b, v in zip(bars, vals):
        if v >= 0:
            y = v + 0.012
            va = "bottom"
        else:
            y = v - 0.012
            va = "top"
        ax.text(b.get_x() + b.get_width() / 2, y,
                f"{v:+.1%}", ha="center", va=va,
                fontsize=11, fontweight="bold", color=p["fg"])

    ax.set_xticks(np.arange(len(keys)))
    ax.set_xticklabels(labs, fontsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_ylim(-0.45, 0.25)
    ax.set_ylabel(s["ylabel"])

    # Highlight CTA bar with annotation.
    ax.annotate(s["annot_cta"],
                xy=(3, RETS["cta"]),
                xytext=(2.55, 0.205),
                fontsize=9.5, color=p["fg"], ha="center",
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
