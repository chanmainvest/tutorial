"""
Week 40 - VIX Futures Term Structure
=====================================
Visualizes VIX futures term structure in two market regimes:
  - Contango (normal market): futures prices rise with maturity
  - Backwardation (crisis): futures prices fall with maturity
Both curves are plotted on the same chart for comparison.
Output: week40_vix_term_structure.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Data: synthetic VIX futures term structure
# ---------------------------------------------------------------------------
months = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # months to expiration
labels = [f"M{m}" for m in months]

# Contango: spot VIX is low (~14), futures curve slopes upward
contango = np.array([14.0, 15.2, 16.1, 16.8, 17.3, 17.7, 18.0, 18.2])

# Backwardation: spot VIX is high (~35), futures curve slopes downward
backwardation = np.array([35.0, 31.5, 28.5, 26.0, 24.0, 22.5, 21.5, 20.8])

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Contango curve
ax.plot(months, contango, marker="o", linewidth=2.5, color="#2196F3",
        label="Contango (Normal Market)", markersize=8)

# Backwardation curve
ax.plot(months, backwardation, marker="s", linewidth=2.5, color="#F44336",
        label="Backwardation (Crisis)", markersize=8)

# Shade the area between the two curves to emphasize the difference
ax.fill_between(months, contango, backwardation, alpha=0.08, color="gray")

# Spot VIX markers
ax.annotate("Spot VIX = 14", xy=(1, 14), xytext=(2.2, 12),
            fontsize=10, color="#1565C0",
            arrowprops=dict(arrowstyle="->", color="#1565C0"))
ax.annotate("Spot VIX = 35", xy=(1, 35), xytext=(2.2, 37),
            fontsize=10, color="#C62828",
            arrowprops=dict(arrowstyle="->", color="#C62828"))

# Formatting
ax.set_xlabel("Months to Expiration", fontsize=12)
ax.set_ylabel("VIX Futures Price", fontsize=12)
ax.set_title("VIX Futures Term Structure:\nContango vs Backwardation", fontsize=14, fontweight="bold")
ax.set_xticks(months)
ax.set_xticklabels(labels)
ax.legend(fontsize=11, loc="center right")
ax.grid(True, alpha=0.3)
ax.set_ylim(8, 42)

# Add regime description text boxes
props = dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="gray", alpha=0.9)
ax.text(6.5, 13, "Normal: investors pay\npremium for protection",
        fontsize=9, ha="center", bbox=props, color="#1565C0")
ax.text(6.5, 35, "Crisis: near-term fear\nexceeds long-term expectation",
        fontsize=9, ha="center", bbox=props, color="#C62828")

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week40_vix_term_structure.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
