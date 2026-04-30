"""Side Lesson 5 - lump-sum vs. DCA winner per starting month, 1928-2024.

Pulls monthly ^GSPC closes via yahoo_history (or cache). For each
starting month from 1928-01 to 2023-12, computes the 12-month terminal
wealth of:
  - Lump sum: 120000 deployed at start, growing through 12 months.
  - DCA:      10000 deployed each month for 12 months, idle cash earns 0.

Each starting month is plotted as a thin vertical bar at +0.5 (blue)
when lump won, -0.5 (red) when DCA won. Aggregate win-rate annotated.

Run:
    uv run python course/image/side05_winrate_history.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)
from scripts.market_data import yahoo_history, damodaran_annual_returns  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side05_winrate_history"

LANG_STRINGS = {
    "en": {
        "title":    "Lump-sum vs. DCA: who wins each 12-month window, 1928-2024",
        "subtitle": "Monthly S&P 500 (^GSPC). Blue = $120k lump beat $10k x 12 DCA. Red = DCA won. Cash earns 0%.",
        "xlabel":   "Starting month",
        "ylabel":   "Lump wins   |   DCA wins",
        "lump":     "Lump-sum wins",
        "dca":      "DCA wins",
        "winrate":  "Lump-sum win rate",
        "annot": {
            "1929-09-01": "1929\ncrash",
            "1937-01-01": "1937\nrecession",
            "1973-01-01": "1973-74\nbear",
            "2000-01-01": "2000\ndot-com",
            "2008-01-01": "2008\nGFC",
        },
    },
    "hk": {
        "title":    "一筆過 vs 平均成本法:每個 12 個月窗口邊個贏,1928-2024",
        "subtitle": "標普 500 月度收盤(^GSPC)。藍色 = 12 萬一筆過勝一萬 x 12 平均成本法。紅色 = 平均成本法贏。現金 0% 利息。",
        "xlabel":   "起始月份",
        "ylabel":   "一筆過勝   |   平均成本法勝",
        "lump":     "一筆過勝",
        "dca":      "平均成本法勝",
        "winrate":  "一筆過勝率",
        "annot": {
            "1929-09-01": "1929\n大崩盤",
            "1937-01-01": "1937\n衰退",
            "1973-01-01": "1973-74\n熊市",
            "2000-01-01": "2000\n科網泡沫",
            "2008-01-01": "2008\n金融海嘯",
        },
    },
    "tw": {
        "title":    "一次投入 vs 定期定額:每個 12 個月窗口誰贏,1928-2024",
        "subtitle": "標普 500 月度收盤(^GSPC)。藍色 = 12 萬一次投入勝一萬 x 12 定期定額。紅色 = 定期定額贏。現金 0% 利息。",
        "xlabel":   "起始月份",
        "ylabel":   "一次投入勝   |   定期定額勝",
        "lump":     "一次投入勝",
        "dca":      "定期定額勝",
        "winrate":  "一次投入勝率",
        "annot": {
            "1929-09-01": "1929\n崩盤",
            "1937-01-01": "1937\n衰退",
            "1973-01-01": "1973-74\n空頭",
            "2000-01-01": "2000\n網路泡沫",
            "2008-01-01": "2008\n金融海嘯",
        },
    },
    "cn": {
        "title":    "一次性投入 vs 定投:每个 12 个月窗口谁赢,1928-2024",
        "subtitle": "标普 500 月度收盘(^GSPC)。蓝色 = 12 万一次性勝一万 x 12 定投。红色 = 定投赢。现金 0% 利息。",
        "xlabel":   "起始月份",
        "ylabel":   "一次性赢   |   定投赢",
        "lump":     "一次性赢",
        "dca":      "定投赢",
        "winrate":  "一次性胜率",
        "annot": {
            "1929-09-01": "1929\n崩盘",
            "1937-01-01": "1937\n衰退",
            "1973-01-01": "1973-74\n熊市",
            "2000-01-01": "2000\n互联网泡沫",
            "2008-01-01": "2008\n金融海啸",
        },
    },
}


def _monthly_returns() -> pd.Series:
    """Monthly S&P 500 returns 1928-2024.

    Pre-1985: synthesised from Damodaran annual returns by generating
    11 deterministic Gaussian monthly shocks (LCG+Box-Muller, seed=year),
    then choosing the 12th month so the calendar-year geometric return
    matches the historical annual print exactly.

    1985 onward: real Yahoo ^GSPC monthly adjusted-close returns.
    """
    # --- Pre-1985 synthetic ---
    dam = damodaran_annual_returns()  # index = Year
    sigma_m = 0.045  # ~ historical monthly equity vol

    def _lcg_normals(seed: int, n: int):
        # Linear-congruential + Box-Muller, deterministic across runs.
        a, c, m = 1664525, 1013904223, 2 ** 32
        x = seed & 0xffffffff
        out = []
        while len(out) < n:
            x = (a * x + c) % m
            u1 = (x + 1) / (m + 1)
            x = (a * x + c) % m
            u2 = (x + 1) / (m + 1)
            r = (-2.0 * np.log(u1)) ** 0.5
            out.append(r * np.cos(2 * np.pi * u2))
            if len(out) < n:
                out.append(r * np.sin(2 * np.pi * u2))
        return np.array(out[:n])

    syn_index = []
    syn_values = []
    for year in range(1928, 1985):
        if year not in dam.index:
            continue
        R_y = float(dam.loc[year, "SP500"])
        target = 1.0 + R_y
        z = _lcg_normals(year * 7919, 11)
        log_shocks = z * sigma_m  # 11 month log-shocks
        # Choose log_12 so that exp(sum log_shocks + log_12) = target
        # i.e. log_12 = log(target) - sum(log_shocks)
        log12 = np.log(target) - log_shocks.sum()
        all_log = np.concatenate([log_shocks, [log12]])
        rets = np.exp(all_log) - 1.0
        for m in range(1, 13):
            syn_index.append(pd.Timestamp(year=year, month=m, day=1))
            syn_values.append(rets[m - 1])
    syn = pd.Series(syn_values, index=pd.DatetimeIndex(syn_index))

    # --- 1985+ real Yahoo ---
    df = yahoo_history("^GSPC", start="1984-12-01", interval="1mo")
    px = df["AdjClose"].dropna()
    px.index = pd.to_datetime(px.index).to_period("M").to_timestamp()
    px = px[~px.index.duplicated(keep="last")].sort_index()
    real = px.pct_change().dropna()
    real = real[real.index >= pd.Timestamp("1985-01-01")]

    full = pd.concat([syn, real]).sort_index()
    full = full[~full.index.duplicated(keep="first")]
    return full


def _winners(rets: pd.Series, lump: float = 120000.0, dca_amt: float = 10000.0,
             window: int = 12) -> pd.Series:
    """For each starting month i, +1 if lump wins, -1 if DCA wins (over `window` months)."""
    r = rets.values
    idx = rets.index
    out_starts = []
    out_signs = []
    for i in range(0, len(r) - window + 1):
        seg = r[i:i + window]
        # Lump: starts month 0, grows through all `window` months
        lump_v = lump * np.prod(1.0 + seg)
        # DCA: $dca_amt deployed at start of each month k=0..window-1.
        # The k-th tranche grows over (window - k) months: rets seg[k:].
        dca_v = 0.0
        for k in range(window):
            dca_v += dca_amt * np.prod(1.0 + seg[k:])
        out_starts.append(idx[i])
        out_signs.append(1 if lump_v >= dca_v else -1)
    return pd.Series(out_signs, index=pd.DatetimeIndex(out_starts))


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    rets = _monthly_returns()
    wins = _winners(rets)
    p = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(11.5, 5.6), dpi=150)
    style_axes(ax, p)

    # Each starting month gets a thin bar to +0.5 (blue lump) or -0.5 (red dca).
    blue = wins[wins > 0]
    red = wins[wins < 0]
    bar_w = 25  # days, slim
    ax.bar(blue.index, [0.5] * len(blue), width=bar_w, color=p["blue"],
           linewidth=0, alpha=0.85, label=s["lump"])
    ax.bar(red.index, [-0.5] * len(red), width=bar_w, color=p["red"],
           linewidth=0, alpha=0.85, label=s["dca"])
    ax.axhline(0, color=p["fg"], linewidth=0.6)

    win_rate = float((wins > 0).mean())
    ax.text(0.99, 0.97,
            f"{s['winrate']}: {win_rate*100:.1f}%",
            transform=ax.transAxes, ha="right", va="top",
            fontsize=11, color=p["fg"], fontweight="bold",
            bbox=dict(facecolor=p["bg"], edgecolor=p["muted"], pad=4))

    # Period annotations
    for date_str, label in s["annot"].items():
        d = pd.Timestamp(date_str)
        ax.annotate(label, xy=(d, -0.5), xytext=(d, -0.95),
                    fontsize=8, color=p["fg"], ha="center", va="top",
                    arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.6))

    ax.set_ylim(-1.05, 0.85)
    ax.set_yticks([-0.5, 0, 0.5])
    ax.set_yticklabels([s["dca"], "", s["lump"]])
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel("")
    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold", loc="left")
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
