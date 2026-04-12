"""
Week 07: Portfolio Rebalancing Demonstration
=============================================
Stacked area chart showing how a 60/40 portfolio drifts as stocks outperform bonds,
eventually reaching ~75/25. Then shows the rebalancing action that snaps the
allocation back to the target 60/40 split.

Output: week07_rebalancing_demo.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Simulate portfolio drift ---
# Phase 1: Stocks outperform, allocation drifts from 60/40 toward 75/25 (months 0-24)
# Phase 2: Rebalancing event at month 24, snaps back to 60/40
# Phase 3: Drift resumes (months 24-36)

months = np.arange(0, 37)  # 0 to 36 months (3 years)

# Stock allocation drifts upward as stocks outperform
stock_alloc = np.zeros(len(months))
for i, m in enumerate(months):
    if m <= 24:
        # Gradual drift from 60% to 75% over 24 months
        stock_alloc[i] = 60 + (15 * m / 24)
    elif m == 24:
        # This is handled above; rebalance happens visually between 24 and 25
        stock_alloc[i] = 75
    else:
        # After rebalancing at month 24, start from 60% and drift again
        months_after = m - 24
        stock_alloc[i] = 60 + (15 * months_after / 24)

# Insert the rebalance snap: at month 24, allocation is 75; at month 25, it's ~60.6
# The array already handles this since month 25 -> 60 + 15*1/24 = 60.625

bond_alloc = 100 - stock_alloc

# --- Create figure ---
fig, ax = plt.subplots(figsize=(13, 7))

# Stacked area chart
ax.fill_between(months, 0, stock_alloc, color="#2196F3", alpha=0.8, label="Stocks")
ax.fill_between(months, stock_alloc, 100, color="#FF9800", alpha=0.8, label="Bonds")

# Target allocation lines
ax.axhline(y=60, color="white", linestyle="--", linewidth=2, alpha=0.8)
ax.axhline(y=40, color="white", linestyle=":", linewidth=1, alpha=0.4)

# Rebalance event marker
ax.axvline(x=24, color="#F44336", linestyle="-", linewidth=2.5, alpha=0.8)
ax.annotate(
    "REBALANCE\nSell stocks, buy bonds\nBack to 60/40 target",
    xy=(24, 50),
    xytext=(28, 82),
    fontsize=11,
    fontweight="bold",
    color="#C62828",
    ha="center",
    arrowprops=dict(arrowstyle="->, head_width=0.3", color="#C62828", lw=2),
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#C62828"),
)

# Label the drift
ax.annotate(
    "Portfolio drifts\nto 75/25",
    xy=(22, 75),
    xytext=(16, 85),
    fontsize=10,
    color="#1565C0",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="#1565C0", lw=1.5),
)

# Label the allocations
ax.text(12, 35, "STOCKS", fontsize=16, fontweight="bold", color="white", ha="center", alpha=0.7)
ax.text(12, 85, "BONDS", fontsize=16, fontweight="bold", color="white", ha="center", alpha=0.7)

# Target label
ax.text(1, 61.5, "Target: 60% Stocks", fontsize=9, color="white", fontweight="bold")

# --- Formatting ---
ax.set_title("Portfolio Rebalancing: Why It Matters",
             fontsize=17, fontweight="bold", pad=15)
ax.set_xlabel("Months", fontsize=13)
ax.set_ylabel("Allocation (%)", fontsize=13)
ax.set_ylim(0, 100)
ax.set_xlim(0, 36)
ax.legend(fontsize=12, loc="lower left",
          bbox_to_anchor=(0.0, 0.0),
          facecolor="white", edgecolor="gray")

# Explanation box
ax.text(
    0.98, 0.02,
    "Without rebalancing, a rising stock market pushes\n"
    "your portfolio to take more risk than intended.\n"
    "Regular rebalancing maintains your target risk level.",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="bottom",
    horizontalalignment="right",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#E8F5E9", edgecolor="#2E7D32", alpha=0.9),
)

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week07_rebalancing_demo.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
