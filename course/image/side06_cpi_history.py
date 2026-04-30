"""Side 06, sec 1 -- US CPI year-over-year, 1914 to April 2026.

FRED CPIAUCSL monthly index, converted to YoY% via 12-month diff.
Annotates WW1, WW2, the 1970s wave, the March 1980 peak (14.8%),
the 2008 oil spike, and the June 2022 peak (9.1%). 2% Fed target
and 5% high-inflation threshold drawn as dashed/dotted reference
lines.

Run:
    uv run python course/image/side06_cpi_history.py
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
BASE = "side06_cpi_history"


# Annotated peaks: (date, yoy_pct, en, hk, tw, cn).
EVENTS = [
    ("1918-06-01", 17.5,  "WW1 supply",          "一戰物資",          "一戰物資",          "一战物资"),
    ("1947-03-01", 19.7,  "WW2 reset",           "戰後重置",          "戰後重置",          "战后重置"),
    ("1974-12-01", 12.3,  "1974 oil",            "1974 石油",         "1974 石油",         "1974 石油"),
    ("1980-03-01", 14.8,  "Mar-1980 peak 14.8",  "1980-03 峰 14.8",   "1980-03 峰 14.8",   "1980-03 峰 14.8"),
    ("2008-07-01", 5.6,   "2008 oil spike",      "2008 油價",         "2008 油價",         "2008 油价"),
    ("2022-06-01", 9.1,   "Jun-2022 peak 9.1",   "2022-06 峰 9.1",    "2022-06 峰 9.1",    "2022-06 峰 9.1"),
]


# Embedded annual fallback (Jan-of-year YoY%), 1914-2026, used only if
# FRED is unreachable. Sourced from BLS historical tables; sufficient to
# render the chart shape.
_FALLBACK = {
    1914: 1.0, 1915: 1.0, 1916: 7.9, 1917: 17.4, 1918: 18.0, 1919: 14.6,
    1920: 15.6, 1921: -10.5, 1922: -6.1, 1923: 1.8, 1924: 0.0, 1925: 2.3,
    1926: 1.1, 1927: -1.7, 1928: -1.7, 1929: 0.0, 1930: -2.3, 1931: -9.0,
    1932: -9.9, 1933: -5.1, 1934: 3.1, 1935: 2.2, 1936: 1.5, 1937: 3.6,
    1938: -2.1, 1939: -1.4, 1940: 0.7, 1941: 5.0, 1942: 10.9, 1943: 6.1,
    1944: 1.7, 1945: 2.3, 1946: 8.3, 1947: 14.4, 1948: 8.1, 1949: -1.2,
    1950: 1.3, 1951: 7.9, 1952: 2.3, 1953: 0.8, 1954: 0.7, 1955: -0.4,
    1956: 1.5, 1957: 3.3, 1958: 2.8, 1959: 0.7, 1960: 1.7, 1961: 1.0,
    1962: 1.0, 1963: 1.3, 1964: 1.3, 1965: 1.6, 1966: 2.9, 1967: 3.1,
    1968: 4.2, 1969: 5.5, 1970: 5.7, 1971: 4.4, 1972: 3.2, 1973: 6.2,
    1974: 11.0, 1975: 9.1, 1976: 5.7, 1977: 6.5, 1978: 7.6, 1979: 11.3,
    1980: 13.5, 1981: 10.3, 1982: 6.2, 1983: 3.2, 1984: 4.3, 1985: 3.6,
    1986: 1.9, 1987: 3.6, 1988: 4.1, 1989: 4.8, 1990: 5.4, 1991: 4.2,
    1992: 3.0, 1993: 3.0, 1994: 2.6, 1995: 2.8, 1996: 3.0, 1997: 2.3,
    1998: 1.6, 1999: 2.2, 2000: 3.4, 2001: 2.8, 2002: 1.6, 2003: 2.3,
    2004: 2.7, 2005: 3.4, 2006: 3.2, 2007: 2.8, 2008: 3.8, 2009: -0.4,
    2010: 1.6, 2011: 3.2, 2012: 2.1, 2013: 1.5, 2014: 1.6, 2015: 0.1,
    2016: 1.3, 2017: 2.1, 2018: 2.4, 2019: 1.8, 2020: 1.2, 2021: 4.7,
    2022: 8.0, 2023: 4.1, 2024: 2.9, 2025: 3.0, 2026: 3.2,
}


def _load_cpi_yoy() -> pd.Series:
    # FRED CPIAUCSL starts Jan 1947, so pre-1947 always comes from the
    # embedded annual fallback. Splice the two so the chart is continuous
    # back to 1914.
    pre_idx = pd.to_datetime(
        [f"{y}-06-15" for y in _FALLBACK.keys() if y < 1947]
    )
    pre_vals = [_FALLBACK[y] for y in _FALLBACK.keys() if y < 1947]
    pre = pd.Series(pre_vals, index=pre_idx).sort_index()
    try:
        df = fred_series("CPIAUCSL", start="1946-01-01")
        s = df["CPIAUCSL"].dropna()
        if s.empty:
            raise RuntimeError("empty FRED CPI")
        yoy = (s / s.shift(12) - 1.0) * 100.0
        yoy = yoy.dropna()
        if yoy.empty:
            raise RuntimeError("empty YoY")
        combined = pd.concat([pre, yoy]).sort_index()
        return combined
    except Exception as e:
        print(f"FRED CPI unavailable ({e}); using embedded annual fallback")
        idx = pd.to_datetime([f"{y}-06-15" for y in _FALLBACK.keys()])
        return pd.Series(list(_FALLBACK.values()), index=idx).sort_index()


LANG_STRINGS = {
    "en": {
        "title":    "US CPI year-over-year, 1914 - April 2026",
        "subtitle": "Inflation is regime-ish: long quiet stretches punctuated by 1970s-style spikes. SOUL #2 (regime change), SOUL #3 (stores of value).",
        "xlabel":   "Year",
        "ylabel":   "CPI YoY (%)",
        "target":   "Fed target 2%",
        "stress":   "High-inflation 5%",
        "footer":   "Source: BLS via FRED CPIAUCSL. YoY = 12-month percentage change of seasonally-adjusted headline CPI.",
    },
    "hk": {
        "title":    "美國 CPI 按年變動,1914 - 2026 年 4 月",
        "subtitle": "通脹是周期性的:長期平靜被 1970 年代式急升打斷。SOUL #2(體制轉變)、SOUL #3(價值儲藏)。",
        "xlabel":   "年份",
        "ylabel":   "CPI 按年(%)",
        "target":   "聯儲目標 2%",
        "stress":   "高通脹 5%",
        "footer":   "資料來源:BLS / FRED CPIAUCSL。按年 = 經季節調整 CPI 的 12 個月百分比變動。",
    },
    "tw": {
        "title":    "美國 CPI 年增率,1914 - 2026 年 4 月",
        "subtitle": "通膨具體制特性:長期平靜被 1970 年代式飆升打斷。SOUL #2(體制轉變)、SOUL #3(價值儲藏)。",
        "xlabel":   "年份",
        "ylabel":   "CPI 年增(%)",
        "target":   "聯準目標 2%",
        "stress":   "高通膨 5%",
        "footer":   "資料來源:BLS / FRED CPIAUCSL。年增 = 經季節調整 CPI 的 12 個月百分比變動。",
    },
    "cn": {
        "title":    "美国 CPI 同比变动,1914 - 2026 年 4 月",
        "subtitle": "通胀具有体制性:长期平静被 1970 年代式飙升打断。SOUL #2(体制转变)、SOUL #3(价值储藏)。",
        "xlabel":   "年份",
        "ylabel":   "CPI 同比(%)",
        "target":   "美联储目标 2%",
        "stress":   "高通胀 5%",
        "footer":   "数据来源:BLS / FRED CPIAUCSL。同比 = 经季节调整 CPI 的 12 个月百分比变动。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    cpi = _load_cpi_yoy()

    fig, ax = plt.subplots(figsize=(12.0, 6.2), dpi=150)
    style_axes(ax, p)

    # Shade positive area red, negative area blue (deflation).
    pos = cpi.where(cpi >= 0, 0)
    neg = cpi.where(cpi < 0, 0)
    ax.fill_between(cpi.index, pos.values, color=p["red"], alpha=0.15,
                    linewidth=0)
    ax.fill_between(cpi.index, neg.values, color=p["blue"], alpha=0.15,
                    linewidth=0)
    ax.plot(cpi.index, cpi.values, color=p["red"], linewidth=0.9)

    # Reference lines.
    ax.axhline(2.0, color=p["green"], linewidth=1.0, linestyle="--",
               alpha=0.85)
    ax.axhline(5.0, color=p["accent"], linewidth=0.9, linestyle=":",
               alpha=0.80)
    ax.axhline(0.0, color=p["fg"], linewidth=0.7)

    ax.text(cpi.index[10], 2.5, s["target"],
            color=p["green"], fontsize=8.5, fontweight="bold")
    ax.text(cpi.index[10], 5.4, s["stress"],
            color=p["accent"], fontsize=8.5, fontweight="bold")

    # Annotations per lang.
    lang_idx = {"en": 2, "hk": 3, "tw": 4, "cn": 5}
    li = lang_idx.get(s.get("_lang", "en"), 2)
    for ev in EVENTS:
        date = pd.to_datetime(ev[0])
        level = ev[1]
        label = ev[li]
        ax.plot([date], [level], "o", color=p["fg"], markersize=5,
                markerfacecolor=p["accent"], zorder=5)
        ax.annotate(
            f"{label}",
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
    ax.set_ylim(-13, 22)
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"])

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


if __name__ == "__main__":
    for lc in ("en", "hk", "tw", "cn"):
        LANG_STRINGS[lc]["_lang"] = lc
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
