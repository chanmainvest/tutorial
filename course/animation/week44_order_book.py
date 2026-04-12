"""
Week 44 - Order Book Visualization
====================================
Displays a simplified limit order book with:
  - Bid levels (buy orders) on the left in green
  - Ask levels (sell orders) on the right in red
  - Depth bars showing volume at each price level
  - Spread highlighted between best bid and best ask
Output: week44_order_book.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Synthetic order book data
# ---------------------------------------------------------------------------
# Price levels and volumes for bids (buy side)
bid_prices = np.array([99.50, 99.40, 99.30, 99.20, 99.10, 99.00, 98.90, 98.80])
bid_volumes = np.array([120, 250, 180, 400, 320, 550, 280, 150])

# Price levels and volumes for asks (sell side)
ask_prices = np.array([99.60, 99.70, 99.80, 99.90, 100.00, 100.10, 100.20, 100.30])
ask_volumes = np.array([100, 200, 350, 150, 480, 220, 300, 170])

# Best bid / best ask
best_bid = bid_prices[0]
best_ask = ask_prices[0]
spread = best_ask - best_bid
mid_price = (best_bid + best_ask) / 2

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))

bar_height = 0.06  # thickness of each bar

# Bid bars (extend to the LEFT, so use negative volumes for visual direction)
ax.barh(bid_prices, -bid_volumes, height=bar_height, color="#4CAF50", alpha=0.8,
        edgecolor="#2E7D32", linewidth=0.8, label="Bids (Buy Orders)")

# Ask bars (extend to the RIGHT)
ax.barh(ask_prices, ask_volumes, height=bar_height, color="#F44336", alpha=0.8,
        edgecolor="#C62828", linewidth=0.8, label="Asks (Sell Orders)")

# Add volume labels on each bar
for p, v in zip(bid_prices, bid_volumes):
    ax.text(-v - 15, p, str(v), ha="right", va="center", fontsize=9, color="#2E7D32")
for p, v in zip(ask_prices, ask_volumes):
    ax.text(v + 15, p, str(v), ha="left", va="center", fontsize=9, color="#C62828")

# Spread region
ax.axhspan(best_bid, best_ask, alpha=0.15, color="#FFC107", zorder=0)
ax.annotate(f"Spread = ${spread:.2f}",
            xy=(0, mid_price), fontsize=11, fontweight="bold",
            ha="center", va="center", color="#F57F17",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="#F57F17", alpha=0.9))

# Best bid / best ask lines
ax.axhline(y=best_bid, color="#4CAF50", linewidth=1.2, linestyle="--", alpha=0.6)
ax.axhline(y=best_ask, color="#F44336", linewidth=1.2, linestyle="--", alpha=0.6)

# Labels for best bid / ask
ax.text(-max(bid_volumes) * 0.5, best_bid + 0.025,
        f"Best Bid: ${best_bid:.2f}", fontsize=10, color="#2E7D32", fontweight="bold")
ax.text(max(ask_volumes) * 0.5, best_ask + 0.025,
        f"Best Ask: ${best_ask:.2f}", fontsize=10, color="#C62828", fontweight="bold",
        ha="center")

# Center line
ax.axvline(x=0, color="gray", linewidth=1, linestyle="-", alpha=0.4)

# Formatting
ax.set_xlabel("Volume (shares)", fontsize=12)
ax.set_ylabel("Price ($)", fontsize=12)
ax.set_title("Order Book: Bid and Ask Depth", fontsize=14, fontweight="bold")
ax.legend(fontsize=11, loc="lower left")
ax.grid(True, alpha=0.2, axis="y")

# Make x-axis show absolute values
from matplotlib.ticker import FuncFormatter
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{abs(int(x))}"))
ax.set_xlabel("Volume (shares) -- Bids (left) | Asks (right)", fontsize=11)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week44_order_book.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
