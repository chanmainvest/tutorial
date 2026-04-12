"""
Week 06: Asset Correlation Matrix Heatmap
==========================================
Correlation matrix heatmap showing how Stocks, Bonds, Gold, Commodities,
and Cash correlate with each other. Uses realistic long-term correlation
values to demonstrate diversification benefits (especially gold's low
correlation with other assets).

Output: week06_gold_correlation.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Realistic long-term correlation data ---
assets = ["US Stocks", "Bonds", "Gold", "Commodities", "Cash"]
n = len(assets)

# Correlation matrix (symmetric, diagonal = 1.0)
# Values approximate long-term historical correlations
corr_matrix = np.array([
    [ 1.00,  0.05,  0.02,  0.30, -0.02],   # US Stocks
    [ 0.05,  1.00, -0.10, -0.15,  0.25],   # Bonds
    [ 0.02, -0.10,  1.00,  0.25, -0.05],   # Gold
    [ 0.30, -0.15,  0.25,  1.00, -0.10],   # Commodities
    [-0.02,  0.25, -0.05, -0.10,  1.00],   # Cash
])

# --- Create figure ---
fig, ax = plt.subplots(figsize=(9, 8))

# Create heatmap
cmap = plt.cm.RdBu_r  # Red-Blue diverging colormap (red = positive, blue = negative)
im = ax.imshow(corr_matrix, cmap=cmap, vmin=-1, vmax=1, aspect="equal")

# Add colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.8, label="Correlation Coefficient")
cbar.ax.tick_params(labelsize=11)

# Set tick labels
ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(assets, fontsize=12, rotation=30, ha="right")
ax.set_yticklabels(assets, fontsize=12)

# Add correlation values as text in each cell
for i in range(n):
    for j in range(n):
        val = corr_matrix[i, j]
        # Choose text color based on background intensity
        text_color = "white" if abs(val) > 0.5 else "black"
        ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                fontsize=14, fontweight="bold", color=text_color)

# --- Formatting ---
ax.set_title("Asset Class Correlation Matrix\n(Long-Term Historical Estimates)",
             fontsize=16, fontweight="bold", pad=15)

# Add interpretation guide
fig.text(0.5, 0.01,
         "Low or negative correlations = better diversification benefits.  "
         "Gold shows near-zero correlation with stocks, making it a useful diversifier.",
         ha="center", fontsize=10, color="#555", style="italic",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF9C4", edgecolor="#F9A825", alpha=0.9))

fig.tight_layout(rect=[0, 0.05, 1, 1])

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week06_gold_correlation.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
