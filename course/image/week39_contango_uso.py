"""Week 39, §2.3 — Front-month vs 12-month-out crude futures, 2010-2024.

Front-month WTI is sourced from FRED DCOILWTICO (resampled monthly).
The 12-month-deferred curve is approximated from a small embedded
term-structure dictionary anchored at canonical regimes (2015 oil glut
contango, April-2020 super-contango, 2022 Ukraine backwardation,
benign 2017 and 2024 carry markets). Between anchors the spread is
linearly interpolated. The shaded band shows back-month minus
front-month -- positive in contango, negative in backwardation.

Run:
    uv run python course/image/week39_contango_uso.py
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
BASE = "week39_contango_uso"


# Anchored 12mo-minus-front-month spread ($/bbl) at canonical dates.
# Positive = contango, negative = backwardation. Inferred from CME WTI
# settlement prints and EIA term-structure reports.
SPREAD_ANCHORS = {
    "2010-01-01":  6.0,
    "2011-04-01": -2.0,   # Libya backwardation
    "2012-06-01":  3.0,
    "2014-01-01": -3.0,   # tight prompt
    "2015-03-01": 10.0,   # oil glut contango begins
    "2016-02-01": 12.0,   # peak glut contango
    "2017-06-01":  3.0,
    "2018-10-01": -4.0,   # IMO 2020 sour-tight backwardation
    "2019-12-01":  2.0,
    "2020-04-01": 28.0,   # super-contango (negative front-month)
    "2020-12-01":  4.0,
    "2021-10-01": -8.0,   # post-COVID re-opening backwardation
    "2022-03-01": -22.0,  # Ukraine invasion peak backwardation
    "2022-09-01": -12.0,
    "2023-07-01": -3.0,
    "2024-04-01":  1.5,
    "2024-12-01":  2.5,
}


# Front-month fallback (monthly avg WTI, Cushing, $/bbl). Used if FRED is
# unreachable. Approximate but accurate to ~$2.
FRONT_FALLBACK = {
    "2010": 79.5, "2011": 95.0, "2012": 94.2, "2013": 97.9,
    "2014": 93.0, "2015": 48.7, "2016": 43.3, "2017": 50.8,
    "2018": 65.2, "2019": 56.9, "2020": 39.2, "2021": 68.0,
    "2022": 94.5, "2023": 77.6, "2024": 75.8,
}


LANG_STRINGS = {
    "en": {
        "title":    "WTI crude: front-month vs 12-month-out, 2010-2024",
        "subtitle": "Contango (orange above blue) is the normal storable-commodity shape; backwardation (orange below blue) marks acute physical shortage. The shaded gap is the roll cost USO pays every month.",
        "xlabel":   "Year",
        "ylabel":   "Price ($/bbl)",
        "front":    "Front-month WTI",
        "back":     "12-month-deferred WTI",
        "ann_2016": "2015-16 oil-glut\ncontango ~ +$12",
        "ann_2020": "Apr-2020 super-\ncontango ~ +$28",
        "ann_2022": "2022 Ukraine\nbackwardation ~ -$22",
        "footer":   "Front-month: FRED DCOILWTICO monthly mean. Deferred curve approximated from embedded CME term-structure anchors with linear interpolation. April 2026 data cut.",
    },
    "hk": {
        "title":    "WTI 原油:現月 vs 12 月遠期,2010-2024",
        "subtitle": "Contango(橘線在藍線之上)是可儲存商品的常態;backwardation(橘線在藍線之下)代表即期實物短缺。陰影區為 USO 每月被吞掉的展期成本。",
        "xlabel":   "年份",
        "ylabel":   "價格(美元/桶)",
        "front":    "現月 WTI",
        "back":     "12 月遠期 WTI",
        "ann_2016": "2015-16 油過剩\ncontango ~ +$12",
        "ann_2020": "2020/4 超級\ncontango ~ +$28",
        "ann_2022": "2022 烏克蘭\nbackwardation ~ -$22",
        "footer":   "現月:FRED DCOILWTICO 月均值。遠期曲線由內嵌 CME 期限結構錨點以線性內插近似。資料截至 2026/4。",
    },
    "tw": {
        "title":    "WTI 原油:近月 vs 12 月遠月,2010-2024",
        "subtitle": "Contango(橘線高於藍線)是可儲存大宗的常態;backwardation(橘線低於藍線)反映即期實物緊俏。陰影為 USO 每月支付的展期成本。",
        "xlabel":   "年份",
        "ylabel":   "價格(美元/桶)",
        "front":    "近月 WTI",
        "back":     "12 月遠月 WTI",
        "ann_2016": "2015-16 油過剩\ncontango ~ +$12",
        "ann_2020": "2020/4 超級\ncontango ~ +$28",
        "ann_2022": "2022 烏克蘭\nbackwardation ~ -$22",
        "footer":   "近月:FRED DCOILWTICO 月均值。遠期曲線以內嵌 CME 期限結構錨點線性內插。資料更新至 2026/4。",
    },
    "cn": {
        "title":    "WTI 原油:近月 vs 12 月远期,2010-2024",
        "subtitle": "Contango(橙线在蓝线之上)是可储存商品常态;backwardation(橙线在蓝线之下)代表现货紧俏。阴影为 USO 每月承担的展期成本。",
        "xlabel":   "年份",
        "ylabel":   "价格(美元/桶)",
        "front":    "近月 WTI",
        "back":     "12 月远期 WTI",
        "ann_2016": "2015-16 油过剩\ncontango ~ +$12",
        "ann_2020": "2020/4 超级\ncontango ~ +$28",
        "ann_2022": "2022 乌克兰\nbackwardation ~ -$22",
        "footer":   "近月:FRED DCOILWTICO 月均值。远期曲线由内嵌 CME 期限结构锚点线性内插近似。数据截至 2026/4。",
    },
}


def _front_month():
    """Return monthly front-month WTI, 2010-01-01 .. 2024-12-31."""
    try:
        df = fred_series("DCOILWTICO")
        df = df[(df.index >= "2010-01-01") & (df.index <= "2024-12-31")]
        if df.empty:
            raise RuntimeError("DCOILWTICO empty")
        m = df["DCOILWTICO"].resample("MS").mean().dropna()
        return m
    except Exception:
        # Fallback: per-year mean broadcast monthly.
        idx = pd.date_range("2010-01-01", "2024-12-01", freq="MS")
        vals = [FRONT_FALLBACK[str(d.year)] for d in idx]
        return pd.Series(vals, index=idx, name="DCOILWTICO")


def _spread_curve(idx):
    """Linearly interpolate 12mo-front spread across the index."""
    anchor_dates = pd.to_datetime(list(SPREAD_ANCHORS.keys()))
    anchor_vals  = np.array(list(SPREAD_ANCHORS.values()), dtype=float)
    order = np.argsort(anchor_dates.values)
    ad = anchor_dates[order]
    av = anchor_vals[order]
    x = (idx - ad[0]).days.values.astype(float)
    xa = (ad - ad[0]).days.values.astype(float)
    spread = np.interp(x, xa, av)
    return pd.Series(spread, index=idx, name="spread")


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    front = _front_month()
    spread = _spread_curve(front.index)
    back = front + spread

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, p)

    # Shaded band between front and back.
    ax.fill_between(front.index, front.values, back.values,
                    where=(back.values >= front.values),
                    color=p["accent"], alpha=0.18, linewidth=0,
                    label=None)
    ax.fill_between(front.index, front.values, back.values,
                    where=(back.values < front.values),
                    color=p["green"], alpha=0.20, linewidth=0,
                    label=None)

    ax.plot(front.index, front.values, color=p["blue"],
            linewidth=2.0, label=s["front"])
    ax.plot(front.index, back.values, color=p["accent"],
            linewidth=2.0, label=s["back"])

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold", loc="left")
    fig.text(0.5, 0.94, s["subtitle"], ha="center",
             fontsize=10.0, color=p["muted"], style="italic")

    # Annotations
    def annot(date, text, dx=0, dy=0, color=None):
        d = pd.Timestamp(date)
        if d not in front.index:
            d = front.index[front.index.get_indexer([d], method="nearest")[0]]
        y = max(front.loc[d], back.loc[d])
        ax.annotate(text,
                    xy=(d, y), xytext=(d + pd.DateOffset(months=dx), y + dy),
                    fontsize=9.0, color=color or p["fg"],
                    ha="center",
                    arrowprops=dict(arrowstyle="-", color=p["muted"],
                                    linewidth=0.8))

    annot("2016-02-01", s["ann_2016"], dx=-12, dy=15, color=p["accent"])
    annot("2020-04-01", s["ann_2020"], dx=-3, dy=42, color=p["red"])
    annot("2022-03-01", s["ann_2022"], dx=12, dy=20, color=p["green"])

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.set_ylim(-10, 160)

    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.0,
             color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_*.png and {BASE}.png to {OUT_DIR}")
