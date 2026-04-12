"""
Week 09: Index Construction - Price-Weighted vs Cap-Weighted
==============================================================
Side-by-side bar charts comparing how the same 5 stocks receive different
weights in a price-weighted index vs. a capitalization-weighted index.
Demonstrates why index methodology matters.

Output: week09_index_construction.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Sample stock data ---
stocks = ["MegaCorp", "TechGiant", "BankCo", "RetailInc", "SmallFirm"]

# Stock prices (price-weighted indexing uses share price)
prices = np.array([350, 180, 55, 40, 15])

# Market capitalizations in billions (cap-weighted uses total market value)
market_caps = np.array([2200, 3100, 450, 120, 30])

# --- Calculate weights ---
# Price-weighted: weight = price / sum(prices)
price_weights = prices / prices.sum() * 100

# Cap-weighted: weight = market_cap / sum(market_caps)
cap_weights = market_caps / market_caps.sum() * 100

# --- Create figure with side-by-side subplots ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Colors for each stock
colors = ["#1565C0", "#2196F3", "#4CAF50", "#FF9800", "#F44336"]

# --- Left panel: Price-Weighted ---
bars1 = ax1.barh(stocks, price_weights, color=colors, edgecolor="white", linewidth=1.5, height=0.6)
ax1.set_xlabel("Weight in Index (%)", fontsize=12)
ax1.set_title("Price-Weighted Index", fontsize=15, fontweight="bold", color="#1565C0")
ax1.set_xlim(0, 65)
ax1.invert_yaxis()

# Add value labels
for bar, w, p in zip(bars1, price_weights, prices):
    ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
             f"{w:.1f}%  (${p})", va="center", fontsize=11, fontweight="bold")

# Add subtitle
ax1.text(0.5, -0.12, f"Weight = Stock Price / Sum of Prices\nHighest priced stock dominates",
         transform=ax1.transAxes, ha="center", fontsize=10, color="#666", style="italic")

ax1.grid(axis="x", alpha=0.3, linestyle="--")
ax1.set_axisbelow(True)

# --- Right panel: Cap-Weighted ---
bars2 = ax2.barh(stocks, cap_weights, color=colors, edgecolor="white", linewidth=1.5, height=0.6)
ax2.set_xlabel("Weight in Index (%)", fontsize=12)
ax2.set_title("Cap-Weighted Index", fontsize=15, fontweight="bold", color="#2E7D32")
ax2.set_xlim(0, 65)
ax2.invert_yaxis()

# Add value labels
for bar, w, mc in zip(bars2, cap_weights, market_caps):
    label = f"${mc:,}B" if mc >= 1000 else f"${mc}B"
    ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
             f"{w:.1f}%  ({label})", va="center", fontsize=11, fontweight="bold")

# Add subtitle
ax2.text(0.5, -0.12, f"Weight = Market Cap / Sum of Market Caps\nLargest company dominates",
         transform=ax2.transAxes, ha="center", fontsize=10, color="#666", style="italic")

ax2.grid(axis="x", alpha=0.3, linestyle="--")
ax2.set_axisbelow(True)

# --- Main title ---
fig.suptitle("Index Construction Methods: Same Stocks, Different Weights",
             fontsize=17, fontweight="bold", y=1.02)

# --- Key insight box ---
fig.text(0.5, -0.06,
         "Key Insight: MegaCorp has the highest share price but TechGiant has the largest market cap.\n"
         "Price-weighted indexes (like the Dow) are biased by stock price; "
         "Cap-weighted indexes (like the S&P 500) reflect true economic size.",
         ha="center", fontsize=11, color="#333",
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", edgecolor="#F9A825", alpha=0.9))

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week09_index_construction.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
