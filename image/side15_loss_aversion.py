"""Side 15, §2.1 — Kahneman-Tversky value function (loss aversion).

Schematic teaching plot. Gain side concave; loss side convex AND
steeper, with loss-aversion coefficient lambda = 2.25 per Tversky &
Kahneman (1992) cumulative prospect theory:

    v(x) =  x^a            if x >= 0
    v(x) = -lambda * (-x)^b if x <  0

Defaults: a = b = 0.88, lambda = 2.25.

Run:
    uv run python course/image/side15_loss_aversion.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "side15_loss_aversion"

ALPHA  = 0.88
BETA   = 0.88
LAMBDA = 2.25

LANG_STRINGS = {
    "en": {
        "title":    "Loss aversion: the Kahneman-Tversky value function",
        "subtitle": "Gains are concave (diminishing pleasure). Losses are convex AND steeper: a -100 dollar loss feels ~2.25x worse than a +100 dollar gain feels good.",
        "xlabel":   "Dollar gain or loss from reference point",
        "ylabel":   "Perceived utility (psychological value)",
        "gain":     "gains: v(x) = x^0.88",
        "loss":     "losses: v(x) = -2.25 * (-x)^0.88",
        "ref":      "reference point",
        "ann_gain": "+$100 = +{vg:.0f} units",
        "ann_loss": "-$100 = {vl:.0f} units",
        "kink":     "kink at zero -- losses ~2.25x steeper than gains",
        "sym":      "(symmetric ref.)",
    },
    "hk": {
        "title":    "損失厭惡:Kahneman-Tversky 價值函數",
        "subtitle": "收益面凹(邊際快樂遞減)。損失面凸且更陡:蝕 100 元的痛苦約為賺 100 元快樂的 2.25 倍。",
        "xlabel":   "相對於參考點的美元盈虧",
        "ylabel":   "感知效用(心理價值)",
        "gain":     "收益:v(x) = x^0.88",
        "loss":     "損失:v(x) = -2.25 * (-x)^0.88",
        "ref":      "參考點",
        "ann_gain": "+100 美元 = +{vg:.0f} 單位",
        "ann_loss": "-100 美元 = {vl:.0f} 單位",
        "kink":     "零點折拗 -- 損失斜率約為收益的 2.25 倍",
        "sym":      "(對稱參考)",
    },
    "tw": {
        "title":    "損失趨避:Kahneman-Tversky 價值函數",
        "subtitle": "收益面凹(邊際快樂遞減)。損失面凸且更陡:虧 100 元的痛苦約為賺 100 元快樂的 2.25 倍。",
        "xlabel":   "相對於參考點的美元損益",
        "ylabel":   "感知效用(心理價值)",
        "gain":     "收益:v(x) = x^0.88",
        "loss":     "損失:v(x) = -2.25 * (-x)^0.88",
        "ref":      "參考點",
        "ann_gain": "+100 美元 = +{vg:.0f} 單位",
        "ann_loss": "-100 美元 = {vl:.0f} 單位",
        "kink":     "零點折拗 -- 損失斜率約為收益的 2.25 倍",
        "sym":      "(對稱參考)",
    },
    "cn": {
        "title":    "损失厌恶:Kahneman-Tversky 价值函数",
        "subtitle": "收益面凹(边际快乐递减)。损失面凸且更陡:亏 100 元的痛苦约为赚 100 元快乐的 2.25 倍。",
        "xlabel":   "相对于参考点的美元盈亏",
        "ylabel":   "感知效用(心理价值)",
        "gain":     "收益:v(x) = x^0.88",
        "loss":     "损失:v(x) = -2.25 * (-x)^0.88",
        "ref":      "参考点",
        "ann_gain": "+100 美元 = +{vg:.0f} 单位",
        "ann_loss": "-100 美元 = {vl:.0f} 单位",
        "kink":     "零点折拗 -- 损失斜率约为收益的 2.25 倍",
        "sym":      "(对称参考)",
    },
}


def value(x):
    return np.where(x >= 0, np.power(np.abs(x), ALPHA),
                    -LAMBDA * np.power(np.abs(x), BETA))


def build_fig(s):
    # Escape any '$' so matplotlib doesn't enter mathtext mode.
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=150)
    style_axes(ax, p)

    xg = np.linspace(0, 100, 200)
    xl = np.linspace(-100, 0, 200)
    yg = value(xg)
    yl = value(xl)

    ax.plot(xg, yg, color=p["green"], linewidth=3.0, label=s["gain"])
    ax.plot(xl, yl, color=p["red"],   linewidth=3.0, label=s["loss"])

    ax.axhline(0, color=p["muted"], linewidth=0.8, alpha=0.6)
    ax.axvline(0, color=p["muted"], linewidth=0.8, alpha=0.6)

    v_pos = float(value(np.array([100.0]))[0])
    v_neg = float(value(np.array([-100.0]))[0])

    ax.scatter([100, -100], [v_pos, v_neg],
               color=[p["green"], p["red"]], s=70, zorder=5,
               edgecolor="white", linewidth=1.5)

    ax.annotate(
        s["ann_gain"].format(vg=v_pos),
        xy=(100, v_pos), xytext=(58, v_pos + 30),
        fontsize=10, color=p["green"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["green"], lw=1.0),
    )
    ax.annotate(
        s["ann_loss"].format(vl=v_neg),
        xy=(-100, v_neg), xytext=(-90, v_neg - 35),
        fontsize=10, color=p["red"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0),
    )

    # Mirror of gain curve onto loss side, to visualise the asymmetry.
    ax.plot(-xg, -yg, color=p["green"], linewidth=1.2,
            linestyle="--", alpha=0.45)
    ax.text(-95, -value(np.array([95.0]))[0] + 4, s["sym"],
            fontsize=8, color=p["muted"], alpha=0.8)

    ax.annotate(
        s["kink"],
        xy=(0, 0), xytext=(15, -120),
        fontsize=9.5, color=p["accent"], style="italic",
        arrowprops=dict(arrowstyle="->", color=p["accent"], lw=0.8),
    )

    ax.text(2, 6, s["ref"], fontsize=9, color=p["muted"])

    ax.set_xlim(-110, 110)
    ax.set_ylim(-260, 80)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.04, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
