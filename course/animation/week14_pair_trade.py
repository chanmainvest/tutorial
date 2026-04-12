"""
Week 14 - Pair Trading Visualization
=====================================
Two correlated stock price lines (Stock A and Stock B) showing
divergence and convergence, with profit area shaded.
Output: week14_pair_trade.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Generate synthetic correlated stock prices
# ---------------------------------------------------------------------------
np.random.seed(42)
days = 252  # one trading year
t = np.arange(days)

# Common market factor
market = np.cumsum(np.random.randn(days) * 0.3)

# Stock A follows market closely
stock_a = 100 + market + np.cumsum(np.random.randn(days) * 0.15)

# Stock B follows market but with a temporary divergence in the middle
divergence = np.zeros(days)
# Create divergence: Stock B drops away from Stock A then converges back
divergence[80:130] = np.linspace(0, -8, 50)   # diverge
divergence[130:180] = np.linspace(-8, 0, 50)   # converge
stock_b = 100 + market + np.cumsum(np.random.randn(days) * 0.15) + divergence

# ---------------------------------------------------------------------------
# 2. Compute the spread
# ---------------------------------------------------------------------------
spread = stock_a - stock_b

# ---------------------------------------------------------------------------
# 3. Plot
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8),
                                gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Pair Trading: Divergence & Convergence',
             fontsize=16, fontweight='bold', y=0.97)

# -- Top panel: stock prices --
ax1.plot(t, stock_a, color='#2196F3', linewidth=2, label='Stock A')
ax1.plot(t, stock_b, color='#FF5722', linewidth=2, label='Stock B')

# Shade the divergence region where profit is captured
entry_day = 100   # approximate entry after spread widens
exit_day  = 170   # approximate exit when spread narrows
ax1.axvspan(entry_day, exit_day, alpha=0.12, color='green',
            label='Trade Window')

# Annotations
ax1.annotate('Spread widens\n(Enter trade)',
             xy=(entry_day, stock_b[entry_day]),
             xytext=(entry_day - 40, stock_b[entry_day] - 6),
             fontsize=10, color='green',
             arrowprops=dict(arrowstyle='->', color='green'))
ax1.annotate('Spread narrows\n(Exit trade)',
             xy=(exit_day, stock_b[exit_day]),
             xytext=(exit_day + 10, stock_b[exit_day] - 6),
             fontsize=10, color='green',
             arrowprops=dict(arrowstyle='->', color='green'))

ax1.set_ylabel('Price ($)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.set_title('Stock A vs Stock B (Correlated Pair)', fontsize=13)
ax1.grid(True, alpha=0.3)

# -- Bottom panel: spread --
ax2.plot(t, spread, color='purple', linewidth=1.5)
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
mean_spread = np.mean(spread)
std_spread  = np.std(spread)
ax2.axhline(y=mean_spread, color='blue', linestyle=':', linewidth=1,
            label=f'Mean = {mean_spread:.1f}')
ax2.axhline(y=mean_spread + 2 * std_spread, color='red', linestyle=':',
            linewidth=1, label='+2 Std Dev')
ax2.axhline(y=mean_spread - 2 * std_spread, color='red', linestyle=':',
            linewidth=1, label='-2 Std Dev')

# Shade the profit area in the spread chart
ax2.fill_between(t[entry_day:exit_day], spread[entry_day:exit_day],
                 mean_spread, alpha=0.25, color='green', label='Profit Area')

ax2.set_xlabel('Trading Days', fontsize=12)
ax2.set_ylabel('Spread ($)', fontsize=12)
ax2.set_title('Price Spread (Stock A - Stock B)', fontsize=13)
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# ---------------------------------------------------------------------------
# 4. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__), 'week14_pair_trade.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
