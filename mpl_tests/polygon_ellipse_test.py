import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

# Create Ellipse
my_ellipse = Ellipse((0.5, 0.5), width=0.4, height=0.4, angle=40, color='blue')

# Create polygon
vertices = [
    [0.40, 0.65],  # left corner
    [0.60, 0.65],  # right corner
    [0.55, 0.75],  # top corner
    [0.45, 0.75]   # bottom corner (slight overlap for closure)
]
my_polygon = Polygon(vertices, closed=True, color='black')

# another polygon (inside the ellipse)
pol2_vertices = [[0.35, 0.45], [0.65, 0.45], [0.60, 0.40], [0.40, 0.40]]
my_pol2 = Polygon(pol2_vertices, closed=True, color='white')

# adding more 
pol3_vertices = [[0.38, 0.55], [0.42, 0.55],  [0.42, 0.60], [0.38, 0.60]]
my_pol3 = Polygon(pol3_vertices, closed=True, color='white')

pol4_vertices = [[0.58, 0.55], [0.62, 0.55],  [0.62, 0.60], [0.58, 0.60]]
my_pol4 = Polygon(pol4_vertices, closed=True, color='white')


fig, ax = plt.subplots()
ax.add_patch(my_ellipse)
ax.add_patch(my_polygon)
ax.add_patch(my_pol2)
ax.add_patch(my_pol3)
ax.add_patch(my_pol4)

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()