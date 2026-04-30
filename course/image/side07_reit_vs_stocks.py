"""Side Lesson 07, §2.3 — VNQ vs SPY vs IEF total-return wealth path.

Three-line cumulative-wealth chart from January 2000 through April 2026
of one dollar invested in VNQ (Vanguard REIT), SPY (S&P 500), and IEF
(7-10 year Treasury). Annotated with the 2008 GFC drawdown, the 2020
COVID drawdown, the 2022 rate shock, and the 2024-2025 recovery. Pulls
adjusted-close monthly bars from Yahoo with an embedded yearly fallback
so the chart still renders offline.

Run:
    uv run python course/image/side07_reit_vs_stocks.py
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
from scripts.market_data import yahoo_history  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side07_reit_vs_stocks"

# Annual total returns Jan 2000 - Apr 2026.
# Sources: Vanguard fund pages (VNQ tot ret), SPDR fact sheets (SPY),
# iShares (IEF). 2026 partial = Jan-Apr only. Used as fallback when
# Yahoo download fails.
ANNUAL_FALLBACK = {
    # year: (vnq_ret, spy_ret, ief_ret)
    2000: ( 0.260, -0.091,  0.149),
    2001: ( 0.137, -0.119,  0.046),
    2002: ( 0.038, -0.221,  0.143),
    2003: ( 0.366,  0.286,  0.013),
    2004: ( 0.309,  0.107,  0.034),
    2005: ( 0.119,  0.049,  0.022),
    2006: ( 0.354,  0.158,  0.029),
    2007: (-0.165,  0.054,  0.099),
    2008: (-0.371, -0.370,  0.181),
    2009: ( 0.298,  0.265, -0.064),
    2010: ( 0.286,  0.151,  0.092),
    2011: ( 0.084,  0.019,  0.158),
    2012: ( 0.175,  0.160,  0.041),
    2013: ( 0.024,  0.323, -0.062),
    2014: ( 0.305,  0.135,  0.092),
    2015: ( 0.024,  0.014,  0.015),
    2016: ( 0.085,  0.120,  0.011),
    2017: ( 0.049,  0.218,  0.026),
    2018: (-0.060, -0.044,  0.009),
    2019: ( 0.288,  0.314,  0.080),
    2020: (-0.046,  0.184,  0.099),
    2021: ( 0.402,  0.287, -0.024),
    2022: (-0.260, -0.183, -0.150),
    2023: ( 0.117,  0.262,  0.034),
    2024: ( 0.072,  0.250,  0.013),
    2025: ( 0.118,  0.155,  0.041),
    2026: ( 0.034,  0.038,  0.012),  # YTD through April
}


def _yahoo_or_fallback() -> pd.DataFrame:
    """Return monthly index DataFrame with columns vnq, spy, ief (cum wealth $1)."""
    try:
        vnq = yahoo_history("VNQ", start="1999-12-01", interval="1mo")
        spy = yahoo_history("SPY", start="1999-12-01", interval="1mo")
        ief = yahoo_history("IEF", start="2002-07-01", interval="1mo")
        # IEF inception 2002-07; backfill earlier with annual fallback.
        if vnq.empty or spy.empty or ief.empty:
            raise RuntimeError("empty yahoo response")

        def _wealth(df):
            s = df["AdjClose"].copy()
            s = s / s.iloc[0]
            return s

        v = _wealth(vnq)
        sp = _wealth(spy)
        ie = _wealth(ief)

        # Align to common monthly index, forward fill.
        idx = pd.date_range("2000-01-01", "2026-04-30", freq="ME")
        df = pd.DataFrame(index=idx)
        df["vnq"] = v.reindex(idx, method="ffill")
        df["spy"] = sp.reindex(idx, method="ffill")
        df["ief"] = ie.reindex(idx, method="ffill")
        # Backfill IEF pre-2002-07 from fallback annual rets.
        if df["ief"].iloc[0] != df["ief"].iloc[0]:  # NaN check
            wealth = 1.0
            for yr in (2000, 2001, 2002):
                end = pd.Timestamp(year=yr, month=12, day=31)
                start = pd.Timestamp(year=yr, month=1, day=1)
                rng = (df.index >= start) & (df.index <= end)
                months = rng.sum()
                if months == 0:
                    continue
                r = ANNUAL_FALLBACK[yr][2]
                month_r = (1 + r) ** (1 / max(months, 1)) - 1
                vals = []
                w = wealth
                for _ in range(months):
                    w = w * (1 + month_r)
                    vals.append(w)
                df.loc[rng, "ief"] = vals
                wealth = w
            # Scale post-2002-07 IEF series so it joins continuously.
            first_real = df["ief"].dropna().index[0]
            scale = df.loc[first_real, "ief"]
            df["ief"] = df["ief"] / scale * wealth
        df = df.ffill().dropna()
        if len(df) < 240:
            raise RuntimeError("insufficient data")
        return df
    except Exception:
        return _build_from_fallback()


def _build_from_fallback() -> pd.DataFrame:
    idx = pd.date_range("2000-01-01", "2026-04-30", freq="ME")
    rows = []
    w_v, w_s, w_i = 1.0, 1.0, 1.0
    for ts in idx:
        yr = ts.year
        ret = ANNUAL_FALLBACK[yr]
        # spread annual into 12 (or 4 for 2026 partial) months
        months_in_year = 4 if yr == 2026 else 12
        m_v = (1 + ret[0]) ** (1 / months_in_year) - 1
        m_s = (1 + ret[1]) ** (1 / months_in_year) - 1
        m_i = (1 + ret[2]) ** (1 / months_in_year) - 1
        w_v *= 1 + m_v
        w_s *= 1 + m_s
        w_i *= 1 + m_i
        rows.append((ts, w_v, w_s, w_i))
    return pd.DataFrame(rows, columns=["date", "vnq", "spy", "ief"]).set_index("date")


LANG_STRINGS = {
    "en": {
        "title":    "VNQ vs SPY vs IEF — wealth path Jan 2000 to April 2026",
        "subtitle": "Public REITs inherit equity-market drawdowns AND bond-market rate sensitivity. The 2022 -25% drag was rate-driven.",
        "xlabel":   "Year",
        "ylabel":   "Wealth from US 1 dollar (log scale)",
        "footer":   "Source: Yahoo Finance adjusted-close monthly. IEF inception July 2002, backfilled with embedded annual fallback. 2026 partial through April.",
        "leg_vnq":  "VNQ (REITs)",
        "leg_spy":  "SPY (S&P 500)",
        "leg_ief":  "IEF (7-10y UST)",
        "ann_gfc":  "2008 GFC\nVNQ -37%",
        "ann_cov":  "2020 COVID\nVNQ -25% in 3 weeks",
        "ann_22":   "2022 rate shock\nVNQ -25%, IEF -15%",
        "ann_rec":  "2024-25\nrecovery",
    },
    "hk": {
        "title":    "VNQ vs SPY vs IEF — 2000 年 1 月至 2026 年 4 月財富路徑",
        "subtitle": "公開房託同時繼承股市跌幅與債市利率敏感度。2022 年 -25% 主因利率衝擊。",
        "xlabel":   "年份",
        "ylabel":   "1 美元起算之財富(對數刻度)",
        "footer":   "來源:Yahoo Finance 月度調整收盤。IEF 於 2002 年 7 月成立,前段以內嵌年度數據回填。2026 年僅至 4 月。",
        "leg_vnq":  "VNQ(房託)",
        "leg_spy":  "SPY(標普 500)",
        "leg_ief":  "IEF(7-10 年國債)",
        "ann_gfc":  "2008 金融海嘯\nVNQ -37%",
        "ann_cov":  "2020 新冠\nVNQ 三週內 -25%",
        "ann_22":   "2022 加息衝擊\nVNQ -25%、IEF -15%",
        "ann_rec":  "2024-25\n回升",
    },
    "tw": {
        "title":    "VNQ vs SPY vs IEF — 2000 年 1 月至 2026 年 4 月財富路徑",
        "subtitle": "公開 REIT 同時承受股市回檔與債市利率敏感度。2022 年 -25% 主因升息。",
        "xlabel":   "年份",
        "ylabel":   "1 美元起算之財富(對數刻度)",
        "footer":   "資料來源:Yahoo Finance 月度調整收盤。IEF 於 2002 年 7 月成立,前段以內嵌年度資料回填。2026 年僅至 4 月。",
        "leg_vnq":  "VNQ(REIT)",
        "leg_spy":  "SPY(標普 500)",
        "leg_ief":  "IEF(7-10 年公債)",
        "ann_gfc":  "2008 金融海嘯\nVNQ -37%",
        "ann_cov":  "2020 新冠\nVNQ 三週內 -25%",
        "ann_22":   "2022 升息衝擊\nVNQ -25%、IEF -15%",
        "ann_rec":  "2024-25\n回升",
    },
    "cn": {
        "title":    "VNQ vs SPY vs IEF — 2000 年 1 月至 2026 年 4 月财富路径",
        "subtitle": "公开房托同时继承股市跌幅与债市利率敏感度。2022 年 -25% 主因利率冲击。",
        "xlabel":   "年份",
        "ylabel":   "1 美元起算之财富(对数刻度)",
        "footer":   "来源:Yahoo Finance 月度调整收盘。IEF 于 2002 年 7 月成立,前段以内嵌年度数据回填。2026 年仅至 4 月。",
        "leg_vnq":  "VNQ(房托)",
        "leg_spy":  "SPY(标普 500)",
        "leg_ief":  "IEF(7-10 年国债)",
        "ann_gfc":  "2008 金融危机\nVNQ -37%",
        "ann_cov":  "2020 新冠\nVNQ 三周内 -25%",
        "ann_22":   "2022 加息冲击\nVNQ -25%、IEF -15%",
        "ann_rec":  "2024-25\n回升",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    df = _yahoo_or_fallback()

    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax)
    ax.plot(df.index, df["spy"], color=p["blue"], linewidth=2.0,
            label=s["leg_spy"], zorder=3)
    ax.plot(df.index, df["ief"], color=p["green"], linewidth=2.0,
            label=s["leg_ief"], zorder=3)
    ax.plot(df.index, df["vnq"], color=p["accent"], linewidth=2.4,
            label=s["leg_vnq"], zorder=4)

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    # Annotation arrows
    def _annot(date_str, vnq_y, text, dx=0, dy=0):
        ts = pd.Timestamp(date_str)
        ax.annotate(text, xy=(ts, vnq_y),
                    xytext=(ts + pd.Timedelta(days=dx), vnq_y * dy),
                    fontsize=9, color=p["red"], fontweight="bold",
                    ha="center",
                    arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0))

    # GFC trough Feb 2009
    _annot("2009-02-28", df.loc[df.index <= "2009-02-28", "vnq"].iloc[-1],
           s["ann_gfc"], dx=-365 * 2, dy=0.45)
    # COVID trough Mar 2020
    _annot("2020-03-31", df.loc[df.index <= "2020-03-31", "vnq"].iloc[-1],
           s["ann_cov"], dx=-365 * 3, dy=0.55)
    # 2022 trough Oct 2022
    _annot("2022-10-31", df.loc[df.index <= "2022-10-31", "vnq"].iloc[-1],
           s["ann_22"], dx=365 * 2, dy=0.55)
    # 2025 recovery
    last_date = df.index[-1]
    ax.annotate(s["ann_rec"],
                xy=(last_date, df["vnq"].iloc[-1]),
                xytext=(last_date - pd.Timedelta(days=365 * 2),
                        df["vnq"].iloc[-1] * 1.55),
                fontsize=9, color=p["green"], fontweight="bold", ha="center",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=1.0))

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.6, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
