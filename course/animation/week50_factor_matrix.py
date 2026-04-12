"""
Week 50 - Factor Performance Across Economic Regimes
======================================================
Heatmap showing how different investment factors perform across
four economic regimes defined by growth and inflation:
  1. Growth Up / Inflation Down   (Goldilocks)
  2. Growth Up / Inflation Up     (Reflation)
  3. Growth Down / Inflation Down (Deflation)
  4. Growth Down / Inflation Up   (Stagflation)
Output: week50_factor_matrix.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Factor performance data (synthetic, directionally realistic)
# ---------------------------------------------------------------------------
# Regimes (columns)
regimes = [
    "Goldilocks\n(Growth Up,\nInflation Down)",
    "Reflation\n(Growth Up,\nInflation Up)",
    "Deflation\n(Growth Down,\nInflation Down)",
    "Stagflation\n(Growth Down,\nInflation Up)"
]

# Factors (rows)
factors = [
    "Value",
    "Growth/Momentum",
    "Quality",
    "Low Volatility",
    "Small Cap",
    "Commodities",
    "Long-Term Bonds",
    "TIPS",
    "Gold",
    "REITs"
]

# Performance matrix: annualized excess return (%)
# Rows = factors, Columns = regimes
performance = np.array([
    [ 8,  5, -3, -2],   # Value
    [12,  6, -8, -10],  # Growth/Momentum
    [ 6,  4,  2,  0],   # Quality
    [ 2,  0,  5,  1],   # Low Volatility
    [10,  8, -6, -8],   # Small Cap
    [-2,  9, -5,  6],   # Commodities
    [ 4, -4,  8, -6],   # Long-Term Bonds
    [ 1,  3,  2,  5],   # TIPS
    [-3,  2,  4,  8],   # Gold
    [ 7,  4, -4, -1],   # REITs
], dtype=float)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 8))

# Heatmap
im = ax.imshow(performance, cmap="RdYlGn", aspect="auto", vmin=-12, vmax=12)

# Color bar
cbar = plt.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
cbar.set_label("Annualized Excess Return (%)", fontsize=11)

# Add text annotations in each cell
for i in range(len(factors)):
    for j in range(len(regimes)):
        value = performance[i, j]
        # Choose text color based on background
        text_color = "white" if abs(value) > 6 else "black"
        sign = "+" if value > 0 else ""
        ax.text(j, i, f"{sign}{value:.0f}%", ha="center", va="center",
                fontsize=11, fontweight="bold", color=text_color)

# Axis labels
ax.set_xticks(np.arange(len(regimes)))
ax.set_xticklabels(regimes, fontsize=9.5, ha="center")
ax.set_yticks(np.arange(len(factors)))
ax.set_yticklabels(factors, fontsize=10)

# Move x-axis labels to the top
ax.xaxis.set_ticks_position("top")
ax.xaxis.set_label_position("top")

# Title
ax.set_title("Factor Performance Across Economic Regimes\n\n\n",
             fontsize=14, fontweight="bold", pad=40)

# Grid lines between cells
ax.set_xticks(np.arange(-0.5, len(regimes), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(factors), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=2)
ax.tick_params(which="minor", size=0)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week50_factor_matrix.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
