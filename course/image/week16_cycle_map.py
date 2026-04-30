"""Week 16, §2.2 — Schematic 4-quadrant cycle map of sector leadership.

A hand-drawn matplotlib chart, NOT a backtest. Horizontal axis is the
business cycle phase from early recovery on the left through recession
on the right. Vertical axis distinguishes cyclical (top) from defensive
(bottom). Each quadrant lists the sectors that historically lead in
that phase. A grey arrow loops clockwise to indicate the rotation.

Run:
    uv run python course/image/week16_cycle_map.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week16_cycle_map"

LANG_STRINGS = {
    "en": {
        "title":    "Sector rotation cycle map",
        "subtitle": "Which slice of the equity market historically leads in each phase. Statistical tendency, not a calendar.",
        "phase_early":    "EARLY RECOVERY",
        "phase_mid":      "MID-EXPANSION",
        "phase_late":     "LATE EXPANSION",
        "phase_recession":"RECESSION",
        "axis_phase":     "Business cycle phase",
        "axis_type":      "Cyclical \u2190\u2192 Defensive",
        "early_caption":  "Steep curve. Pent-up demand.\nFed cutting. Credit easing.",
        "mid_caption":    "Broad growth. Capex cycle.\nLow rates, rising margins.",
        "late_caption":   "Tight capacity. Rising inflation.\nFed hiking. Wages up.",
        "rec_caption":    "Earnings falling. Rates cut.\nFear dominates.",
        "early_sectors":  ["Financials  XLF", "Cons. Discretionary  XLY",
                           "Industrials  XLI", "Real Estate  XLRE"],
        "mid_sectors":    ["Technology  XLK", "Communication  XLC",
                           "Industrials  XLI"],
        "late_sectors":   ["Energy  XLE", "Materials  XLB",
                           "Health Care  XLV"],
        "rec_sectors":    ["Cons. Staples  XLP", "Utilities  XLU",
                           "Health Care  XLV"],
        "footer":         "Map source: standard CFA / Fidelity / S&P sector-cycle framework. Real years deviate; see week16_sector_winners.png.",
    },
    "hk": {
        "title":    "行業輪動週期圖",
        "subtitle": "歷史上每個階段哪一片股市領跑。統計趨勢,並非日曆。",
        "phase_early":    "早期復甦",
        "phase_mid":      "中期擴張",
        "phase_late":     "晚期擴張",
        "phase_recession":"衰退",
        "axis_phase":     "經濟週期階段",
        "axis_type":      "週期性 \u2190\u2192 防守性",
        "early_caption":  "曲線陡峭、被壓抑需求釋放。\n聯儲減息,信貸放寬。",
        "mid_caption":    "增長廣泛。資本開支週期。\n利率低、利潤率上升。",
        "late_caption":   "產能緊張、通脹抬頭。\n聯儲加息,工資上行。",
        "rec_caption":    "盈利下滑、減息。\n恐懼主導。",
        "early_sectors":  ["金融  XLF", "非必需消費  XLY",
                           "工業  XLI", "房地產  XLRE"],
        "mid_sectors":    ["科技  XLK", "通信服務  XLC",
                           "工業  XLI"],
        "late_sectors":   ["能源  XLE", "原材料  XLB",
                           "醫療  XLV"],
        "rec_sectors":    ["必需消費  XLP", "公用事業  XLU",
                           "醫療  XLV"],
        "footer":         "圖譜源自 CFA / Fidelity / S&P 標準行業週期框架。實際年份有偏差,見 week16_sector_winners.png。",
    },
    "tw": {
        "title":    "行業輪動週期圖",
        "subtitle": "歷史上每個階段哪一片股市領跑。統計趨勢,並非日曆。",
        "phase_early":    "早期復甦",
        "phase_mid":      "中期擴張",
        "phase_late":     "晚期擴張",
        "phase_recession":"衰退",
        "axis_phase":     "景氣循環階段",
        "axis_type":      "循環性 \u2190\u2192 防禦性",
        "early_caption":  "殖利率曲線陡峭、遞延需求釋放。\n聯準會降息,信用放鬆。",
        "mid_caption":    "成長廣泛。資本支出循環。\n利率低、利潤率上升。",
        "late_caption":   "產能緊張、通膨抬頭。\n聯準會升息,工資上行。",
        "rec_caption":    "盈餘下滑、降息。\n恐懼主導。",
        "early_sectors":  ["金融  XLF", "非必需消費  XLY",
                           "工業  XLI", "房地產  XLRE"],
        "mid_sectors":    ["科技  XLK", "通訊服務  XLC",
                           "工業  XLI"],
        "late_sectors":   ["能源  XLE", "原物料  XLB",
                           "醫療  XLV"],
        "rec_sectors":    ["必需消費  XLP", "公用事業  XLU",
                           "醫療  XLV"],
        "footer":         "圖譜源自 CFA / Fidelity / S&P 標準行業循環框架。實際年份有偏差,見 week16_sector_winners.png。",
    },
    "cn": {
        "title":    "行业轮动周期图",
        "subtitle": "历史上每个阶段哪一片股市领跑。统计趋势,并非日历。",
        "phase_early":    "早期复苏",
        "phase_mid":      "中期扩张",
        "phase_late":     "晚期扩张",
        "phase_recession":"衰退",
        "axis_phase":     "经济周期阶段",
        "axis_type":      "周期性 \u2190\u2192 防御性",
        "early_caption":  "曲线陡峭、被压抑需求释放。\n美联储降息,信贷放松。",
        "mid_caption":    "增长广泛。资本开支周期。\n利率低、利润率上升。",
        "late_caption":   "产能紧张、通胀抬头。\n美联储加息,工资上行。",
        "rec_caption":    "盈利下滑、降息。\n恐惧主导。",
        "early_sectors":  ["金融  XLF", "非必需消费  XLY",
                           "工业  XLI", "房地产  XLRE"],
        "mid_sectors":    ["科技  XLK", "通信服务  XLC",
                           "工业  XLI"],
        "late_sectors":   ["能源  XLE", "原材料  XLB",
                           "医疗  XLV"],
        "rec_sectors":    ["必需消费  XLP", "公用事业  XLU",
                           "医疗  XLV"],
        "footer":         "图谱源自 CFA / Fidelity / S&P 标准行业周期框架。实际年份偏差见 week16_sector_winners.png。",
    },
}


def _quadrant(ax, x, y, w, h, color, alpha=0.18):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.5, edgecolor=color, facecolor=color, alpha=alpha,
    )
    ax.add_patch(box)


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.6, 7.0), dpi=150)
    style_axes(ax, p)
    ax.set_facecolor(p["bg"])
    fig.set_facecolor(p["bg"])

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    # Quadrant colors
    c_early = p["green"]
    c_mid   = p["blue"]
    c_late  = p["orange"]
    c_rec   = p["red"]

    # Top-left: early recovery (cyclical, early)
    # Top-right: mid expansion (cyclical, mid)
    # Bottom-right: late expansion (defensive-tilted, late)
    # Bottom-left: recession (defensive, late->trough)
    # Reading clockwise from top-left: early -> mid -> late -> recession.
    _quadrant(ax, 0.4, 3.6, 4.6, 2.8, c_early, alpha=0.16)
    _quadrant(ax, 5.0, 3.6, 4.6, 2.8, c_mid, alpha=0.16)
    _quadrant(ax, 5.0, 0.7, 4.6, 2.8, c_late, alpha=0.16)
    _quadrant(ax, 0.4, 0.7, 4.6, 2.8, c_rec, alpha=0.18)

    # Phase headers
    head_kw = dict(ha="center", fontsize=12, fontweight="bold")
    ax.text(2.7, 6.1, s["phase_early"], color=c_early, **head_kw)
    ax.text(7.3, 6.1, s["phase_mid"],   color=c_mid,   **head_kw)
    ax.text(7.3, 3.2, s["phase_late"],  color=c_late,  **head_kw)
    ax.text(2.7, 3.2, s["phase_recession"], color=c_rec, **head_kw)

    # Phase macro captions
    cap_kw = dict(ha="center", fontsize=8.5, color=p["muted"], style="italic")
    ax.text(2.7, 5.75, s["early_caption"], **cap_kw)
    ax.text(7.3, 5.75, s["mid_caption"],   **cap_kw)
    ax.text(7.3, 2.85, s["late_caption"],  **cap_kw)
    ax.text(2.7, 2.85, s["rec_caption"],   **cap_kw)

    # Sector lists
    def _list(ax, x, y_top, items, color):
        for k, item in enumerate(items):
            ax.text(x, y_top - 0.42 * k, "\u2022 " + item,
                    ha="center", fontsize=10.6, color=p["fg"],
                    fontweight="bold")
    _list(ax, 2.7, 5.2, s["early_sectors"], c_early)
    _list(ax, 7.3, 5.2, s["mid_sectors"],   c_mid)
    _list(ax, 7.3, 2.3, s["late_sectors"],  c_late)
    _list(ax, 2.7, 2.3, s["rec_sectors"],   c_rec)

    # Clockwise rotation arrows: top-left -> top-right -> bottom-right
    # -> bottom-left -> top-left
    arrow_kw = dict(arrowstyle="->,head_width=0.4,head_length=0.5",
                    color=p["grey"], linewidth=2.0,
                    connectionstyle="arc3,rad=0.18", alpha=0.65)
    ax.add_patch(FancyArrowPatch((4.95, 5.0), (5.05, 5.0), **arrow_kw))
    ax.add_patch(FancyArrowPatch((7.3, 3.55), (7.3, 3.45),
                                  arrowstyle="->,head_width=0.4,head_length=0.5",
                                  color=p["grey"], linewidth=2.0, alpha=0.65))
    ax.add_patch(FancyArrowPatch((5.05, 2.1), (4.95, 2.1), **arrow_kw))
    ax.add_patch(FancyArrowPatch((2.7, 3.45), (2.7, 3.55),
                                  arrowstyle="->,head_width=0.4,head_length=0.5",
                                  color=p["grey"], linewidth=2.0, alpha=0.65))

    # Axis labels (we hide ticks)
    ax.text(5.0, 0.18, s["axis_phase"], ha="center",
            fontsize=10, color=p["muted"])
    ax.text(0.06, 3.55, s["axis_type"], ha="center", va="center",
            rotation=90, fontsize=10, color=p["muted"])

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.grid(False)

    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold",
                 loc="left", color=p["fg"])
    fig.text(0.13, 0.94, s["subtitle"], fontsize=10, color=p["muted"],
             style="italic")
    fig.text(0.5, 0.015, s["footer"], ha="center", fontsize=8.2,
             color=p["muted"])
    fig.tight_layout(rect=[0, 0.03, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"wrote {BASE}.png and locale variants to {OUT_DIR}")
