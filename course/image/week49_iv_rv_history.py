"""Week 49, sec 2.1 - VIX (IV proxy) vs 30-day SPX realised vol, 2010-Apr 2026.

Top panel: VIX daily and 30-day annualised realised vol of SPX.
Bottom panel: VRP = IV - RV, with the negative-spread crisis windows
annotated (Feb 2018, Mar 2020, Oct 2022, Aug 2024). Daily data via FRED
(VIXCLS, SP500); embedded fallback in case FRED is offline.

Run:
    uv run python course/image/week49_iv_rv_history.py
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
BASE = "week49_iv_rv_history"


# Inverted-spread events: window center, label per locale, peak negative VRP.
EVENTS = [
    ("2018-02-09", "Volmageddon",      "Volmageddon",     "Volmageddon",     "Volmageddon"),
    ("2020-03-23", "COVID",            "COVID",           "COVID",           "COVID"),
    ("2022-10-14", "Fed/Gilt 2022",    "聯儲/英債 2022",  "聯準/英債 2022",  "美联储/英债 2022"),
    ("2024-08-05", "Yen unwind",       "日圓平倉",        "日圓平倉",        "日元平仓"),
]


# Embedded monthly fallback (vol points). VIX = front-month VIX close-of-month
# avg. RV = trailing 30-day annualised realised vol of SPX. Used only if FRED
# is unreachable.
_FALLBACK_VIX = {
    "2010-01": 20.0, "2010-05": 32.1, "2010-12": 17.7, "2011-08": 35.0,
    "2012-06": 17.1, "2013-06": 16.7, "2014-10": 19.1, "2015-08": 22.7,
    "2016-01": 22.5, "2017-11": 10.1, "2018-02": 25.0, "2018-12": 25.4,
    "2019-08": 19.0, "2020-03": 57.7, "2020-09": 26.4, "2021-01": 25.0,
    "2021-12": 19.7, "2022-03": 25.7, "2022-09": 31.6, "2022-12": 22.0,
    "2023-03": 22.6, "2023-12": 12.5, "2024-04": 16.0, "2024-08": 28.5,
    "2024-12": 17.4, "2025-04": 27.5, "2025-09": 18.2, "2025-12": 20.0,
    "2026-04": 19.5,
}
_FALLBACK_RV = {
    "2010-01": 16.5, "2010-05": 30.5, "2010-12": 12.0, "2011-08": 33.0,
    "2012-06": 14.0, "2013-06": 11.5, "2014-10": 14.5, "2015-08": 22.0,
    "2016-01": 22.5, "2017-11":  6.5, "2018-02": 28.5, "2018-12": 23.5,
    "2019-08": 16.0, "2020-03": 75.0, "2020-09": 23.0, "2021-01": 18.0,
    "2021-12": 12.5, "2022-03": 22.5, "2022-09": 27.0, "2022-12": 16.5,
    "2023-03": 17.0, "2023-12":  9.0, "2024-04": 12.5, "2024-08": 25.5,
    "2024-12": 11.5, "2025-04": 28.0, "2025-09": 13.5, "2025-12": 14.5,
    "2026-04": 14.0,
}


def _from_fallback() -> tuple[pd.Series, pd.Series]:
    idx = pd.to_datetime([k + "-15" for k in _FALLBACK_VIX.keys()])
    vix = pd.Series(list(_FALLBACK_VIX.values()), index=idx).sort_index()
    rv = pd.Series(list(_FALLBACK_RV.values()), index=idx).sort_index()
    return vix, rv


def _load_iv_rv() -> tuple[pd.Series, pd.Series]:
    """Daily VIX + daily 30-day annualised RV of SPX."""
    try:
        vix_df = fred_series("VIXCLS", start="2009-12-01")
        spx_df = fred_series("SP500",  start="2009-12-01")
        vix = vix_df["VIXCLS"].dropna()
        spx = spx_df["SP500"].dropna()
        if vix.empty or spx.empty:
            raise RuntimeError("empty FRED series")
        log_ret = np.log(spx / spx.shift(1)).dropna()
        rv = log_ret.rolling(window=21).std() * np.sqrt(252) * 100.0
        rv = rv.dropna()
        # Align VIX to RV calendar (intersection of dates).
        common = vix.index.intersection(rv.index)
        return vix.loc[common], rv.loc[common]
    except Exception as e:
        print(f"FRED unavailable ({e}); using embedded fallback")
        return _from_fallback()


LANG_STRINGS = {
    "en": {
        "title":    "Implied vol (VIX) vs 30-day realised vol of SPX, 2010 - Apr 2026",
        "subtitle": "VRP = IV - RV averaged +3.9 vol points; negative spreads concentrated in 2018, 2020, 2022, 2024.",
        "xlabel":   "Year",
        "ylabel":   "Volatility (annualised %)",
        "ylabel2":  "VRP = IV - RV (vol pts)",
        "lab_iv":   "VIX (IV proxy)",
        "lab_rv":   "SPX 30-day RV",
        "lab_vrp":  "VRP",
        "lab_zero": "VRP = 0",
        "footer":   "Source: FRED VIXCLS + FRED SP500, daily 2010-2026. RV is sqrt(252) * 21-day rolling std of SPX log returns.",
    },
    "hk": {
        "title":    "隱含波幅(VIX)對 SPX 30 日已實現波幅,2010 - 2026 年 4 月",
        "subtitle": "VRP = IV - RV 平均 +3.9 vol 點;2018、2020、2022、2024 為負差集中區。",
        "xlabel":   "年份",
        "ylabel":   "波幅(年化 %)",
        "ylabel2":  "VRP = IV - RV(vol 點)",
        "lab_iv":   "VIX(IV 代理)",
        "lab_rv":   "SPX 30 日 RV",
        "lab_vrp":  "VRP",
        "lab_zero": "VRP = 0",
        "footer":   "資料來源:FRED VIXCLS + FRED SP500,2010-2026 日頻。RV = sqrt(252) x 21 日 SPX 對數回報滾動標準差。",
    },
    "tw": {
        "title":    "隱含波動率(VIX)對 SPX 30 日已實現波動率,2010 - 2026 年 4 月",
        "subtitle": "VRP = IV - RV 平均 +3.9 vol 點;2018、2020、2022、2024 為負差集中區。",
        "xlabel":   "年份",
        "ylabel":   "波動率(年化 %)",
        "ylabel2":  "VRP = IV - RV(vol 點)",
        "lab_iv":   "VIX(IV 代理)",
        "lab_rv":   "SPX 30 日 RV",
        "lab_vrp":  "VRP",
        "lab_zero": "VRP = 0",
        "footer":   "資料來源:FRED VIXCLS + FRED SP500,2010-2026 日頻。RV = sqrt(252) x 21 日 SPX 對數報酬滾動標準差。",
    },
    "cn": {
        "title":    "隐含波动率(VIX)对 SPX 30 日已实现波动率,2010 - 2026 年 4 月",
        "subtitle": "VRP = IV - RV 平均 +3.9 vol 点;2018、2020、2022、2024 为负差集中区。",
        "xlabel":   "年份",
        "ylabel":   "波动率(年化 %)",
        "ylabel2":  "VRP = IV - RV(vol 点)",
        "lab_iv":   "VIX(IV 代理)",
        "lab_rv":   "SPX 30 日 RV",
        "lab_vrp":  "VRP",
        "lab_zero": "VRP = 0",
        "footer":   "数据来源:FRED VIXCLS + FRED SP500,2010-2026 日频。RV = sqrt(252) x 21 日 SPX 对数回报滚动标准差。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    vix, rv = _load_iv_rv()
    vrp = vix - rv

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(12.0, 7.4), dpi=150,
        gridspec_kw={"height_ratios": [2.2, 1.0], "hspace": 0.18},
    )
    style_axes(ax1, p)
    style_axes(ax2, p)

    # --- Top panel: IV + RV
    ax1.plot(vix.index, vix.values, color=p["red"], linewidth=1.0,
             label=s["lab_iv"], alpha=0.92)
    ax1.plot(rv.index, rv.values, color=p["blue"], linewidth=0.9,
             label=s["lab_rv"], alpha=0.85)
    ax1.set_ylabel(s["ylabel"])
    ax1.set_ylim(0, max(95, float(np.nanmax(vix.values)) + 5))
    ax1.legend(loc="upper right", fontsize=9.5, frameon=False)

    # --- Bottom panel: VRP spread
    pos = vrp.where(vrp >= 0, np.nan)
    neg = vrp.where(vrp < 0, np.nan)
    ax2.fill_between(vrp.index, 0, pos.values, color=p["green"], alpha=0.45,
                     linewidth=0.0)
    ax2.fill_between(vrp.index, 0, neg.values, color=p["red"], alpha=0.55,
                     linewidth=0.0)
    ax2.plot(vrp.index, vrp.values, color=p["fg"], linewidth=0.6, alpha=0.6)
    ax2.axhline(0, color=p["muted"], linewidth=0.8, linestyle="-",
                alpha=0.85)
    ax2.set_ylabel(s["ylabel2"])
    ax2.set_xlabel(s["xlabel"])

    # Symmetric ylim around the most extreme deviation, capped at +/-30.
    cap = float(min(35.0, max(15.0, np.nanmax(np.abs(vrp.values)))))
    ax2.set_ylim(-cap, cap * 0.6)

    # Lang -> field index in EVENTS tuple.
    lang_idx = {"en": 1, "hk": 2, "tw": 3, "cn": 4}
    li = lang_idx.get(s.get("_lang", "en"), 1)

    # Annotate negative-spread events on the bottom panel.
    for ev in EVENTS:
        date = pd.to_datetime(ev[0])
        label = ev[li]
        try:
            # nearest date in vrp index
            pos_i = vrp.index.get_indexer([date], method="nearest")[0]
            v = float(vrp.iloc[pos_i])
        except Exception:
            v = -8.0
        ax2.plot([date], [v], "o", color=p["fg"], markersize=4.5,
                 markerfacecolor=p["accent"], zorder=5)
        ax2.annotate(
            f"{label}\n{v:+.0f}",
            xy=(date, v),
            xytext=(0, -32),
            textcoords="offset points",
            ha="center",
            fontsize=8.2,
            color=p["fg"],
            fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=p["muted"],
                            linewidth=0.6, alpha=0.7),
        )

    ax1.set_title(s["title"], fontsize=14, fontweight="bold",
                  loc="left", pad=24)
    ax1.text(0, 1.02, s["subtitle"], transform=ax1.transAxes,
             fontsize=10, color=p["muted"])
    ax2.text(0, -0.32, s["footer"], transform=ax2.transAxes,
             fontsize=8.5, color=p["muted"])

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig


if __name__ == "__main__":
    for lc in ("en", "hk", "tw", "cn"):
        LANG_STRINGS[lc]["_lang"] = lc
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
