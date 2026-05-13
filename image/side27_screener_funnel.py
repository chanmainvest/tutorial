"""Side 27, S2.6 - Screening funnel: 4,000 -> 250 -> 50 -> 10 -> 3.

Five-stage trapezoidal funnel showing how a retail watchlist pipeline
converts the universe of US-listed equities into a held position book.
Each stage is labelled with a count and an activity.

Run:
    uv run python course/image/side27_screener_funnel.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side27_screener_funnel"


# Stage counts (top -> bottom).
COUNTS = [4000, 250, 50, 10, 3]

LANG_STRINGS = {
    "en": {
        "title":    "From 4,000 to 3 - the watchlist funnel",
        "subtitle": "Filter -> triage -> deep dive -> watchlist -> position. Most names die in the first two stages.",
        "stages": [
            ("US-listed universe",  "all NYSE + Nasdaq, mkt cap > 50M"),
            ("Pass screen",         "6 filters, monthly"),
            ("Triage",              "2 min/name eyeball check"),
            ("Active watchlist",    "10-K read, thesis written, trigger set"),
            ("Held position",       "trigger hit, sized, owned"),
        ],
        "footer":   "The bottleneck is the 50 -> 10 stage. That is where research lives, and where retail edge lives.",
    },
    "hk": {
        "title":    "由 4,000 到 3 - 觀察名單漏斗",
        "subtitle": "篩選 -> 分流 -> 深研 -> 名單 -> 倉位。大部分名字都死在前兩階段。",
        "stages": [
            ("美股全集",        "全部 NYSE + Nasdaq,市值 > 5,000 萬"),
            ("通過篩選",        "6 條過濾,每月一次"),
            ("分流",            "每名 2 分鐘目測"),
            ("觀察名單",        "讀 10-K、寫論點、設買入價"),
            ("已持倉",          "觸發、定碼、持有"),
        ],
        "footer":   "瓶頸在 50 -> 10。那一階段才是研究發生的地方,也是散戶優勢真正存在的地方。",
    },
    "tw": {
        "title":    "從 4,000 到 3 - 觀察清單漏斗",
        "subtitle": "篩選 -> 分流 -> 深研 -> 清單 -> 部位。大多數名字都死在前兩階段。",
        "stages": [
            ("美股全集",        "全部 NYSE + Nasdaq,市值 > 5,000 萬"),
            ("通過篩選",        "6 條條件,每月跑一次"),
            ("分流",            "每名 2 分鐘目測"),
            ("觀察清單",        "讀 10-K、寫論點、設觸發價"),
            ("已建立部位",      "觸發、計量、持有"),
        ],
        "footer":   "瓶頸在 50 -> 10。那一階段才是研究發生的地方,也是散戶優勢真正存在的地方。",
    },
    "cn": {
        "title":    "从 4,000 到 3 - 观察清单漏斗",
        "subtitle": "筛选 -> 分流 -> 深研 -> 名单 -> 仓位。大多数名字都死在前两个阶段。",
        "stages": [
            ("美股全集",        "全部 NYSE + Nasdaq,市值 > 5,000 万"),
            ("通过筛选",        "6 条过滤,每月一次"),
            ("分流",            "每名 2 分钟目测"),
            ("观察清单",        "读 10-K、写论点、设触发价"),
            ("已持仓",          "触发、定量、持有"),
        ],
        "footer":   "瓶颈在 50 -> 10。那一阶段才是研究发生的地方,也是散户优势真正存在的地方。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.6), dpi=150)
    style_axes(ax, p)

    # Map counts to log-space widths so the visual gradient is readable.
    max_w = 1.0
    min_w = 0.10
    log_counts = np.log10(np.array(COUNTS, dtype=float))
    lo, hi = log_counts.min(), log_counts.max()
    widths = min_w + (log_counts - lo) / (hi - lo) * (max_w - min_w)

    # Stage vertical bands.
    n = len(COUNTS)
    band_h = 1.0 / n
    colors = [p["blue"], p["accent"], p["purple"], p["green"], p["red"]]

    for i in range(n):
        y_top = 1.0 - i * band_h
        y_bot = y_top - band_h * 0.86  # leave gap between bands
        w_top = widths[i] / 2
        w_bot = widths[i + 1] / 2 if i + 1 < n else widths[i] / 2 * 0.55
        poly = Polygon(
            [(-w_top, y_top), (w_top, y_top), (w_bot, y_bot), (-w_bot, y_bot)],
            closed=True, facecolor=colors[i], edgecolor=p["fg"],
            linewidth=0.8, alpha=0.85,
        )
        ax.add_patch(poly)

        count = COUNTS[i]
        label, blurb = s["stages"][i]
        # Count + label centred in the band.
        ax.text(0, (y_top + y_bot) / 2 + 0.018,
                f"{count:,}", ha="center", va="center",
                fontsize=22, fontweight="bold", color="white")
        ax.text(0, (y_top + y_bot) / 2 - 0.030,
                label, ha="center", va="center",
                fontsize=11.5, color="white")

        # Right-side blurb.
        ax.text(0.62, (y_top + y_bot) / 2,
                blurb, ha="left", va="center",
                fontsize=10, color=p["fg"], style="italic")

        # Conversion ratio between bands.
        if i + 1 < n:
            ratio = COUNTS[i + 1] / COUNTS[i]
            ax.text(-0.62, y_bot - 0.005,
                    f"{ratio*100:.1f}%", ha="right", va="center",
                    fontsize=9.5, color=p["muted"])
            ax.annotate("", xy=(-0.55, y_bot - 0.005), xytext=(-0.40, y_bot - 0.005),
                        arrowprops=dict(arrowstyle="->", color=p["muted"],
                                        lw=1.0, alpha=0.7))

    ax.text(-0.62, 1.02, "stage pass rate",
            ha="right", va="bottom", fontsize=8.5, color=p["muted"], style="italic")
    ax.text(0.62, 1.02, "what happens at this stage",
            ha="left",  va="bottom", fontsize=8.5, color=p["muted"], style="italic")

    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-0.08, 1.10)
    ax.set_aspect("auto")
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ("left", "right", "top", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.grid(False)

    fig.suptitle(s["title"], fontsize=15, fontweight="bold", y=0.97)
    fig.text(0.5, 0.92, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.5, color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.90])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_*.png to {OUT_DIR}")
