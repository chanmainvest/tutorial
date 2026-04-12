"""
Week 03: Risk-Return Frontier
===============================
Scatter plot of historical risk (standard deviation) vs. annualized return
for major asset classes. Demonstrates the general upward-sloping relationship
between risk and expected return.

Output: week03_risk_return_frontier.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Historical approximate data (annualized, long-term averages) ---
# Format: (name, std_dev %, annualized_return %, color)
asset_classes = [
    ("Cash",                1.0,   2.5,  "#9E9E9E"),
    ("T-Bills",             2.0,   3.5,  "#78909C"),
    ("Bonds\n(Agg)",        5.5,   5.0,  "#42A5F5"),
    ("Corporate\nBonds",    7.0,   6.0,  "#1565C0"),
    ("US Stocks\n(S&P500)", 15.0, 10.0,  "#4CAF50"),
    ("Int'l Stocks\n(EAFE)",17.0,  8.5,  "#FF9800"),
    ("Emerging\nMarkets",   22.0,  9.5,  "#F44336"),
    ("REITs",               19.0, 10.5,  "#9C27B0"),
]

names   = [a[0] for a in asset_classes]
risks   = [a[1] for a in asset_classes]
returns = [a[2] for a in asset_classes]
colors  = [a[3] for a in asset_classes]

# --- Create figure ---
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each asset class as a labeled scatter point
for name, risk, ret, color in asset_classes:
    ax.scatter(risk, ret, s=200, color=color, edgecolors="white", linewidths=1.5, zorder=5)
    # Offset labels so they don't overlap the dot
    offset_x = 0.8
    offset_y = 0.3
    ax.annotate(
        name,
        xy=(risk, ret),
        xytext=(risk + offset_x, ret + offset_y),
        fontsize=10,
        fontweight="bold",
        color=color,
        ha="left",
    )

# Draw a rough "frontier" trend line
z = np.polyfit(risks, returns, 2)
p = np.poly1d(z)
x_smooth = np.linspace(0, 25, 100)
ax.plot(x_smooth, p(x_smooth), "--", color="gray", alpha=0.4, linewidth=1.5, label="Trend line")

# --- Formatting ---
ax.set_title("Risk vs. Return: Major Asset Classes", fontsize=18, fontweight="bold", pad=15)
ax.set_xlabel("Risk (Annualized Standard Deviation %)", fontsize=14)
ax.set_ylabel("Annualized Return (%)", fontsize=14)
ax.set_xlim(-1, 26)
ax.set_ylim(0, 13)
ax.grid(True, alpha=0.3, linestyle="--")

# Add quadrant labels
ax.text(2, 11.5, "Low Risk / High Return\n(ideal but rare)", fontsize=9, color="green", alpha=0.6,
        bbox=dict(boxstyle="round", facecolor="#E8F5E9", alpha=0.5))
ax.text(18, 2.5, "High Risk / Low Return\n(avoid)", fontsize=9, color="red", alpha=0.6,
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", alpha=0.5))

# Arrow showing the general principle
ax.annotate(
    "Higher risk generally\nmeans higher return",
    xy=(13, 8),
    xytext=(6, 11),
    fontsize=11,
    color="#333",
    arrowprops=dict(arrowstyle="->", color="#333", lw=1.5),
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF9C4", edgecolor="#F9A825"),
)

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week03_risk_return_frontier.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
