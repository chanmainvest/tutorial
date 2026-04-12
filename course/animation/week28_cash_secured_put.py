"""
Week 28: Cash-Secured Put Payoff Diagram
==========================================
Shows the payoff of selling a cash-secured put. Compares the effective
purchase price (strike - premium) to simply buying the stock outright.

Output: week28_cash_secured_put.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------
current_price = 100         # current stock price
strike_price = 95           # put strike (willing to buy at $95)
premium_received = 3.50     # premium collected for selling the put

# -------------------------------------------------------------------
# Stock price range at expiration
# -------------------------------------------------------------------
stock_prices = np.linspace(60, 130, 300)

# -------------------------------------------------------------------
# Payoff calculations
# -------------------------------------------------------------------
# Cash-secured put P&L (sold put, secured by cash = strike amount)
# If stock >= strike: keep premium, no assignment
# If stock <  strike: forced to buy at strike, P&L = (stock - strike) + premium
csp_pnl = np.where(
    stock_prices >= strike_price,
    premium_received,
    (stock_prices - strike_price) + premium_received
)

# "Just buy stock at current price" P&L
buy_stock_pnl = stock_prices - current_price

# Effective purchase price if assigned
effective_price = strike_price - premium_received

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Stock purchase payoff
ax.plot(stock_prices, buy_stock_pnl, color="#2196F3", linewidth=2,
        linestyle="--", label=f"Buy Stock at ${current_price}")

# Cash-secured put payoff
ax.plot(stock_prices, csp_pnl, color="#FF5722", linewidth=2.5,
        label=f"Cash-Secured Put (Strike ${strike_price}, Premium ${premium_received})")

# Shade profit zone for CSP
profit_mask = csp_pnl > 0
ax.fill_between(stock_prices, 0, csp_pnl,
                where=profit_mask, color="#4CAF50", alpha=0.15,
                label="CSP Profit Zone")

# Reference lines
ax.axhline(0, color="grey", linewidth=0.8)
ax.axvline(strike_price, color="#9C27B0", linewidth=1, linestyle=":",
           label=f"Strike Price (${strike_price})")
ax.axvline(effective_price, color="#FF9800", linewidth=1.5, linestyle="--",
           label=f"Effective Buy Price (${effective_price:.2f})")

# Breakeven annotation
ax.annotate(
    f"Breakeven = ${effective_price:.2f}\n(Strike - Premium)",
    xy=(effective_price, 0),
    xytext=(effective_price - 18, -12),
    fontsize=10, fontweight="bold", color="#FF9800",
    arrowprops=dict(arrowstyle="->", color="#FF9800", lw=1.5),
)

# Max profit annotation
ax.annotate(
    f"Max Profit = ${premium_received}\n(Premium Collected)",
    xy=(strike_price + 5, premium_received),
    xytext=(strike_price + 10, premium_received + 8),
    fontsize=10, fontweight="bold", color="#4CAF50",
    arrowprops=dict(arrowstyle="->", color="#4CAF50", lw=1.5),
)

# Discount annotation
discount = current_price - effective_price
ax.annotate(
    f"Discount vs Market: ${discount:.2f}\n({discount/current_price*100:.1f}%)",
    xy=(80, -15),
    fontsize=10, fontweight="bold", color="#3F51B5",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#E8EAF6", alpha=0.8),
)

# Labels and formatting
ax.set_title("Cash-Secured Put vs Buying Stock", fontsize=14, fontweight="bold")
ax.set_xlabel("Stock Price at Expiration ($)", fontsize=12)
ax.set_ylabel("Profit / Loss ($)", fontsize=12)
ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(60, 130)
ax.set_ylim(-35, 35)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week28_cash_secured_put.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week28_cash_secured_put.png")
