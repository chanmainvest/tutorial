"""
Week 01: Compound Growth Visualization
========================================
Shows compound growth of $10,000 over 30 years at different annual rates (4%, 7%, 10%).
Three curves on the same chart demonstrate the exponential nature of compound interest.

Output: week01_compound_growth.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Parameters ---
initial_investment = 10_000  # Starting amount in dollars
years = np.arange(0, 31)     # 0 to 30 years
rates = [0.04, 0.07, 0.10]   # Annual growth rates
colors = ["#2196F3", "#FF9800", "#4CAF50"]  # Blue, Orange, Green
labels = ["4% Annual Return", "7% Annual Return", "10% Annual Return"]

# --- Create figure ---
fig, ax = plt.subplots(figsize=(12, 7))

for rate, color, label in zip(rates, colors, labels):
    # Compound growth formula: FV = PV * (1 + r)^n
    values = initial_investment * (1 + rate) ** years
    ax.plot(years, values, color=color, linewidth=2.5, label=label)
    # Annotate the final value at year 30
    final_value = values[-1]
    ax.annotate(
        f"${final_value:,.0f}",
        xy=(30, final_value),
        xytext=(27, final_value * 1.08),
        fontsize=11,
        fontweight="bold",
        color=color,
        arrowprops=dict(arrowstyle="->", color=color, lw=1.5),
    )

# --- Formatting ---
ax.set_title("The Power of Compound Growth", fontsize=18, fontweight="bold", pad=15)
ax.set_xlabel("Years", fontsize=14)
ax.set_ylabel("Portfolio Value ($)", fontsize=14)
ax.set_xlim(0, 30)
ax.set_ylim(0, None)

# Format y-axis with dollar signs and commas
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

# Add gridlines for readability
ax.grid(True, alpha=0.3, linestyle="--")

# Add a horizontal reference line for the initial investment
ax.axhline(y=initial_investment, color="gray", linestyle=":", alpha=0.5)
ax.text(0.5, initial_investment * 1.05, f"Initial: ${initial_investment:,}", fontsize=10, color="gray")

ax.legend(fontsize=12, loc="upper left")
fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week01_compound_growth.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
