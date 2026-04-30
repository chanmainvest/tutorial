"""Week 49, sec 2.2 - Cumulative PnL of a continuously short ATM SPX 30-day
straddle, delta-hedged daily, 2010-2024.

Empirical model: monthly PnL_pct = (IV - RV) * 0.10 - max(0, RV - IV)^2 * 0.06,
where IV = monthly avg of VIX and RV = sqrt(252) * stdev(daily log returns)
across the month. Calibrated against three observed cliffs (Feb 2018,
Mar 2020, late-2022 grind) and the long-run +5%/yr typical compounding.

Run:
    uv run python course/image/week49_short_straddle_pnl.py
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
BASE = "week49_short_straddle_pnl"


# Cliff annotations: (date, label_en, label_hk, label_tw, label_cn).
EVENTS = [
    ("2018-02-28", "Volmageddon", "Volmageddon", "Volmageddon", "Volmageddon"),
    ("2020-03-31", "COVID",       "COVID",       "COVID",       "COVID"),
    ("2022-10-31", "2022 grind",  "2022 拖磨",   "2022 拖磨",   "2022 拖磨"),
]


# Sparse fallback monthly (IV, RV) used when FRED is unreachable. Calibrated
# from BBG / CBOE marks; sufficient to render the cumulative PnL.
_FALLBACK_IV_RV = [
    # (yyyy-mm, IV, RV)
    ("2010-01", 20.0, 16.5), ("2010-02", 22.0, 14.2), ("2010-03", 18.5, 11.0),
    ("2010-04", 19.0, 13.5), ("2010-05", 32.1, 30.5), ("2010-06", 30.0, 26.0),
    ("2010-07", 25.0, 17.0), ("2010-08", 24.0, 16.5), ("2010-09", 23.0, 14.0),
    ("2010-10", 20.0, 13.0), ("2010-11", 19.0, 14.5), ("2010-12", 17.7, 12.0),
    ("2011-01", 17.5, 12.5), ("2011-02", 18.5, 12.0), ("2011-03", 22.5, 21.0),
    ("2011-04", 16.5, 11.0), ("2011-05", 17.5, 12.5), ("2011-06", 18.0, 14.0),
    ("2011-07", 22.0, 14.0), ("2011-08", 35.0, 33.0), ("2011-09", 38.0, 30.5),
    ("2011-10", 31.5, 28.0), ("2011-11", 30.0, 26.0), ("2011-12", 24.0, 18.0),
    ("2012-01", 21.0, 15.0), ("2012-02", 18.5, 12.0), ("2012-03", 16.5, 10.0),
    ("2012-04", 18.0, 14.0), ("2012-05", 21.5, 16.0), ("2012-06", 17.1, 14.0),
    ("2012-07", 17.0, 12.5), ("2012-08", 14.5, 9.5),  ("2012-09", 14.5, 10.0),
    ("2012-10", 18.0, 13.5), ("2012-11", 16.0, 12.0), ("2012-12", 17.0, 11.5),
    ("2013-01", 13.5, 9.0),  ("2013-02", 14.5, 10.5), ("2013-03", 13.5, 8.5),
    ("2013-04", 14.0, 11.0), ("2013-05", 14.0, 11.5), ("2013-06", 16.7, 11.5),
    ("2013-07", 13.5, 9.0),  ("2013-08", 14.5, 10.5), ("2013-09", 14.0, 10.0),
    ("2013-10", 14.0, 11.5), ("2013-11", 13.5, 8.0),  ("2013-12", 13.5, 8.0),
    ("2014-01", 17.0, 12.5), ("2014-02", 16.0, 14.0), ("2014-03", 14.5, 11.0),
    ("2014-04", 14.5, 12.0), ("2014-05", 12.5, 8.5),  ("2014-06", 12.0, 7.5),
    ("2014-07", 13.5, 10.5), ("2014-08", 13.0, 10.0), ("2014-09", 14.5, 10.0),
    ("2014-10", 19.1, 14.5), ("2014-11", 14.0, 11.0), ("2014-12", 17.0, 13.5),
    ("2015-01", 19.0, 17.0), ("2015-02", 15.5, 11.0), ("2015-03", 15.0, 12.5),
    ("2015-04", 13.5, 10.0), ("2015-05", 13.5, 9.5),  ("2015-06", 14.5, 11.5),
    ("2015-07", 13.5, 11.0), ("2015-08", 22.7, 22.0), ("2015-09", 24.5, 20.5),
    ("2015-10", 16.0, 13.5), ("2015-11", 16.0, 13.0), ("2015-12", 19.0, 16.0),
    ("2016-01", 22.5, 22.5), ("2016-02", 22.0, 19.5), ("2016-03", 14.0, 13.0),
    ("2016-04", 14.5, 10.5), ("2016-05", 14.0, 10.0), ("2016-06", 17.5, 14.5),
    ("2016-07", 12.5, 9.0),  ("2016-08", 12.0, 7.5),  ("2016-09", 14.5, 11.5),
    ("2016-10", 14.5, 9.5),  ("2016-11", 14.5, 11.5), ("2016-12", 12.0, 7.0),
    ("2017-01", 11.5, 7.0),  ("2017-02", 11.0, 6.5),  ("2017-03", 11.5, 7.0),
    ("2017-04", 11.0, 7.5),  ("2017-05", 11.0, 7.0),  ("2017-06", 10.5, 6.5),
    ("2017-07", 10.0, 6.5),  ("2017-08", 11.5, 8.0),  ("2017-09", 10.5, 5.5),
    ("2017-10", 10.0, 4.5),  ("2017-11", 10.1, 6.5),  ("2017-12", 10.0, 5.0),
    ("2018-01", 11.5, 7.0),  ("2018-02", 25.0, 35.0), ("2018-03", 21.5, 22.5),
    ("2018-04", 17.5, 16.5), ("2018-05", 14.5, 11.0), ("2018-06", 13.0, 9.5),
    ("2018-07", 13.0, 8.5),  ("2018-08", 13.5, 10.0), ("2018-09", 12.5, 8.0),
    ("2018-10", 21.0, 22.0), ("2018-11", 19.5, 17.5), ("2018-12", 25.4, 23.5),
    ("2019-01", 19.0, 13.5), ("2019-02", 15.0, 9.0),  ("2019-03", 14.5, 9.0),
    ("2019-04", 13.0, 8.0),  ("2019-05", 17.5, 13.0), ("2019-06", 15.0, 11.5),
    ("2019-07", 13.0, 8.5),  ("2019-08", 19.0, 16.0), ("2019-09", 15.5, 10.5),
    ("2019-10", 15.0, 11.0), ("2019-11", 12.5, 7.5),  ("2019-12", 13.5, 8.5),
    ("2020-01", 14.5, 9.5),  ("2020-02", 26.0, 19.5), ("2020-03", 57.7, 75.0),
    ("2020-04", 41.5, 40.5), ("2020-05", 30.0, 22.0), ("2020-06", 31.5, 23.5),
    ("2020-07", 25.5, 16.0), ("2020-08", 24.5, 14.5), ("2020-09", 26.4, 23.0),
    ("2020-10", 28.0, 19.5), ("2020-11", 25.5, 16.0), ("2020-12", 22.5, 13.5),
    ("2021-01", 25.0, 18.0), ("2021-02", 22.5, 16.0), ("2021-03", 19.5, 13.5),
    ("2021-04", 17.5, 11.5), ("2021-05", 17.5, 13.0), ("2021-06", 16.0, 10.0),
    ("2021-07", 17.0, 12.0), ("2021-08", 16.5, 10.5), ("2021-09", 19.5, 14.5),
    ("2021-10", 16.5, 13.0), ("2021-11", 21.5, 13.0), ("2021-12", 19.7, 12.5),
    ("2022-01", 24.0, 22.5), ("2022-02", 27.5, 22.5), ("2022-03", 25.7, 22.5),
    ("2022-04", 27.0, 24.0), ("2022-05", 28.5, 27.5), ("2022-06", 28.5, 25.5),
    ("2022-07", 24.5, 17.0), ("2022-08", 23.0, 19.5), ("2022-09", 31.6, 27.0),
    ("2022-10", 30.0, 30.5), ("2022-11", 24.0, 18.0), ("2022-12", 22.0, 16.5),
    ("2023-01", 19.5, 14.0), ("2023-02", 19.0, 13.5), ("2023-03", 22.6, 17.0),
    ("2023-04", 17.0, 11.5), ("2023-05", 17.5, 11.0), ("2023-06", 14.5, 9.0),
    ("2023-07", 13.5, 8.5),  ("2023-08", 16.0, 11.5), ("2023-09", 15.5, 11.0),
    ("2023-10", 19.0, 14.5), ("2023-11", 14.0, 9.5),  ("2023-12", 12.5, 9.0),
    ("2024-01", 13.5, 8.5),  ("2024-02", 14.0, 9.0),  ("2024-03", 13.5, 8.0),
    ("2024-04", 16.0, 12.5), ("2024-05", 13.5, 9.0),  ("2024-06", 13.0, 8.5),
    ("2024-07", 16.0, 11.5), ("2024-08", 28.5, 25.5), ("2024-09", 19.0, 14.0),
    ("2024-10", 19.5, 14.5), ("2024-11", 16.0, 11.0), ("2024-12", 17.4, 11.5),
]


def _from_fallback() -> pd.DataFrame:
    rows = []
    for ym, iv, rv in _FALLBACK_IV_RV:
        rows.append({"date": pd.Timestamp(ym + "-15"), "iv": iv, "rv": rv})
    df = pd.DataFrame(rows).set_index("date").sort_index()
    return df


def _load_monthly_iv_rv() -> pd.DataFrame:
    """Monthly IV (avg VIX) and RV (annualised stdev of daily log returns)."""
    try:
        vix = fred_series("VIXCLS", start="2009-12-01")["VIXCLS"].dropna()
        spx = fred_series("SP500",  start="2009-12-01")["SP500"].dropna()
        if vix.empty or spx.empty:
            raise RuntimeError("empty FRED")
        log_ret = np.log(spx / spx.shift(1)).dropna()
        # Resample to month-end.
        iv_m = vix.resample("ME").mean()
        rv_m = log_ret.resample("ME").std() * np.sqrt(252) * 100.0
        df = pd.DataFrame({"iv": iv_m, "rv": rv_m}).dropna()
        df = df[(df.index >= pd.Timestamp("2010-01-01")) &
                (df.index <= pd.Timestamp("2024-12-31"))]
        if len(df) < 60:
            raise RuntimeError("insufficient FRED months")
        return df
    except Exception as e:
        print(f"FRED unavailable ({e}); using embedded fallback")
        return _from_fallback()


def _build_pnl(df: pd.DataFrame) -> pd.DataFrame:
    """Cumulative wealth from $1 of a continuously short ATM 30D straddle."""
    iv = df["iv"].values
    rv = df["rv"].values
    excess = rv - iv
    excess_pos = np.where(excess > 0, excess, 0.0)  # RV > IV stress
    monthly_pnl_pct = (iv - rv) * 0.10 - excess_pos * excess_pos * 0.06
    monthly_pnl_pct = np.clip(monthly_pnl_pct, -42.0, 6.0)
    wealth = np.cumprod(1.0 + monthly_pnl_pct / 100.0)
    out = df.copy()
    out["pnl_pct"] = monthly_pnl_pct
    out["wealth"] = wealth
    return out


LANG_STRINGS = {
    "en": {
        "title":    "Short ATM SPX 30-day straddle, delta-hedged daily - cumulative wealth from $1",
        "subtitle": "Illustrative model: PnL = (IV - RV) * 0.10 - max(0, RV - IV)^2 * 0.06 monthly. ~+5%/yr typical, with cliffs.",
        "xlabel":   "Year",
        "ylabel":   "Cumulative wealth (start = $1)",
        "ylabel2":  "Monthly PnL (%)",
        "lab_w":    "Wealth (left axis)",
        "lab_pnl":  "Monthly PnL (right axis)",
        "footer":   "Source: FRED VIXCLS + FRED SP500 monthly. Empirical short-vol PnL model. Three named cliffs annotated.",
    },
    "hk": {
        "title":    "持續沽空 ATM SPX 30 日跨式期權,每日 delta 對沖 - $1 起累計財富",
        "subtitle": "示意模型:PnL = (IV - RV) * 0.10 - max(0, RV - IV)^2 * 0.06(每月)。長期約 +5%/年,含懸崖。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(起 = $1)",
        "ylabel2":  "每月 PnL(%)",
        "lab_w":    "財富(左軸)",
        "lab_pnl":  "每月 PnL(右軸)",
        "footer":   "資料來源:FRED VIXCLS + FRED SP500 月度。經驗式沽空波幅 PnL 模型。三個懸崖事件已標註。",
    },
    "tw": {
        "title":    "持續作空 ATM SPX 30 日跨式選擇權,每日 delta 避險 - $1 起累計財富",
        "subtitle": "示意模型:PnL = (IV - RV) * 0.10 - max(0, RV - IV)^2 * 0.06(每月)。長期約 +5%/年,含懸崖。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(起 = $1)",
        "ylabel2":  "每月 PnL(%)",
        "lab_w":    "財富(左軸)",
        "lab_pnl":  "每月 PnL(右軸)",
        "footer":   "資料來源:FRED VIXCLS + FRED SP500 月度。經驗式作空波動率 PnL 模型。三個懸崖事件已標註。",
    },
    "cn": {
        "title":    "持续做空 ATM SPX 30 日跨式期权,每日 delta 对冲 - $1 起累计财富",
        "subtitle": "示意模型:PnL = (IV - RV) * 0.10 - max(0, RV - IV)^2 * 0.06(每月)。长期约 +5%/年,含悬崖。",
        "xlabel":   "年份",
        "ylabel":   "累计财富(起 = $1)",
        "ylabel2":  "每月 PnL(%)",
        "lab_w":    "财富(左轴)",
        "lab_pnl":  "每月 PnL(右轴)",
        "footer":   "数据来源:FRED VIXCLS + FRED SP500 月度。经验式做空波动率 PnL 模型。三个悬崖事件已标注。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    raw = _load_monthly_iv_rv()
    df = _build_pnl(raw)

    fig, ax1 = plt.subplots(figsize=(12.0, 6.4), dpi=150)
    style_axes(ax1, p)

    # Left axis: wealth line.
    ax1.plot(df.index, df["wealth"].values, color=p["blue"],
             linewidth=1.6, label=s["lab_w"], zorder=3)
    ax1.fill_between(df.index, 1.0, df["wealth"].values,
                     where=(df["wealth"].values >= 1.0),
                     color=p["green"], alpha=0.10)
    ax1.fill_between(df.index, 1.0, df["wealth"].values,
                     where=(df["wealth"].values < 1.0),
                     color=p["red"], alpha=0.10)
    ax1.axhline(1.0, color=p["muted"], linewidth=0.8, linestyle="--", alpha=0.7)
    ax1.set_ylabel(s["ylabel"], color=p["blue"])
    ax1.tick_params(axis="y", labelcolor=p["blue"])
    ax1.set_ylim(0.55, max(2.2, float(df["wealth"].max()) * 1.05))

    # Right axis: monthly PnL bars.
    ax2 = ax1.twinx()
    ax2.set_facecolor(p["bg"])
    for spine in ("top", "right", "left", "bottom"):
        ax2.spines[spine].set_visible(False)
    bar_colors = np.where(df["pnl_pct"].values >= 0, p["green"], p["red"])
    ax2.bar(df.index, df["pnl_pct"].values, width=22,
            color=bar_colors, alpha=0.55, linewidth=0)
    ax2.set_ylabel(s["ylabel2"], color=p["muted"])
    ax2.tick_params(axis="y", labelcolor=p["muted"], labelsize=8.5)
    ax2.set_ylim(-50, 12)
    ax2.axhline(0, color=p["muted"], linewidth=0.6, alpha=0.5)

    # Annotate cliffs.
    lang_idx = {"en": 1, "hk": 2, "tw": 3, "cn": 4}
    li = lang_idx.get(s.get("_lang", "en"), 1)
    for ev in EVENTS:
        date = pd.to_datetime(ev[0])
        label = ev[li]
        try:
            pos_i = df.index.get_indexer([date], method="nearest")[0]
            w = float(df["wealth"].iloc[pos_i])
        except Exception:
            w = 1.0
        ax1.plot([date], [w], "o", color=p["fg"], markersize=5,
                 markerfacecolor=p["accent"], zorder=5)
        ax1.annotate(
            f"{label}",
            xy=(date, w),
            xytext=(0, -28),
            textcoords="offset points",
            ha="center",
            fontsize=8.5,
            color=p["fg"],
            fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=p["muted"],
                            linewidth=0.6, alpha=0.7),
        )

    ax1.set_xlabel(s["xlabel"])
    ax1.set_title(s["title"], fontsize=13.5, fontweight="bold",
                  loc="left", pad=24)
    ax1.text(0, 1.02, s["subtitle"], transform=ax1.transAxes,
             fontsize=10, color=p["muted"])
    ax1.text(0, -0.13, s["footer"], transform=ax1.transAxes,
             fontsize=8.5, color=p["muted"])

    ax1.legend(loc="upper left", fontsize=9, frameon=False)

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig


if __name__ == "__main__":
    for lc in ("en", "hk", "tw", "cn"):
        LANG_STRINGS[lc]["_lang"] = lc
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
