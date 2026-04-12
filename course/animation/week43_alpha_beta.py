"""
Week 43 - Alpha and Beta: Portfolio vs Benchmark
==================================================
Scatter plot of monthly portfolio returns vs benchmark (S&P 500) returns.
A regression line is fitted:
  - Alpha (intercept) = excess return independent of market
  - Beta (slope) = sensitivity to market moves
Output: week43_alpha_beta.png
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
import os

# ---------------------------------------------------------------------------
# Synthetic data: 36 months of returns
# ---------------------------------------------------------------------------
np.random.seed(42)
n_months = 36

# Benchmark returns (market): mean ~0.8%/month, std ~4%
benchmark = np.random.normal(0.008, 0.04, n_months)

# Portfolio returns: beta=1.2, alpha=0.3%/month, plus noise
true_alpha = 0.003
true_beta = 1.2
noise = np.random.normal(0, 0.015, n_months)
portfolio = true_alpha + true_beta * benchmark + noise

# ---------------------------------------------------------------------------
# Regression
# ---------------------------------------------------------------------------
# polyfit returns [intercept, slope] with deg=1
coeffs = np.polyfit(benchmark, portfolio, 1)
beta_est = coeffs[0]
alpha_est = coeffs[1]

# R-squared
y_pred = beta_est * benchmark + alpha_est
ss_res = np.sum((portfolio - y_pred) ** 2)
ss_tot = np.sum((portfolio - np.mean(portfolio)) ** 2)
r_squared = 1 - ss_res / ss_tot

# Regression line x-values
x_line = np.linspace(benchmark.min() - 0.01, benchmark.max() + 0.01, 100)
y_line = beta_est * x_line + alpha_est

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))

# Scatter plot of monthly returns
ax.scatter(benchmark * 100, portfolio * 100, color="#1976D2", alpha=0.7,
           s=60, edgecolors="white", linewidth=0.5, zorder=3,
           label="Monthly Returns")

# Regression line
ax.plot(x_line * 100, y_line * 100, color="#F44336", linewidth=2.5,
        label=f"Regression: R = {alpha_est*100:.2f}% + {beta_est:.2f} x Benchmark",
        zorder=2)

# Zero lines
ax.axhline(y=0, color="gray", linewidth=0.8, linestyle="--", alpha=0.5)
ax.axvline(x=0, color="gray", linewidth=0.8, linestyle="--", alpha=0.5)

# Alpha annotation (intercept at x=0)
ax.plot(0, alpha_est * 100, marker="D", color="#FF9800", markersize=10, zorder=4)
ax.annotate(f"Alpha = {alpha_est*100:.2f}%/month\n(intercept at x=0)",
            xy=(0, alpha_est * 100), xytext=(3, -4),
            fontsize=10, fontweight="bold", color="#E65100",
            arrowprops=dict(arrowstyle="->", color="#E65100", lw=1.5))

# Beta annotation
ax.annotate(f"Beta = {beta_est:.2f}\n(slope of line)",
            xy=(x_line[70] * 100, y_line[70] * 100),
            xytext=(x_line[70] * 100 + 2, y_line[70] * 100 - 3),
            fontsize=10, fontweight="bold", color="#C62828",
            arrowprops=dict(arrowstyle="->", color="#C62828", lw=1.5))

# Stats box
props = dict(boxstyle="round,pad=0.5", facecolor="#E8F5E9", edgecolor="#4CAF50", alpha=0.9)
stats_text = (f"Alpha (monthly) = {alpha_est*100:.2f}%\n"
              f"Alpha (annualized) = {alpha_est*12*100:.1f}%\n"
              f"Beta = {beta_est:.2f}\n"
              f"R-squared = {r_squared:.3f}")
ax.text(0.03, 0.97, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment="top", bbox=props, family="monospace")

# Formatting
ax.set_xlabel("Benchmark Return (%)", fontsize=12)
ax.set_ylabel("Portfolio Return (%)", fontsize=12)
ax.set_title("Alpha and Beta: Portfolio vs Benchmark Returns",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=10, loc="lower right")
ax.grid(True, alpha=0.3)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week43_alpha_beta.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
