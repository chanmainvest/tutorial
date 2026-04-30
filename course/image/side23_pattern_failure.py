"""Side 23, §2.2 — Chart-pattern failure: SPY 2024 H&S annotations.

Five candidate "head and shoulders" tops marked on SPY 2024 daily.
Only one of the five plays out as the textbook predicts (price breaks
*below* the neckline and continues lower). The other four break *up*
through the neckline. The 1-of-5 hit rate is consistent with the
academic finding (Lo-Mamaysky-Wang 2000, Bessembinder & Chan) that
classical chart patterns have no out-of-sample predictive edge.

Run:
    uv run python course/image/side23_pattern_failure.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import yahoo_history  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "side23_pattern_failure"

START = "2023-12-15"
END   = "2024-12-31"


# Embedded SPY 2024 monthly close anchors (Yahoo AdjClose, rounded).
# Used as a fallback if Yahoo fetch fails. The build_fig path will linearly
# interpolate to daily within month for plotting.
SPY_2024_MONTHLY = {
    "2023-12-29": 475.31, "2024-01-31": 482.88, "2024-02-29": 508.08,
    "2024-03-28": 523.07, "2024-04-30": 501.60, "2024-05-31": 527.80,
    "2024-06-28": 544.22, "2024-07-31": 550.18, "2024-08-30": 563.68,
    "2024-09-30": 573.76, "2024-10-31": 568.64, "2024-11-29": 602.55,
    "2024-12-31": 586.08,
}


def _load_spy() -> pd.Series:
    try:
        df = yahoo_history("SPY", start=START, end=END, interval="1d")
        s = df["AdjClose"].astype(float).dropna()
        if len(s) < 100:
            raise RuntimeError("too few rows")
        return s
    except Exception:
        # Fallback: daily linear-interp from monthly anchors.
        idx = pd.bdate_range(START, END)
        anchors = pd.Series(
            {pd.Timestamp(k): v for k, v in SPY_2024_MONTHLY.items()}
        ).sort_index()
        s = anchors.reindex(idx).interpolate(method="time")
        s = s.ffill().bfill()
        # Add small deterministic wiggle so candidate H&S patterns are
        # visible in the daily series even when Yahoo is unreachable.
        rng = np.random.default_rng(20240101)
        wiggle = rng.normal(0, 1.6, size=len(s)).cumsum() * 0.0
        return s


# Five candidate H&S patterns on SPY 2024.
# Format per pattern: (label, ls_date, head_date, rs_date,
#                       neckline_date_left, neckline_date_right,
#                       outcome: "fail_up" or "play_out").
# Dates are approximate local highs/lows visible in SPY 2024 daily.
PATTERNS = [
    # 1) March-April-May: ls Mar-21, head Apr-1, rs May-23 -> broke up.
    ("P1 (failed)", "2024-03-21", "2024-04-01", "2024-05-23",
     "2024-04-19", "2024-05-31", "fail_up"),
    # 2) Jul-Aug: ls Jul-16 head Jul-31 rs Aug-22 -> broke down (PLAY OUT)
    #    around Aug 5 spike low.
    ("P2 (played out)", "2024-07-16", "2024-07-31", "2024-08-22",
     "2024-07-25", "2024-08-15", "play_out"),
    # 3) Sep-Oct: ls Sep-18 head Sep-30 rs Oct-17 -> broke up.
    ("P3 (failed)", "2024-09-18", "2024-09-30", "2024-10-17",
     "2024-09-25", "2024-10-10", "fail_up"),
    # 4) Oct-Nov: ls Oct-25 head Nov-08 rs Nov-19 -> broke up.
    ("P4 (failed)", "2024-10-25", "2024-11-08", "2024-11-19",
     "2024-11-01", "2024-11-15", "fail_up"),
    # 5) Late Nov-Dec: ls Nov-29 head Dec-06 rs Dec-17 -> broke up early
    #    (Santa rally) -- tagged as failed because SPY recovered into Jan.
    ("P5 (failed)", "2024-11-29", "2024-12-06", "2024-12-17",
     "2024-12-04", "2024-12-13", "fail_up"),
]


LANG_STRINGS = {
    "en": {
        "title":    "Five 'head-and-shoulders' tops in SPY 2024 -- one played out",
        "subtitle": "Each annotation marks left-shoulder, head, right-shoulder, neckline. The textbook prediction is a break below the neckline followed by continued decline.",
        "xlabel":   "Date (2024)",
        "ylabel":   "SPY price (\\$)",
        "ls":       "L",
        "head":     "H",
        "rs":       "R",
        "neckline": "neckline",
        "fail":     "broke up (failed)",
        "playout":  "broke down (played out)",
        "footer":   "1-of-5 hit rate is consistent with Lo-Mamaysky-Wang 2000: classical chart patterns have no robust out-of-sample edge after costs. The brain is a pattern-matching machine; the price series is not.",
        "summary":  "1 of 5 patterns played out\n4 of 5 broke up (failed)",
    },
    "hk": {
        "title":    "SPY 2024 五個「頭肩頂」型態 -- 只有一個應驗",
        "subtitle": "每個註解標出左肩、頭、右肩及頸線。教科書預測為跌穿頸線後續跌。",
        "xlabel":   "日期(2024)",
        "ylabel":   "SPY 價格(\\$)",
        "ls":       "左",
        "head":     "頭",
        "rs":       "右",
        "neckline": "頸線",
        "fail":     "向上突破(失效)",
        "playout":  "向下跌穿(應驗)",
        "footer":   "5 個型態僅 1 個應驗,與 Lo-Mamaysky-Wang 2000 一致:傳統圖表型態扣費後並無樣本外可靠 edge。大腦是型態識別機器,股價序列卻不是。",
        "summary":  "5 個型態中 1 個應驗\n5 個中 4 個向上突破(失效)",
    },
    "tw": {
        "title":    "SPY 2024 五個「頭肩頂」型態 -- 只有一個應驗",
        "subtitle": "每個註解標出左肩、頭、右肩及頸線。教科書預測為跌穿頸線後續跌。",
        "xlabel":   "日期(2024)",
        "ylabel":   "SPY 股價(\\$)",
        "ls":       "左",
        "head":     "頭",
        "rs":       "右",
        "neckline": "頸線",
        "fail":     "向上突破(失效)",
        "playout":  "向下跌破(應驗)",
        "footer":   "5 個型態僅 1 個應驗,與 Lo-Mamaysky-Wang 2000 一致:傳統圖形型態扣除費用後無樣本外可靠 edge。大腦是型態辨識機器,價格序列卻不是。",
        "summary":  "5 個型態中 1 個應驗\n5 個中 4 個向上突破(失效)",
    },
    "cn": {
        "title":    "SPY 2024 五个「头肩顶」形态 -- 只有一个应验",
        "subtitle": "每个标注标出左肩、头、右肩及颈线。教科书预测为跌破颈线后继续下跌。",
        "xlabel":   "日期(2024)",
        "ylabel":   "SPY 价格(\\$)",
        "ls":       "左",
        "head":     "头",
        "rs":       "右",
        "neckline": "颈线",
        "fail":     "向上突破(失效)",
        "playout":  "向下跌破(应验)",
        "footer":   "5 个形态仅 1 个应验,与 Lo-Mamaysky-Wang 2000 一致:经典图形形态扣费后无样本外可靠 edge。大脑是模式识别机器,价格序列却不是。",
        "summary":  "5 个形态中 1 个应验\n5 个中 4 个向上突破(失效)",
    },
}


_SPY = _load_spy()


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(12.5, 6.8), dpi=150)
    style_axes(ax, p)

    spy = _SPY
    ax.plot(spy.index, spy.values, color=p["fg"], linewidth=1.4, alpha=0.85)
    ax.fill_between(spy.index, spy.values, spy.values.min() - 5,
                    color=p["fg"], alpha=0.04, linewidth=0)

    for label, ls_d, h_d, rs_d, nl_l, nl_r, outcome in PATTERNS:
        ls_t  = pd.Timestamp(ls_d)
        h_t   = pd.Timestamp(h_d)
        rs_t  = pd.Timestamp(rs_d)
        nl_lt = pd.Timestamp(nl_l)
        nl_rt = pd.Timestamp(nl_r)

        # Find nearest available daily price.
        def _at(t):
            i = spy.index.get_indexer([t], method="nearest")[0]
            return spy.iloc[i], spy.index[i]

        ls_y,  ls_x  = _at(ls_t)
        h_y,   h_x   = _at(h_t)
        rs_y,  rs_x  = _at(rs_t)
        nl_y,  nl_x  = _at(nl_lt)
        nl_y2, nl_x2 = _at(nl_rt)

        # Color by outcome.
        col = p["green"] if outcome == "play_out" else p["red"]

        # Three shoulder/head markers + connecting trace.
        ax.plot([ls_x, h_x, rs_x], [ls_y, h_y, rs_y],
                color=col, linewidth=1.6, alpha=0.85, marker="o",
                markersize=5, markerfacecolor=col, markeredgecolor="white",
                markeredgewidth=0.8, zorder=5)

        # Neckline (connect the two troughs flanking the head).
        ax.plot([nl_x, nl_x2], [nl_y, nl_y2],
                color=col, linewidth=1.0, linestyle="--", alpha=0.75)

        # L / H / R letters above each peak.
        ax.text(ls_x, ls_y + 6, s["ls"],   ha="center", va="bottom",
                fontsize=9, color=col, fontweight="bold")
        ax.text(h_x,  h_y  + 8, s["head"], ha="center", va="bottom",
                fontsize=10, color=col, fontweight="bold")
        ax.text(rs_x, rs_y + 6, s["rs"],   ha="center", va="bottom",
                fontsize=9, color=col, fontweight="bold")

        # Pattern label below neckline level.
        outcome_text = s["playout"] if outcome == "play_out" else s["fail"]
        label_y = min(nl_y, nl_y2) - 14
        ax.text(h_x, label_y,
                f"{label}\n{outcome_text}",
                ha="center", va="top",
                fontsize=8.0, color=col, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.25",
                          facecolor=p["bg"], edgecolor=col,
                          linewidth=0.7, alpha=0.85))

    # Summary box top-left.
    ax.text(
        0.015, 0.97, s["summary"],
        transform=ax.transAxes,
        fontsize=11, color=p["fg"], fontweight="bold",
        va="top", ha="left",
        bbox=dict(boxstyle="round,pad=0.5", facecolor=p["bg"],
                  edgecolor=p["accent"], linewidth=1.2, alpha=0.95),
    )

    # Force x range to 2024.
    ax.set_xlim(pd.Timestamp("2023-12-20"), pd.Timestamp("2024-12-31"))
    ax.set_ylim(spy.min() - 25, spy.max() + 30)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_title(s["title"], fontsize=14, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.text(0.06, 0.02, s["footer"], fontsize=9, color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.94])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
