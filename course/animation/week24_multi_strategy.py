"""
Week 24 - Multi-Strategy Correlation Matrix
=============================================
Correlation matrix heatmap showing low correlation between
different investment strategies, demonstrating diversification benefit.
Output: week24_multi_strategy.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define strategies and their correlation matrix
# ---------------------------------------------------------------------------
strategies = [
    'Long/Short\nEquity',
    'Global\nMacro',
    'Trend\nFollowing',
    'Merger\nArbitrage',
    'Fixed Income\nArbitrage',
    'Market\nNeutral',
    'Distressed\nDebt',
    'Volatility\nTrading',
]

n = len(strategies)

# Construct a realistic correlation matrix
# Most hedge fund strategies have low cross-correlation
corr_matrix = np.array([
    [ 1.00,  0.25,  0.10,  0.35,  0.15,  0.05,  0.30,  0.10],  # L/S Equity
    [ 0.25,  1.00,  0.30, -0.05,  0.20,  0.10,  0.05,  0.15],  # Global Macro
    [ 0.10,  0.30,  1.00, -0.10,  0.05,  0.00, -0.05,  0.20],  # Trend
    [ 0.35, -0.05, -0.10,  1.00,  0.25,  0.15,  0.40, -0.10],  # Merger Arb
    [ 0.15,  0.20,  0.05,  0.25,  1.00,  0.10,  0.20,  0.05],  # FI Arb
    [ 0.05,  0.10,  0.00,  0.15,  0.10,  1.00,  0.10, -0.05],  # Mkt Neutral
    [ 0.30,  0.05, -0.05,  0.40,  0.20,  0.10,  1.00,  0.00],  # Distressed
    [ 0.10,  0.15,  0.20, -0.10,  0.05, -0.05,  0.00,  1.00],  # Vol Trading
])

# ---------------------------------------------------------------------------
# 2. Plot
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7),
                                gridspec_kw={'width_ratios': [3, 1]})
fig.suptitle('Multi-Strategy Portfolio: Correlation Matrix',
             fontsize=16, fontweight='bold')

# -- Left panel: heatmap --
im = ax1.imshow(corr_matrix, cmap='RdYlGn_r', vmin=-0.5, vmax=1.0,
                aspect='equal')

# Add text annotations in each cell
for i in range(n):
    for j in range(n):
        value = corr_matrix[i, j]
        text_color = 'white' if abs(value) > 0.35 else 'black'
        ax1.text(j, i, f'{value:.2f}', ha='center', va='center',
                 fontsize=9, fontweight='bold', color=text_color)

ax1.set_xticks(range(n))
ax1.set_yticks(range(n))
ax1.set_xticklabels(strategies, fontsize=8.5, rotation=45, ha='right')
ax1.set_yticklabels(strategies, fontsize=8.5)
ax1.set_title('Pairwise Correlation Between Strategies', fontsize=13)

# Colorbar
cbar = plt.colorbar(im, ax=ax1, shrink=0.8, pad=0.02)
cbar.set_label('Correlation', fontsize=11)

# -- Right panel: average correlation summary --
avg_corr = []
for i in range(n):
    # Average absolute correlation with other strategies (exclude self)
    other_corrs = [abs(corr_matrix[i, j]) for j in range(n) if i != j]
    avg_corr.append(np.mean(other_corrs))

y_pos = np.arange(n)
short_names = ['L/S Equity', 'Global Macro', 'Trend', 'Merger Arb',
               'FI Arb', 'Mkt Neutral', 'Distressed', 'Vol Trading']

colors = ['#4CAF50' if a < 0.15 else '#FF9800' if a < 0.25 else '#F44336'
          for a in avg_corr]

bars = ax2.barh(y_pos, avg_corr, 0.6, color=colors,
                edgecolor='white', linewidth=1)

for i, (bar, ac) in enumerate(zip(bars, avg_corr)):
    ax2.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
             f'{ac:.2f}', ha='left', va='center', fontsize=9,
             fontweight='bold', color=colors[i])

ax2.set_yticks(y_pos)
ax2.set_yticklabels(short_names, fontsize=9)
ax2.set_xlabel('Avg |Correlation|', fontsize=11)
ax2.set_title('Diversification Score\n(lower = better)', fontsize=12)
ax2.set_xlim(0, 0.35)
ax2.grid(True, axis='x', alpha=0.25)
ax2.invert_yaxis()

# Add legend for the color coding
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#4CAF50', label='Low (<0.15) - Best diversifier'),
    Patch(facecolor='#FF9800', label='Medium (0.15-0.25)'),
    Patch(facecolor='#F44336', label='Higher (>0.25)'),
]
ax2.legend(handles=legend_elements, loc='lower right', fontsize=8)

# Portfolio-level insight
avg_all = np.mean(np.abs(corr_matrix[np.triu_indices(n, k=1)]))
fig.text(0.5, 0.01,
         f'Average pairwise |correlation|: {avg_all:.2f} -- '
         f'Low cross-correlation enables smoother combined portfolio returns',
         ha='center', fontsize=10, style='italic', color='#555555')

plt.tight_layout(rect=[0, 0.04, 1, 0.95])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week24_multi_strategy.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
