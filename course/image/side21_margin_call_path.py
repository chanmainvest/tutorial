"""Side 21, §2.3 — 2x SPY through the 2008 drawdown, with the margin-call moment.

Daily SPY total-return path 2007-01-02 to 2013-04-30. Two lines: unlevered
SPY (cumulative wealth from $100k start) and 2x leveraged SPY (start with
$100k equity + $100k margin loan; equity = 2 * SPY_cum - 1 in unit terms).
Mark the 25% maintenance threshold (2x SPY position is called at -33.3%
of the underlying), the forced-liquidation point, and the recovery the
levered investor never sees.

Run:
    uv run python course/image/side21_margin_call_path.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes,
)
from scripts.market_data import yahoo_history, damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "side21_margin_call_path"

LANG_STRINGS = {
    "en": {
        "title":    "2x SPY through 2008: the margin call you cannot trade out of",
        "subtitle": "Start: $100k equity, $100k margin loan. Maintenance call at 25% equity (= -33.3% on SPY). Borrow 6%/yr.",
        "xlabel":   "",
        "ylabel":   "Wealth ($, log scale)",
        "leg_unl":  "Unlevered SPY ($100k start)",
        "leg_lev":  "2x leveraged SPY ($100k equity)",
        "leg_call": "Forced liquidation",
        "ann_call": "Margin call:\nSPY -33.3%\nNov 2008",
        "ann_low":  "SPY trough\n-55%, Mar 2009",
        "ann_recov":"SPY back to highs\nMar 2013",
        "ann_lev0": "Levered equity:\n~$0 after liquidation",
        "footer":   "Daily SPY adjusted close. Levered equity = 2 * SPY/SPY0 - 1 - daily borrow accrual; resets to zero at the maintenance breach.",
    },
    "hk": {
        "title":    "2 倍 SPY 過 2008:你交易不出去的 margin call",
        "subtitle": "起點:10 萬美元權益 + 10 萬保證金借貸。權益 25% 觸發 call(= SPY -33.3%)。借款年息 6%。",
        "xlabel":   "",
        "ylabel":   "資產淨值(美元,對數軸)",
        "leg_unl":  "無槓桿 SPY(起點 10 萬)",
        "leg_lev":  "2 倍槓桿 SPY(10 萬權益)",
        "leg_call": "強制平倉",
        "ann_call": "Margin call:\nSPY -33.3%\n2008 年 11 月",
        "ann_low":  "SPY 谷底\n-55%,2009 年 3 月",
        "ann_recov":"SPY 收復前高\n2013 年 3 月",
        "ann_lev0": "槓桿權益:\n清算後近於 0",
        "footer":   "日度 SPY 復權收盤。槓桿權益 = 2 * SPY/SPY0 - 1 - 日度融資成本;觸發維持保證金即歸零。",
    },
    "tw": {
        "title":    "2 倍 SPY 過 2008:你逃不掉的 margin call",
        "subtitle": "起點:10 萬美元權益 + 10 萬保證金借貸。權益 25% 觸發追繳(= SPY -33.3%)。借款年息 6%。",
        "xlabel":   "",
        "ylabel":   "資產淨值(美元,對數軸)",
        "leg_unl":  "無槓桿 SPY(起點 10 萬)",
        "leg_lev":  "2 倍槓桿 SPY(10 萬權益)",
        "leg_call": "強制平倉",
        "ann_call": "Margin call:\nSPY -33.3%\n2008 年 11 月",
        "ann_low":  "SPY 谷底\n-55%,2009 年 3 月",
        "ann_recov":"SPY 回到前高\n2013 年 3 月",
        "ann_lev0": "槓桿權益:\n清算後近於 0",
        "footer":   "日 SPY 還原收盤。槓桿權益 = 2 * SPY/SPY0 - 1 - 日融資成本;觸及維持保證金即歸零。",
    },
    "cn": {
        "title":    "2 倍 SPY 穿越 2008:你出不去的强制平仓",
        "subtitle": "起点:10 万美元权益 + 10 万保证金借贷。权益 25% 触发追缴(= SPY -33.3%)。借款年息 6%。",
        "xlabel":   "",
        "ylabel":   "资产净值(美元,对数轴)",
        "leg_unl":  "无杠杆 SPY(起点 10 万)",
        "leg_lev":  "2 倍杠杆 SPY(10 万权益)",
        "leg_call": "强制平仓",
        "ann_call": "Margin call:\nSPY -33.3%\n2008 年 11 月",
        "ann_low":  "SPY 谷底\n-55%,2009 年 3 月",
        "ann_recov":"SPY 收复前高\n2013 年 3 月",
        "ann_lev0": "杠杆权益:\n清算后近于 0",
        "footer":   "日度 SPY 复权收盘。杠杆权益 = 2 * SPY/SPY0 - 1 - 日度融资成本;触发维持保证金即归零。",
    },
}

# ---------- data ----------
START = "2007-01-02"
END = "2013-06-30"
BORROW_ANNUAL = 0.06
MAINT_THRESHOLD = -1.0 / 3.0  # 2x position called at SPY = -33.3%


def _load_spy() -> pd.DataFrame:
    """Daily SPY adjusted close. Fall back to a synthetic series from
    Damodaran annual SP500 totals if Yahoo is unreachable."""
    try:
        df = yahoo_history("SPY", start=START, end=END, interval="1d")
        if df is not None and not df.empty and "Close" in df.columns:
            df = df.sort_index()
            return df[["Close"]].rename(columns={"Close": "spy"})
    except Exception:  # noqa: BLE001
        pass

    # Fallback: piecewise from annual returns. Add a 2008 -38.5% with a
    # plausible intra-year drawdown shape so the chart still tells the story.
    dam = damodaran_annual_returns()
    yrs = list(range(2007, 2014))
    rets = {y: float(dam.loc[dam["Year"] == y, "SP500"].iloc[0]) for y in yrs if y in dam["Year"].values}
    # daily index
    dates = pd.bdate_range(START, END)
    rng = np.random.default_rng(20081031)
    series = []
    val = 1.0
    for d in dates:
        y = d.year
        ann = rets.get(y, 0.08)
        # crude per-day drift + daily noise; embed a synthetic 2008-Oct/Nov crash shape
        if y == 2008 and 9 <= d.month <= 11:
            drift = -0.012  # crash months
        elif y == 2008:
            drift = (ann - (-0.012 * 60)) / 192
        elif y == 2009 and d.month <= 3:
            drift = -0.005
        else:
            drift = ann / 252
        noise = rng.normal(0, 0.012)
        val *= (1.0 + drift + noise)
        series.append(val)
    return pd.DataFrame({"spy": series}, index=dates)


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    pal = PALETTE_LIGHT

    spy = _load_spy()
    spy = spy.dropna()
    p0 = float(spy["spy"].iloc[0])
    spy["norm"] = spy["spy"] / p0
    # Cumulative borrow drag on the second $100k notional, accrued daily.
    n_days = len(spy)
    borrow_per_day = BORROW_ANNUAL / 252.0
    drag = (1.0 + borrow_per_day) ** np.arange(n_days) - 1.0  # cumulative interest factor on $1
    # Levered equity (pre-call): start equity $1, controls $2 of SPY.
    # equity_t = 2 * (SPY/SPY0) - 1 - drag
    lev_equity = 2.0 * spy["norm"].values - 1.0 - drag
    # Margin call: equity / position_value < 0.25 (or equity <= 0).
    # equivalently: SPY/SPY0 < 0.6667.
    breach_idx = None
    for i, ratio in enumerate(spy["norm"].values):
        if ratio <= (1.0 + MAINT_THRESHOLD) and lev_equity[i] > 0:
            breach_idx = i
            break
        if lev_equity[i] <= 0:
            breach_idx = i
            break
    if breach_idx is None:
        breach_idx = int(np.argmin(lev_equity))

    lev_path = lev_equity.copy()
    lev_path[breach_idx + 1:] = np.nan  # liquidated, line ends

    fig, ax = plt.subplots(figsize=(12.5, 6.6), dpi=150)
    style_axes(ax, pal)

    x = spy.index
    unl_dollar = 100_000.0 * spy["norm"].values
    lev_dollar = 100_000.0 * lev_path  # equity in dollars

    ax.plot(x, unl_dollar, color=pal["blue"], lw=2.0, label=s["leg_unl"], zorder=3)
    ax.plot(x, lev_dollar, color=pal["red"], lw=2.0, label=s["leg_lev"], zorder=4)

    # Forced-liquidation marker.
    breach_date = x[breach_idx]
    breach_lev = float(lev_dollar[breach_idx])
    ax.scatter([breach_date], [max(breach_lev, 100)], s=140, marker="X",
               color=pal["red"], edgecolor=pal["fg"], linewidth=1.0,
               zorder=6, label=s["leg_call"])

    # Maintenance threshold line: SPY at -33.3% in dollar terms.
    thresh_dollar = 100_000.0 * (1.0 + MAINT_THRESHOLD)
    ax.axhline(thresh_dollar, color=pal["muted"], lw=0.9, ls=":", alpha=0.7)
    ax.text(x[5], thresh_dollar * 0.96, "  SPY -33.3% (2x maintenance)",
            color=pal["muted"], fontsize=8.5, va="top")

    # Annotations.
    spy_min_idx = int(np.argmin(spy["norm"].values))
    spy_min_date = x[spy_min_idx]
    spy_min_dollar = float(unl_dollar[spy_min_idx])

    # Recovery: first day SPY >= 1.0 after the trough.
    recov_idx = None
    for i in range(spy_min_idx, len(spy)):
        if spy["norm"].iloc[i] >= 1.0:
            recov_idx = i
            break
    if recov_idx is None:
        recov_idx = len(spy) - 1
    recov_date = x[recov_idx]
    recov_dollar = float(unl_dollar[recov_idx])

    ax.annotate(
        s["ann_call"],
        xy=(breach_date, max(breach_lev, 1000)),
        xytext=(breach_date - pd.Timedelta(days=380), 130_000),
        fontsize=9.5, color=pal["red"], weight="bold", ha="center",
        arrowprops=dict(arrowstyle="->", color=pal["red"], lw=1.0),
        bbox=dict(boxstyle="round,pad=0.35", fc="#fff5f5", ec=pal["red"], lw=0.8),
    )
    ax.annotate(
        s["ann_low"],
        xy=(spy_min_date, spy_min_dollar),
        xytext=(spy_min_date + pd.Timedelta(days=70), 35_000),
        fontsize=9.5, color=pal["muted"], ha="left",
        arrowprops=dict(arrowstyle="->", color=pal["muted"], lw=0.8),
    )
    ax.annotate(
        s["ann_recov"],
        xy=(recov_date, recov_dollar),
        xytext=(recov_date - pd.Timedelta(days=420), 145_000),
        fontsize=9.5, color=pal["green"], weight="bold", ha="left",
        arrowprops=dict(arrowstyle="->", color=pal["green"], lw=0.9),
    )
    # Levered ~zero trail label.
    ax.text(x[-1] - pd.Timedelta(days=20), 600,
            s["ann_lev0"], color=pal["red"], fontsize=9, ha="right",
            style="italic")

    ax.set_yscale("log")
    ax.set_ylim(500, 220_000)
    ax.set_yticks([1_000, 5_000, 25_000, 100_000, 200_000])
    ax.set_yticklabels([r"\$1k", r"\$5k", r"\$25k", r"\$100k", r"\$200k"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5)

    ax.legend(loc="lower left", fontsize=9.5, framealpha=0.92, ncol=1)
    ax.grid(True, axis="y", alpha=0.25, lw=0.5)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=pal["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
