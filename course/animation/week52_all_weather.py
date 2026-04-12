"""
Week 52 - All-Weather Portfolio: Radar Chart
==============================================
Radar (spider) chart comparing an All-Weather portfolio against
a traditional 60/40 portfolio across five dimensions:
  - Return
  - Volatility (inverted: lower is better)
  - Max Drawdown (inverted: smaller is better)
  - Sharpe Ratio
  - Diversification
Output: week52_all_weather.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Portfolio metrics (scored 0-10 scale for radar chart)
# Higher is better for all displayed values
# ---------------------------------------------------------------------------
categories = ["Return", "Low Volatility", "Low Drawdown", "Sharpe Ratio", "Diversification"]
n_cats = len(categories)

# All-Weather Portfolio (e.g., Bridgewater-style risk parity)
all_weather = [6.5, 8.5, 8.0, 8.5, 9.0]

# Traditional 60/40 Portfolio
trad_6040 = [7.0, 5.5, 5.0, 6.0, 5.0]

# 100% Equities (for additional comparison)
all_equity = [8.5, 3.0, 3.0, 5.0, 2.5]

# Close the radar chart (repeat first value)
all_weather += [all_weather[0]]
trad_6040 += [trad_6040[0]]
all_equity += [all_equity[0]]

# Compute angles for each category
angles = np.linspace(0, 2 * np.pi, n_cats, endpoint=False).tolist()
angles += angles[:1]  # close the circle

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# All-Weather
ax.plot(angles, all_weather, "o-", linewidth=2.5, color="#4CAF50", markersize=8,
        label="All-Weather Portfolio")
ax.fill(angles, all_weather, color="#4CAF50", alpha=0.15)

# 60/40
ax.plot(angles, trad_6040, "s-", linewidth=2.5, color="#2196F3", markersize=8,
        label="60/40 Portfolio")
ax.fill(angles, trad_6040, color="#2196F3", alpha=0.1)

# 100% Equity
ax.plot(angles, all_equity, "^-", linewidth=2.5, color="#F44336", markersize=8,
        label="100% Equity")
ax.fill(angles, all_equity, color="#F44336", alpha=0.08)

# Category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, fontweight="bold")

# Y-axis (radial) configuration
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=8, color="gray")
ax.set_rlabel_position(30)

# Grid styling
ax.grid(True, alpha=0.3)

# Title
ax.set_title("All-Weather Portfolio: Multi-Dimensional Comparison\n",
             fontsize=14, fontweight="bold", pad=25)

# Legend
ax.legend(fontsize=10, loc="lower right", bbox_to_anchor=(1.25, -0.05))

# Add score labels next to each data point for All-Weather
for i in range(n_cats):
    angle = angles[i]
    val = all_weather[i]
    ax.text(angle, val + 0.5, f"{val:.1f}", ha="center", va="center",
            fontsize=8, color="#2E7D32", fontweight="bold")

# Insight box
fig.text(0.5, 0.02,
         "All-Weather aims for consistent performance across economic regimes\n"
         "by diversifying risk, not just assets. It trades peak returns for stability.",
         ha="center", fontsize=10, style="italic",
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#E8F5E9",
                   edgecolor="#4CAF50", alpha=0.9))

plt.tight_layout()
plt.subplots_adjust(bottom=0.1)

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week52_all_weather.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
