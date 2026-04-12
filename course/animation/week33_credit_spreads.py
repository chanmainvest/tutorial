"""
Week 33: Credit Spreads by Rating
====================================
Dual-axis bar chart showing:
  - Credit spread over Treasuries (left axis, bars)
  - Historical default rate (right axis, line + markers)
for each credit rating from AAA down to CCC.

Output: week33_credit_spreads.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Data: credit ratings, spreads (bps), and 10-year cumulative
# default rates (approximate historical averages)
# -------------------------------------------------------------------
ratings = ["AAA", "AA", "A", "BBB", "BB", "B", "CCC"]

# Spread over Treasuries in basis points
spreads_bps = [30, 50, 80, 150, 300, 500, 900]

# 10-year cumulative default rate (%)
default_rates = [0.1, 0.3, 0.8, 2.5, 10.0, 25.0, 50.0]

# Colour gradient: green (safe) to red (risky)
bar_colors = ["#2E7D32", "#43A047", "#66BB6A",
              "#FFC107", "#FF9800", "#F44336", "#B71C1C"]

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(11, 6))

x = np.arange(len(ratings))
bar_width = 0.55

# --- Left axis: Credit Spreads (bars) ---
bars = ax1.bar(x, spreads_bps, width=bar_width, color=bar_colors,
               edgecolor="white", linewidth=0.8, alpha=0.85,
               label="Credit Spread (bps)", zorder=3)

# Add spread labels on bars
for bar, spread in zip(bars, spreads_bps):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 15,
             f"{spread}bp", ha="center", va="bottom", fontsize=9,
             fontweight="bold", color="#333")

ax1.set_ylabel("Credit Spread over Treasuries (bps)", fontsize=11,
               color="#1565C0")
ax1.set_ylim(0, 1100)
ax1.tick_params(axis="y", labelcolor="#1565C0")

# --- Right axis: Default Rates (line) ---
ax2 = ax1.twinx()
ax2.plot(x, default_rates, color="#D32F2F", linewidth=2.5,
         marker="D", markersize=7, markerfacecolor="white",
         markeredgecolor="#D32F2F", markeredgewidth=2,
         label="10-Year Default Rate (%)", zorder=4)

# Add default-rate labels
for i, rate in enumerate(default_rates):
    ax2.text(i + 0.15, rate + 1.5, f"{rate}%", fontsize=8,
             color="#D32F2F", fontweight="bold")

ax2.set_ylabel("10-Year Cumulative Default Rate (%)", fontsize=11,
               color="#D32F2F")
ax2.set_ylim(0, 60)
ax2.tick_params(axis="y", labelcolor="#D32F2F")

# --- X-axis ---
ax1.set_xticks(x)
ax1.set_xticklabels(ratings, fontsize=11, fontweight="bold")
ax1.set_xlabel("Credit Rating", fontsize=12)

# --- Divider between investment-grade and high-yield ---
ax1.axvline(2.5, color="#555", linewidth=1.5, linestyle="--", alpha=0.6)
ax1.text(1.0, 1020, "Investment Grade", ha="center", fontsize=10,
         color="#2E7D32", fontweight="bold")
ax1.text(5.0, 1020, "High Yield / Junk", ha="center", fontsize=10,
         color="#C62828", fontweight="bold")

# --- Combined legend ---
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           loc="upper left", fontsize=9, framealpha=0.9)

# --- Title and grid ---
ax1.set_title("Credit Spreads and Default Rates by Rating",
              fontsize=14, fontweight="bold")
ax1.grid(True, axis="y", alpha=0.3, zorder=0)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week33_credit_spreads.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week33_credit_spreads.png")
