"""Week 23, S2.3 - Rolling 10-year HML and UMD premium, 1990-2024.

Annual factor returns embedded as approximate aggregates of the
Kenneth French monthly series (1981-2024, 44 obs each). The chart
plots the trailing 10-year arithmetic mean for HML (value) and UMD
(momentum), making the post-2003 value decay and the 2009 momentum
crash visible at a glance.

Run:
    uv run python course/image/week23_factor_decay.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week23_factor_decay"

YEARS = list(range(1981, 2025))  # 1981..2024 inclusive (44 years)

# Approximate annual returns for the academic HML factor (long-short).
HML = [
    0.12, 0.08, 0.14, 0.09, 0.04,-0.03,-0.05, 0.13, 0.01,  # 1981-1989
   -0.07, 0.01, 0.13, 0.18,-0.01,-0.02, 0.01, 0.12,-0.08,-0.15,  # 1990-1999
    0.21, 0.18, 0.08, 0.04, 0.07, 0.09, 0.13,-0.10, 0.02,-0.10,  # 2000-2009
   -0.04,-0.08, 0.10, 0.01,-0.01,-0.10, 0.24,-0.14,-0.09,-0.10,  # 2010-2019
   -0.47, 0.28, 0.21,-0.08, 0.00,                                  # 2020-2024
]

# Approximate annual returns for the academic UMD factor (long-short).
UMD = [
    0.11, 0.14, 0.08, 0.06, 0.18, 0.10, 0.14, 0.04, 0.18,  # 1981-1989
    0.16, 0.06, 0.07, 0.25, 0.00, 0.17, 0.07, 0.16, 0.22, 0.24,  # 1990-1999
    0.19, 0.07, 0.25,-0.02, 0.04, 0.18, 0.09, 0.15, 0.17,-0.45,  # 2000-2009
   -0.07,-0.07, 0.01, 0.08, 0.05, 0.09,-0.10, 0.11,-0.03, 0.08,  # 2010-2019
    0.22, 0.01, 0.17, 0.09, 0.14,                                  # 2020-2024
]

WINDOW = 10


LANG_STRINGS = {
    "en": {
        "title":    "Rolling 10-year mean of HML (value) and UMD (momentum), 1990-2024",
        "subtitle": "Trailing 10-year arithmetic mean of the academic long-short factor. Value flatlined post-2008; momentum took a single-year -45% blow in 2009.",
        "xlabel":   "Year (end of trailing 10-year window)",
        "ylabel":   "10-year mean factor return (annualised)",
        "hml":      "HML 10y mean (value)",
        "umd":      "UMD 10y mean (momentum)",
        "ann_value":"Value collapse 2008-2020",
        "ann_mom":  "Momentum crash 2009 (one-year -45%)",
        "footer":   "Approximate annual aggregates of the Kenneth French daily/monthly series. Rolling means computed on a 10-year trailing window.",
    },
    "hk": {
        "title":    "HML(價值)與 UMD(動量)滾動 10 年平均,1990-2024",
        "subtitle": "學術多空因子的過去 10 年算術平均。價值在 2008 後走平;動量在 2009 一年內遭遇 -45% 重擊。",
        "xlabel":   "年份(滾動 10 年窗口結束)",
        "ylabel":   "10 年平均因子回報(年化)",
        "hml":      "HML 10 年平均(價值)",
        "umd":      "UMD 10 年平均(動量)",
        "ann_value":"價值崩塌 2008-2020",
        "ann_mom":  "動量崩盤 2009(單年 -45%)",
        "footer":   "Kenneth French 日/月度因子的近似年度聚合。滾動平均使用過去 10 年窗口。",
    },
    "tw": {
        "title":    "HML(價值)與 UMD(動量)滾動 10 年平均,1990-2024",
        "subtitle": "學術多空因子的過去 10 年算術平均。價值在 2008 後走平;動量在 2009 一年內遭遇 -45% 重擊。",
        "xlabel":   "年份(滾動 10 年窗口結束)",
        "ylabel":   "10 年平均因子報酬(年化)",
        "hml":      "HML 10 年平均(價值)",
        "umd":      "UMD 10 年平均(動量)",
        "ann_value":"價值崩塌 2008-2020",
        "ann_mom":  "動量崩盤 2009(單年 -45%)",
        "footer":   "Kenneth French 日/月度因子的近似年度聚合。滾動平均使用過去 10 年窗口。",
    },
    "cn": {
        "title":    "HML(价值)与 UMD(动量)滚动 10 年平均,1990-2024",
        "subtitle": "学术多空因子的过去 10 年算术平均。价值在 2008 后走平;动量在 2009 一年内遭遇 -45% 重击。",
        "xlabel":   "年份(滚动 10 年窗口结束)",
        "ylabel":   "10 年平均因子回报(年化)",
        "hml":      "HML 10 年平均(价值)",
        "umd":      "UMD 10 年平均(动量)",
        "ann_value":"价值崩塌 2008-2020",
        "ann_mom":  "动量崩盘 2009(单年 -45%)",
        "footer":   "Kenneth French 日/月度因子的近似年度聚合。滚动平均使用过去 10 年窗口。",
    },
}


def _rolling(series, window):
    s = np.asarray(series, dtype=float)
    out = np.full_like(s, np.nan)
    for i in range(window - 1, len(s)):
        out[i] = s[i - window + 1: i + 1].mean()
    return out


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.0), dpi=150)
    style_axes(ax, p)

    yrs = np.array(YEARS)
    hml = np.array(HML)
    umd = np.array(UMD)
    rh = _rolling(hml, WINDOW)
    ru = _rolling(umd, WINDOW)

    # Restrict plot to 1990 onwards (first valid window ends 1990).
    mask = yrs >= 1990
    ax.plot(yrs[mask], rh[mask], color=p["blue"], linewidth=2.6, label=s["hml"])
    ax.plot(yrs[mask], ru[mask], color=p["red"],  linewidth=2.6, label=s["umd"])

    ax.axhline(0, color=p["fg"], linewidth=0.7)

    # Shaded band: 2008-2020 value collapse era.
    ax.axvspan(2008, 2020, color=p["accent"], alpha=0.08)
    ax.text(2014, 0.135, s["ann_value"], ha="center", fontsize=9.5,
            color=p["accent"], fontweight="bold")

    # Annotate 2009 momentum crash impact on the rolling mean.
    if not np.isnan(ru[yrs.tolist().index(2010)]):
        y_at = ru[yrs.tolist().index(2010)]
        ax.annotate(s["ann_mom"], xy=(2010, y_at), xytext=(2002, -0.04),
                    fontsize=9.5, color=p["red"],
                    arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.2))

    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))
    ax.set_xlim(1989.5, 2024.5)
    ax.set_ylim(-0.07, 0.16)

    ax.set_title(s["title"], fontsize=13.5, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.legend(loc="upper right", frameon=False, fontsize=10)
    fig.text(0.06, 0.02, s["footer"], fontsize=8.5, color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.95])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
