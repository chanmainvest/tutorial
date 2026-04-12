"""
Week 32: Bond Duration -- Price Sensitivity to Yield Changes
==============================================================
Shows how bonds of different durations (2yr, 5yr, 10yr, 30yr) react
to yield changes. Longer duration = steeper price change curve.

Output: week32_duration.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Bond price approximation using modified duration & convexity
# -------------------------------------------------------------------
def bond_price_change(duration, convexity, yield_change):
    """
    Approximate percentage price change for a given yield shift.
    %dP ~ -D * dy + 0.5 * C * dy^2
    """
    return -duration * yield_change + 0.5 * convexity * yield_change**2

# -------------------------------------------------------------------
# Bond characteristics (modified duration, convexity)
# -------------------------------------------------------------------
bonds = {
    "2-Year Bond":  {"duration": 1.9,  "convexity": 5,    "color": "#4CAF50"},
    "5-Year Bond":  {"duration": 4.5,  "convexity": 25,   "color": "#2196F3"},
    "10-Year Bond": {"duration": 8.5,  "convexity": 90,   "color": "#FF9800"},
    "30-Year Bond": {"duration": 19.0, "convexity": 450,  "color": "#F44336"},
}

# Yield change range: -300bp to +300bp
yield_changes = np.linspace(-0.03, 0.03, 300)

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7))

for name, params in bonds.items():
    pct_change = bond_price_change(
        params["duration"], params["convexity"], yield_changes
    ) * 100  # convert to percentage

    ax.plot(yield_changes * 100, pct_change,
            color=params["color"], linewidth=2.5,
            label=f'{name} (Dur={params["duration"]:.1f})')

# Reference lines
ax.axhline(0, color="grey", linewidth=0.8)
ax.axvline(0, color="grey", linewidth=0.8)

# Shade rate-increase loss zone
ax.fill_betweenx([-60, 0], 0, 3, color="#FFEBEE", alpha=0.3)
ax.text(1.5, -50, "Rates Rise\nPrices Fall", ha="center", fontsize=10,
        color="#C62828", fontweight="bold", alpha=0.7)

# Shade rate-decrease gain zone
ax.fill_betweenx([0, 70], -3, 0, color="#E8F5E9", alpha=0.3)
ax.text(-1.5, 55, "Rates Fall\nPrices Rise", ha="center", fontsize=10,
        color="#2E7D32", fontweight="bold", alpha=0.7)

# Duration interpretation box
info_text = (
    "Duration = approximate % price change\n"
    "for a 1% change in yield.\n\n"
    "Longer duration --> more interest-rate risk"
)
ax.text(0.98, 0.02, info_text, transform=ax.transAxes, fontsize=9,
        verticalalignment="bottom", horizontalalignment="right",
        fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", alpha=0.9))

# 100bp example annotations
for name, params in bonds.items():
    pct_at_100bp = bond_price_change(params["duration"], params["convexity"], 0.01) * 100
    ax.plot(1.0, pct_at_100bp, "o", color=params["color"], markersize=6)

ax.annotate("+100bp impact",
            xy=(1.0, -0.5), xytext=(1.8, -5),
            fontsize=9, color="#555",
            arrowprops=dict(arrowstyle="->", color="#555", lw=1))

# Labels and formatting
ax.set_title("Bond Price Sensitivity by Duration", fontsize=14, fontweight="bold")
ax.set_xlabel("Yield Change (basis points / 100 = %)", fontsize=12)
ax.set_ylabel("Price Change (%)", fontsize=12)
ax.legend(loc="upper right", fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 3)
ax.set_ylim(-60, 70)

# Custom x-axis labels in basis points
tick_vals = np.arange(-3, 3.5, 0.5)
ax.set_xticks(tick_vals)
ax.set_xticklabels([f"{int(v*100)}bp" for v in tick_vals], fontsize=8)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week32_duration.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week32_duration.png")
