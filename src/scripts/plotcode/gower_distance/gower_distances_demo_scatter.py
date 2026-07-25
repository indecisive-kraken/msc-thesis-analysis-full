import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Simulated 2D coordinates for 24 variables in 2 groups
np.random.seed(42)
group1 = np.random.normal(loc=[1, 1], scale=0.5, size=(24, 2))  # Group 1
group2 = np.random.normal(loc=[2.5, 2.5], scale=0.5, size=(24, 2))  # Group 2

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Plot each group's variables as scatter points
ax.scatter(group1[:, 0], group1[:, 1], color='skyblue', label='Group 1', s=60)
ax.scatter(group2[:, 0], group2[:, 1], color='salmon', label='Group 2', s=60)

# Add ellipses to indicate group spread
def add_ellipse(data, ax, color, label):
    mean = np.mean(data, axis=0)
    cov = np.cov(data.T)
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    angle = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
    width, height = 2 * np.sqrt(vals)
    ellipse = Ellipse(mean, width, height, edgecolor=color, facecolor='none', lw=2, label=label)
    ax.add_patch(ellipse)

add_ellipse(group1, ax, 'blue', 'Group 1 Ellipse')
add_ellipse(group2, ax, 'red', 'Group 2 Ellipse')

# Draw example Gower distance line between corresponding variables (e.g., Var5 in both groups)
i = 5  # Index of example variable
ax.plot(
    [group1[i, 0], group2[i, 0]],
    [group1[i, 1], group2[i, 1]],
    color='gray', linestyle='--', linewidth=2, label='Example Gower Distance'
)

# Labels and styling
ax.set_title("Variable Representation by Group with Example Gower Distance")
ax.set_xlabel("Feature Space Dimension 1")
ax.set_ylabel("Feature Space Dimension 2")
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("gower_distance_scatter.png")
