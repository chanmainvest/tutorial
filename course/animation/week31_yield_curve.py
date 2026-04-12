"""
Week 31: Yield Curve Shapes
==============================
Three yield curves plotted on the same chart:
  - Normal (upward sloping) -- healthy economy
  - Flat -- transition / uncertainty
  - Inverted -- recession signal

Output: week31_yield_curve.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Maturity points (in years)
# -------------------------------------------------------------------
maturities = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30])
maturity_labels = ["3M", "6M", "1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "20Y", "30Y"]

# -------------------------------------------------------------------
# Yield data (stylised, representative shapes)
# -------------------------------------------------------------------
# Normal curve: short rates low, long rates higher
normal_yields = np.array([2.0, 2.2, 2.5, 2.9, 3.2, 3.6, 3.9, 4.1, 4.3, 4.4])

# Flat curve: all maturities roughly the same
flat_yields = np.array([3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5])

# Inverted curve: short rates higher than long rates
inverted_yields = np.array([5.2, 5.1, 4.9, 4.6, 4.3, 4.0, 3.8, 3.6, 3.5, 3.4])

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6))

# Normal yield curve
ax.plot(maturities, normal_yields, color="#4CAF50", linewidth=2.5,
        marker="o", markersize=5, label="Normal (Upward Sloping)")
ax.fill_between(maturities, normal_yields, alpha=0.08, color="#4CAF50")

# Flat yield curve
ax.plot(maturities, flat_yields, color="#FF9800", linewidth=2.5,
        marker="s", markersize=5, label="Flat")

# Inverted yield curve
ax.plot(maturities, inverted_yields, color="#F44336", linewidth=2.5,
        marker="D", markersize=5, label="Inverted")
ax.fill_between(maturities, inverted_yields, alpha=0.08, color="#F44336")

# Annotations for each curve
ax.annotate("Healthy economy:\nlong-term rates > short-term",
            xy=(20, 4.3), xytext=(15, 4.8),
            fontsize=9, color="#2E7D32", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#2E7D32", lw=1.2))

ax.annotate("Transition /\nUncertainty",
            xy=(15, 3.5), xytext=(18, 2.8),
            fontsize=9, color="#E65100", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#E65100", lw=1.2))

ax.annotate("Recession signal:\nshort-term rates > long-term",
            xy=(1, 4.9), xytext=(3, 5.5),
            fontsize=9, color="#C62828", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#C62828", lw=1.2))

# Spread annotation
spread = normal_yields[-1] - normal_yields[0]
ax.annotate("",
            xy=(30, normal_yields[0]), xytext=(30, normal_yields[-1]),
            arrowprops=dict(arrowstyle="<->", color="#4CAF50", lw=1.5))
ax.text(31, (normal_yields[0] + normal_yields[-1]) / 2,
        f"Term Spread\n{spread:.1f}%", fontsize=8, color="#4CAF50",
        ha="left", va="center", fontweight="bold")

# X-axis formatting
ax.set_xticks(maturities)
ax.set_xticklabels(maturity_labels, fontsize=9)

# Labels and formatting
ax.set_title("Treasury Yield Curve Shapes", fontsize=14, fontweight="bold")
ax.set_xlabel("Maturity", fontsize=12)
ax.set_ylabel("Yield (%)", fontsize=12)
ax.legend(loc="center left", fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_ylim(1.5, 6.0)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week31_yield_curve.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week31_yield_curve.png")
