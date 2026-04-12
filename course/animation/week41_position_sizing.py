"""
Week 41 - Position Sizing: The 2% Rule
========================================
Demonstrates portfolio survival under the 2% risk-per-trade rule.
Starting with $100,000, each losing trade costs 2% of the *current*
balance. After 50 consecutive losses the portfolio still has ~$36k,
proving the rule's protective power.
Output: week41_position_sizing.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Simulation: 50 consecutive losing trades, risking 2% each time
# ---------------------------------------------------------------------------
initial_capital = 100_000
risk_per_trade = 0.02
num_trades = 50

balance = [initial_capital]
for i in range(num_trades):
    new_balance = balance[-1] * (1 - risk_per_trade)
    balance.append(new_balance)

trades = np.arange(0, num_trades + 1)
balance = np.array(balance)

# For comparison: fixed-dollar risk (2% of initial = $2,000 per trade)
fixed_risk = initial_capital * risk_per_trade  # $2,000
balance_fixed = initial_capital - trades * fixed_risk
balance_fixed = np.maximum(balance_fixed, 0)  # floor at zero

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# 2% of current balance (percentage-based)
ax.plot(trades, balance / 1000, marker="o", markersize=3, linewidth=2.2,
        color="#4CAF50", label="2% of Current Balance (% Rule)")

# Fixed $2,000 per trade (for contrast)
ax.plot(trades, balance_fixed / 1000, marker="x", markersize=3, linewidth=2.2,
        color="#F44336", linestyle="--", label="Fixed $2,000 per Trade")

# Annotate key points
ax.annotate(f"Start: $100,000", xy=(0, 100), xytext=(5, 102),
            fontsize=10, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="black"))
ax.annotate(f"After 50 losses:\n${balance[-1]:,.0f}", xy=(50, balance[-1]/1000),
            xytext=(38, 50), fontsize=10, fontweight="bold", color="#2E7D32",
            arrowprops=dict(arrowstyle="->", color="#2E7D32"))
ax.annotate(f"Wiped out at\ntrade {int(initial_capital / fixed_risk)}",
            xy=(50, 0), xytext=(38, 15), fontsize=10, fontweight="bold",
            color="#C62828",
            arrowprops=dict(arrowstyle="->", color="#C62828"))

# Formatting
ax.set_xlabel("Number of Consecutive Losing Trades", fontsize=12)
ax.set_ylabel("Portfolio Value ($k)", fontsize=12)
ax.set_title("Position Sizing: The 2% Rule Ensures Survival",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=11, loc="upper right")
ax.grid(True, alpha=0.3)
ax.set_xlim(-1, 52)
ax.set_ylim(-5, 115)

# Survival zone shading
ax.axhspan(0, 100, alpha=0.03, color="green")
ax.axhline(y=0, color="red", linewidth=1, linestyle=":")

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week41_position_sizing.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
