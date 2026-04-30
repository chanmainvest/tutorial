"""Week 33, §2.5 — High-yield OAS history, 1997 to April 2026.

Plots the ICE BofA US High Yield Index option-adjusted spread (FRED
series BAMLH0A0HYM2) and annotates the four panic prints. Falls back to
an embedded annual-peak series if FRED is unreachable.

Run:
    uv run python course/image/week33_hy_spread_history.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import _http_get, cache_path, _save_df, _load_df, _cache_fresh  # noqa: E402
import io  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week33_hy_spread_history"


# Embedded monthly HY OAS samples (decimal percent, ie 10.0 == 1000bps),
# constructed from FRED BAMLH0A0HYM2 month-end values. Used only if the
# FRED fetch fails. Covers Jan 1997 - Apr 2026 at quarterly granularity
# with extra detail near the four panic prints.
_FALLBACK = [
    ("1997-01", 3.4), ("1997-07", 3.0), ("1998-01", 3.0), ("1998-07", 3.5),
    ("1998-10", 7.5), ("1999-01", 5.7), ("1999-07", 5.0), ("2000-01", 5.6),
    ("2000-07", 6.0), ("2000-12", 9.4), ("2001-04", 8.6), ("2001-10", 9.6),
    ("2002-04", 8.6), ("2002-07", 9.8), ("2002-10",10.4), ("2003-01", 8.4),
    ("2003-07", 5.6), ("2004-01", 4.0), ("2004-07", 3.7), ("2005-01", 3.2),
    ("2005-07", 3.4), ("2006-01", 3.3), ("2006-07", 3.4), ("2007-01", 2.8),
    ("2007-06", 2.6), ("2007-12", 5.7), ("2008-03", 7.9), ("2008-06", 6.6),
    ("2008-09", 9.6), ("2008-11",21.8), ("2008-12",18.7), ("2009-03",17.5),
    ("2009-06",10.8), ("2009-12", 6.4), ("2010-06", 7.2), ("2010-12", 5.5),
    ("2011-06", 5.5), ("2011-09", 8.8), ("2012-01", 7.0), ("2012-07", 6.4),
    ("2013-01", 5.1), ("2013-07", 4.7), ("2014-01", 3.9), ("2014-07", 3.6),
    ("2014-12", 5.2), ("2015-06", 5.1), ("2015-12", 6.9), ("2016-02", 8.4),
    ("2016-12", 4.0), ("2017-06", 3.7), ("2017-12", 3.4), ("2018-06", 3.6),
    ("2018-12", 5.3), ("2019-06", 4.0), ("2019-12", 3.4), ("2020-02", 5.0),
    ("2020-03",10.9), ("2020-06", 6.4), ("2020-12", 3.9), ("2021-06", 3.0),
    ("2021-12", 3.1), ("2022-03", 3.5), ("2022-06", 5.7), ("2022-09", 5.5),
    ("2022-10", 5.0), ("2023-03", 5.2), ("2023-06", 4.0), ("2023-12", 3.3),
    ("2024-06", 3.2), ("2024-12", 2.9), ("2025-04", 4.2), ("2025-12", 3.6),
    ("2026-04", 5.0),
]

# Annotation events: (date_str, spread_pct, label_key, dx_years, dy_pct)
EVENTS = [
    ("2002-10", 10.4, "ann_2002",  +2.5,  +5.0),
    ("2008-11", 21.8, "ann_2008",  -3.0,  -3.0),
    ("2020-03", 10.9, "ann_2020",  +2.5,  +6.5),
    ("2022-10",  5.0, "ann_2022",  +2.0,  +6.0),
    ("2026-04",  5.0, "ann_2026",  -3.5,  +3.5),
]


def _load_series() -> pd.Series:
    """Fetch full BAMLH0A0HYM2 history with cosd parameter, fallback to embedded."""
    sid = "BAMLH0A0HYM2"
    p = cache_path(f"fred_{sid}_full")
    try:
        if not _cache_fresh(p):
            url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd=1996-12-31"
            raw = _http_get(url)
            df = pd.read_csv(io.BytesIO(raw))
            df[df.columns[1]] = pd.to_numeric(df[df.columns[1]], errors="coerce")
            df = df.dropna(subset=[df.columns[1]])
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df = df.set_index(df.columns[0])
            df.columns = [sid]
            _save_df(df, p)
        else:
            df = _load_df(p)
        s = df[sid].dropna()
        if s.index.min() > pd.Timestamp("2000-01-01"):
            raise RuntimeError("FRED returned truncated history")
        return s
    except Exception:
        idx = pd.to_datetime([d for d, _ in _FALLBACK])
        vals = [v for _, v in _FALLBACK]
        return pd.Series(vals, index=idx).sort_index()


LANG_STRINGS = {
    "en": {
        "title":    "ICE BofA US High Yield OAS, 1997 to April 2026",
        "subtitle": "Four panic prints since 1997. Each one was a two-year buying window. Apr 2026 is fairly priced.",
        "ylabel":   "Option-adjusted spread (%)",
        "xlabel":   "Year",
        "panic":    "Panic > 1000 bps",
        "avg":      "Long-run avg ~520 bps",
        "complacent": "Complacency < 350 bps",
        "ann_2002": "2002\nTelecom / Enron\n~1040 bps",
        "ann_2008": "2008\nLehman / GFC\n~2180 bps",
        "ann_2020": "2020\nCOVID\n~1090 bps",
        "ann_2022": "2022\nFed hikes\n~600 bps",
        "ann_2026": "Apr 2026\n~500 bps",
        "footer":   "Source: FRED series BAMLH0A0HYM2 (ICE BofA US High Yield Index OAS).",
    },
    "hk": {
        "title":    "ICE BofA 美國高收益 OAS,1997 至 2026 年 4 月",
        "subtitle": "1997 年以來四次恐慌打點,每次都是兩年的買入窗口。2026 年 4 月屬合理定價。",
        "ylabel":   "期權調整利差(%)",
        "xlabel":   "年份",
        "panic":    "恐慌 > 1000 點",
        "avg":      "長期平均約 520 點",
        "complacent": "鬆懈 < 350 點",
        "ann_2002": "2002\n電訊 / 安然\n約 1040 點",
        "ann_2008": "2008\n雷曼 / 金融海嘯\n約 2180 點",
        "ann_2020": "2020\n新冠\n約 1090 點",
        "ann_2022": "2022\n聯儲加息\n約 600 點",
        "ann_2026": "2026 年 4 月\n約 500 點",
        "footer":   "資料:FRED 系列 BAMLH0A0HYM2(ICE BofA 美國高收益指數 OAS)。",
    },
    "tw": {
        "title":    "ICE BofA 美國高收益 OAS,1997 至 2026 年 4 月",
        "subtitle": "1997 年以來四次恐慌打點,每次都是兩年的買進窗口。2026 年 4 月屬合理定價。",
        "ylabel":   "選擇權調整利差(%)",
        "xlabel":   "年份",
        "panic":    "恐慌 > 1000 點",
        "avg":      "長期平均約 520 點",
        "complacent": "鬆懈 < 350 點",
        "ann_2002": "2002\n電信 / 安隆\n約 1040 點",
        "ann_2008": "2008\n雷曼 / 金融海嘯\n約 2180 點",
        "ann_2020": "2020\nCOVID\n約 1090 點",
        "ann_2022": "2022\n聯準會升息\n約 600 點",
        "ann_2026": "2026 年 4 月\n約 500 點",
        "footer":   "資料:FRED 系列 BAMLH0A0HYM2(ICE BofA 美國高收益指數 OAS)。",
    },
    "cn": {
        "title":    "ICE BofA 美国高收益 OAS,1997 至 2026 年 4 月",
        "subtitle": "1997 年以来四次恐慌打点,每次都是两年的买入窗口。2026 年 4 月属于合理定价。",
        "ylabel":   "期权调整利差(%)",
        "xlabel":   "年份",
        "panic":    "恐慌 > 1000 点",
        "avg":      "长期平均约 520 点",
        "complacent": "松懈 < 350 点",
        "ann_2002": "2002\n电信 / 安然\n约 1040 点",
        "ann_2008": "2008\n雷曼 / 金融危机\n约 2180 点",
        "ann_2020": "2020\n新冠\n约 1090 点",
        "ann_2022": "2022\n美联储加息\n约 600 点",
        "ann_2026": "2026 年 4 月\n约 500 点",
        "footer":   "资料:FRED 系列 BAMLH0A0HYM2(ICE BofA 美国高收益指数 OAS)。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    series = _load_series()
    fig, ax = plt.subplots(figsize=(12, 6.4))
    style_axes(ax, p)

    ax.fill_between(series.index, 0, series.values,
                    color=p["red"], alpha=0.18, linewidth=0)
    ax.plot(series.index, series.values,
            color=p["red"], linewidth=1.4)

    # Reference bands
    ax.axhline(10.0, color=p["red"], linewidth=0.9, linestyle="--", alpha=0.7)
    ax.axhline(5.2,  color=p["accent"], linewidth=0.9, linestyle="--", alpha=0.7)
    ax.axhline(3.5,  color=p["green"], linewidth=0.9, linestyle="--", alpha=0.7)

    ax.text(pd.Timestamp("1997-03-01"), 10.3, s["panic"],
            color=p["red"], fontsize=9, fontweight="bold", va="bottom")
    ax.text(pd.Timestamp("1997-03-01"), 5.5, s["avg"],
            color=p["accent"], fontsize=9, fontweight="bold", va="bottom")
    ax.text(pd.Timestamp("1997-03-01"), 3.7, s["complacent"],
            color=p["green"], fontsize=9, fontweight="bold", va="bottom")

    # Event annotations
    for date_str, sp, key, dx_years, dy_pct in EVENTS:
        x = pd.Timestamp(date_str)
        x_text = x + pd.DateOffset(years=int(dx_years), months=int((dx_years % 1) * 12))
        y_text = sp + dy_pct
        ax.annotate(s[key],
                    xy=(x, sp), xytext=(x_text, y_text),
                    ha="center", va="center",
                    fontsize=8.8, color=p["fg"], fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.3",
                              facecolor=p["bg"], edgecolor=p["muted"],
                              linewidth=0.7),
                    arrowprops=dict(arrowstyle="->", color=p["muted"],
                                    lw=0.9, connectionstyle="arc3,rad=0.1"))

    ax.set_xlim(pd.Timestamp("1996-12-01"), pd.Timestamp("2026-08-01"))
    ax.set_ylim(0, 25)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
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
