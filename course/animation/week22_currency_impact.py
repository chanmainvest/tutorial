"""
Week 22 - Currency Impact on International Portfolio Returns
==============================================================
Bar chart showing the same international portfolio return in
local currency vs USD, demonstrating the FX impact.
Output: week22_currency_impact.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define regional data
# ---------------------------------------------------------------------------
regions = ['Japan\n(Nikkei)', 'Europe\n(STOXX 600)', 'UK\n(FTSE 100)',
           'Emerging\nMarkets', 'Australia\n(ASX 200)', 'Canada\n(TSX)']

# Returns in local currency (%)
local_returns = [18.0, 12.0, 9.0, 14.0, 10.0, 11.0]

# FX impact (currency change vs USD, negative = USD strengthened)
fx_impact = [-8.0, -5.0, -3.0, -9.0, -4.0, 2.0]

# USD returns = local return + FX impact (approximation)
usd_returns = [l + f for l, f in zip(local_returns, fx_impact)]

# ---------------------------------------------------------------------------
# 2. Plot
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9),
                                gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Currency Impact on International Portfolio Returns',
             fontsize=16, fontweight='bold', y=0.97)

x = np.arange(len(regions))
width = 0.35

# -- Top panel: side-by-side bars --
bars_local = ax1.bar(x - width / 2, local_returns, width,
                     label='Local Currency Return',
                     color='#2196F3', edgecolor='white', linewidth=1)
bars_usd   = ax1.bar(x + width / 2, usd_returns, width,
                     label='USD Return',
                     color='#FF9800', edgecolor='white', linewidth=1)

# Value labels
for bar in bars_local:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, h + 0.3,
             f'{h:.1f}%', ha='center', va='bottom', fontsize=9,
             fontweight='bold', color='#2196F3')

for bar in bars_usd:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, h + 0.3,
             f'{h:.1f}%', ha='center', va='bottom', fontsize=9,
             fontweight='bold', color='#FF9800')

# Draw arrows showing FX impact
for i in range(len(regions)):
    if fx_impact[i] != 0:
        arrow_color = '#F44336' if fx_impact[i] < 0 else '#4CAF50'
        ax1.annotate(f'{fx_impact[i]:+.0f}%',
                     xy=(x[i] + width / 2, usd_returns[i]),
                     xytext=(x[i], local_returns[i] + 2),
                     fontsize=8, fontweight='bold', color=arrow_color,
                     ha='center',
                     arrowprops=dict(arrowstyle='->', color=arrow_color,
                                     lw=1.5, ls='--'))

ax1.set_ylabel('Return (%)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(regions, fontsize=10)
ax1.legend(loc='upper right', fontsize=11)
ax1.set_title('Local Currency vs USD Returns by Region (1 Year)', fontsize=13)
ax1.grid(True, axis='y', alpha=0.25)
ax1.set_ylim(0, 24)

# -- Bottom panel: FX impact bars --
colors_fx = ['#F44336' if f < 0 else '#4CAF50' for f in fx_impact]
bars_fx = ax2.bar(x, fx_impact, 0.5, color=colors_fx, edgecolor='white',
                  linewidth=1)
ax2.axhline(y=0, color='black', linewidth=0.8)

for i, bar in enumerate(bars_fx):
    h = bar.get_height()
    offset = -1.0 if h < 0 else 0.5
    ax2.text(bar.get_x() + bar.get_width() / 2, h + offset,
             f'{fx_impact[i]:+.1f}%', ha='center', va='center',
             fontsize=9, fontweight='bold', color=colors_fx[i])

ax2.set_xlabel('Region', fontsize=12)
ax2.set_ylabel('FX Impact (%)', fontsize=11)
ax2.set_title('Currency Effect on Returns (vs USD)', fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(regions, fontsize=10)
ax2.grid(True, axis='y', alpha=0.25)

# Key insight box
insight = ("Key Insight: A strong local return can be eroded by\n"
           "currency depreciation against the USD. Japan's 18% local\n"
           "return became only 10% in USD terms due to yen weakness.")
fig.text(0.5, 0.01, insight, ha='center', fontsize=10,
         style='italic', color='#555555',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF8E1',
                   edgecolor='#FFD54F'))

plt.tight_layout(rect=[0, 0.06, 1, 0.95])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week22_currency_impact.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
