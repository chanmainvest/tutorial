"""
Week 12: Life-Stage Portfolio Builder
=======================================
Three pie charts showing recommended asset allocation for different life stages:
- Young Professional (age ~25-35): 80% Stocks / 15% Bonds / 5% Cash
- Mid-Career (age ~40-55): 60% Stocks / 30% Bonds / 10% Cash
- Retirement (age ~60+): 40% Stocks / 40% Bonds / 20% Cash

Shows how allocation shifts from aggressive to conservative as you age.

Output: week12_portfolio_builder.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Portfolio allocations for each life stage ---
categories = ["Stocks", "Bonds", "Cash & Alternatives"]
colors = ["#2196F3", "#FF9800", "#4CAF50"]
explode_slight = (0.03, 0.03, 0.03)  # Slight separation for visual clarity

portfolios = [
    {
        "title": "Young Professional\n(Age 25-35)",
        "allocations": [80, 15, 5],
        "subtitle": "Aggressive Growth",
        "color_accent": "#1565C0",
        "description": "Long time horizon.\nCan tolerate volatility.\nFocus on growth.",
    },
    {
        "title": "Mid-Career\n(Age 40-55)",
        "allocations": [60, 30, 10],
        "subtitle": "Balanced Growth",
        "color_accent": "#E65100",
        "description": "Moderate time horizon.\nBalancing growth\nwith stability.",
    },
    {
        "title": "Retirement\n(Age 60+)",
        "allocations": [40, 40, 20],
        "subtitle": "Conservative Income",
        "color_accent": "#2E7D32",
        "description": "Short time horizon.\nFocus on income\nand capital preservation.",
    },
]

# --- Create figure with 3 subplots ---
fig, axes = plt.subplots(1, 3, figsize=(16, 7))

for ax, portfolio in zip(axes, portfolios):
    allocs = portfolio["allocations"]

    # Draw pie chart
    wedges, texts, autotexts = ax.pie(
        allocs,
        labels=categories,
        colors=colors,
        autopct="%1.0f%%",
        startangle=90,
        explode=explode_slight,
        textprops={"fontsize": 11},
        pctdistance=0.65,
        labeldistance=1.15,
        wedgeprops=dict(edgecolor="white", linewidth=2),
    )

    # Style the percentage text
    for autotext in autotexts:
        autotext.set_fontweight("bold")
        autotext.set_fontsize(13)
        autotext.set_color("white")

    # Title above the pie
    ax.set_title(portfolio["title"], fontsize=14, fontweight="bold",
                 color=portfolio["color_accent"], pad=15)

    # Subtitle below
    ax.text(0, -1.35, portfolio["subtitle"], fontsize=12, fontweight="bold",
            ha="center", color=portfolio["color_accent"])

    # Description text
    ax.text(0, -1.65, portfolio["description"], fontsize=9,
            ha="center", color="#555", linespacing=1.4)

# --- Main title ---
fig.suptitle("Asset Allocation Across Life Stages",
             fontsize=20, fontweight="bold", y=1.0, color="#333")

# --- Legend at the bottom ---
legend_elements = [
    plt.Line2D([0], [0], marker="s", color="w", markerfacecolor=c, markersize=14, label=cat)
    for cat, c in zip(categories, colors)
]
fig.legend(handles=legend_elements, loc="lower center", ncol=3, fontsize=12,
           frameon=True, edgecolor="#ccc", fancybox=True)

# --- Arrow showing the shift ---
fig.text(0.25, 0.05, "More Risk", fontsize=10, ha="center", color="#1565C0", fontweight="bold")
fig.text(0.75, 0.05, "Less Risk", fontsize=10, ha="center", color="#2E7D32", fontweight="bold")
# Use axes[1] annotate with figure fraction coordinates for the arrow
axes[1].annotate(
    "", xy=(0.72, 0.06), xytext=(0.28, 0.06),
    xycoords="figure fraction",
    arrowprops=dict(arrowstyle="->, head_width=0.3", color="#999", lw=2),
)

fig.tight_layout(rect=[0, 0.1, 1, 0.95])

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week12_portfolio_builder.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
