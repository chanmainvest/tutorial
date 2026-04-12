"""
Week 18 - Interest Rate Impact on Asset Classes
=================================================
Multi-panel chart showing how rising rates affect:
  - Bond prices (down)
  - Growth stocks (down)
  - Value stocks (less down)
  - Bank stocks (up)
Output: week18_rate_impact.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define rate scenario and asset responses
# ---------------------------------------------------------------------------
# Timeline: quarters over 2 years as rates rise
quarters = np.arange(0, 9)
quarter_labels = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']

# Federal funds rate rising from 2% to 5.5%
fed_rate = np.array([2.0, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.50])

# Cumulative price changes (indexed to 100)
bond_prices    = np.array([100, 98, 95, 92, 89, 87, 85, 84, 83])
growth_stocks  = np.array([100, 97, 93, 88, 84, 82, 80, 79, 78])
value_stocks   = np.array([100, 99, 97, 96, 95, 94, 93, 93, 94])
bank_stocks    = np.array([100, 102, 105, 108, 112, 115, 118, 120, 121])

# ---------------------------------------------------------------------------
# 2. Create multi-panel chart
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9), sharex=True)
fig.suptitle('Impact of Rising Interest Rates on Asset Classes',
             fontsize=16, fontweight='bold')

panels = [
    (axes[0, 0], bond_prices,   'Bond Prices (Aggregate Index)',
     '#F44336', 'Bonds fall as rates rise\n(inverse relationship)'),
    (axes[0, 1], growth_stocks, 'Growth Stocks',
     '#FF9800', 'High-duration equities\nhurt by higher discount rates'),
    (axes[1, 0], value_stocks,  'Value Stocks',
     '#4CAF50', 'Lower duration, less\nimpact from rate rises'),
    (axes[1, 1], bank_stocks,   'Bank / Financial Stocks',
     '#2196F3', 'Net interest margins\nexpand with higher rates'),
]

for ax, data, title, color, note in panels:
    # Price line
    ax.plot(quarters, data, color=color, linewidth=2.5, marker='o',
            markersize=6, zorder=3)

    # Shade area relative to starting value
    ax.fill_between(quarters, data, 100, alpha=0.15, color=color)

    # Reference line at 100
    ax.axhline(y=100, color='gray', linestyle='--', linewidth=0.8)

    # Change annotation
    total_change = data[-1] - 100
    sign = '+' if total_change > 0 else ''
    ax.annotate(f'{sign}{total_change:.0f}%',
                xy=(8, data[-1]), xytext=(7.2, data[-1] + 3 * np.sign(total_change)),
                fontsize=12, fontweight='bold', color=color,
                arrowprops=dict(arrowstyle='->', color=color))

    # Explanatory note
    ax.text(0.98, 0.05, note, transform=ax.transAxes,
            ha='right', va='bottom', fontsize=9, fontstyle='italic',
            color='#555555',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f9f9f9',
                      edgecolor='#dddddd'))

    ax.set_title(title, fontsize=13, fontweight='bold', color=color)
    ax.set_xticks(quarters)
    ax.set_xticklabels(quarter_labels, fontsize=9)
    ax.set_ylabel('Index Level', fontsize=10)
    ax.grid(True, alpha=0.25)

# Add rate overlay on each panel
for row in axes:
    for ax in row:
        ax2 = ax.twinx()
        ax2.plot(quarters, fed_rate, color='black', linewidth=1,
                 linestyle=':', alpha=0.4)
        ax2.set_ylabel('Fed Rate (%)', fontsize=8, color='gray')
        ax2.tick_params(axis='y', labelsize=8, colors='gray')
        ax2.set_ylim(0, 8)

# Common x-label
for ax in axes[1]:
    ax.set_xlabel('Time (Quarters)', fontsize=11)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week18_rate_impact.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
