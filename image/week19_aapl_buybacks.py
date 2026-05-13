"""Week 19, §2.4 — Apple share count and dollar buybacks, FY2013-FY2024.

Two-panel chart:
    Top: diluted weighted-average shares outstanding (split-adjusted, billions),
         declining from ~26.5B in FY2013 to ~15.4B in FY2024.
    Bottom: dollar buybacks per fiscal year ($B), with the cumulative spend
         annotated.

Constants are approximate published 10-K values (split-adjusted to the
post-2020 4-for-1 basis).

Run:
    uv run python course/image/week19_aapl_buybacks.py
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
BASE = "week19_aapl_buybacks"

# Fiscal years (Apple FY ends late September).
YEARS = list(range(2013, 2025))

# Diluted weighted-average shares outstanding, split-adjusted to the
# post-Aug-2020 4-for-1 basis, in billions. Approx 10-K values.
SHARES = [
    26.47,  # 2013
    25.72,  # 2014
    23.17,  # 2015
    21.88,  # 2016
    21.00,  # 2017 (~20.87)
    20.00,  # 2018
    18.60,  # 2019
    17.53,  # 2020
    16.86,  # 2021
    16.32,  # 2022
    15.81,  # 2023
    15.41,  # 2024
]

# Dollar buybacks per fiscal year, in $ billions (approx 10-K cash-flow
# statement, common-stock repurchases line).
BUYBACKS = [
    22.9,   # 2013
    45.0,   # 2014
    35.3,   # 2015
    29.0,   # 2016
    33.0,   # 2017
    72.7,   # 2018
    66.9,   # 2019
    72.4,   # 2020
    85.5,   # 2021
    89.4,   # 2022
    77.6,   # 2023
    94.9,   # 2024
]

CUM_TOTAL = sum(BUYBACKS)  # ~ $724B


LANG_STRINGS = {
    "en": {
        "title":    "Apple's silent compounder: shares retired, FY2013-FY2024",
        "subtitle": "Diluted weighted-average shares outstanding (split-adjusted) and dollar buybacks per fiscal year. Same business, smaller denominator.",
        "ylabel_top":    "Shares outstanding (billions, split-adjusted)",
        "ylabel_bot":    "Buybacks ($ billions)",
        "xlabel":        "Fiscal year",
        "split_note":    "4-for-1 split (Aug 2020)",
        "footer":   "FY2013 to FY2024: total dollars repurchased ~${tot:.0f}B. Diluted share count ~{s0:.1f}B -> ~{s1:.1f}B (-{pct:.0%}).",
    },
    "hk": {
        "title":    "蘋果的隱形複利:回購註銷股份 FY2013-FY2024",
        "subtitle": "稀釋加權平均流通股數(已調整拆股)與每年回購金額。同一個生意,更小的分母。",
        "ylabel_top":    "流通股數(十億,已調整拆股)",
        "ylabel_bot":    "回購金額(十億美元)",
        "xlabel":        "財政年度",
        "split_note":    "4 拆 1(2020 年 8 月)",
        "footer":   "FY2013 至 FY2024:累計回購約 {tot:.0f} 億美元(約 7,240 億)。稀釋股數由約 {s0:.1f} 十億減至約 {s1:.1f} 十億(-{pct:.0%})。",
    },
    "tw": {
        "title":    "蘋果的隱形複利:回購註銷股數 FY2013-FY2024",
        "subtitle": "稀釋加權平均流通股數(已調整拆股)與每年回購金額。同一門生意,更小的分母。",
        "ylabel_top":    "流通股數(十億,已調整拆股)",
        "ylabel_bot":    "回購金額(十億美元)",
        "xlabel":        "會計年度",
        "split_note":    "4 拆 1(2020 年 8 月)",
        "footer":   "FY2013 至 FY2024:累計回購約 {tot:.0f} 億美元(約 7,240 億)。稀釋股數由約 {s0:.1f} 十億減至約 {s1:.1f} 十億(-{pct:.0%})。",
    },
    "cn": {
        "title":    "苹果的隐形复利:回购注销股份 FY2013-FY2024",
        "subtitle": "稀释加权平均流通股数(已调整拆股)与每年回购金额。同一门生意,更小的分母。",
        "ylabel_top":    "流通股数(十亿,已调整拆股)",
        "ylabel_bot":    "回购金额(十亿美元)",
        "xlabel":        "财政年度",
        "split_note":    "4 拆 1(2020 年 8 月)",
        "footer":   "FY2013 至 FY2024:累计回购约 {tot:.0f} 亿美元(约 7,240 亿)。稀释股数由约 {s0:.1f} 十亿减至约 {s1:.1f} 十亿(-{pct:.0%})。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(11, 7.0), sharex=True,
        gridspec_kw={"height_ratios": [1.0, 0.85], "hspace": 0.18},
    )
    style_axes(ax_top, p)
    style_axes(ax_bot, p)

    # --- Top: shares outstanding line ----------------------------------
    ax_top.plot(YEARS, SHARES, color=p["blue"], linewidth=2.6,
                marker="o", markersize=5.5, markerfacecolor=p["blue"],
                markeredgecolor=p["bg"], markeredgewidth=1.2)
    # Endpoint labels
    ax_top.text(YEARS[0] - 0.05, SHARES[0] + 0.6,
                f"{SHARES[0]:.1f}B", color=p["blue"],
                fontsize=10, fontweight="bold", ha="left")
    ax_top.text(YEARS[-1] + 0.05, SHARES[-1] - 0.7,
                f"{SHARES[-1]:.1f}B", color=p["blue"],
                fontsize=10, fontweight="bold", ha="right")
    # Split annotation at FY2020
    ax_top.axvline(2020, color=p["muted"], linewidth=0.8,
                   linestyle="--", alpha=0.6)
    ax_top.text(2020, max(SHARES) + 0.4, s["split_note"],
                color=p["muted"], fontsize=9, ha="center",
                style="italic")

    ax_top.set_ylabel(s["ylabel_top"], fontsize=10)
    ax_top.set_ylim(13, max(SHARES) + 2.0)
    ax_top.set_title(s["title"], fontsize=14, fontweight="bold",
                     loc="left", pad=24)
    ax_top.text(0, 1.04, s["subtitle"], transform=ax_top.transAxes,
                fontsize=10, color=p["muted"])

    # --- Bottom: buyback bars ------------------------------------------
    ax_bot.bar(YEARS, BUYBACKS, color=p["accent"], edgecolor=p["accent"],
               width=0.7, alpha=0.92)
    for yr, val in zip(YEARS, BUYBACKS):
        ax_bot.text(yr, val + 1.5, f"{val:.0f}",
                    color=p["fg"], fontsize=8.5, ha="center")
    ax_bot.set_ylabel(s["ylabel_bot"], fontsize=10)
    ax_bot.set_xlabel(s["xlabel"], fontsize=10)
    ax_bot.set_xticks(YEARS)
    ax_bot.set_ylim(0, max(BUYBACKS) + 14)

    # Footer with cumulative + reduction
    pct = (SHARES[0] - SHARES[-1]) / SHARES[0]
    footer = s["footer"].format(tot=CUM_TOTAL, s0=SHARES[0],
                                s1=SHARES[-1], pct=pct)
    ax_bot.text(0, -0.22, footer, transform=ax_bot.transAxes,
                fontsize=10, color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
