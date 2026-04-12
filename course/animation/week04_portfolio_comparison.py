"""
Week 04: Portfolio Comparison - Stocks vs Balanced Portfolios
==============================================================
Line chart comparing 100% stocks vs 60/40 vs 40/60 portfolio growth over 20 years.
Highlights drawdown periods (2008 financial crisis, 2020 COVID crash) to show
how balanced portfolios reduce losses during downturns.

Output: week04_portfolio_comparison.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Simulate realistic annual returns (2004-2023, 20 years) ---
# Approximate annual returns for stocks and bonds
np.random.seed(42)
years = np.arange(2004, 2024)

# Simplified annual returns inspired by real data
stock_returns = np.array([
    0.109, 0.049, 0.158, 0.055, -0.370, 0.265,   # 2004-2009
    0.151, 0.021, 0.160, 0.323, 0.136, 0.014,     # 2010-2015
    0.120, 0.217, -0.044, 0.314, 0.183, 0.285,    # 2016-2021
    -0.182, 0.263                                    # 2022-2023
])

bond_returns = np.array([
    0.043, 0.024, 0.044, 0.070, 0.053, 0.059,     # 2004-2009
    0.065, 0.078, 0.042, -0.020, 0.060, 0.006,    # 2010-2015
    0.026, 0.035, 0.001, 0.087, 0.075, -0.015,    # 2016-2021
    -0.130, 0.055                                    # 2022-2023
])

# Calculate cumulative growth for each portfolio
initial = 10_000

def portfolio_growth(stock_w, bond_w, stock_ret, bond_ret, initial_val):
    """Calculate cumulative portfolio value given stock/bond weights and returns."""
    portfolio_returns = stock_w * stock_ret + bond_w * bond_ret
    values = [initial_val]
    for r in portfolio_returns:
        values.append(values[-1] * (1 + r))
    return np.array(values)

# Three portfolios
vals_100 = portfolio_growth(1.0, 0.0, stock_returns, bond_returns, initial)
vals_60_40 = portfolio_growth(0.6, 0.4, stock_returns, bond_returns, initial)
vals_40_60 = portfolio_growth(0.4, 0.6, stock_returns, bond_returns, initial)

# Year labels including start year
year_labels = np.arange(2003, 2024)  # Starts at end of 2003

# --- Create figure ---
fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(year_labels, vals_100, color="#F44336", linewidth=2.5, label="100% Stocks")
ax.plot(year_labels, vals_60_40, color="#2196F3", linewidth=2.5, label="60% Stocks / 40% Bonds")
ax.plot(year_labels, vals_40_60, color="#4CAF50", linewidth=2.5, label="40% Stocks / 60% Bonds")

# Highlight drawdown periods
# 2008 Financial Crisis (shaded region)
ax.axvspan(2007.5, 2009.5, alpha=0.12, color="red", label="Crisis periods")
ax.text(2008.5, max(vals_100) * 0.95, "2008\nFinancial\nCrisis", ha="center", fontsize=9,
        color="#B71C1C", fontweight="bold")

# 2020 COVID crash
ax.axvspan(2019.5, 2020.5, alpha=0.12, color="red")
ax.text(2020, max(vals_100) * 0.88, "2020\nCOVID", ha="center", fontsize=9,
        color="#B71C1C", fontweight="bold")

# Annotate final values
for vals, color, yoff in [(vals_100, "#F44336", 0), (vals_60_40, "#2196F3", 0), (vals_40_60, "#4CAF50", 0)]:
    ax.annotate(
        f"${vals[-1]:,.0f}",
        xy=(2023, vals[-1]),
        xytext=(2023.3, vals[-1]),
        fontsize=10,
        fontweight="bold",
        color=color,
        va="center",
    )

# --- Formatting ---
ax.set_title("Portfolio Comparison: More Bonds = Less Volatility", fontsize=17, fontweight="bold", pad=15)
ax.set_xlabel("Year", fontsize=13)
ax.set_ylabel("Portfolio Value ($)", fontsize=13)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.legend(fontsize=11, loc="upper left")
ax.grid(True, alpha=0.3, linestyle="--")
ax.set_xlim(2003, 2024.5)

# Add takeaway box
ax.text(
    0.02, 0.02,
    "Balanced portfolios gave up some upside but significantly\nreduced losses during market downturns.",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="bottom",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#E3F2FD", edgecolor="#1565C0", alpha=0.9),
)

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week04_portfolio_comparison.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
