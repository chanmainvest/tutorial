"""
Week 23 - Factor Returns Visualization
========================================
Line chart showing cumulative returns of Value, Momentum, Quality,
and Size factors over time.
Output: week23_factor_returns.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Generate synthetic factor return data (10 years, monthly)
# ---------------------------------------------------------------------------
np.random.seed(42)
months = 120  # 10 years
t = np.arange(months)
dates_numeric = t  # months from start

# Monthly expected returns and volatilities for each factor
factors = {
    'Value': {
        'monthly_ret': 0.004,    # ~5% annualised premium
        'monthly_vol': 0.025,
        'color': '#2196F3',
        'style': '-',
    },
    'Momentum': {
        'monthly_ret': 0.006,    # ~7.5% annualised premium
        'monthly_vol': 0.035,
        'color': '#FF5722',
        'style': '-',
    },
    'Quality': {
        'monthly_ret': 0.003,    # ~3.6% annualised premium
        'monthly_vol': 0.015,
        'color': '#4CAF50',
        'style': '-',
    },
    'Size (Small-Big)': {
        'monthly_ret': 0.002,    # ~2.4% annualised premium
        'monthly_vol': 0.030,
        'color': '#9C27B0',
        'style': '-',
    },
}

# Add regime effects: value does poorly mid-period, momentum crashes
# This creates more realistic-looking divergences
factor_data = {}
for name, params in factors.items():
    monthly_returns = np.random.normal(params['monthly_ret'],
                                       params['monthly_vol'], months)

    # Add regime effects for realism
    if name == 'Value':
        # Value underperforms in growth-led years (year 4-6)
        monthly_returns[36:72] -= 0.003
        # Value recovers strongly later
        monthly_returns[84:] += 0.002
    elif name == 'Momentum':
        # Momentum crash around month 60 (like 2009)
        monthly_returns[58:63] = np.array([-0.08, -0.10, -0.06, 0.04, 0.03])
        # Strong recovery after
        monthly_returns[63:75] += 0.005
    elif name == 'Quality':
        # Quality is more stable, slight boost in downturns
        monthly_returns[58:63] += 0.01

    # Cumulative return (growth of $1)
    cumulative = np.cumprod(1 + monthly_returns)
    factor_data[name] = {
        'monthly': monthly_returns,
        'cumulative': cumulative,
        'params': params,
    }

# ---------------------------------------------------------------------------
# 2. Plot
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 9),
                                gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Factor Returns: Value, Momentum, Quality & Size',
             fontsize=16, fontweight='bold', y=0.97)

# Year labels for x-axis
year_labels = [f'Y{i}' for i in range(11)]
year_ticks  = [i * 12 for i in range(11)]

# -- Top panel: cumulative returns --
for name, data in factor_data.items():
    params = data['params']
    ax1.plot(t, data['cumulative'], color=params['color'],
             linewidth=2.2, linestyle=params['style'], label=name)

    # End label
    final_val = data['cumulative'][-1]
    total_ret = (final_val - 1) * 100
    ax1.text(months + 1, final_val, f'{name}\n({total_ret:+.0f}%)',
             fontsize=9, fontweight='bold', color=params['color'],
             va='center')

ax1.axhline(y=1, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# Highlight momentum crash
ax1.axvspan(58, 63, alpha=0.1, color='red')
ax1.text(60.5, 0.85, 'Momentum\nCrash', ha='center', fontsize=8,
         color='red', fontstyle='italic')

ax1.set_ylabel('Growth of $1', fontsize=12)
ax1.set_xticks(year_ticks)
ax1.set_xticklabels(year_labels)
ax1.set_title('Cumulative Factor Returns (10 Years)', fontsize=13)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.25)
ax1.set_xlim(-2, months + 15)

# -- Bottom panel: rolling 12-month returns --
for name, data in factor_data.items():
    params = data['params']
    # Rolling 12-month return
    rolling_12m = np.full(months, np.nan)
    for i in range(12, months):
        rolling_12m[i] = (data['cumulative'][i] /
                          data['cumulative'][i - 12] - 1) * 100

    ax2.plot(t, rolling_12m, color=params['color'],
             linewidth=1.5, alpha=0.8, label=name)

ax2.axhline(y=0, color='black', linewidth=0.8)
ax2.set_xlabel('Time (Years)', fontsize=12)
ax2.set_ylabel('Rolling 12M Return (%)', fontsize=11)
ax2.set_title('Rolling 12-Month Factor Returns', fontsize=12)
ax2.set_xticks(year_ticks)
ax2.set_xticklabels(year_labels)
ax2.legend(loc='lower left', fontsize=9)
ax2.grid(True, alpha=0.25)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week23_factor_returns.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
