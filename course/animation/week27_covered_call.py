"""
Week 27: Covered Call Payoff Diagram
=====================================
Visualizes the payoff of a covered call strategy compared to holding
stock only. Shows how the short call caps upside but the premium
received provides a buffer on the downside.

Output: week27_covered_call.png
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------
stock_purchase_price = 100  # bought stock at $100
strike_price = 110          # sold call with strike $110
premium_received = 4        # collected $4 premium

# -------------------------------------------------------------------
# Stock price range at expiration
# -------------------------------------------------------------------
stock_prices = np.linspace(70, 140, 300)

# -------------------------------------------------------------------
# Payoff calculations
# -------------------------------------------------------------------
# Stock-only P&L
stock_pnl = stock_prices - stock_purchase_price

# Short call P&L (obligation to sell at strike if exercised)
short_call_pnl = np.where(
    stock_prices <= strike_price,
    premium_received,                                   # call expires worthless
    premium_received - (stock_prices - strike_price)    # call exercised
)

# Covered call = stock + short call
covered_call_pnl = stock_pnl + short_call_pnl

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Stock-only payoff
ax.plot(stock_prices, stock_pnl, color="#2196F3", linewidth=2,
        label="Stock Only", linestyle="--")

# Covered call payoff
ax.plot(stock_prices, covered_call_pnl, color="#FF5722", linewidth=2.5,
        label="Covered Call (Stock + Short Call)")

# Shade the premium-received area (buffer zone between the two lines
# where covered call outperforms stock-only, i.e. below strike)
mask_below = stock_prices <= strike_price
ax.fill_between(
    stock_prices[mask_below],
    stock_pnl[mask_below],
    covered_call_pnl[mask_below],
    color="#4CAF50", alpha=0.25,
    label=f"Premium Buffer (${premium_received})"
)

# Shade the capped-upside area (above strike, where stock outperforms)
mask_above = stock_prices >= strike_price
ax.fill_between(
    stock_prices[mask_above],
    covered_call_pnl[mask_above],
    stock_pnl[mask_above],
    color="#F44336", alpha=0.15,
    label="Capped Upside"
)

# Reference lines
ax.axhline(0, color="grey", linewidth=0.8, linestyle="-")
ax.axvline(strike_price, color="#9C27B0", linewidth=1, linestyle=":",
           label=f"Strike Price (${strike_price})")
ax.axvline(stock_purchase_price, color="#607D8B", linewidth=1,
           linestyle=":", label=f"Purchase Price (${stock_purchase_price})")

# Max profit annotation
max_profit = (strike_price - stock_purchase_price) + premium_received
ax.annotate(
    f"Max Profit = ${max_profit}",
    xy=(strike_price, max_profit),
    xytext=(strike_price + 8, max_profit + 5),
    fontsize=10, fontweight="bold", color="#FF5722",
    arrowprops=dict(arrowstyle="->", color="#FF5722", lw=1.5),
)

# Breakeven annotation
breakeven = stock_purchase_price - premium_received
ax.annotate(
    f"Breakeven = ${breakeven}",
    xy=(breakeven, 0),
    xytext=(breakeven - 12, -10),
    fontsize=10, fontweight="bold", color="#4CAF50",
    arrowprops=dict(arrowstyle="->", color="#4CAF50", lw=1.5),
)

# Labels and formatting
ax.set_title("Covered Call Payoff Diagram", fontsize=14, fontweight="bold")
ax.set_xlabel("Stock Price at Expiration ($)", fontsize=12)
ax.set_ylabel("Profit / Loss ($)", fontsize=12)
ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(70, 140)
ax.set_ylim(-35, 45)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week27_covered_call.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week27_covered_call.png")
