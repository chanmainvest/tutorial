"""
Week 25 - Option Payoff Diagrams
==================================
Classic option payoff diagrams in a 2x2 grid:
  Long Call, Long Put, Short Call, Short Put.
Output: week25_option_payoff.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Parameters
# ---------------------------------------------------------------------------
strike = 100        # strike price
premium = 5         # option premium
stock_range = np.linspace(70, 130, 300)

# ---------------------------------------------------------------------------
# 2. Payoff functions (profit = payoff - premium paid/received)
# ---------------------------------------------------------------------------
def long_call_profit(S, K, p):
    """Long call: pay premium, profit when S > K + p"""
    return np.maximum(S - K, 0) - p

def long_put_profit(S, K, p):
    """Long put: pay premium, profit when S < K - p"""
    return np.maximum(K - S, 0) - p

def short_call_profit(S, K, p):
    """Short call: receive premium, lose when S > K + p"""
    return -(np.maximum(S - K, 0)) + p

def short_put_profit(S, K, p):
    """Short put: receive premium, lose when S < K - p"""
    return -(np.maximum(K - S, 0)) + p

payoffs = [
    ('Long Call', long_call_profit, '#2196F3',
     f'Buy right to purchase at ${strike}\nMax loss: ${premium} (premium paid)\n'
     f'Breakeven: ${strike + premium}'),
    ('Long Put', long_put_profit, '#4CAF50',
     f'Buy right to sell at ${strike}\nMax loss: ${premium} (premium paid)\n'
     f'Breakeven: ${strike - premium}'),
    ('Short Call', short_call_profit, '#FF5722',
     f'Sell obligation to deliver at ${strike}\nMax gain: ${premium} (premium received)\n'
     f'Breakeven: ${strike + premium}'),
    ('Short Put', short_put_profit, '#9C27B0',
     f'Sell obligation to buy at ${strike}\nMax gain: ${premium} (premium received)\n'
     f'Breakeven: ${strike - premium}'),
]

# ---------------------------------------------------------------------------
# 3. Plot 2x2 grid
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10), sharex=True, sharey=True)
fig.suptitle('Option Payoff Diagrams at Expiration',
             fontsize=16, fontweight='bold', y=0.97)

for ax, (title, func, color, info) in zip(axes.flat, payoffs):
    profit = func(stock_range, strike, premium)

    # Plot profit/loss line
    ax.plot(stock_range, profit, color=color, linewidth=2.5, zorder=3)

    # Shade profit (green) and loss (red) regions
    ax.fill_between(stock_range, profit, 0,
                    where=(profit >= 0), alpha=0.15, color='green',
                    interpolate=True)
    ax.fill_between(stock_range, profit, 0,
                    where=(profit < 0), alpha=0.12, color='red',
                    interpolate=True)

    # Zero line
    ax.axhline(y=0, color='black', linewidth=0.8)

    # Strike price line
    ax.axvline(x=strike, color='gray', linestyle='--', linewidth=1,
               alpha=0.6)
    ax.text(strike + 0.5, ax.get_ylim()[0] if ax.get_ylim()[0] != 0 else -20,
            f'K={strike}', fontsize=8, color='gray', va='bottom')

    # Breakeven marker
    # Find where profit crosses zero
    zero_crossings = np.where(np.diff(np.sign(profit)))[0]
    for zc in zero_crossings:
        be_price = stock_range[zc]
        ax.scatter(be_price, 0, s=80, color='black', zorder=5, marker='D')
        ax.annotate(f'BE=${be_price:.0f}',
                    xy=(be_price, 0),
                    xytext=(be_price, 8 if 'Long' in title else -8),
                    fontsize=8, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color='black', lw=1))

    # Max profit/loss annotations
    if 'Long' in title:
        ax.annotate(f'Max Loss: -${premium}',
                    xy=(75, -premium), fontsize=9, color='red',
                    fontweight='bold')
    else:
        ax.annotate(f'Max Gain: +${premium}',
                    xy=(75 if 'Put' in title else 108, premium),
                    fontsize=9, color='green', fontweight='bold')

    # Info box
    ax.text(0.02, 0.98, info, transform=ax.transAxes,
            fontsize=7.5, va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f5f5f5',
                      edgecolor='#cccccc', alpha=0.9))

    ax.set_title(title, fontsize=13, fontweight='bold', color=color)
    ax.grid(True, alpha=0.2)
    ax.set_xlim(70, 130)
    ax.set_ylim(-28, 28)

# Common axis labels
for ax in axes[1]:
    ax.set_xlabel('Stock Price at Expiration ($)', fontsize=11)
for ax in axes[:, 0]:
    ax.set_ylabel('Profit / Loss ($)', fontsize=11)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# ---------------------------------------------------------------------------
# 4. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week25_option_payoff.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
