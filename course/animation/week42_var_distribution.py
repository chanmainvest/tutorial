"""
Week 42 - Value at Risk (VaR) and Conditional VaR (CVaR)
=========================================================
Visualizes a normal distribution of portfolio returns with:
  - VaR at the 5th percentile (95% confidence level)
  - CVaR (Expected Shortfall) = expected loss beyond VaR
Both regions are shaded for clarity.
Output: week42_var_distribution.png
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# ---------------------------------------------------------------------------
# Distribution parameters
# ---------------------------------------------------------------------------
mu = 0.08       # mean daily return (annualized for illustration)
sigma = 0.15    # standard deviation
alpha = 0.05    # 5th percentile

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
pdf = stats.norm.pdf(x, mu, sigma)

# VaR: 5th percentile
var_95 = stats.norm.ppf(alpha, mu, sigma)

# CVaR (Expected Shortfall): E[X | X < VaR]
# For normal distribution: CVaR = mu - sigma * phi(z_alpha) / alpha
z_alpha = stats.norm.ppf(alpha)
cvar_95 = mu - sigma * stats.norm.pdf(z_alpha) / alpha

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Full distribution curve
ax.plot(x, pdf, color="#333333", linewidth=2, label="Return Distribution (Normal)")

# Shade CVaR region (beyond VaR, the deeper tail)
x_cvar = x[x <= var_95]
ax.fill_between(x_cvar, stats.norm.pdf(x_cvar, mu, sigma),
                color="#D32F2F", alpha=0.5, label=f"CVaR Region (E[loss | loss > VaR])")

# Shade VaR line region (between CVaR marker and VaR)
x_var_region = x[x <= var_95]
ax.fill_between(x_var_region, stats.norm.pdf(x_var_region, mu, sigma),
                color="#F44336", alpha=0.25)

# VaR vertical line
ax.axvline(x=var_95, color="#D32F2F", linewidth=2, linestyle="--",
           label=f"VaR (5%) = {var_95:.2%}")

# CVaR vertical line
ax.axvline(x=cvar_95, color="#B71C1C", linewidth=2, linestyle=":",
           label=f"CVaR (ES) = {cvar_95:.2%}")

# Mean line
ax.axvline(x=mu, color="#4CAF50", linewidth=1.5, linestyle="-.",
           label=f"Mean = {mu:.2%}", alpha=0.7)

# Annotations
ax.annotate(f"VaR = {var_95:.2%}\n(5th percentile)",
            xy=(var_95, stats.norm.pdf(var_95, mu, sigma)),
            xytext=(var_95 - 0.12, 1.8),
            fontsize=10, color="#D32F2F", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#D32F2F"))

ax.annotate(f"CVaR = {cvar_95:.2%}\n(Expected Shortfall)",
            xy=(cvar_95, 0.3),
            xytext=(cvar_95 - 0.14, 1.2),
            fontsize=10, color="#B71C1C", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#B71C1C"))

# Description box
props = dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", edgecolor="#F9A825", alpha=0.9)
explanation = ("VaR: Maximum expected loss at 95% confidence\n"
               "CVaR: Average loss in the worst 5% of cases")
ax.text(0.97, 0.95, explanation, transform=ax.transAxes,
        fontsize=10, verticalalignment="top", horizontalalignment="right", bbox=props)

# Formatting
ax.set_xlabel("Portfolio Return", fontsize=12)
ax.set_ylabel("Probability Density", fontsize=12)
ax.set_title("Value at Risk (VaR) and Expected Shortfall (CVaR)",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=9.5, loc="upper left")
ax.grid(True, alpha=0.3)

# Format x-axis as percentage
from matplotlib.ticker import PercentFormatter
ax.xaxis.set_major_formatter(PercentFormatter(1.0))

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week42_var_distribution.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
