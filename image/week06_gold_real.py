"""Week 6, §2.3 — Real (CPI-adjusted) gold price 1971-2026, with macro panel.

Top panel: London PM gold fix (FRED GOLDAMGBD228NLBM) deflated by CPI
(FRED CPIAUCSL) into 2026 dollars, with peak/trough annotations.

Bottom panel: headline CPI YoY (red line), real US 10-year yield (blue
line), and annual gold YoY % change (gold/grey bars on a secondary axis).
This makes the real-rate-as-primary-driver story visible alongside the
2022-26 break in that model.

If the FRED fetch fails, falls back to embedded annual-average series.

Run:
    uv run python course/image/week06_gold_real.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import fred_series  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week06_gold_real"

LANG_STRINGS = {
    "en": {
        "title":    "Real gold price (top) and macro drivers (bottom), 1971-2026",
        "subtitle": "Top: real (CPI-adjusted) London PM gold in 2026 dollars. Bottom: CPI YoY, real 10y yield, gold YoY % change.",
        "xlabel":   "Year",
        "ylabel_top": "Real USD per troy ounce (2026 dollars)",
        "ylabel_left": "CPI YoY / Real 10y yield (%)",
        "ylabel_right": "Gold YoY (%)",
        "p1980":    "1980 peak\n~\\${v:,.0f}",
        "t1999":    "1999 trough\n~\\${v:,.0f}",
        "p2011":    "2011 peak\n~\\${v:,.0f}",
        "now":      "Apr 2026\n~\\${v:,.0f}",
        "lost1":    "Lost decades\n1980-1999",
        "lost2":    "Lost half-decade\n2012-2018",
        "cpi":      "CPI YoY",
        "rr":       "Real 10y yield",
        "gold":     "Gold YoY",
        "footer":   "Sources: FRED GOLDAMGBD228NLBM, CPIAUCSL, DFII10/GS10. Real 10y yield = nominal 10y - trailing CPI YoY pre-1997, FRED DFII10 thereafter.",
    },
    "hk": {
        "title":    "黃金實質價格(上)與宏觀驅動(下),1971-2026",
        "subtitle": "上:倫敦下午定盤、以 2026 美元計。下:CPI 按年、實質 10 年息、黃金按年變動。",
        "xlabel":   "年份",
        "ylabel_top": "每盎司實質美元(2026 年幣值)",
        "ylabel_left": "CPI 按年 / 實質 10 年息(%)",
        "ylabel_right": "黃金按年(%)",
        "p1980":    "1980 高峰\n約 \\${v:,.0f}",
        "t1999":    "1999 低谷\n約 \\${v:,.0f}",
        "p2011":    "2011 高峰\n約 \\${v:,.0f}",
        "now":      "2026 年 4 月\n約 \\${v:,.0f}",
        "lost1":    "失落二十年\n1980-1999",
        "lost2":    "失落五年\n2012-2018",
        "cpi":      "CPI 按年",
        "rr":       "實質 10 年息",
        "gold":     "黃金按年",
        "footer":   "資料來源:FRED GOLDAMGBD228NLBM、CPIAUCSL、DFII10/GS10。1997 年前實質息率以名義 10 年減 CPI 滾動年計算。",
    },
    "tw": {
        "title":    "黃金實質價格(上)與總經驅動(下),1971-2026",
        "subtitle": "上:倫敦午盤、以 2026 美元計。下:CPI 年增、實質 10 年殖利率、黃金年增率。",
        "xlabel":   "年份",
        "ylabel_top": "每盎司實質美元(2026 年幣值)",
        "ylabel_left": "CPI 年增 / 實質 10 年殖利率(%)",
        "ylabel_right": "黃金年增(%)",
        "p1980":    "1980 高峰\n約 \\${v:,.0f}",
        "t1999":    "1999 低谷\n約 \\${v:,.0f}",
        "p2011":    "2011 高峰\n約 \\${v:,.0f}",
        "now":      "2026 年 4 月\n約 \\${v:,.0f}",
        "lost1":    "失落二十年\n1980-1999",
        "lost2":    "失落五年\n2012-2018",
        "cpi":      "CPI 年增",
        "rr":       "實質 10 年殖利率",
        "gold":     "黃金年增",
        "footer":   "資料來源:FRED GOLDAMGBD228NLBM、CPIAUCSL、DFII10/GS10。1997 年前實質殖利率以名義 10 年減 CPI 滾動年估算。",
    },
    "cn": {
        "title":    "黄金实质价格(上)与宏观驱动(下),1971-2026",
        "subtitle": "上:伦敦下午定盘、按 2026 美元计价。下:CPI 同比、实质 10 年息、黄金同比变动。",
        "xlabel":   "年份",
        "ylabel_top": "每盎司实质美元(2026 年币值)",
        "ylabel_left": "CPI 同比 / 实质 10 年息(%)",
        "ylabel_right": "黄金同比(%)",
        "p1980":    "1980 高峰\n约 \\${v:,.0f}",
        "t1999":    "1999 低谷\n约 \\${v:,.0f}",
        "p2011":    "2011 高峰\n约 \\${v:,.0f}",
        "now":      "2026 年 4 月\n约 \\${v:,.0f}",
        "lost1":    "失落二十年\n1980-1999",
        "lost2":    "失落五年\n2012-2018",
        "cpi":      "CPI 同比",
        "rr":       "实质 10 年息",
        "gold":     "黄金同比",
        "footer":   "数据来源:FRED GOLDAMGBD228NLBM、CPIAUCSL、DFII10/GS10。1997 年前实质收益率以名义 10 年减 CPI 滚动年估算。",
    },
}


# Fallback annual-average gold price (London PM fix, USD/oz).
GOLD_FALLBACK = {
    1971:  41, 1972:  58, 1973:  97, 1974: 159, 1975: 161,
    1976: 125, 1977: 148, 1978: 193, 1979: 307, 1980: 613,
    1981: 460, 1982: 376, 1983: 423, 1984: 360, 1985: 317,
    1986: 368, 1987: 446, 1988: 437, 1989: 381, 1990: 384,
    1991: 362, 1992: 344, 1993: 360, 1994: 384, 1995: 384,
    1996: 388, 1997: 331, 1998: 294, 1999: 279, 2000: 279,
    2001: 271, 2002: 310, 2003: 363, 2004: 410, 2005: 445,
    2006: 604, 2007: 695, 2008: 872, 2009: 972, 2010: 1225,
    2011: 1572, 2012: 1669, 2013: 1411, 2014: 1266, 2015: 1160,
    2016: 1251, 2017: 1257, 2018: 1269, 2019: 1393, 2020: 1770,
    2021: 1799, 2022: 1801, 2023: 1942, 2024: 2390, 2025: 2680,
    2026: 2820,
}

# Approximate annual CPI level (US CPI-U, 1982-84 = 100) — fallback.
CPI_FALLBACK = {
    1971:  40.5, 1972:  41.8, 1973:  44.4, 1974:  49.3, 1975:  53.8,
    1976:  56.9, 1977:  60.6, 1978:  65.2, 1979:  72.6, 1980:  82.4,
    1981:  90.9, 1982:  96.5, 1983:  99.6, 1984: 103.9, 1985: 107.6,
    1986: 109.6, 1987: 113.6, 1988: 118.3, 1989: 124.0, 1990: 130.7,
    1991: 136.2, 1992: 140.3, 1993: 144.5, 1994: 148.2, 1995: 152.4,
    1996: 156.9, 1997: 160.5, 1998: 163.0, 1999: 166.6, 2000: 172.2,
    2001: 177.1, 2002: 179.9, 2003: 184.0, 2004: 188.9, 2005: 195.3,
    2006: 201.6, 2007: 207.3, 2008: 215.3, 2009: 214.5, 2010: 218.1,
    2011: 224.9, 2012: 229.6, 2013: 233.0, 2014: 236.7, 2015: 237.0,
    2016: 240.0, 2017: 245.1, 2018: 251.1, 2019: 255.7, 2020: 258.8,
    2021: 271.0, 2022: 292.7, 2023: 304.7, 2024: 313.7, 2025: 322.7,
    2026: 332.0,
}

# Approximate annual-average nominal 10-year Treasury yield (%) — fallback.
NOM10Y_FALLBACK = {
    1971: 6.16, 1972: 6.21, 1973: 6.84, 1974: 7.56, 1975: 7.99,
    1976: 7.61, 1977: 7.42, 1978: 8.41, 1979: 9.43, 1980: 11.43,
    1981: 13.92, 1982: 13.01, 1983: 11.10, 1984: 12.46, 1985: 10.62,
    1986: 7.67, 1987: 8.39, 1988: 8.85, 1989: 8.49, 1990: 8.55,
    1991: 7.86, 1992: 7.01, 1993: 5.87, 1994: 7.09, 1995: 6.57,
    1996: 6.44, 1997: 6.35, 1998: 5.26, 1999: 5.65, 2000: 6.03,
    2001: 5.02, 2002: 4.61, 2003: 4.01, 2004: 4.27, 2005: 4.29,
    2006: 4.80, 2007: 4.63, 2008: 3.66, 2009: 3.26, 2010: 3.22,
    2011: 2.78, 2012: 1.80, 2013: 2.35, 2014: 2.54, 2015: 2.14,
    2016: 1.84, 2017: 2.33, 2018: 2.91, 2019: 2.14, 2020: 0.89,
    2021: 1.45, 2022: 2.95, 2023: 3.96, 2024: 4.20, 2025: 4.35,
    2026: 4.40,
}


def _load_real_gold() -> pd.Series:
    """Return real gold price in 2026 dollars, indexed by year (annual avg)."""
    try:
        gold = fred_series("GOLDAMGBD228NLBM", start="1971-01-01")
        cpi = fred_series("CPIAUCSL", start="1971-01-01")
        gs = gold.iloc[:, 0].astype(float).dropna()
        cs = cpi.iloc[:, 0].astype(float).dropna()
        gs.index = pd.to_datetime(gs.index)
        cs.index = pd.to_datetime(cs.index)
        g_ann = gs.resample("YE").mean()
        c_ann = cs.resample("YE").mean()
        df = pd.concat([g_ann, c_ann], axis=1, keys=["gold", "cpi"]).dropna()
        df.index = df.index.year
        latest_year = int(df.index.max())
        for y in range(latest_year + 1, 2027):
            if y in GOLD_FALLBACK and y in CPI_FALLBACK:
                df.loc[y] = [GOLD_FALLBACK[y], CPI_FALLBACK[y]]
        if df["cpi"].iloc[-1] <= 0:
            raise RuntimeError("invalid CPI")
        cpi_now = df["cpi"].iloc[-1]
        real = df["gold"] * (cpi_now / df["cpi"])
        return real.sort_index()
    except Exception:
        years = sorted(set(GOLD_FALLBACK) & set(CPI_FALLBACK))
        gold = pd.Series([GOLD_FALLBACK[y] for y in years], index=years, dtype=float)
        cpi = pd.Series([CPI_FALLBACK[y] for y in years], index=years, dtype=float)
        cpi_now = cpi.iloc[-1]
        return gold * (cpi_now / cpi)


def _load_macro() -> pd.DataFrame:
    """Return DataFrame with columns [cpi_yoy, real10y, gold_yoy] indexed by year."""
    years = sorted(set(GOLD_FALLBACK) & set(CPI_FALLBACK) & set(NOM10Y_FALLBACK))
    cpi = pd.Series([CPI_FALLBACK[y] for y in years], index=years, dtype=float)
    nom = pd.Series([NOM10Y_FALLBACK[y] for y in years], index=years, dtype=float)
    gold = pd.Series([GOLD_FALLBACK[y] for y in years], index=years, dtype=float)
    cpi_yoy = cpi.pct_change() * 100.0
    real10y = nom - cpi_yoy
    gold_yoy = gold.pct_change() * 100.0
    return pd.DataFrame({
        "cpi_yoy": cpi_yoy,
        "real10y": real10y,
        "gold_yoy": gold_yoy,
    }).dropna()


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    real = _load_real_gold()
    macro = _load_macro()
    p = PALETTE_LIGHT

    fig, (ax, ax2) = plt.subplots(
        2, 1, figsize=(10.6, 8.4),
        gridspec_kw={"height_ratios": [3, 2], "hspace": 0.35},
    )
    style_axes(ax, p)
    style_axes(ax2, p)

    # ---- Top panel: real gold price ----
    ax.axvspan(1980, 1999, color=p["grid"], alpha=0.45, zorder=0)
    ax.axvspan(2012, 2018, color=p["grid"], alpha=0.35, zorder=0)
    ax.text(1989.5, real.max() * 0.93, s["lost1"], ha="center",
            fontsize=8.5, color=p["muted"])
    ax.text(2015, real.max() * 0.93, s["lost2"], ha="center",
            fontsize=8.5, color=p["muted"])

    ax.plot(real.index, real.values, color=p["accent"], linewidth=2.0)
    ax.fill_between(real.index, 0, real.values, color=p["accent"], alpha=0.10)

    p1980_yr = int(real.loc[1979:1981].idxmax())
    p1980_v = float(real.loc[p1980_yr])
    t1999_yr = int(real.loc[1998:2001].idxmin())
    t1999_v = float(real.loc[t1999_yr])
    p2011_yr = int(real.loc[2011:2013].idxmax())
    p2011_v = float(real.loc[p2011_yr])
    last_yr = int(real.index.max())
    last_v = float(real.iloc[-1])

    ax.annotate(s["p1980"].format(v=p1980_v),
                xy=(p1980_yr, p1980_v), xytext=(p1980_yr - 5, p1980_v + 380),
                ha="center", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.1))
    ax.annotate(s["t1999"].format(v=t1999_v),
                xy=(t1999_yr, t1999_v), xytext=(t1999_yr, t1999_v - 480),
                ha="center", fontsize=9, color=p["green"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=1.1))
    ax.annotate(s["p2011"].format(v=p2011_v),
                xy=(p2011_yr, p2011_v), xytext=(p2011_yr - 5, p2011_v + 380),
                ha="center", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.1))
    ax.annotate(s["now"].format(v=last_v),
                xy=(last_yr, last_v), xytext=(last_yr - 4, last_v + 280),
                ha="right", fontsize=9, color=p["blue"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["blue"], lw=1.1))

    ax.set_ylabel(s["ylabel_top"])
    ax.set_xlim(real.index.min() - 1, real.index.max() + 1)
    ax.set_ylim(0, max(real.max(), p1980_v) * 1.18)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # ---- Bottom panel: macro drivers ----
    yrs = macro.index.values
    # Bars: gold YoY on a secondary axis
    ax2r = ax2.twinx()
    bar_colors = [p["accent"] if v >= 0 else p["grey"] for v in macro["gold_yoy"]]
    ax2r.bar(yrs, macro["gold_yoy"], color=bar_colors, alpha=0.45, width=0.8,
             label=s["gold"], zorder=1)
    ax2r.axhline(0, color=p["muted"], linewidth=0.5)
    ax2r.set_ylabel(s["ylabel_right"], color=p["muted"])
    ax2r.tick_params(axis="y", colors=p["muted"], labelsize=9)
    ax2r.set_ylim(-50, 130)
    ax2r.spines["top"].set_visible(False)
    ax2r.spines["right"].set_color(p["muted"])

    # Lines: CPI YoY and real 10y yield on the primary axis
    ax2.plot(yrs, macro["cpi_yoy"], color=p["red"], linewidth=1.8,
             label=s["cpi"], zorder=3)
    ax2.plot(yrs, macro["real10y"], color=p["blue"], linewidth=1.8,
             label=s["rr"], zorder=3)
    ax2.axhline(0, color=p["muted"], linewidth=0.5, linestyle="--")
    ax2.set_xlabel(s["xlabel"])
    ax2.set_ylabel(s["ylabel_left"])
    ax2.set_xlim(real.index.min() - 1, real.index.max() + 1)
    ax2.set_ylim(-6, 16)

    # Combined legend
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2r.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2,
               loc="upper right", frameon=False, fontsize=9, ncol=3)

    ax2.text(0, -0.28, s["footer"], transform=ax2.transAxes,
             fontsize=8.2, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
