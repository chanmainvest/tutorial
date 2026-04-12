"""
Week 15 - Efficient Frontier Visualization
============================================
Classic efficient frontier curve with individual assets as dots
and the curve showing optimal portfolios.
Output: week15_efficient_frontier.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define individual assets (expected return, std dev)
# ---------------------------------------------------------------------------
assets = {
    'Bonds':        (0.04, 0.05),
    'Large Cap':    (0.10, 0.15),
    'Small Cap':    (0.12, 0.20),
    'Intl Equity':  (0.09, 0.18),
    'Real Estate':  (0.08, 0.14),
    'Commodities':  (0.06, 0.22),
    'Tech':         (0.14, 0.25),
}

# ---------------------------------------------------------------------------
# 2. Simulate random portfolios to trace the frontier
# ---------------------------------------------------------------------------
np.random.seed(42)
n_assets = len(assets)
returns = np.array([v[0] for v in assets.values()])
stds    = np.array([v[1] for v in assets.values()])

# Approximate correlation matrix (simplified)
corr = np.array([
    [1.0,  0.2,  0.1,  0.15, 0.25, 0.05, 0.1 ],
    [0.2,  1.0,  0.8,  0.6,  0.5,  0.3,  0.7 ],
    [0.1,  0.8,  1.0,  0.5,  0.4,  0.2,  0.65],
    [0.15, 0.6,  0.5,  1.0,  0.35, 0.25, 0.5 ],
    [0.25, 0.5,  0.4,  0.35, 1.0,  0.2,  0.3 ],
    [0.05, 0.3,  0.2,  0.25, 0.2,  1.0,  0.15],
    [0.1,  0.7,  0.65, 0.5,  0.3,  0.15, 1.0 ],
])

# Covariance matrix from correlation and individual stds
cov = np.outer(stds, stds) * corr

n_portfolios = 8000
port_returns = []
port_risks   = []
port_sharpe  = []
risk_free    = 0.03  # risk-free rate

for _ in range(n_portfolios):
    weights = np.random.dirichlet(np.ones(n_assets))
    p_ret   = np.dot(weights, returns)
    p_var   = np.dot(weights, cov @ weights)
    p_std   = np.sqrt(p_var)
    p_sharpe = (p_ret - risk_free) / p_std
    port_returns.append(p_ret)
    port_risks.append(p_std)
    port_sharpe.append(p_sharpe)

port_returns = np.array(port_returns)
port_risks   = np.array(port_risks)
port_sharpe  = np.array(port_sharpe)

# ---------------------------------------------------------------------------
# 3. Find key portfolios
# ---------------------------------------------------------------------------
# Maximum Sharpe ratio portfolio
idx_max_sharpe = np.argmax(port_sharpe)
# Minimum variance portfolio
idx_min_var    = np.argmin(port_risks)

# ---------------------------------------------------------------------------
# 4. Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 8))

# Scatter all portfolios coloured by Sharpe ratio
scatter = ax.scatter(port_risks * 100, port_returns * 100,
                     c=port_sharpe, cmap='viridis', s=6, alpha=0.5,
                     edgecolors='none')
cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label('Sharpe Ratio', fontsize=11)

# Plot individual assets
for name, (r, s) in assets.items():
    ax.scatter(s * 100, r * 100, marker='D', s=100, zorder=5,
               edgecolors='black', linewidths=1.2, color='white')
    ax.annotate(name, (s * 100, r * 100),
                textcoords="offset points", xytext=(8, 4),
                fontsize=9, fontweight='bold')

# Highlight max-Sharpe portfolio
ax.scatter(port_risks[idx_max_sharpe] * 100,
           port_returns[idx_max_sharpe] * 100,
           marker='*', s=350, color='red', zorder=6,
           edgecolors='black', linewidths=1,
           label=f'Max Sharpe ({port_sharpe[idx_max_sharpe]:.2f})')

# Highlight min-variance portfolio
ax.scatter(port_risks[idx_min_var] * 100,
           port_returns[idx_min_var] * 100,
           marker='*', s=350, color='gold', zorder=6,
           edgecolors='black', linewidths=1,
           label='Min Variance')

# Capital Market Line (CML)
cml_x = np.linspace(0, port_risks.max() * 100, 100)
cml_slope = (port_returns[idx_max_sharpe] - risk_free) / port_risks[idx_max_sharpe]
cml_y = risk_free * 100 + cml_slope * cml_x
ax.plot(cml_x, cml_y, color='red', linestyle='--', linewidth=1.5,
        label='Capital Market Line')

# Risk-free rate point
ax.scatter(0, risk_free * 100, marker='o', s=100, color='red', zorder=6)
ax.annotate(f'Risk-Free\n({risk_free*100:.0f}%)',
            (0, risk_free * 100),
            textcoords="offset points", xytext=(10, -15), fontsize=9)

ax.set_xlabel('Risk (Standard Deviation %)', fontsize=13)
ax.set_ylabel('Expected Return (%)', fontsize=13)
ax.set_title('Efficient Frontier & Capital Market Line',
             fontsize=15, fontweight='bold')
ax.legend(loc='lower right', fontsize=10)
ax.set_xlim(0, 28)
ax.set_ylim(2, 16)
ax.grid(True, alpha=0.3)

plt.tight_layout()

# ---------------------------------------------------------------------------
# 5. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week15_efficient_frontier.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
