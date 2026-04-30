"""Week 45, S2.7 - In-sample vs out-of-sample Sharpe across model complexity.

The canonical overfitting hump: in-sample Sharpe rises monotonically with
the number of model parameters (degrees of freedom), while out-of-sample
Sharpe rises briefly, peaks at moderate complexity, then collapses. The
gap between the two curves is the overfitting tax.

Curves are stylised but quantitatively reasonable for a typical equity
return-prediction model fit on a few hundred observations: in-sample
Sharpe approaches an asymptote near 3.0, out-of-sample peaks near 0.7
at about 8 parameters and then collapses to negative as parameters
grow past ~30 (memorising noise that does not generalise).

Run:
    uv run python course/image/week45_overfit_curve.py
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
BASE = "week45_overfit_curve"

DOF = np.arange(1, 51)


def _curves():
    # In-sample Sharpe: rises monotonically toward an asymptote.
    # Sigmoid-style: 0.4 at dof=1, ~3.0 at dof=50.
    in_sample = 0.4 + 2.7 * (1.0 - np.exp(-DOF / 12.0))

    # Out-of-sample Sharpe: rises briefly to a peak, then declines.
    # Quadratic peak around dof=8 at ~0.7, falls to negative beyond ~35.
    peak = 8.0
    out_sample = 0.4 + 0.4 * (1.0 - np.exp(-DOF / 4.0)) - 0.0028 * (DOF - peak) ** 2
    # Clamp the negative tail to a stylised floor of -0.6
    out_sample = np.maximum(out_sample, -0.6)
    return in_sample, out_sample


LANG_STRINGS = {
    "en": {
        "title":    "Overfitting hump: in-sample vs out-of-sample Sharpe by model complexity",
        "subtitle": "Stylised single-asset return-prediction model fit on ~500 monthly observations. In-sample memorises the noise; out-of-sample collapses past a moderate parameter count.",
        "xlabel":   "Number of model parameters (degrees of freedom)",
        "ylabel":   "Sharpe ratio (annualised)",
        "in_label":  "In-sample Sharpe (training data)",
        "out_label": "Out-of-sample Sharpe (held-out data)",
        "gap_label": "Overfitting tax (gap)",
        "ann_peak":  "Out-of-sample peak\n~0.7 at 8 parameters",
        "ann_break": "Out-of-sample collapses\npast ~25 parameters",
        "footer":    "The honest performance estimate is the held-out curve. Whenever adding parameters does not raise out-of-sample Sharpe, the in-sample improvement is overfitting.",
    },
    "hk": {
        "title":    "過擬合曲線:模型複雜度下的樣本內 vs 樣本外 Sharpe",
        "subtitle": "風格化的單資產回報預測模型,基於約 500 個月度觀測。樣本內把噪音記下來;樣本外在中等參數量之後崩潰。",
        "xlabel":   "模型參數數(自由度)",
        "ylabel":   "Sharpe 比率(年化)",
        "in_label":  "樣本內 Sharpe(訓練集)",
        "out_label": "樣本外 Sharpe(保留集)",
        "gap_label": "過擬合代價(差距)",
        "ann_peak":  "樣本外峰值\n約 0.7,在 8 個參數",
        "ann_break": "樣本外在約 25 個\n參數後崩潰",
        "footer":    "誠實的績效估計是保留集那條線。當增加參數不能再提升樣本外 Sharpe 時,樣本內的提升就是過擬合。",
    },
    "tw": {
        "title":    "過擬合曲線:模型複雜度下的樣本內 vs 樣本外 Sharpe",
        "subtitle": "風格化的單資產報酬預測模型,基於約 500 個月度觀測。樣本內把雜訊記下來;樣本外在中等參數量之後崩潰。",
        "xlabel":   "模型參數數(自由度)",
        "ylabel":   "Sharpe 比率(年化)",
        "in_label":  "樣本內 Sharpe(訓練集)",
        "out_label": "樣本外 Sharpe(保留集)",
        "gap_label": "過擬合代價(差距)",
        "ann_peak":  "樣本外峰值\n約 0.7,在 8 個參數",
        "ann_break": "樣本外在約 25 個\n參數後崩潰",
        "footer":    "誠實的績效估計是保留集那條線。當增加參數不能再提升樣本外 Sharpe 時,樣本內的提升就是過擬合。",
    },
    "cn": {
        "title":    "过拟合曲线:模型复杂度下的样本内 vs 样本外 Sharpe",
        "subtitle": "风格化的单资产回报预测模型,基于约 500 个月度观测。样本内把噪音记下来;样本外在中等参数量之后崩溃。",
        "xlabel":   "模型参数数(自由度)",
        "ylabel":   "Sharpe 比率(年化)",
        "in_label":  "样本内 Sharpe(训练集)",
        "out_label": "样本外 Sharpe(保留集)",
        "gap_label": "过拟合代价(差距)",
        "ann_peak":  "样本外峰值\n约 0.7,在 8 个参数",
        "ann_break": "样本外在约 25 个\n参数后崩溃",
        "footer":    "诚实的绩效估计是保留集那条线。当增加参数不再提升样本外 Sharpe 时,样本内的提升就是过拟合。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    in_s, out_s = _curves()

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, p)

    # Shaded gap between curves
    ax.fill_between(DOF, out_s, in_s, color=p["red"], alpha=0.12,
                    linewidth=0, label=s["gap_label"])

    # In-sample line (dashed, muted)
    ax.plot(DOF, in_s, color=p["blue"], linewidth=2.6, linestyle="--",
            label=s["in_label"])

    # Out-of-sample line (solid, bold)
    ax.plot(DOF, out_s, color=p["green"], linewidth=2.8,
            label=s["out_label"])

    # Mark out-of-sample peak.
    peak_idx = int(np.argmax(out_s))
    ax.plot(DOF[peak_idx], out_s[peak_idx], "o",
            color=p["green"], markersize=10, zorder=5,
            markeredgecolor="white", markeredgewidth=1.2)
    ax.annotate(s["ann_peak"],
                xy=(DOF[peak_idx], out_s[peak_idx]),
                xytext=(DOF[peak_idx] + 6, out_s[peak_idx] + 0.7),
                fontsize=9.5, color=p["fg"],
                arrowprops=dict(arrowstyle="->", color=p["muted"],
                                connectionstyle="arc3,rad=0.2"))

    # Mark out-of-sample break (where it crosses zero)
    cross_idx = int(np.argmax(out_s < 0)) if (out_s < 0).any() else len(DOF) - 1
    if cross_idx > 0:
        ax.plot(DOF[cross_idx], out_s[cross_idx], "o",
                color=p["red"], markersize=8, zorder=5,
                markeredgecolor="white", markeredgewidth=1.2)
        ax.annotate(s["ann_break"],
                    xy=(DOF[cross_idx], out_s[cross_idx]),
                    xytext=(DOF[cross_idx] - 4, out_s[cross_idx] - 0.9),
                    fontsize=9.5, color=p["fg"],
                    ha="right",
                    arrowprops=dict(arrowstyle="->", color=p["muted"],
                                    connectionstyle="arc3,rad=-0.2"))

    ax.axhline(0, color=p["muted"], linewidth=0.8)
    ax.set_xlim(1, 50)
    ax.set_ylim(-1.0, 3.4)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.92,
              facecolor=p["bg"], edgecolor=p["grid"])

    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    fig.text(0.06, 0.02, s["footer"], fontsize=9, color=p["muted"])
    fig.tight_layout(rect=[0, 0.05, 1, 0.95])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
