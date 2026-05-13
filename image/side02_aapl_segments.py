"""Side 02, S2.3 - Apple FY2024 revenue by segment with YoY growth.

Source: Apple Inc. FY2024 10-K (fiscal year ended September 28, 2024),
Note 12 - Segment Information. Five reportable revenue categories.

Run:
    uv run python course/image/side02_aapl_segments.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side02_aapl_segments"


# Apple FY2024 10-K - Note 12. Revenue ($B) and YoY growth %.
SEGMENTS = [
    ("iPhone",      201.2,  0.3),
    ("Services",     96.2, 13.0),
    ("Wearables",    37.0, -7.0),
    ("Mac",          30.0,  2.0),
    ("iPad",         26.7,  5.0),
]
TOTAL = sum(s[1] for s in SEGMENTS)  # 391.0B


LANG_STRINGS = {
    "en": {
        "title":    "Apple FY2024 revenue by segment",
        "subtitle": "Total $391B, up 2% YoY. Services up 13% is the only line that matters for the multiple.",
        "footer":   "Source: AAPL FY2024 10-K, Note 12 (Segment Information). FYE Sep 28, 2024.",
        "xlabel":   "Revenue (USD billions)",
        "ylabel":   "",
        "yoy_label": "YoY",
        "names":    [s[0] for s in SEGMENTS],
        "callout":  "Services growth = the entire investment thesis",
    },
    "hk": {
        "title":    "蘋果 FY2024 營收分部",
        "subtitle": "總額 3,910 億美元、按年增 2%。13% 增長的服務分部是唯一影響估值的一條線。",
        "footer":   "資料來源:AAPL FY2024 10-K 第 12 號附註(分部資料)。財年結 2024-09-28。",
        "xlabel":   "營收(十億美元)",
        "ylabel":   "",
        "yoy_label": "按年",
        "names":    ["iPhone", "服務", "穿戴裝置", "Mac", "iPad"],
        "callout":  "服務增長 = 完整的投資論點",
    },
    "tw": {
        "title":    "蘋果 FY2024 營收分部",
        "subtitle": "總額 3,910 億美元、年增 2%。13% 成長的服務分部是唯一影響估值的一條線。",
        "footer":   "資料來源:AAPL FY2024 10-K 第 12 號附註(分部資料)。會計年度結 2024-09-28。",
        "xlabel":   "營收(十億美元)",
        "ylabel":   "",
        "yoy_label": "年增",
        "names":    ["iPhone", "服務", "穿戴裝置", "Mac", "iPad"],
        "callout":  "服務成長 = 完整的投資論點",
    },
    "cn": {
        "title":    "苹果 FY2024 营收分部",
        "subtitle": "总额 3,910 亿美元、同比增 2%。13% 增长的服务分部是唯一影响估值的一条线。",
        "footer":   "资料来源:AAPL FY2024 10-K 第 12 号附注(分部资料)。财年结 2024-09-28。",
        "xlabel":   "营收(十亿美元)",
        "ylabel":   "",
        "yoy_label": "同比",
        "names":    ["iPhone", "服务", "穿戴设备", "Mac", "iPad"],
        "callout":  "服务增长 = 完整的投资论点",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    # Escape any leading-dollar literals to avoid mathtext mode in titles.
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax, p)

    rev = [seg[1] for seg in SEGMENTS]
    yoy = [seg[2] for seg in SEGMENTS]
    names = s["names"]
    n = len(rev)
    y = np.arange(n)[::-1]  # iPhone on top

    # Color: gold for Services (the story), navy for the rest, red if negative growth.
    colors = []
    for i, (_, _, g) in enumerate(SEGMENTS):
        if i == 1:           # Services
            colors.append(p["accent"])
        elif g < 0:
            colors.append(p["red"])
        else:
            colors.append(p["blue"])

    bars = ax.barh(y, rev, color=colors, edgecolor=p["fg"], linewidth=0.6, alpha=0.9, height=0.62)

    # In-bar revenue label (white) for tall bars, outside for short bars.
    for i, b in enumerate(bars):
        v = rev[i]
        if v >= 50:
            ax.text(v - 2, b.get_y() + b.get_height() / 2,
                    f"\\${v:.1f}B", ha="right", va="center",
                    fontsize=11.5, fontweight="bold", color="white")
        else:
            ax.text(v + 2, b.get_y() + b.get_height() / 2,
                    f"\\${v:.1f}B", ha="left", va="center",
                    fontsize=11.5, fontweight="bold", color=p["fg"])

    # YoY pill outside each bar (right-side block reserved).
    yoy_x = max(rev) * 1.12
    ax.set_xlim(0, max(rev) * 1.32)
    for i, g in enumerate(yoy):
        col = p["green"] if g > 0 else (p["red"] if g < 0 else p["muted"])
        sign = "+" if g > 0 else ""
        label = f"{s['yoy_label']} {sign}{g:.1f}%"
        ax.text(yoy_x, y[i], label,
                ha="left", va="center",
                fontsize=10.5, fontweight="bold", color=col,
                bbox=dict(boxstyle="round,pad=0.30", facecolor="white",
                          edgecolor=col, linewidth=1.0))

    # Services callout arrow.
    services_y = y[1]
    services_x = rev[1]
    ax.annotate(s["callout"],
                xy=(services_x, services_y),
                xytext=(services_x + 70, services_y - 0.85),
                fontsize=10, color=p["accent"], fontweight="bold", style="italic",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff5cc",
                          edgecolor=p["accent"], linewidth=1.0),
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.2))

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=11)
    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["muted"])
    ax.set_title(s["title"], pad=24, fontsize=15, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=9, color=p["muted"], style="italic")

    # Total annotation upper right.
    ax.text(0.99, 1.02,
            f"Total: \\${TOTAL:.1f}B",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=10, color=p["fg"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_*.png to {OUT_DIR}")
