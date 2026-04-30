"""Side 13, sec 2.4 -- 2021 deSPAC cohort 12-month post-merger return distribution.

Box-and-whisker style chart showing the dispersion of 12-month
post-merger returns for the 2021 SPAC vintage:
  - bottom quartile  : -85%
  - median           : -50%
  - top quartile     : -25%
  - top decile       :  +5% (one of the few positive outcomes)

Plus a couple of named blowups for orientation. The point of the
chart is the structure: even with a thick floor of dispersion, the
*distribution* is shifted dramatically left of zero.

Run:
    uv run python course/image/side13_spac_blowups.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side13_spac_blowups"


# Quartile / decile estimates curated from de Bakker / Klausner / Ohlrogge
# work and Ritter SPAC tracker for 2021 deSPAC cohort 12-month post-merger.
QUARTILES = {
    "p10":  -0.95,
    "p25":  -0.85,
    "p50":  -0.50,
    "p75":  -0.25,
    "p90":  +0.05,
}

# Named representative outcomes for orientation. Approximate 12-month
# post-merger numbers (rounded). These are illustrative anchors, not
# precise per-name returns.
NAMED = [
    ("LCID",  -0.55),
    ("NKLA",  -0.85),
    ("RIDE",  -0.95),
    ("JOBY",  -0.40),
    ("BARK",  -0.85),
    ("OPEN",  -0.80),
    ("BRDS",  -0.95),
    ("CHPT",  -0.70),
    ("DKNG",  -0.30),
    ("SOFI",  -0.55),
]

LANG_STRINGS = {
    "en": {
        "title":     "2021 deSPAC cohort: 12-month post-merger returns",
        "subtitle":  "Median -50%. Top quartile -25%. Bottom quartile -85%. Only the top decile produced a positive 12-month return.",
        "xlabel":    "12-month post-merger return",
        "ylabel":    "",
        "lbl_dist":  "Distribution",
        "lbl_p25":   "25th pct",
        "lbl_p50":   "Median",
        "lbl_p75":   "75th pct",
        "lbl_zero":  "Zero",
        "annot_struct": "Sponsor promote 20% + redemptions 60-90% +\nPIPE dilution + fantasy forecasts =\n structurally negative cohort return",
        "footer":    "Sources: Klausner-Ohlrogge-Ruan (Stanford 2022), Jay Ritter SPAC tracker (UF), public deSPAC merger filings 2020-2021. Distribution stats are pooled cohort medians; named tickers are illustrative anchors.",
    },
    "hk": {
        "title":     "2021 deSPAC 群組:合併後 12 個月回報",
        "subtitle":  "中位數 -50%。前四分位 -25%。後四分位 -85%。只有前 10% 個股錄得正回報。",
        "xlabel":    "合併後 12 個月回報",
        "ylabel":    "",
        "lbl_dist":  "分佈",
        "lbl_p25":   "25 百分位",
        "lbl_p50":   "中位數",
        "lbl_p75":   "75 百分位",
        "lbl_zero":  "零線",
        "annot_struct": "贊助商 promote 20% + 贖回 60-90%\n + PIPE 稀釋 + 幻想預測 =\n結構性負回報的群組",
        "footer":    "資料:Klausner-Ohlrogge-Ruan(史丹福 2022)、Jay Ritter SPAC tracker(佛羅里達大學)、2020-2021 公開 deSPAC 合併文件。分佈統計為群組中位,個股代號僅為定位錨點。",
    },
    "tw": {
        "title":     "2021 deSPAC 群組:合併後 12 個月報酬",
        "subtitle":  "中位數 -50%。第三四分位 -25%。第一四分位 -85%。僅前 10% 個股有正報酬。",
        "xlabel":    "合併後 12 個月報酬",
        "ylabel":    "",
        "lbl_dist":  "分布",
        "lbl_p25":   "25 百分位",
        "lbl_p50":   "中位數",
        "lbl_p75":   "75 百分位",
        "lbl_zero":  "零線",
        "annot_struct": "贊助商 promote 20% + 贖回 60-90%\n + PIPE 稀釋 + 夢幻預測 =\n結構性負報酬的群組",
        "footer":    "資料:Klausner-Ohlrogge-Ruan(史丹佛 2022)、Jay Ritter SPAC tracker(佛羅里達大學)、2020-2021 公開 deSPAC 合併文件。分布統計為群組中位,個股代號僅為定位錨點。",
    },
    "cn": {
        "title":     "2021 年 deSPAC 群组:合并后 12 个月回报",
        "subtitle":  "中位数 -50%。第三四分位 -25%。第一四分位 -85%。仅前 10% 个股录得正回报。",
        "xlabel":    "合并后 12 个月回报",
        "ylabel":    "",
        "lbl_dist":  "分布",
        "lbl_p25":   "25 百分位",
        "lbl_p50":   "中位数",
        "lbl_p75":   "75 百分位",
        "lbl_zero":  "零线",
        "annot_struct": "发起人 promote 20% + 赎回 60-90%\n + PIPE 稀释 + 幻想预测 =\n结构性负回报的群组",
        "footer":    "数据:Klausner-Ohlrogge-Ruan(斯坦福 2022)、Jay Ritter SPAC tracker(佛罗里达大学)、2020-2021 公开 deSPAC 合并文件。分布统计为群组中位,个股代号仅为定位锚点。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.0, 6.4), dpi=150)
    style_axes(ax, p)

    q = QUARTILES
    y_box = 0.5  # vertical center for the boxplot row.
    box_h = 0.30

    # Whiskers from p10 to p90.
    ax.plot([q["p10"], q["p90"]], [y_box, y_box], color=p["red"],
            linewidth=2.0, zorder=4)
    # Whisker caps.
    for x in (q["p10"], q["p90"]):
        ax.plot([x, x], [y_box - 0.06, y_box + 0.06], color=p["red"],
                linewidth=2.0, zorder=4)

    # Box from p25 to p75.
    ax.add_patch(plt.Rectangle((q["p25"], y_box - box_h / 2),
                               q["p75"] - q["p25"], box_h,
                               facecolor=p["red"], alpha=0.30,
                               edgecolor=p["red"], linewidth=1.5,
                               zorder=5))
    # Median line.
    ax.plot([q["p50"], q["p50"]], [y_box - box_h / 2, y_box + box_h / 2],
            color=p["fg"], linewidth=2.6, zorder=6)

    # Quartile labels above box.
    for key, label_key, va_off in [
        ("p25", "lbl_p25", 0.21),
        ("p50", "lbl_p50", 0.21),
        ("p75", "lbl_p75", 0.21),
    ]:
        ax.text(q[key], y_box + va_off, f"{s[label_key]}\n{q[key]:+.0%}",
                ha="center", va="bottom", fontsize=9.2, fontweight="bold",
                color=p["fg"])

    # Whisker endpoint labels.
    ax.text(q["p10"], y_box - 0.20, f"P10\n{q['p10']:+.0%}",
            ha="center", va="top", fontsize=8.6, color=p["red"])
    ax.text(q["p90"], y_box - 0.20, f"P90\n{q['p90']:+.0%}",
            ha="center", va="top", fontsize=8.6, color=p["green"])

    # Named tickers as scatter dots below the box.
    y_named = -0.45
    xs = [v for _, v in NAMED]
    ax.scatter(xs, [y_named] * len(NAMED), s=44,
               facecolor=p["red"], edgecolor=p["bg"], linewidth=1.0,
               alpha=0.85, zorder=4)
    # Stagger labels by clustered layer assignment so close x-values
    # don't collide horizontally.
    sorted_idx = sorted(range(len(NAMED)), key=lambda i: NAMED[i][1])
    last_x_at_layer = {0: -10.0, 1: -10.0, 2: -10.0, 3: -10.0}
    min_gap = 0.18
    for i in sorted_idx:
        nm, vv = NAMED[i]
        # Pick layer with largest available distance from last entry.
        best_layer = 0
        best_dist = vv - last_x_at_layer[0]
        for L in (1, 2, 3):
            d = vv - last_x_at_layer[L]
            if d > best_dist:
                best_dist = d
                best_layer = L
        chosen = best_layer
        last_x_at_layer[chosen] = vv
        ax.text(vv, y_named - 0.18 - chosen * 0.16,
                f"{nm}\n{vv:+.0%}",
                ha="center", va="top", fontsize=7.6, color=p["fg"])

    # Zero reference.
    ax.axvline(0.0, color=p["fg"], linewidth=1.0, linestyle="--", zorder=3)
    ax.text(0.0, 1.05, s["lbl_zero"], color=p["fg"], fontsize=9,
            ha="center", fontweight="bold")

    # Structure annotation box on the right.
    ax.text(0.18, 0.85, s["annot_struct"],
            fontsize=9.5, color=p["fg"], ha="left", va="top",
            bbox=dict(boxstyle="round,pad=0.5",
                      facecolor=p["bg"], edgecolor=p["muted"], linewidth=0.8))

    ax.set_xlim(-1.05, 0.45)
    ax.set_ylim(-1.55, 1.20)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:+.0%}"))
    ax.set_yticks([])
    ax.set_xlabel(s["xlabel"])

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.3, color=p["muted"])

    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
