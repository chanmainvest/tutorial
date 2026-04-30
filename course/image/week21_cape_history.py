"""Week 21, §2.5 — Shiller CAPE 1881-Apr 2026.

Annual cyclically-adjusted P/E (10-year smoothed real earnings) for the
S&P Composite, from Robert Shiller's online dataset. Approximate annual
year-end values are embedded inline so the chart renders offline.

Run:
    uv run python course/image/week21_cape_history.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week21_cape_history"


# Approximate end-of-year Shiller CAPE values. Source: Robert Shiller's
# online dataset (econ.yale.edu/~shiller/data.htm), rounded to 0.1.
# Values for 1881..1924 are the 10-year-trailing CAPE he reconstructs.
# Apr 2026 is the trailing reading shown on multpl.com / GuruFocus.
CAPE = {
    1881: 18.5, 1882: 17.4, 1883: 17.0, 1884: 14.8, 1885: 15.6,
    1886: 16.6, 1887: 18.5, 1888: 17.6, 1889: 17.6, 1890: 17.0,
    1891: 16.0, 1892: 17.7, 1893: 13.6, 1894: 14.8, 1895: 14.6,
    1896: 13.4, 1897: 16.0, 1898: 18.4, 1899: 22.6, 1900: 18.3,
    1901: 22.7, 1902: 20.7, 1903: 16.5, 1904: 18.9, 1905: 20.4,
    1906: 19.6, 1907: 13.4, 1908: 16.0, 1909: 17.9, 1910: 14.5,
    1911: 13.7, 1912: 13.5, 1913: 11.0, 1914: 10.5, 1915: 11.5,
    1916: 12.4, 1917: 7.4,  1918: 6.3,  1919: 7.4,  1920: 5.0,
    1921: 5.1,  1922: 7.5,  1923: 8.2,  1924: 9.5,  1925: 11.3,
    1926: 12.4, 1927: 15.0, 1928: 21.0, 1929: 32.6, 1930: 22.3,
    1931: 8.8,  1932: 6.1,  1933: 11.0, 1934: 13.0, 1935: 15.3,
    1936: 17.6, 1937: 12.0, 1938: 13.2, 1939: 13.7, 1940: 11.0,
    1941: 8.9,  1942: 9.5,  1943: 11.0, 1944: 11.3, 1945: 13.7,
    1946: 14.3, 1947: 11.4, 1948: 10.4, 1949: 9.8,  1950: 10.7,
    1951: 11.7, 1952: 11.9, 1953: 12.6, 1954: 17.0, 1955: 19.3,
    1956: 19.7, 1957: 14.5, 1958: 17.7, 1959: 18.3, 1960: 17.7,
    1961: 21.4, 1962: 17.5, 1963: 19.1, 1964: 21.1, 1965: 23.0,
    1966: 19.3, 1967: 21.6, 1968: 21.6, 1969: 17.6, 1970: 16.4,
    1971: 17.7, 1972: 18.7, 1973: 13.5, 1974: 8.3,  1975: 11.2,
    1976: 11.7, 1977: 9.3,  1978: 9.2,  1979: 9.3,  1980: 8.8,
    1981: 7.4,  1982: 9.7,  1983: 11.7, 1984: 10.3, 1985: 13.7,
    1986: 16.2, 1987: 15.7, 1988: 14.4, 1989: 17.7, 1990: 15.0,
    1991: 19.5, 1992: 20.4, 1993: 21.4, 1994: 20.4, 1995: 24.6,
    1996: 27.7, 1997: 32.9, 1998: 40.6, 1999: 44.2, 2000: 36.4,
    2001: 28.3, 2002: 22.7, 2003: 26.5, 2004: 27.5, 2005: 26.5,
    2006: 27.0, 2007: 26.4, 2008: 15.2, 2009: 20.3, 2010: 22.1,
    2011: 21.2, 2012: 22.4, 2013: 25.4, 2014: 27.0, 2015: 26.0,
    2016: 28.1, 2017: 32.4, 2018: 28.4, 2019: 30.3, 2020: 33.5,
    2021: 38.6, 2022: 28.3, 2023: 31.0, 2024: 35.1, 2025: 36.5,
    2026: 36.0,  # April 2026 reading
}

YEARS = sorted(CAPE.keys())
VALUES = [CAPE[y] for y in YEARS]
LONG_RUN_MEAN = float(np.mean(VALUES))  # ~17

# Major peaks/troughs to annotate.
PEAKS = [(1929, 32.6, "1929"), (1966, 23.0, "1966"),
         (1999, 44.2, "2000"), (2021, 38.6, "2021"),
         (2026, 36.0, "Apr 2026")]
TROUGHS = [(1920, 5.0, "1920"), (1932, 6.1, "1932"),
           (1981, 7.4, "1981"), (2009, 20.3, "2009")]


LANG_STRINGS = {
    "en": {
        "title":    "Shiller CAPE, 1881 to April 2026",
        "subtitle": "Cyclically-adjusted P/E: S&P Composite price divided by 10-year average of real earnings. Source: Shiller dataset (Yale); April 2026 reading approx 36.",
        "xlabel":   "Year",
        "ylabel":   "CAPE (P / 10-yr real earnings)",
        "mean":     "Long-run mean ~ 17",
        "footer":   "April 2026 sits in the most expensive decile of US-stock-market history. Only 1929 and 1999-2000 were materially higher.",
    },
    "hk": {
        "title":    "席勒 CAPE,1881 至 2026 年 4 月",
        "subtitle": "周期調整本益比:標普綜合指數除以過去十年實質盈利平均。資料來源:Shiller 數據集(耶魯);2026 年 4 月讀數約 36。",
        "xlabel":   "年份",
        "ylabel":   "CAPE(價格 / 10 年實質盈利)",
        "mean":     "長期平均約 17",
        "footer":   "2026 年 4 月處於美股歷史最貴的十分位內。只有 1929 與 1999-2000 比現在更貴。",
    },
    "tw": {
        "title":    "席勒 CAPE,1881 至 2026 年 4 月",
        "subtitle": "循環調整本益比:標普綜合指數除以過去十年實質盈餘平均。資料來源:Shiller 資料集(耶魯);2026 年 4 月讀數約 36。",
        "xlabel":   "年份",
        "ylabel":   "CAPE(價格 / 10 年實質盈餘)",
        "mean":     "長期平均約 17",
        "footer":   "2026 年 4 月處於美股歷史最貴的十分位內。只有 1929 與 1999-2000 比現在更貴。",
    },
    "cn": {
        "title":    "席勒 CAPE,1881 至 2026 年 4 月",
        "subtitle": "周期调整市盈率:标普综合指数除以过去十年实际盈利平均。资料来源:Shiller 数据集(耶鲁);2026 年 4 月读数约 36。",
        "xlabel":   "年份",
        "ylabel":   "CAPE(价格 / 10 年实际盈利)",
        "mean":     "长期平均约 17",
        "footer":   "2026 年 4 月处于美股历史最贵的十分位内。只有 1929 与 1999-2000 比现在更贵。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.6, 6.0))
    style_axes(ax, p)

    ax.fill_between(YEARS, 0, VALUES, color=p["accent"], alpha=0.10)
    ax.plot(YEARS, VALUES, color=p["accent"], linewidth=1.7)

    # Long-run mean line.
    ax.axhline(LONG_RUN_MEAN, color=p["muted"], linewidth=1.0,
               linestyle="--", alpha=0.85)
    ax.text(YEARS[2], LONG_RUN_MEAN + 0.8, s["mean"],
            fontsize=9.5, color=p["muted"], style="italic")

    # Peaks (red).
    for yr, val, lbl in PEAKS:
        ax.plot(yr, val, "o", color=p["red"], markersize=6, zorder=5)
        ax.annotate(f"{lbl}\n{val:.0f}",
                    xy=(yr, val), xytext=(0, 14),
                    textcoords="offset points",
                    ha="center", fontsize=9, color=p["red"],
                    fontweight="bold")

    # Troughs (blue).
    for yr, val, lbl in TROUGHS:
        ax.plot(yr, val, "o", color=p["blue"], markersize=6, zorder=5)
        ax.annotate(f"{lbl}\n{val:.0f}",
                    xy=(yr, val), xytext=(0, -22),
                    textcoords="offset points",
                    ha="center", fontsize=9, color=p["blue"],
                    fontweight="bold")

    ax.set_xlim(1875, 2032)
    ax.set_ylim(0, 50)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontweight="bold")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
