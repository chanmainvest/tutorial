"""Side 17, sec 1 -- US Fed funds effective rate, 1955 to April 2026.

FRED FEDFUNDS monthly. Annotates Volcker peak (Jul 1981, 19.10%),
the 2008 zero-bound, the 2015-19 normalisation, the Mar 2020 emergency
cut to 0.05%, the 2022-23 hiking cycle (525 bps in 18 months), and the
April 2026 setting around 3.6%.

Run:
    uv run python course/image/side17_ffr_history.py
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
from scripts.market_data import fred_series  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side17_ffr_history"


# Embedded fallback monthly snapshots (year-month, FFR%). Used only if
# FRED is unreachable. Quarter-end-ish samples are enough to render the
# right shape.
_FALLBACK = {
    "1955-07": 1.68, "1957-01": 2.84, "1958-01": 2.72, "1960-01": 3.99,
    "1962-01": 2.15, "1965-01": 3.90, "1968-01": 4.61, "1970-01": 8.98,
    "1971-07": 5.31, "1973-07": 10.40, "1974-07": 12.92, "1975-01": 7.13,
    "1977-01": 4.61, "1979-01": 10.07, "1980-04": 17.61,
    "1981-07": 19.04, "1982-01": 13.22, "1983-01": 8.68, "1985-01": 8.35,
    "1987-10": 7.29, "1989-01": 9.12, "1990-01": 8.23, "1992-09": 3.22,
    "1994-01": 3.05, "1995-07": 5.74, "1998-01": 5.56, "2000-05": 6.27,
    "2001-01": 5.98, "2003-06": 1.00, "2004-06": 1.03, "2006-06": 4.99,
    "2007-09": 4.94, "2008-09": 1.81, "2008-12": 0.16, "2010-01": 0.11,
    "2012-01": 0.08, "2014-01": 0.07, "2015-12": 0.24, "2017-01": 0.65,
    "2018-12": 2.40, "2019-07": 2.40, "2019-12": 1.55, "2020-03": 0.65,
    "2020-04": 0.05, "2021-01": 0.09, "2022-03": 0.20, "2022-09": 2.56,
    "2023-07": 5.12, "2023-12": 5.33, "2024-09": 5.13, "2024-12": 4.48,
    "2025-06": 3.88, "2026-04": 3.625,
}


# Annotations: (date, level, en, hk, tw, cn, dx, dy)
EVENTS = [
    ("1981-07-01", 19.04,
        "Volcker peak\n19.1% (Jul 1981)",
        "沃爾克峰\n19.1%(1981-07)",
        "沃克峰\n19.1%(1981-07)",
        "沃尔克峰\n19.1%(1981-07)",
        25, -10),
    ("2008-12-01", 0.16,
        "2008 ZLB\n0.00-0.25%",
        "2008 零利率\n0.00-0.25%",
        "2008 零利率\n0.00-0.25%",
        "2008 零利率\n0.00-0.25%",
        -10, 50),
    ("2018-12-01", 2.40,
        "2015-19\nnormalisation",
        "2015-19\n正常化",
        "2015-19\n正常化",
        "2015-19\n正常化",
        -25, 60),
    ("2020-04-01", 0.05,
        "Mar 2020\nemergency cut",
        "2020-03\n緊急減息",
        "2020-03\n緊急降息",
        "2020-03\n紧急降息",
        15, 65),
    ("2023-07-01", 5.33,
        "525 bps\nin 18 months",
        "18 個月\n加 525 bp",
        "18 個月\n升 525 bp",
        "18 个月\n加 525 bp",
        -110, -20),
    ("2026-04-01", 3.625,
        "Apr 2026\n3.625% (today)",
        "2026-04\n3.625%(當前)",
        "2026-04\n3.625%(當前)",
        "2026-04\n3.625%(当前)",
        -160, 35),
]


LANG_STRINGS = {
    "en": {
        "title":    "US Fed funds effective rate, 1955 - April 2026",
        "subtitle": "FRED FEDFUNDS monthly. Volcker peak, 2008 ZLB, 2020 emergency cut, 2022-23 fastest hiking cycle since Volcker, and the 2024-26 normalisation.",
        "xlabel":   "Year",
        "ylabel":   "Fed funds effective rate (% annual)",
        "neutral":  "Long-run neutral ~2.75-3.00%",
        "footer":   "Source: Federal Reserve Board H.15 / FRED FEDFUNDS. Effective rate (monthly average). 2026-04 reading approximate (mid-month).",
    },
    "hk": {
        "title":    "美國聯邦基金有效利率,1955 - 2026 年 4 月",
        "subtitle": "FRED FEDFUNDS 月度。沃爾克峰、2008 零利率下限、2020 緊急減息、2022-23 沃爾克後最快加息周期、以及 2024-26 正常化。",
        "xlabel":   "年份",
        "ylabel":   "聯邦基金有效利率(年化 %)",
        "neutral":  "長期中性利率 ~2.75-3.00%",
        "footer":   "資料來源:美國聯儲局 H.15 / FRED FEDFUNDS。月度平均有效利率。2026-04 為月中估值。",
    },
    "tw": {
        "title":    "美國聯邦資金有效利率,1955 - 2026 年 4 月",
        "subtitle": "FRED FEDFUNDS 月度資料。沃克峰、2008 零利率下限、2020 緊急降息、2022-23 沃克後最快升息循環,以及 2024-26 正常化。",
        "xlabel":   "年份",
        "ylabel":   "聯邦資金有效利率(年化 %)",
        "neutral":  "長期中性利率 ~2.75-3.00%",
        "footer":   "資料來源:美國聯準會 H.15 / FRED FEDFUNDS。月度平均有效利率。2026-04 為月中估值。",
    },
    "cn": {
        "title":    "美国联邦基金有效利率,1955 - 2026 年 4 月",
        "subtitle": "FRED FEDFUNDS 月度。沃尔克峰、2008 零利率下限、2020 紧急降息、2022-23 沃尔克之后最快加息周期,以及 2024-26 正常化。",
        "xlabel":   "年份",
        "ylabel":   "联邦基金有效利率(年化 %)",
        "neutral":  "长期中性利率 ~2.75-3.00%",
        "footer":   "数据来源:美国联储 H.15 / FRED FEDFUNDS。月度平均有效利率。2026-04 为月中估值。",
    },
}


def _load_ffr() -> pd.Series:
    try:
        df = fred_series("FEDFUNDS", start="1954-07-01")
        s = df.iloc[:, 0].dropna().astype(float)
        s.index = pd.to_datetime(s.index)
        s = s[s.index <= "2026-04-30"]
        if s.empty or s.iloc[-1] != s.iloc[-1]:
            raise RuntimeError("empty FRED FEDFUNDS")
        # ensure we have a 2026-04 reading; if not, append known snapshot.
        if s.index.max() < pd.Timestamp("2026-04-01"):
            s = pd.concat([s, pd.Series([3.625],
                          index=[pd.Timestamp("2026-04-01")])])
        return s.sort_index()
    except Exception as e:
        print(f"FRED FEDFUNDS unavailable ({e}); using embedded fallback")
        idx = pd.to_datetime([k + "-15" for k in _FALLBACK.keys()])
        return pd.Series(list(_FALLBACK.values()), index=idx).sort_index()


def build_fig(s):
    p = PALETTE_LIGHT
    ffr = _load_ffr()

    fig, ax = plt.subplots(figsize=(12.0, 6.4), dpi=150)
    style_axes(ax, p)

    # Shaded ZLB era
    ax.axvspan(pd.Timestamp("2008-12-01"), pd.Timestamp("2015-12-01"),
               color=p["muted"], alpha=0.10)
    ax.axvspan(pd.Timestamp("2020-03-01"), pd.Timestamp("2022-03-01"),
               color=p["muted"], alpha=0.10)

    # Hiking cycle 2022-23 in accent
    ax.axvspan(pd.Timestamp("2022-03-01"), pd.Timestamp("2023-07-01"),
               color=p["accent"], alpha=0.10)

    # Main line + light fill below
    ax.fill_between(ffr.index, ffr.values, 0,
                    color=p["blue"], alpha=0.12, linewidth=0)
    ax.plot(ffr.index, ffr.values, color=p["blue"], linewidth=1.5)

    # Long-run neutral band 2.75-3.00%
    ax.axhspan(2.75, 3.00, color=p["green"], alpha=0.10)
    ax.text(pd.Timestamp("1957-01-01"), 3.45, s["neutral"],
            color=p["green"], fontsize=8.6, fontweight="bold")

    # Annotations per locale.
    lang_idx = {"en": 2, "hk": 3, "tw": 4, "cn": 5}
    li = lang_idx.get(s.get("_lang", "en"), 2)
    for ev in EVENTS:
        date = pd.to_datetime(ev[0])
        level = ev[1]
        label = ev[li]
        dx, dy = ev[6], ev[7]
        ax.plot([date], [level], "o", color=p["fg"],
                markersize=5.5, markerfacecolor=p["accent"], zorder=5)
        ax.annotate(
            label, xy=(date, level),
            xytext=(dx, dy), textcoords="offset points",
            ha="center", fontsize=8.3, color=p["fg"], fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=p["muted"],
                            linewidth=0.6, alpha=0.7),
        )

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(-1, 22)
    ax.set_xlim(pd.Timestamp("1954-01-01"), pd.Timestamp("2027-06-01"))
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.4, color=p["muted"])

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


def build_fig_with_lang(lang_key):
    def _build(strings):
        strings = dict(strings)
        strings["_lang"] = lang_key
        return build_fig(strings)
    return _build


if __name__ == "__main__":
    apply_cjk_font()
    paths = []
    for lang in ("en", "hk", "tw", "cn"):
        from scripts.chart_helpers import save_localized_png  # noqa: E402
        fig = build_fig_with_lang(lang)(LANG_STRINGS[lang])
        paths.append(save_localized_png(fig, BASE, lang, OUT_DIR, dpi=160))
        plt.close(fig)
    for pth in paths:
        print(f"wrote {pth}")
