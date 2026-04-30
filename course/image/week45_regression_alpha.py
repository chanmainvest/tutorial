"""Week 45, S2.1 - Single-factor regression: monthly portfolio returns vs S&P 500.

Synthetic 60-month series calibrated to alpha = 2%/yr (about 17 bps/mo)
and beta = 0.85, with realistic monthly residual volatility. Fits OLS,
draws the regression line, and annotates alpha and beta. Deterministic
seed so the chart is reproducible.

Run:
    uv run python course/image/week45_regression_alpha.py
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
BASE = "week45_regression_alpha"

# True parameters baked into the synthetic data.
TRUE_ALPHA_MO = 0.02 / 12.0       # 2%/yr expressed monthly
TRUE_BETA = 0.85
N_MONTHS = 60                     # 5 years
MKT_MEAN_MO = 0.08 / 12.0         # market mean ~8%/yr
MKT_VOL_MO = 0.155 / np.sqrt(12)  # market vol ~15.5%/yr
RES_VOL_MO = 0.045 / np.sqrt(12)  # residual vol ~4.5%/yr (idiosyncratic)
SEED = 20260429


def _simulate():
    rng = np.random.default_rng(SEED)
    rm = rng.normal(MKT_MEAN_MO, MKT_VOL_MO, size=N_MONTHS)
    eps = rng.normal(0.0, RES_VOL_MO, size=N_MONTHS)
    rp = TRUE_ALPHA_MO + TRUE_BETA * rm + eps
    return rm, rp


def _ols(x: np.ndarray, y: np.ndarray):
    n = len(x)
    xb = x.mean()
    yb = y.mean()
    sxx = np.sum((x - xb) ** 2)
    sxy = np.sum((x - xb) * (y - yb))
    beta = sxy / sxx
    alpha = yb - beta * xb
    yhat = alpha + beta * x
    resid = y - yhat
    sse = np.sum(resid ** 2)
    sse_dof = sse / (n - 2)
    se_beta = np.sqrt(sse_dof / sxx)
    se_alpha = np.sqrt(sse_dof * (1.0 / n + (xb ** 2) / sxx))
    sst = np.sum((y - yb) ** 2)
    r2 = 1.0 - sse / sst
    t_alpha = alpha / se_alpha
    t_beta = beta / se_beta
    return {
        "alpha": alpha, "beta": beta,
        "se_alpha": se_alpha, "se_beta": se_beta,
        "t_alpha": t_alpha, "t_beta": t_beta,
        "r2": r2, "yhat": yhat, "resid": resid,
        "sse_dof": sse_dof, "sxx": sxx, "xb": xb, "n": n,
    }


LANG_STRINGS = {
    "en": {
        "title":    "Single-factor regression: portfolio vs S&P 500, 60 monthly returns",
        "subtitle": "Synthetic data calibrated to true alpha = 2%/yr, true beta = 0.85. OLS fit recovers both.",
        "xlabel":   "S&P 500 monthly excess return",
        "ylabel":   "Portfolio monthly excess return",
        "scatter":  "Monthly observations",
        "fitline":  "OLS regression line",
        "alpha_lbl": "Estimated alpha",
        "beta_lbl":  "Estimated beta",
        "r2_lbl":    "R-squared",
        "t_alpha":   "t-stat",
        "footer":   "Alpha = intercept * 12. Beta = slope. R-squared is the variance explained by the market factor. t-stats use OLS standard errors.",
    },
    "hk": {
        "title":    "單因子迴歸:組合 vs S&P 500,60 個月度回報",
        "subtitle": "合成資料,真實 alpha = 2%/年,真實 beta = 0.85。OLS 擬合可同時還原兩者。",
        "xlabel":   "S&P 500 月度超額回報",
        "ylabel":   "組合月度超額回報",
        "scatter":  "月度觀測",
        "fitline":  "OLS 迴歸線",
        "alpha_lbl": "估計 alpha",
        "beta_lbl":  "估計 beta",
        "r2_lbl":    "R 平方",
        "t_alpha":   "t 值",
        "footer":   "Alpha = 截距 * 12。Beta = 斜率。R 平方是市場因子解釋的變異。t 值採用 OLS 標準誤。",
    },
    "tw": {
        "title":    "單因子迴歸:組合 vs S&P 500,60 個月度報酬",
        "subtitle": "合成資料,真實 alpha = 2%/年,真實 beta = 0.85。OLS 擬合可同時還原兩者。",
        "xlabel":   "S&P 500 月度超額報酬",
        "ylabel":   "組合月度超額報酬",
        "scatter":  "月度觀測",
        "fitline":  "OLS 迴歸線",
        "alpha_lbl": "估計 alpha",
        "beta_lbl":  "估計 beta",
        "r2_lbl":    "R 平方",
        "t_alpha":   "t 值",
        "footer":   "Alpha = 截距 * 12。Beta = 斜率。R 平方是市場因子解釋的變異。t 值採用 OLS 標準誤。",
    },
    "cn": {
        "title":    "单因子回归:组合 vs S&P 500,60 个月度回报",
        "subtitle": "合成数据,真实 alpha = 2%/年,真实 beta = 0.85。OLS 拟合可同时还原两者。",
        "xlabel":   "S&P 500 月度超额回报",
        "ylabel":   "组合月度超额回报",
        "scatter":  "月度观测",
        "fitline":  "OLS 回归线",
        "alpha_lbl": "估计 alpha",
        "beta_lbl":  "估计 beta",
        "r2_lbl":    "R 平方",
        "t_alpha":   "t 值",
        "footer":   "Alpha = 截距 * 12。Beta = 斜率。R 平方是市场因子解释的方差。t 值采用 OLS 标准误。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    rm, rp = _simulate()
    fit = _ols(rm, rp)

    # Confidence band on the fitted line: SE of mean prediction at each x.
    xs = np.linspace(rm.min() - 0.005, rm.max() + 0.005, 200)
    yhat_xs = fit["alpha"] + fit["beta"] * xs
    se_pred = np.sqrt(fit["sse_dof"] * (1.0 / fit["n"]
                                        + (xs - fit["xb"]) ** 2 / fit["sxx"]))
    band = 1.96 * se_pred

    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax, p)

    # 95% CI band on the regression line.
    ax.fill_between(xs, yhat_xs - band, yhat_xs + band,
                    color=p["accent"], alpha=0.15, linewidth=0,
                    label=None)

    # Scatter points.
    ax.scatter(rm, rp, s=38, color=p["blue"], alpha=0.78,
               edgecolor="white", linewidth=0.7,
               label=s["scatter"], zorder=3)

    # Regression line.
    ax.plot(xs, yhat_xs, color=p["red"], linewidth=2.2,
            label=s["fitline"], zorder=4)

    # Origin reference cross-hairs.
    ax.axhline(0, color=p["muted"], linewidth=0.7, alpha=0.6)
    ax.axvline(0, color=p["muted"], linewidth=0.7, alpha=0.6)

    # Format axes as %.
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.1f}%"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.1f}%"))
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)

    # Annotation box with alpha/beta/R2.
    alpha_pct_yr = fit["alpha"] * 12 * 100
    beta_val = fit["beta"]
    r2_val = fit["r2"]
    box_text = (
        f"{s['alpha_lbl']}: {fit['alpha']*100:.2f}%/mo "
        f"({alpha_pct_yr:+.2f}%/yr)\n"
        f"  {s['t_alpha']} = {fit['t_alpha']:.2f}\n"
        f"{s['beta_lbl']}: {beta_val:.3f}\n"
        f"  {s['t_alpha']} = {fit['t_beta']:.2f}\n"
        f"{s['r2_lbl']}: {r2_val:.3f}"
    )
    ax.text(0.025, 0.975, box_text, transform=ax.transAxes,
            ha="left", va="top", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.55",
                      facecolor=p["bg"], edgecolor=p["grid"], linewidth=1))

    ax.legend(loc="lower right", fontsize=9.5, framealpha=0.92,
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
