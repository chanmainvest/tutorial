"""
Week 34: Interest Rate Sensitivity by Asset Class
====================================================
Horizontal bar chart ranking how sensitive different asset classes
are to interest-rate changes. Colour-coded from high to low.

Output: week34_rate_sensitivity.png
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# -------------------------------------------------------------------
# Data: asset classes and their relative rate sensitivity (1-10 scale)
# -------------------------------------------------------------------
asset_classes = [
    "Long-Term Gov't Bonds",
    "Investment-Grade Corp Bonds",
    "REITs / Real Estate",
    "Utilities Stocks",
    "Growth / Tech Stocks",
    "High-Yield Bonds",
    "Value Stocks",
    "Commodities",
    "Cash / Money Market",
]

# Sensitivity score (higher = more affected by rate changes)
sensitivity = [9.5, 8.0, 7.5, 7.0, 6.5, 5.5, 3.5, 2.5, 1.0]

# Sort by sensitivity (ascending so highest appears at top)
sorted_pairs = sorted(zip(sensitivity, asset_classes))
sensitivity_sorted = [p[0] for p in sorted_pairs]
classes_sorted = [p[1] for p in sorted_pairs]

# -------------------------------------------------------------------
# Colour mapping: green (low sensitivity) -> red (high sensitivity)
# -------------------------------------------------------------------
cmap = LinearSegmentedColormap.from_list(
    "rate_sens", ["#4CAF50", "#FFC107", "#FF5722", "#B71C1C"]
)
norm_vals = np.array(sensitivity_sorted) / max(sensitivity_sorted)
bar_colors = [cmap(v) for v in norm_vals]

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7))

y_pos = np.arange(len(classes_sorted))

bars = ax.barh(y_pos, sensitivity_sorted, height=0.6,
               color=bar_colors, edgecolor="white", linewidth=0.8)

# Value labels at end of each bar
for bar, val in zip(bars, sensitivity_sorted):
    ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}", va="center", fontsize=10, fontweight="bold",
            color="#333")

# Category labels
ax.set_yticks(y_pos)
ax.set_yticklabels(classes_sorted, fontsize=10)

# Sensitivity zones
ax.axvline(3.0, color="#4CAF50", linewidth=1, linestyle="--", alpha=0.5)
ax.axvline(6.0, color="#FF9800", linewidth=1, linestyle="--", alpha=0.5)

ax.text(1.5, -0.8, "Low", ha="center", fontsize=9, color="#4CAF50",
        fontweight="bold")
ax.text(4.5, -0.8, "Medium", ha="center", fontsize=9, color="#FF9800",
        fontweight="bold")
ax.text(7.5, -0.8, "High", ha="center", fontsize=9, color="#F44336",
        fontweight="bold")

# Interpretation box
info_text = (
    "Higher sensitivity means the asset class\n"
    "tends to lose more value when interest\n"
    "rates rise (and gain when rates fall)."
)
ax.text(0.98, 0.05, info_text, transform=ax.transAxes, fontsize=9,
        verticalalignment="bottom", horizontalalignment="right",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#E3F2FD", alpha=0.9))

# Arrow showing direction
ax.annotate("", xy=(10, len(classes_sorted) - 0.5),
            xytext=(10, -0.5),
            arrowprops=dict(arrowstyle="->", color="#B71C1C", lw=2))
ax.text(10.3, len(classes_sorted) / 2, "More\nSensitive",
        ha="left", va="center", fontsize=9, color="#B71C1C",
        fontweight="bold", rotation=90)

# Labels and formatting
ax.set_title("Interest Rate Sensitivity by Asset Class",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Rate Sensitivity Score (1 = Low, 10 = High)", fontsize=12)
ax.grid(True, axis="x", alpha=0.3)
ax.set_xlim(0, 11)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week34_rate_sensitivity.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week34_rate_sensitivity.png")
