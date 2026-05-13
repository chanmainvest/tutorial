"""Week 20, §2.2 — Post-Earnings-Announcement Drift, schematic.

Schematic of the average cumulative abnormal return (CAR) for the top
and bottom earnings-surprise (SUE) quintiles in the 60 trading days
*after* an earnings announcement. Shape is the academic standard from
Bernard & Thomas (1989) and dozens of replications: top SUE quintile
drifts roughly +3-4% over 60 days, bottom SUE quintile drifts roughly
-2-3%. Curves are deterministic (slightly concave: most drift in the
first 30 days, then diminishing).

This is a *schematic* — the y-axis represents the average across many
announcements, not any single stock. The point is the asymmetry and
the persistence.

Run:
    uv run python course/image/week20_pead_drift.py
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
BASE = "week20_pead_drift"


# Deterministic drift curves over 0..60 trading days.
# Concave: cumulative = A * (1 - exp(-k*t)).
DAYS = np.arange(0, 61)
TOP_DRIFT = 3.6 * (1.0 - np.exp(-DAYS / 22.0))   # asymptote ~+3.6%
BOT_DRIFT = -2.9 * (1.0 - np.exp(-DAYS / 22.0))  # asymptote ~-2.9%
MID_DRIFT = 0.10 * (1.0 - np.exp(-DAYS / 30.0))  # near-zero middle quintile


LANG_STRINGS = {
    "en": {
        "title":    "Post-Earnings-Announcement Drift, top vs bottom surprise quintiles",
        "subtitle": "Schematic average cumulative abnormal return in the 60 trading days after the earnings release. Pattern documented since Bernard & Thomas (1989) and replicated many times.",
        "xlabel":   "Trading days after announcement (Day 0 = earnings release)",
        "ylabel":   "Cumulative abnormal return (%)",
        "top":      "Top quintile (positive surprise)",
        "mid":      "Middle quintile (in-line)",
        "bot":      "Bottom quintile (negative surprise)",
        "anno_top": "+3.6% drift in 60 days\n(no further news, just absorption)",
        "anno_bot": "-2.9% drift in 60 days",
        "footer":   "The market reaction on Day 0 is incomplete. The remaining drift is the alpha that careful investors capture.",
    },
    "hk": {
        "title":    "盈利公佈後漂移:正面與負面驚喜五分位",
        "subtitle": "盈利公佈後 60 個交易日的平均累計超額回報示意圖。Bernard & Thomas (1989) 紀錄並多次重現。",
        "xlabel":   "公佈後交易日(第 0 日 = 公佈當日)",
        "ylabel":   "累計超額回報(%)",
        "top":      "正面驚喜五分位",
        "mid":      "符合預期五分位",
        "bot":      "負面驚喜五分位",
        "anno_top": "60 日漂移 +3.6%\n(無新消息,只是市場慢慢消化)",
        "anno_bot": "60 日漂移 -2.9%",
        "footer":   "公佈當日的反應並不完整。剩下的漂移正是用心投資者可以收集的 alpha。",
    },
    "tw": {
        "title":    "盈餘公布後漂移:正面與負面驚奇五分位",
        "subtitle": "盈餘公布後 60 個交易日的平均累計超額報酬示意圖。Bernard & Thomas (1989) 提出並多次重現。",
        "xlabel":   "公布後交易日(第 0 日 = 公布當日)",
        "ylabel":   "累計超額報酬(%)",
        "top":      "正面驚奇五分位",
        "mid":      "符合預期五分位",
        "bot":      "負面驚奇五分位",
        "anno_top": "60 日漂移 +3.6%\n(無新消息,只是市場慢慢消化)",
        "anno_bot": "60 日漂移 -2.9%",
        "footer":   "公布當日的反應並不完整。剩下的漂移正是用心投資者可以收集的 alpha。",
    },
    "cn": {
        "title":    "盈利公布后漂移:正面与负面惊喜五分位",
        "subtitle": "盈利公布后 60 个交易日的平均累计超额回报示意图。Bernard & Thomas (1989) 记录并多次重现。",
        "xlabel":   "公布后交易日(第 0 日 = 公布当日)",
        "ylabel":   "累计超额回报(%)",
        "top":      "正面惊喜五分位",
        "mid":      "符合预期五分位",
        "bot":      "负面惊喜五分位",
        "anno_top": "60 日漂移 +3.6%\n(无新消息,仅是市场慢慢消化)",
        "anno_bot": "60 日漂移 -2.9%",
        "footer":   "公布当日的反应并不完整。剩下的漂移正是用心投资者可以收集的 alpha。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2))
    style_axes(ax, p)

    ax.fill_between(DAYS, 0, TOP_DRIFT, color=p["green"], alpha=0.10)
    ax.fill_between(DAYS, BOT_DRIFT, 0, color=p["red"], alpha=0.10)

    ax.plot(DAYS, TOP_DRIFT, color=p["green"], linewidth=2.6, label=s["top"])
    ax.plot(DAYS, MID_DRIFT, color=p["muted"], linewidth=1.6, linestyle="--",
            label=s["mid"])
    ax.plot(DAYS, BOT_DRIFT, color=p["red"], linewidth=2.6, label=s["bot"])

    ax.axhline(0, color=p["muted"], linewidth=0.8)
    ax.axvline(0, color=p["fg"], linewidth=0.8, linestyle=":")

    # Annotate endpoints
    ax.annotate(
        s["anno_top"],
        xy=(60, TOP_DRIFT[-1]),
        xytext=(34, 4.0),
        fontsize=9.5, color=p["fg"],
        arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8),
    )
    ax.annotate(
        s["anno_bot"],
        xy=(60, BOT_DRIFT[-1]),
        xytext=(34, -4.0),
        fontsize=9.5, color=p["fg"],
        arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8),
    )

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(-1, 64)
    ax.set_ylim(-5.0, 5.0)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60])
    ax.set_yticks([-4, -2, 0, 2, 4])
    ax.set_yticklabels(["-4%", "-2%", "0%", "+2%", "+4%"])

    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontstyle="italic")

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
