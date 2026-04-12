"""
Week 49 - Implied Volatility Surface
======================================
3D surface plot of implied volatility across:
  - X-axis: strike price (moneyness)
  - Y-axis: time to maturity
  - Z-axis: implied volatility
Shows the volatility smile/skew and term structure in one view.
Output: week49_vol_surface.png
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import os

# ---------------------------------------------------------------------------
# Generate synthetic implied volatility surface
# ---------------------------------------------------------------------------
# Strike prices as moneyness (K/S): 0.80 to 1.20
strikes = np.linspace(0.80, 1.20, 50)

# Maturities in years: 0.1 (1 month) to 2.0 (2 years)
maturities = np.linspace(0.1, 2.0, 50)

# Create meshgrid
K, T = np.meshgrid(strikes, maturities)

# Implied volatility surface model:
# - Smile/skew: higher vol for OTM puts (low strike) and slightly for OTM calls
# - Term structure: vol tends to flatten with longer maturity
# - Base vol around 20%
base_vol = 0.20

# Skew component: lower strikes have higher vol (put skew)
skew = 0.15 * (1.0 - K) ** 2

# Smile component: slight uptick for very high strikes
smile = 0.03 * (K - 1.0) ** 2

# Term structure: short-term vol is more variable, converges to mean
term_effect = 0.05 * np.exp(-1.5 * T)

# Combine
IV = base_vol + skew + smile + term_effect

# Add some surface texture
np.random.seed(42)
IV += np.random.normal(0, 0.003, IV.shape)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

# Surface plot
surf = ax.plot_surface(K, T, IV * 100, cmap="RdYlBu_r", alpha=0.85,
                       edgecolor="gray", linewidth=0.2, antialiased=True)

# Color bar
cbar = fig.colorbar(surf, ax=ax, shrink=0.55, aspect=15, pad=0.1)
cbar.set_label("Implied Volatility (%)", fontsize=11)

# ATM line (strike = 1.0)
atm_idx = np.argmin(np.abs(strikes - 1.0))
ax.plot(np.full_like(maturities, strikes[atm_idx]),
        maturities, IV[:, atm_idx] * 100,
        color="black", linewidth=2, linestyle="--", label="ATM (K/S = 1.0)")

# Labels
ax.set_xlabel("Moneyness (K/S)", fontsize=11, labelpad=10)
ax.set_ylabel("Time to Maturity (years)", fontsize=11, labelpad=10)
ax.set_zlabel("Implied Volatility (%)", fontsize=11, labelpad=10)
ax.set_title("Implied Volatility Surface", fontsize=14, fontweight="bold", pad=20)

# View angle
ax.view_init(elev=25, azim=235)

# Annotations (using text on the figure)
fig.text(0.15, 0.85, "OTM Puts\n(higher vol, skew)",
         fontsize=9, color="#C62828", fontweight="bold")
fig.text(0.65, 0.85, "OTM Calls\n(smile uptick)",
         fontsize=9, color="#1565C0", fontweight="bold")

ax.legend(fontsize=9, loc="upper right")

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week49_vol_surface.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
