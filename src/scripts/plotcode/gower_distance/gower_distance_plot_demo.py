import numpy as np
import matplotlib.pyplot as plt

# Example data: 2 groups × 24 variables
# Each row contains Gower distances (mean) per variable for a group
# Replace these with your real values
group1 = np.random.rand(24)
group2 = np.random.rand(24)

# Stack into a 2x24 matrix
data = np.vstack([group1, group2])

# Variable labels
variables = [f'Var{i+1}' for i in range(24)]

# Plotting
x = np.arange(len(variables))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 5))
bars1 = ax.bar(x - width/2, data[0], width, label='Group 1', color='skyblue')
bars2 = ax.bar(x + width/2, data[1], width, label='Group 2', color='salmon')

# Add labels
ax.set_xlabel('Variables')
ax.set_ylabel('Average Gower Distance')
ax.set_title('Per-variable Gower Distances by Group')
ax.set_xticks(x)
ax.set_xticklabels(variables, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.savefig("example_plot_gower.jpg")
