"""Side 16, sec 2.2 -- months to recovery from each major US bear market.

Curated bar chart. Recovery time = months from bear-market trough to
the point at which the S&P 500 retook its prior all-time high on a
total-return basis. 1929 dwarfs everything else; 2020 is barely visible.
Pre-1987 vs post-1987 cluster shading shows the regime shift.

Run:
    uv run python course/image/side16_recovery_times.py
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
BASE = "side16_recovery_times"

BEARS = [
    ("1929",   180),
    ("1937",    49),
    ("1973",    21),
    ("1987",    20),
    ("2000",    85),
    ("2007",    49),
    ("2020",     5),
    ("2022",    21),
]
PRE_1987_COUNT = 3  # first 3 bars are pre-1987

LANG_STRINGS = {
    "en": {
        "title":    "Months to full recovery from each major US bear market",
        "subtitle": "Time from trough to new total-return high. Pre-1987 cluster (red) is multiples of post-1987 cluster (blue).",
        "xlabel":   "Bear market (year of peak)",
        "ylabel":   "Months from trough to new high",
        "pre":      "Pre-1987 (no Fed put)",
        "post":     "Post-1987 (Greenspan put era)",
        "footer":   "Sources: S&P 500 total return data via Damodaran (annual, 1928-84) and Yahoo ^GSPC monthly (1985+). Recovery times rounded to whole months. The 1929 figure is the nominal recovery; total-return recovery was faster but still about 180 months for someone reinvesting dividends.",
    },
    "hk": {
        "title":    "美國各大熊市完全復原所需月數",
        "subtitle": "由谷底回到總回報新高的時間。1987 前(紅色)為 1987 後(藍色)的數倍。",
        "xlabel":   "熊市(高位年份)",
        "ylabel":   "由谷底至新高(月)",
        "pre":      "1987 年前(無 Fed put)",
        "post":     "1987 年後(Greenspan put 時代)",
        "footer":   "資料:標普 500 總回報 — Damodaran 年度 1928-84、Yahoo ^GSPC 月度 1985 起。復原月數取整。1929 為名義復原;總回報復原較快,但連同股息再投資仍約 180 個月。",
    },
    "tw": {
        "title":    "美國各大空頭市場完全恢復所需月數",
        "subtitle": "由谷底回到總報酬新高的時間。1987 前(紅色)為 1987 後(藍色)的倍數。",
        "xlabel":   "空頭(高點年份)",
        "ylabel":   "由谷底至新高(月)",
        "pre":      "1987 年前(無 Fed put)",
        "post":     "1987 年後(Greenspan put 時代)",
        "footer":   "資料:標普 500 總報酬 — Damodaran 年度 1928-84、Yahoo ^GSPC 月度 1985 起。恢復月數取整。1929 為名義恢復;總報酬恢復較快,但連同股息再投資仍約 180 個月。",
    },
    "cn": {
        "title":    "美国各大熊市完全恢复所需月数",
        "subtitle": "由谷底回到总回报新高的时间。1987 年前(红色)为 1987 年后(蓝色)的倍数。",
        "xlabel":   "熊市(高点年份)",
        "ylabel":   "由谷底至新高(月)",
        "pre":      "1987 年前(无 Fed put)",
        "post":     "1987 年后(Greenspan put 时代)",
        "footer":   "数据:标普 500 总回报 — Damodaran 年度 1928-84、Yahoo ^GSPC 月度 1985 起。恢复月数取整。1929 为名义恢复;总回报恢复更快,但含股息再投资仍约 180 个月。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(11.0, 6.0), dpi=150)
    style_axes(ax, p)

    labels = [b[0] for b in BEARS]
    values = [b[1] for b in BEARS]
    colors = [p["red"] if i < PRE_1987_COUNT else p["blue"] for i in range(len(BEARS))]

    xpos = np.arange(len(BEARS))
    bars = ax.bar(xpos, values, color=colors, alpha=0.85, edgecolor="none", width=0.65)

    # Value labels on top of each bar.
    for x, v in zip(xpos, values):
        ax.text(x, v + 4, f"{v} mo", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["fg"])

    # Regime divider.
    ax.axvline(PRE_1987_COUNT - 0.5, color=p["muted"], linewidth=0.8,
               linestyle="--", alpha=0.7)

    # Modern average reference line (post-1987 mean).
    post_mean = float(np.mean([v for i, v in enumerate(values) if i >= PRE_1987_COUNT]))
    ax.axhline(post_mean, color=p["blue"], linewidth=0.9, linestyle=":",
               alpha=0.7, xmin=(PRE_1987_COUNT) / len(BEARS), xmax=1.0)
    ax.text(len(BEARS) - 0.5, post_mean + 4,
            f"post-1987 avg ~ {post_mean:.0f} mo",
            ha="right", va="bottom", fontsize=9, color=p["blue"],
            fontweight="bold")

    # Pre-1987 mean reference.
    pre_mean = float(np.mean([v for i, v in enumerate(values) if i < PRE_1987_COUNT]))
    ax.axhline(pre_mean, color=p["red"], linewidth=0.9, linestyle=":",
               alpha=0.6, xmin=0.0, xmax=PRE_1987_COUNT / len(BEARS))
    ax.text(0, pre_mean + 4, f"pre-1987 avg ~ {pre_mean:.0f} mo",
            ha="left", va="bottom", fontsize=9, color=p["red"],
            fontweight="bold")

    # Cluster labels.
    ax.text(1.0, 195, s["pre"], ha="center", fontsize=9.5,
            color=p["red"], fontweight="bold")
    ax.text(5.5, 195, s["post"], ha="center", fontsize=9.5,
            color=p["blue"], fontweight="bold")

    ax.set_xticks(xpos)
    ax.set_xticklabels(labels)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, 210)
    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold", loc="left")
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
