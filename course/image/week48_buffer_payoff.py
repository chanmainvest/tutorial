"""Week 48, §2.1 — Buffer ETF payoff at 1y expiry.

15% downside buffer + 18% upside cap on SPY at $500. Single-line
total-return P&L curve from -30% to +30% spot move, with the four
characteristic regions (full-loss, buffer, participation, capped)
shaded and annotated. The kink points are the buffer floor (-15%),
breakeven (0%), and the cap (+18%).

Run:
    uv run python course/image/week48_buffer_payoff.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week48_buffer_payoff"

SPOT = 500.0          # SPY spot
BUFFER = 0.15         # 15% downside buffer
CAP = 0.18            # 18% upside cap


def buffered_return(r: np.ndarray) -> np.ndarray:
    """Return the buffered total return for an underlying return r."""
    out = np.where(
        r >= CAP, CAP,
        np.where(
            r >= 0.0, r,
            np.where(r >= -BUFFER, 0.0, r + BUFFER),
        ),
    )
    return out


LANG_STRINGS = {
    "en": {
        "title": "Buffer ETF payoff at 1y: 15% buffer + 18% cap on SPY at \\$500",
        "subtitle": "Total return at expiry as a function of underlying SPY return. Per \\$10,000 of notional.",
        "xlabel": "SPY return at expiry",
        "ylabel": "Buffered total return at expiry (\\$)",
        "line": "Buffered ETF P&L",
        "ref": "Unbuffered SPY (1:1)",
        "r_loss": "Full loss past buffer",
        "r_buffer": "Buffer zone (P&L = 0)",
        "r_part": "Participation zone (1:1)",
        "r_cap": "Capped zone (P&L = +\\$1,800)",
        "annot_floor": "Buffer floor: -15%",
        "annot_cap": "Cap: +18% = +\\$1,800",
        "annot_be": "Breakeven: 0%",
    },
    "hk": {
        "title": "緩衝 ETF 一年到期損益:SPY \\$500 配 15% 緩衝 + 18% 上限",
        "subtitle": "到期總回報為標的 SPY 回報的函數。每 \\$10,000 名義金額。",
        "xlabel": "到期 SPY 回報",
        "ylabel": "到期緩衝總回報 (\\$)",
        "line": "緩衝 ETF 損益",
        "ref": "純 SPY (1:1)",
        "r_loss": "緩衝以下全額虧損",
        "r_buffer": "緩衝區(損益 = 0)",
        "r_part": "參與區(1:1)",
        "r_cap": "封頂區(損益 = +\\$1,800)",
        "annot_floor": "緩衝底:-15%",
        "annot_cap": "上限:+18% = +\\$1,800",
        "annot_be": "打和:0%",
    },
    "tw": {
        "title": "緩衝 ETF 一年到期損益:SPY \\$500 搭 15% 緩衝 + 18% 上限",
        "subtitle": "到期總報酬為標的 SPY 報酬的函數。每 \\$10,000 名目金額。",
        "xlabel": "到期 SPY 報酬",
        "ylabel": "到期緩衝總報酬 (\\$)",
        "line": "緩衝 ETF 損益",
        "ref": "純 SPY (1:1)",
        "r_loss": "緩衝以下全額虧損",
        "r_buffer": "緩衝區(損益 = 0)",
        "r_part": "參與區(1:1)",
        "r_cap": "封頂區(損益 = +\\$1,800)",
        "annot_floor": "緩衝底:-15%",
        "annot_cap": "上限:+18% = +\\$1,800",
        "annot_be": "打平:0%",
    },
    "cn": {
        "title": "缓冲 ETF 一年到期损益:SPY \\$500 配 15% 缓冲 + 18% 上限",
        "subtitle": "到期总回报为标的 SPY 回报的函数。每 \\$10,000 名义金额。",
        "xlabel": "到期 SPY 回报",
        "ylabel": "到期缓冲总回报 (\\$)",
        "line": "缓冲 ETF 损益",
        "ref": "纯 SPY (1:1)",
        "r_loss": "缓冲以下全额亏损",
        "r_buffer": "缓冲区(损益 = 0)",
        "r_part": "参与区(1:1)",
        "r_cap": "封顶区(损益 = +\\$1,800)",
        "annot_floor": "缓冲底:-15%",
        "annot_cap": "上限:+18% = +\\$1,800",
        "annot_be": "打平:0%",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    NOTIONAL = 10_000.0

    rets = np.linspace(-0.30, 0.30, 601)
    buffered = buffered_return(rets) * NOTIONAL
    unbuffered = rets * NOTIONAL

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, p)

    # Region shading.
    ymin, ymax = -0.20 * NOTIONAL, 0.22 * NOTIONAL
    ax.axhspan(ymin, ymax, xmin=0, xmax=0, alpha=0)  # placeholder

    # x-axis spans from -0.30 to +0.30; convert region edges to fractions of x range.
    def xfrac(x):
        return (x - (-0.30)) / (0.30 - (-0.30))

    ax.axvspan(-0.30, -BUFFER, color=p["red"], alpha=0.10, zorder=0)
    ax.axvspan(-BUFFER, 0.0, color=p["accent"], alpha=0.12, zorder=0)
    ax.axvspan(0.0, CAP, color=p["green"], alpha=0.12, zorder=0)
    ax.axvspan(CAP, 0.30, color=p["blue"], alpha=0.10, zorder=0)

    # Region labels at the top of the panel.
    ytop = 0.205 * NOTIONAL
    ax.text((-0.30 + -BUFFER) / 2, ytop, s["r_loss"],
            ha="center", va="top", fontsize=8.5, color=p["red"], fontweight="bold")
    ax.text((-BUFFER + 0.0) / 2, ytop, s["r_buffer"],
            ha="center", va="top", fontsize=8.5, color=p["accent"], fontweight="bold")
    ax.text((0.0 + CAP) / 2, ytop, s["r_part"],
            ha="center", va="top", fontsize=8.5, color=p["green"], fontweight="bold")
    ax.text((CAP + 0.30) / 2, ytop, s["r_cap"],
            ha="center", va="top", fontsize=8.5, color=p["blue"], fontweight="bold")

    # Zero baseline.
    ax.axhline(0, color=p["fg"], linewidth=0.8, zorder=2)

    # Reference unbuffered SPY (dashed muted).
    ax.plot(rets, unbuffered, color=p["muted"], linewidth=1.6,
            linestyle="--", label=s["ref"], zorder=3)

    # Buffered ETF main line.
    ax.plot(rets, buffered, color=p["blue"], linewidth=3.0,
            label=s["line"], zorder=4)

    # Kink-point markers.
    for x, y in [(-BUFFER, 0.0), (0.0, 0.0), (CAP, CAP * NOTIONAL)]:
        ax.plot(x, y, marker="o", markersize=7,
                markerfacecolor=p["accent"],
                markeredgecolor=p["fg"], markeredgewidth=1.0, zorder=5)

    # Annotations.
    ax.annotate(s["annot_floor"],
                xy=(-BUFFER, 0.0), xytext=(-0.26, -1100),
                fontsize=9, color=p["fg"], ha="left",
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))
    ax.annotate(s["annot_cap"],
                xy=(CAP, CAP * NOTIONAL), xytext=(0.06, 1500),
                fontsize=9, color=p["fg"], ha="left",
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))
    ax.annotate(s["annot_be"],
                xy=(0.0, 0.0), xytext=(0.04, -1500),
                fontsize=9, color=p["fg"], ha="left",
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))

    ax.set_xlim(-0.30, 0.30)
    ax.set_ylim(ymin, ymax)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda v, _: f"-${abs(v)/1000:.1f}k" if v < 0 else f"${v/1000:.1f}k"))
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.legend(loc="lower right", frameon=False, fontsize=10)

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
