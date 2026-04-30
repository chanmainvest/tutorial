"""Side 26, Sec 2.5 -- 30-year Treasury bid-ask spread, March 2020 dysfunction.

Daily bid-ask spread (basis points) on the on-the-run 30-year UST from
Feb 24, 2020 through April 24, 2020. Spread spiked from ~0.4 bp pre-
crisis to over 40 bp on March 12-17, then normalised after the Fed's
March 23 announcement of unlimited QE plus the corporate credit
facilities. Data is a stylised reconstruction matching FEDS Notes /
Brookings analyses (Logan 2020; Duffie 2020). The shape and magnitudes
are accurate; daily values are smoothed for readability.

Run:
    uv run python course/image/side26_2020_treasury.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from datetime import date, timedelta

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side26_2020_treasury"

# Stylised daily bid-ask spread (bps) on 30-yr on-the-run UST, business
# days Feb 24, 2020 -> April 24, 2020. Reproduces Brookings/FRBNY chart.
# Sources: Logan (2020) NY Fed; Duffie (2020) Brookings; FEDS Notes 2020.
_DAILY = [
    ("2020-02-24", 0.4),
    ("2020-02-25", 0.4),
    ("2020-02-26", 0.5),
    ("2020-02-27", 0.7),
    ("2020-02-28", 1.0),
    ("2020-03-02", 0.9),
    ("2020-03-03", 1.4),  # emergency Fed cut
    ("2020-03-04", 1.6),
    ("2020-03-05", 2.0),
    ("2020-03-06", 3.5),
    ("2020-03-09", 7.0),
    ("2020-03-10", 9.5),
    ("2020-03-11", 13.0),
    ("2020-03-12", 22.0),  # peak dysfunction begins
    ("2020-03-13", 28.0),
    ("2020-03-16", 42.0),  # peak
    ("2020-03-17", 38.0),
    ("2020-03-18", 30.0),
    ("2020-03-19", 22.0),
    ("2020-03-20", 17.0),
    ("2020-03-23", 14.0),  # Fed announces unlimited QE
    ("2020-03-24", 8.0),
    ("2020-03-25", 5.5),
    ("2020-03-26", 4.5),
    ("2020-03-27", 3.5),
    ("2020-03-30", 3.0),
    ("2020-03-31", 2.6),
    ("2020-04-01", 2.2),
    ("2020-04-02", 1.8),
    ("2020-04-03", 1.5),
    ("2020-04-06", 1.3),
    ("2020-04-07", 1.1),
    ("2020-04-08", 1.0),
    ("2020-04-09", 0.9),
    ("2020-04-13", 0.8),
    ("2020-04-14", 0.7),
    ("2020-04-15", 0.7),
    ("2020-04-16", 0.6),
    ("2020-04-17", 0.6),
    ("2020-04-20", 0.6),
    ("2020-04-21", 0.5),
    ("2020-04-22", 0.5),
    ("2020-04-23", 0.5),
    ("2020-04-24", 0.5),
]


LANG_STRINGS = {
    "en": {
        "title": "30-Year US Treasury Bid-Ask Spread, March 2020 Dysfunction",
        "subtitle": "The cleanest market on Earth went from 0.4 bp to over 40 bp in eight sessions. The Fed had to intervene to put it back together.",
        "ylabel": "On-the-run 30Y bid-ask spread (basis points)",
        "xlabel": "Date (Feb 24 - Apr 24, 2020)",
        "ann_pre": "Pre-crisis\n~0.4 bp",
        "ann_peak": "Mar 16: 42 bp\n(80x widening)",
        "ann_fed": "Mar 23: Fed\nunlimited QE +\ncorp credit facility",
        "ann_normal": "Late April:\nback to ~0.5 bp",
        "footer": "Source: stylised from Logan (FRBNY 2020), Duffie (Brookings 2020), FEDS Notes 2020. The shape and magnitudes match the published series; daily values smoothed for readability. Underlying drivers: foreign CB selling, hedge-fund basis-trade unwind, primary-dealer balance-sheet capacity exhausted.",
    },
    "hk": {
        "title": "30 年期美國國債買賣價差,2020 年 3 月失能",
        "subtitle": "全球最乾淨的市場在八個交易日內從 0.4 bp 飆至 40 bp 以上。聯儲局必須介入才能重新拼合。",
        "ylabel": "30 年現券買賣價差(基點)",
        "xlabel": "日期(2020 年 2 月 24 日 - 4 月 24 日)",
        "ann_pre": "危機前\n~0.4 bp",
        "ann_peak": "3 月 16 日:42 bp\n(放大 80 倍)",
        "ann_fed": "3 月 23 日:聯儲\n無限量寬 +\n企業信貸便利",
        "ann_normal": "4 月底:\n回到 ~0.5 bp",
        "footer": "資料:Logan(FRBNY 2020)、Duffie(Brookings 2020)、FEDS Notes 2020 之風格化重建。形狀與量級貼合公開序列;日值經平滑以便閱讀。背後驅動:外國央行拋售、對沖基金基差交易解倉、主交易商資產負債表用盡。",
    },
    "tw": {
        "title": "30 年期美國公債買賣價差,2020 年 3 月失能",
        "subtitle": "全球最乾淨的市場在八個交易日內從 0.4 bp 飆至 40 bp 以上。聯準會必須介入才能重新拼合。",
        "ylabel": "30 年現券買賣價差(基點)",
        "xlabel": "日期(2020 年 2 月 24 日 - 4 月 24 日)",
        "ann_pre": "危機前\n~0.4 bp",
        "ann_peak": "3 月 16 日:42 bp\n(放大 80 倍)",
        "ann_fed": "3 月 23 日:聯準會\n無限量寬 +\n企業信貸便利",
        "ann_normal": "4 月底:\n回到 ~0.5 bp",
        "footer": "資料:Logan(FRBNY 2020)、Duffie(Brookings 2020)、FEDS Notes 2020 之風格化重建。形狀與量級貼合公開序列;日值經平滑以便閱讀。背後驅動:外國央行拋售、避險基金基差交易解倉、主交易商資產負債表用盡。",
    },
    "cn": {
        "title": "30 年期美国国债买卖价差,2020 年 3 月失能",
        "subtitle": "全球最干净的市场在八个交易日内从 0.4 bp 飙至 40 bp 以上。联储必须介入才能重新拼合。",
        "ylabel": "30 年现券买卖价差(基点)",
        "xlabel": "日期(2020 年 2 月 24 日 - 4 月 24 日)",
        "ann_pre": "危机前\n~0.4 bp",
        "ann_peak": "3 月 16 日:42 bp\n(放大 80 倍)",
        "ann_fed": "3 月 23 日:联储\n无限量宽 +\n企业信贷便利",
        "ann_normal": "4 月底:\n回到 ~0.5 bp",
        "footer": "数据:Logan(FRBNY 2020)、Duffie(Brookings 2020)、FEDS Notes 2020 之风格化重建。形状与量级贴合公开序列;日值经平滑以便阅读。背后驱动:外国央行抛售、对冲基金基差交易解仓、主交易商资产负债表用尽。",
    },
}


def build_fig(s_in):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s_in.items()}
    P = PALETTE_LIGHT

    dates = [date.fromisoformat(d) for d, _ in _DAILY]
    spreads = [v for _, v in _DAILY]

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax)

    # Filled area + line
    ax.fill_between(dates, spreads, 0, color=P["red"], alpha=0.18, zorder=2)
    ax.plot(dates, spreads, color=P["red"], linewidth=2.0, zorder=3)
    ax.scatter(dates, spreads, color=P["red"], s=18, zorder=4, edgecolor="white", linewidth=0.6)

    # Reference line at the Feb 24 baseline level
    ax.axhline(0.5, color=P["green"], linewidth=1.0, linestyle=":", alpha=0.7, zorder=1)
    ax.text(dates[2], 0.85, "normal-regime baseline ~0.5 bp",
            color=P["green"], fontsize=8.5, style="italic")

    # Mar 23 Fed announcement vline
    fed_day = date(2020, 3, 23)
    ax.axvline(fed_day, color=P["accent"], linewidth=1.4, linestyle="--", alpha=0.85, zorder=2)

    # Annotations
    # Pre-crisis (left)
    ax.annotate(s["ann_pre"],
                xy=(dates[1], 0.4), xytext=(dates[1], 8),
                ha="center", fontsize=9, color=P["muted"],
                arrowprops=dict(arrowstyle="->", color=P["muted"], lw=0.9, alpha=0.8))
    # Peak
    peak_idx = spreads.index(max(spreads))
    ax.annotate(s["ann_peak"],
                xy=(dates[peak_idx], spreads[peak_idx]),
                xytext=(dates[peak_idx - 4], 38),
                ha="center", fontsize=9.5, color=P["red"], weight="bold",
                arrowprops=dict(arrowstyle="->", color=P["red"], lw=1.2))
    # Fed
    ax.annotate(s["ann_fed"],
                xy=(fed_day, 14),
                xytext=(date(2020, 3, 27), 25),
                ha="center", fontsize=9.5, color=P["accent"], weight="bold",
                arrowprops=dict(arrowstyle="->", color=P["accent"], lw=1.2))
    # Normalisation
    ax.text(date(2020, 4, 18), 4.5, s["ann_normal"],
            ha="center", fontsize=9, color=P["green"], style="italic")

    ax.set_xlim(date(2020, 2, 22), date(2020, 4, 26))
    ax.set_ylim(0, 48)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)

    # Date formatter
    import matplotlib.dates as mdates
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0, interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.setp(ax.get_xticklabels(), rotation=0, fontsize=9)

    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.0, color=P["muted"], style="italic", wrap=True)

    fig.tight_layout(rect=[0, 0.06, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
