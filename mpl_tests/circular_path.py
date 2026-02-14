import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

# Circle path

# Define the angles
theta = np.linspace(0, 2 * np.pi, 100)

# Define the vertices
vertices = np.column_stack([np.cos(theta), np.sin(theta)])

# Define the codes
codes = [Path.MOVETO] + [Path.LINETO] * (len(vertices) - 1)

# Create circle path
path = Path(vertices, codes)

# Plotting path
fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='none', lw=3)
ax.add_patch(patch)
ax.set_title('Circle Path')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True)
plt.show()