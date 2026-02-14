import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
 
# Make a straight line path
# Define vertices
verts = [(0,0), (1,1)]

# Define the path codes  
codes = [Path.MOVETO, Path.LINETO]

# Creating the straight line path
path = Path(verts, codes)
 
# Plotting the path
fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax.add_patch(patch)
ax.set_title('Straight Line Path')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True)
plt.show()