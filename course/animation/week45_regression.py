"""
Week 45 - Simple Linear Regression
====================================
Demonstrates linear regression with:
  - Scatter plot of data points
  - Best-fit regression line
  - Residual lines from each point to the regression line
  - R-squared value displayed
Output: week45_regression.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Generate synthetic data: y = 2.5x + 10 + noise
# ---------------------------------------------------------------------------
np.random.seed(7)
n = 25
x = np.linspace(1, 10, n)
true_slope = 2.5
true_intercept = 10
noise = np.random.normal(0, 3, n)
y = true_intercept + true_slope * x + noise

# ---------------------------------------------------------------------------
# Fit linear regression
# ---------------------------------------------------------------------------
coeffs = np.polyfit(x, y, 1)
slope = coeffs[0]
intercept = coeffs[1]
y_pred = slope * x + intercept

# R-squared
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - ss_res / ss_tot

# Regression line for plotting
x_line = np.linspace(0, 11, 100)
y_line = slope * x_line + intercept

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))

# Residual lines (point to regression line)
for xi, yi, yp in zip(x, y, y_pred):
    ax.plot([xi, xi], [yi, yp], color="#FF9800", linewidth=1.2, alpha=0.6, zorder=1)

# Data points
ax.scatter(x, y, color="#1976D2", s=70, edgecolors="white", linewidth=0.8,
           zorder=3, label="Observed Data")

# Regression line
ax.plot(x_line, y_line, color="#F44336", linewidth=2.5, zorder=2,
        label=f"y = {slope:.2f}x + {intercept:.2f}")

# Predicted points on the line
ax.scatter(x, y_pred, color="#F44336", s=25, marker="x", zorder=3, alpha=0.6)

# Stats box
props = dict(boxstyle="round,pad=0.5", facecolor="#E3F2FD", edgecolor="#1976D2", alpha=0.9)
stats_text = (f"Slope = {slope:.2f}\n"
              f"Intercept = {intercept:.2f}\n"
              f"R-squared = {r_squared:.4f}\n"
              f"n = {n}")
ax.text(0.03, 0.97, stats_text, transform=ax.transAxes,
        fontsize=11, verticalalignment="top", bbox=props, family="monospace")

# Residual legend entry (dummy for label)
ax.plot([], [], color="#FF9800", linewidth=1.5, label="Residuals (errors)")

# Annotations
ax.annotate("Residual = observed - predicted",
            xy=(x[5], (y[5] + y_pred[5]) / 2),
            xytext=(x[5] + 2, y[5] + 5),
            fontsize=9, color="#E65100",
            arrowprops=dict(arrowstyle="->", color="#E65100"))

# Formatting
ax.set_xlabel("X (Independent Variable)", fontsize=12)
ax.set_ylabel("Y (Dependent Variable)", fontsize=12)
ax.set_title("Simple Linear Regression with Residuals",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=10, loc="lower right")
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.5, 11.5)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week45_regression.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
