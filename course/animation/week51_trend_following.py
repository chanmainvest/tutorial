"""
Week 51 - Trend Following: Moving Average Crossover
=====================================================
Price chart with dual moving average crossover signals:
  - Short MA (e.g., 20-day) and Long MA (e.g., 50-day)
  - BUY signal: short MA crosses above long MA (golden cross)
  - SELL signal: short MA crosses below long MA (death cross)
Output: week51_trend_following.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Generate synthetic price data with trends
# ---------------------------------------------------------------------------
np.random.seed(15)
n_days = 300

# Create a price series with clear trend phases
returns = np.random.normal(0.0005, 0.015, n_days)

# Inject trend phases
returns[0:60] += 0.002      # uptrend
returns[60:100] -= 0.003    # downtrend
returns[100:180] += 0.002   # uptrend
returns[180:220] -= 0.004   # downtrend
returns[220:300] += 0.0015  # uptrend

price = 100 * np.exp(np.cumsum(returns))

# ---------------------------------------------------------------------------
# Calculate moving averages
# ---------------------------------------------------------------------------
short_window = 20
long_window = 50

short_ma = np.full(n_days, np.nan)
long_ma = np.full(n_days, np.nan)

for i in range(short_window - 1, n_days):
    short_ma[i] = np.mean(price[i - short_window + 1:i + 1])

for i in range(long_window - 1, n_days):
    long_ma[i] = np.mean(price[i - long_window + 1:i + 1])

# ---------------------------------------------------------------------------
# Identify crossover signals
# ---------------------------------------------------------------------------
buy_signals = []
sell_signals = []

for i in range(long_window, n_days):
    if np.isnan(short_ma[i]) or np.isnan(long_ma[i]):
        continue
    if np.isnan(short_ma[i-1]) or np.isnan(long_ma[i-1]):
        continue

    # Golden cross: short MA crosses above long MA
    if short_ma[i] > long_ma[i] and short_ma[i-1] <= long_ma[i-1]:
        buy_signals.append(i)

    # Death cross: short MA crosses below long MA
    if short_ma[i] < long_ma[i] and short_ma[i-1] >= long_ma[i-1]:
        sell_signals.append(i)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

days = np.arange(n_days)

# Price
ax.plot(days, price, color="#424242", linewidth=1.2, alpha=0.7, label="Price")

# Moving averages
ax.plot(days, short_ma, color="#2196F3", linewidth=2,
        label=f"Short MA ({short_window}-day)")
ax.plot(days, long_ma, color="#FF9800", linewidth=2,
        label=f"Long MA ({long_window}-day)")

# Buy signals (green triangles pointing up)
for idx in buy_signals:
    ax.scatter(idx, price[idx] * 0.97, marker="^", color="#4CAF50",
               s=150, zorder=5, edgecolors="black", linewidth=0.8)
    ax.annotate("BUY", xy=(idx, price[idx] * 0.96),
                xytext=(idx, price[idx] * 0.92),
                fontsize=8, fontweight="bold", color="#2E7D32", ha="center")

# Sell signals (red triangles pointing down)
for idx in sell_signals:
    ax.scatter(idx, price[idx] * 1.03, marker="v", color="#F44336",
               s=150, zorder=5, edgecolors="black", linewidth=0.8)
    ax.annotate("SELL", xy=(idx, price[idx] * 1.04),
                xytext=(idx, price[idx] * 1.08),
                fontsize=8, fontweight="bold", color="#C62828", ha="center")

# Shade regions where short MA > long MA (bullish)
valid_mask = ~np.isnan(short_ma) & ~np.isnan(long_ma)
for i in range(long_window, n_days - 1):
    if valid_mask[i] and short_ma[i] > long_ma[i]:
        ax.axvspan(i, i + 1, alpha=0.03, color="green")
    elif valid_mask[i] and short_ma[i] < long_ma[i]:
        ax.axvspan(i, i + 1, alpha=0.03, color="red")

# Legend entries for signals
ax.scatter([], [], marker="^", color="#4CAF50", s=100, label="Buy Signal (Golden Cross)")
ax.scatter([], [], marker="v", color="#F44336", s=100, label="Sell Signal (Death Cross)")

# Strategy description
props = dict(boxstyle="round,pad=0.4", facecolor="#E3F2FD", edgecolor="#1976D2", alpha=0.9)
ax.text(0.02, 0.97, "Strategy: Buy when Short MA > Long MA\n"
                     "             Sell when Short MA < Long MA",
        transform=ax.transAxes, fontsize=9, va="top", bbox=props, family="monospace")

# Formatting
ax.set_xlabel("Trading Days", fontsize=12)
ax.set_ylabel("Price ($)", fontsize=12)
ax.set_title("Trend Following: Moving Average Crossover Signals",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=9, loc="lower right")
ax.grid(True, alpha=0.3)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week51_trend_following.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
