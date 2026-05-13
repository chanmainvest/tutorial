"""Side 20, §2.6 - Illustrative SPX intraday during quarterly OpEx pinning.

Illustrative reconstruction of an SPX cash session on a quarterly OpEx
Friday, with the index drifting in the morning and then mean-reverting
toward the 5000 strike (highest open interest) into the close. Synthetic
random-walk + Ornstein-Uhlenbeck pull toward 5000 that strengthens in
the afternoon. Three highest-OI strikes (4950 / 5000 / 5050) shown as
dotted horizontal lines.

Run:
    uv run python course/image/side20_dealer_pinning.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side20_dealer_pinning"


# ---- Synthetic intraday path ----------------------------------------
def _gen_path():
    """Deterministic OU process pulled toward 5000 with rising strength.

    Time is in 1-minute bars from 9:30 AM (0) to 4:00 PM (390 minutes).
    """
    n = 391  # inclusive of close
    rng_seed = 20260619  # June 2026 quarterly OpEx fixed seed
    # LCG.
    state = rng_seed
    def lcg():
        nonlocal state
        state = (state * 1103515245 + 12345) & 0x7fffffff
        return state / 0x7fffffff
    # Box-Muller.
    def randn():
        u1 = max(lcg(), 1e-12)
        u2 = lcg()
        return math.sqrt(-2.0 * math.log(u1)) * math.cos(2 * math.pi * u2)

    pin = 5000.0
    # Start above the pin to give a clear "drift to pin" arc.
    s = 5018.0
    path = np.zeros(n)
    path[0] = s
    sigma_per_min = 0.0008  # ~ 1.6% daily vol annualised reasonable for SPX
    for i in range(1, n):
        # Pull strength rises from 0 in the morning to 0.04 in the last hour.
        frac = i / (n - 1)
        if frac < 0.4:
            kappa = 0.001  # essentially free-walk before lunch
        elif frac < 0.7:
            kappa = 0.010  # afternoon: moderate pull
        else:
            kappa = 0.040  # last 90 min: strong pin
        # Vol also tightens into close.
        local_sigma = sigma_per_min * (1.0 - 0.55 * frac)
        drift = -kappa * (s - pin) / s  # log-space pull
        ret = drift + local_sigma * randn()
        s = s * (1.0 + ret)
        path[i] = s
    return path


LANG_STRINGS = {
    "en": {
        "title":    "SPX intraday on quarterly OpEx Friday - the 5000 pin",
        "subtitle": "Illustrative reconstruction. Index drifts down through the morning, then oscillates in a tightening band around the 5000 strike into the 4 PM print.",
        "ylabel":   "SPX cash index",
        "xlabel":   "Time of day (Eastern)",
        "open_t":   "9:30 open",
        "lunch_t":  "12:00 lunch",
        "close_t":  "4:00 close",
        "pin":      "Pin strike: 5000 (highest OI)",
        "k_lo":     "4950 (heavy put OI)",
        "k_hi":     "5050 (heavy call OI)",
        "morning":  "Morning: free walk",
        "afternoon":"Afternoon: dealer-gamma pull tightens",
        "footer":   "Pinning requires dealers net-short gamma at the strike. Shaded region marks the final 90 minutes when charm and color rise sharply.",
    },
    "hk": {
        "title":    "季度 OpEx 周五 SPX 日內 - 5000 釘住",
        "subtitle": "示意重構。指數早盤下行,午後在 5000 執行價附近逐步收窄,直至 4 點收盤。",
        "ylabel":   "SPX 現貨指數",
        "xlabel":   "時間(東岸)",
        "open_t":   "9:30 開盤",
        "lunch_t":  "12:00 午盤",
        "close_t":  "4:00 收盤",
        "pin":      "釘住執行價:5000(OI 最大)",
        "k_lo":     "4950(認沽 OI 重)",
        "k_hi":     "5050(認購 OI 重)",
        "morning":  "上午:自由游走",
        "afternoon":"下午:做市商 Gamma 拉力增強",
        "footer":   "釘住需要做市商在該執行價淨空 Gamma。陰影區為收盤前 90 分鐘,Charm 與 Color 急升。",
    },
    "tw": {
        "title":    "季度 OpEx 週五 SPX 日內 - 5000 釘樁",
        "subtitle": "示意重構。指數早盤下行,午後在 5000 履約價附近逐步收窄,直至 4 點收盤。",
        "ylabel":   "SPX 現貨指數",
        "xlabel":   "時間(東岸)",
        "open_t":   "9:30 開盤",
        "lunch_t":  "12:00 午盤",
        "close_t":  "4:00 收盤",
        "pin":      "釘樁履約價:5000(OI 最大)",
        "k_lo":     "4950(賣權 OI 重)",
        "k_hi":     "5050(買權 OI 重)",
        "morning":  "上午:自由游走",
        "afternoon":"下午:做市商 Gamma 拉力增強",
        "footer":   "釘樁需做市商於該履約價淨空 Gamma。陰影區為收盤前 90 分鐘,Charm 與 Color 急升。",
    },
    "cn": {
        "title":    "季度 OpEx 周五 SPX 日内 - 5000 钉桩",
        "subtitle": "示意重构。指数早盘下行,午后在 5000 行权价附近逐步收窄,直至 4 点收盘。",
        "ylabel":   "SPX 现货指数",
        "xlabel":   "时间(东岸)",
        "open_t":   "9:30 开盘",
        "lunch_t":  "12:00 午盘",
        "close_t":  "4:00 收盘",
        "pin":      "钉桩行权价:5000(OI 最大)",
        "k_lo":     "4950(看跌 OI 重)",
        "k_hi":     "5050(看涨 OI 重)",
        "morning":  "上午:自由游走",
        "afternoon":"下午:做市商 Gamma 拉力增强",
        "footer":   "钉桩需要做市商在该行权价净空 Gamma。阴影区为收盘前 90 分钟,Charm 与 Color 急升。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    path = _gen_path()
    n = len(path)
    x = np.arange(n)

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax, p)

    # Final-90-min shaded region.
    ax.axvspan(n - 90, n - 1, color=p["accent"], alpha=0.06, zorder=0)

    # Strike lines.
    ax.axhline(5000.0, color=p["accent"], linewidth=1.6, linestyle=":",
               alpha=0.85, zorder=1)
    ax.axhline(4950.0, color=p["red"],    linewidth=1.0, linestyle=":",
               alpha=0.55, zorder=1)
    ax.axhline(5050.0, color=p["green"],  linewidth=1.0, linestyle=":",
               alpha=0.55, zorder=1)

    ax.text(n + 5, 5000.0, "  " + s["pin"],
            color=p["accent"], fontsize=9.5, fontweight="bold",
            va="center", ha="left")
    ax.text(n + 5, 4950.0, "  " + s["k_lo"],
            color=p["red"], fontsize=8.6, va="center", ha="left", alpha=0.85)
    ax.text(n + 5, 5050.0, "  " + s["k_hi"],
            color=p["green"], fontsize=8.6, va="center", ha="left", alpha=0.85)

    # Path itself.
    ax.plot(x, path, color=p["blue"], linewidth=1.8, zorder=3)

    # Period labels.
    ax.text(40, path.max() + 5, s["morning"],
            fontsize=9.5, color=p["muted"], fontweight="bold")
    ax.text(n - 130, path.min() - 6, s["afternoon"],
            fontsize=9.5, color=p["accent"], fontweight="bold")

    # X-axis ticks at 9:30 / 12:00 / 4:00.
    ax.set_xticks([0, 150, 390])
    ax.set_xticklabels([s["open_t"], s["lunch_t"], s["close_t"]],
                       fontsize=10)
    ax.set_xlim(0, n + 95)

    # Y-axis: ensure all three strikes (4950, 5000, 5050) are inside view.
    pad = max(8.0, (path.max() - path.min()) * 0.10)
    y_lo = min(path.min() - pad, 4942.0)
    y_hi = max(path.max() + pad, 5058.0)
    ax.set_ylim(y_lo, y_hi)

    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["muted"])
    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["muted"])
    ax.set_title(s["title"], pad=24, fontsize=15, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.2, color="#4a5568", style="italic")
    fig.text(0.02, 0.01, s["footer"], fontsize=9.2,
             color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.03, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
