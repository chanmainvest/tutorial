"""Week 33, §2.2 — Annual default rates by rating bucket (Moody's long-run averages).

Bar chart of one-year default rates by rating bucket, showing the IG/HY
cliff and the non-linear progression CCC > B > BB > BBB.

Source: Moody's Annual Default Study, long-run averages 1920-2023:
    AAA = 0.00%, AA = 0.02%, A = 0.07%, BBB = 0.18%,
    BB  = 1.16%, B  = 4.10%, CCC = 23.30%

Run:
    uv run python course/image/week33_default_rates.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week33_default_rates"

# (rating, default-rate %, tier)  tier: "ig" | "hy"
BUCKETS = [
    ("AAA",  0.00, "ig"),
    ("AA",   0.02, "ig"),
    ("A",    0.07, "ig"),
    ("BBB",  0.18, "ig"),
    ("BB",   1.16, "hy"),
    ("B",    4.10, "hy"),
    ("CCC", 23.30, "hy"),
]


LANG_STRINGS = {
    "en": {
        "title":    "Annual default rate by rating bucket — Moody's long-run averages",
        "subtitle": "Cross the BBB / BB cliff and the rate jumps 6x. Each notch lower multiplies risk, not adds.",
        "ylabel":   "Annualised default rate (%)",
        "xlabel":   "Rating bucket",
        "ig":       "Investment grade",
        "hy":       "High yield (junk)",
        "cliff":    "IG / HY cliff",
        "footer":   "Source: Moody's Annual Default Study, long-run averages 1920-2023.",
    },
    "hk": {
        "title":    "各評級年度違約率 — 穆迪長期平均",
        "subtitle": "跨過 BBB / BB 那條懸崖,違約率躍升六倍。每降一級是乘數,不是加法。",
        "ylabel":   "年化違約率(%)",
        "xlabel":   "評級",
        "ig":       "投資級",
        "hy":       "高收益(垃圾級)",
        "cliff":    "投資級 / 高收益分界",
        "footer":   "資料:Moody's Annual Default Study,1920-2023 長期平均。",
    },
    "tw": {
        "title":    "各評等年度違約率 — 穆迪長期平均",
        "subtitle": "跨過 BBB / BB 那條懸崖,違約率躍升六倍。每降一級是乘法,不是加法。",
        "ylabel":   "年化違約率(%)",
        "xlabel":   "評等",
        "ig":       "投資級",
        "hy":       "高收益(垃圾等級)",
        "cliff":    "投資級 / 高收益分界",
        "footer":   "資料:Moody's Annual Default Study,1920-2023 長期平均。",
    },
    "cn": {
        "title":    "各评级年度违约率 — 穆迪长期平均",
        "subtitle": "跨过 BBB / BB 那条悬崖,违约率跃升六倍。每降一级是乘数,不是加法。",
        "ylabel":   "年化违约率(%)",
        "xlabel":   "评级",
        "ig":       "投资级",
        "hy":       "高收益(垃圾级)",
        "cliff":    "投资级 / 高收益分界",
        "footer":   "资料:Moody's Annual Default Study,1920-2023 长期平均。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2))
    style_axes(ax, p)

    labels = [b[0] for b in BUCKETS]
    rates = [b[1] for b in BUCKETS]
    colors = [p["blue"] if b[2] == "ig" else p["red"] for b in BUCKETS]
    x = list(range(len(labels)))

    bars = ax.bar(x, rates, color=colors, width=0.66, alpha=0.92,
                  edgecolor="none")

    # Value labels above each bar
    for xi, r in zip(x, rates):
        if r < 0.01:
            txt = "0.00%"
        elif r < 1:
            txt = f"{r:.2f}%"
        else:
            txt = f"{r:.1f}%"
        ax.text(xi, r + 0.7, txt, ha="center", va="bottom",
                fontsize=10.5, fontweight="bold", color=p["fg"])

    # IG / HY cliff line between BBB (idx 3) and BB (idx 4)
    ax.axvline(3.5, color=p["accent"], linewidth=1.4, linestyle="--",
               alpha=0.85)
    ax.text(3.5, 25.5, s["cliff"], ha="center", va="bottom",
            color=p["accent"], fontsize=10.5, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=p["bg"],
                      edgecolor=p["accent"], linewidth=1.0))

    # IG and HY bracket annotations (under axis)
    ax.text(1.5, -2.8, s["ig"], ha="center", va="top",
            color=p["blue"], fontsize=11, fontweight="bold")
    ax.text(5.0, -2.8, s["hy"], ha="center", va="top",
            color=p["red"], fontsize=11, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11.5, fontweight="bold")
    ax.set_xlabel(s["xlabel"], labelpad=28)
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, 27)
    ax.set_xlim(-0.6, 6.6)

    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.8, color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
