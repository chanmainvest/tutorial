"""
Week 36: Income Portfolio -- Sources of Income (Pie Chart)
============================================================
Pie chart breaking down income sources in a sample income-oriented
investment portfolio.

Output: week36_income_sources.png
"""

import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Data
# -------------------------------------------------------------------
labels = [
    "Dividends",
    "Bond Coupons",
    "Option Premium",
    "REIT Distributions",
    "Other (MLP, Preferred, etc.)",
]

sizes = [30, 25, 20, 15, 10]  # percentages

colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#78909C"]

explode = (0.04, 0.04, 0.04, 0.04, 0.04)  # slight separation

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.0f%%",
    startangle=140,
    pctdistance=0.55,
    wedgeprops=dict(edgecolor="white", linewidth=2),
    textprops=dict(fontsize=11),
)

# Style the percentage text
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight("bold")
    autotext.set_color("white")

# Centre label
ax.text(0, 0, "Income\nPortfolio", ha="center", va="center",
        fontsize=13, fontweight="bold", color="#333")

# Title
ax.set_title("Sample Income Portfolio -- Sources of Income",
             fontsize=14, fontweight="bold", pad=20)

# Detail box
detail_text = (
    "Diversified income reduces dependence\n"
    "on any single source and smooths\n"
    "cash flow across market conditions."
)
fig.text(0.5, 0.02, detail_text, ha="center", fontsize=9, color="#555",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#E8F5E9", alpha=0.8))

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week36_income_sources.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week36_income_sources.png")
