"""Week 40, sec 2.1 — VIX daily history 1990 - April 2026 with crisis annotations.

FRED VIXCLS daily series. Annotates LTCM 1998, GFC 2008 peak ~89, May-2010
flash crash, Aug-2011 debt-ceiling, Feb-2018 Volmageddon, Mar-2020 COVID
all-time high 82.69, Sep-2022 Fed shock. Median line + 30-vol stress line.

Run:
    uv run python course/image/week40_vix_history.py
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
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import fred_series  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week40_vix_history"


# Crisis annotations: (date, vix_level, en_label, hk_label, tw_label, cn_label)
EVENTS = [
    ("1998-09-10", 45.7,  "1998 LTCM",        "1998 LTCM",        "1998 LTCM",        "1998 LTCM"),
    ("2008-11-20", 80.9,  "2008 GFC peak",    "2008 金融海嘯",   "2008 金融海嘯",   "2008 金融海啸"),
    ("2010-05-20", 45.8,  "2010 flash crash", "2010 閃崩",        "2010 閃崩",        "2010 闪崩"),
    ("2011-08-08", 48.0,  "2011 debt-ceiling","2011 債限",        "2011 債限",        "2011 债限"),
    ("2018-02-05", 37.3,  "Volmageddon",      "Volmageddon",      "Volmageddon",      "Volmageddon"),
    ("2020-03-16", 82.7,  "COVID ATH 82.7",   "COVID 歷高 82.7",  "COVID 歷高 82.7",  "COVID 历高 82.7"),
    ("2022-09-30", 31.6,  "2022 Fed shock",   "2022 聯儲衝擊",   "2022 聯準衝擊",   "2022 美联储冲击"),
]


# Embedded fallback monthly VIX (close-of-month) 1990-Apr 2026, used only if
# FRED is unreachable. Lightly smoothed; sufficient to render the chart.
_FALLBACK = {
    "1990-01": 26.1, "1990-07": 19.0, "1991-01": 28.2, "1991-07": 16.1,
    "1992-01": 19.3, "1993-01": 12.9, "1994-01": 11.7, "1995-01": 13.5,
    "1996-01": 13.1, "1997-01": 22.0, "1997-10": 38.2, "1998-09": 45.7,
    "1999-01": 27.6, "2000-01": 24.4, "2001-01": 25.4, "2001-09": 43.7,
    "2002-09": 42.7, "2003-01": 35.8, "2004-01": 16.6, "2005-01": 13.3,
    "2006-01": 12.4, "2007-08": 30.8, "2008-10": 80.9, "2008-11": 80.9,
    "2009-01": 44.8, "2009-07": 25.9, "2010-05": 45.8, "2011-08": 48.0,
    "2012-01": 19.4, "2013-01": 14.3, "2014-10": 26.3, "2015-08": 40.7,
    "2016-01": 28.1, "2017-08": 13.5, "2017-11": 9.14, "2018-02": 37.3,
    "2019-01": 16.6, "2020-03": 82.7, "2020-09": 26.4, "2021-01": 33.1,
    "2022-01": 24.8, "2022-09": 31.6, "2023-03": 26.5, "2023-12": 12.5,
    "2024-08": 38.6, "2024-12": 17.4, "2025-04": 28.0, "2025-12": 21.0,
    "2026-04": 19.5,
}


def _load_vix() -> pd.Series:
    try:
        df = fred_series("VIXCLS", start="1990-01-01")
        s = df["VIXCLS"].dropna()
        if s.empty:
            raise RuntimeError("empty FRED VIX")
        return s
    except Exception as e:
        print(f"FRED VIX unavailable ({e}); using embedded fallback")
        idx = pd.to_datetime([k + "-15" for k in _FALLBACK.keys()])
        return pd.Series(list(_FALLBACK.values()), index=idx).sort_index()


LANG_STRINGS = {
    "en": {
        "title":    "VIX daily close, 1990 - April 2026",
        "subtitle": "Median ~16.5 over 36 years; 7 named crises annotated. Vol-tail-wags-dog (SOUL #6).",
        "xlabel":   "Year",
        "ylabel":   "VIX (vol points)",
        "median":   "Median 16.5",
        "stress":   "Stress (VIX 30)",
        "footer":   "Source: CBOE / FRED VIXCLS. The unconditional median of VIX has been roughly stable at 16-18 since 1990.",
    },
    "hk": {
        "title":    "VIX 每日收市,1990 - 2026 年 4 月",
        "subtitle": "36 年中位數約 16.5;標註 7 次危機。波動率尾巴搖狗(SOUL #6)。",
        "xlabel":   "年份",
        "ylabel":   "VIX(vol 點)",
        "median":   "中位數 16.5",
        "stress":   "壓力線(VIX 30)",
        "footer":   "資料來源:CBOE / FRED VIXCLS。1990 年以來 VIX 無條件中位數大致穩定在 16-18。",
    },
    "tw": {
        "title":    "VIX 每日收盤,1990 - 2026 年 4 月",
        "subtitle": "36 年中位數約 16.5;標註 7 次危機。波動率尾巴搖狗(SOUL #6)。",
        "xlabel":   "年份",
        "ylabel":   "VIX(vol 點)",
        "median":   "中位數 16.5",
        "stress":   "壓力線(VIX 30)",
        "footer":   "資料來源:CBOE / FRED VIXCLS。1990 年以來 VIX 無條件中位數大致穩定在 16-18。",
    },
    "cn": {
        "title":    "VIX 每日收盘,1990 - 2026 年 4 月",
        "subtitle": "36 年中位数约 16.5;标注 7 次危机。波动率尾巴摇狗(SOUL #6)。",
        "xlabel":   "年份",
        "ylabel":   "VIX(vol 点)",
        "median":   "中位数 16.5",
        "stress":   "压力线(VIX 30)",
        "footer":   "数据来源:CBOE / FRED VIXCLS。1990 年以来 VIX 无条件中位数大致稳定在 16-18。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    vix = _load_vix()

    fig, ax = plt.subplots(figsize=(12.0, 6.2), dpi=150)
    style_axes(ax, p)

    ax.fill_between(vix.index, vix.values, color=p["red"], alpha=0.10)
    ax.plot(vix.index, vix.values, color=p["red"], linewidth=0.9)

    # Median + stress line
    median = float(np.median(vix.values))
    ax.axhline(median, color=p["muted"], linewidth=1.0, linestyle="--",
               alpha=0.85)
    ax.axhline(30.0, color=p["accent"], linewidth=0.9, linestyle=":",
               alpha=0.75)

    ax.text(vix.index[5], median + 0.8, s["median"],
            color=p["muted"], fontsize=8.5, fontweight="bold")
    ax.text(vix.index[5], 30.5, s["stress"],
            color=p["accent"], fontsize=8.5, fontweight="bold")

    # Lang -> field index in EVENTS tuple.
    lang_idx = {"en": 2, "hk": 3, "tw": 4, "cn": 5}
    li = lang_idx.get(s.get("_lang", "en"), 2)

    # Annotate each event.
    for ev in EVENTS:
        date = pd.to_datetime(ev[0])
        level = ev[1]
        label = ev[li]
        ax.plot([date], [level], "o", color=p["fg"], markersize=5,
                markerfacecolor=p["accent"], zorder=5)
        ax.annotate(
            f"{label}\n{level:.0f}",
            xy=(date, level),
            xytext=(0, 22),
            textcoords="offset points",
            ha="center",
            fontsize=8.3,
            color=p["fg"],
            fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=p["muted"],
                            linewidth=0.6, alpha=0.7),
        )

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, 95)
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"])

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


def _build_fig_with_lang(lang_strings_for_locale, lang_code):
    # Inject locale into strings for build_fig closure.
    s2 = dict(lang_strings_for_locale)
    s2["_lang"] = lang_code
    return build_fig(s2)


if __name__ == "__main__":
    # render_for_all_locales calls build_fig(s); we need to know the lang
    # in build_fig to pick the right annotation labels. We tag each locale
    # block with _lang then strip on render.
    for lc in ("en", "hk", "tw", "cn"):
        LANG_STRINGS[lc]["_lang"] = lc
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
