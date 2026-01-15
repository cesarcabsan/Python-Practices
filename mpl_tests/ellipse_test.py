import matplotlib.pyplot as plt
import matplotlib.patches as patches

# An ellipse is a geometric shape that looks like a slightly stretched circle. It has a curved outline, and unlike a circle, it has two different diameters; 
# a longer one called the major axis and a shorter one called the minor axis. The center of the ellipse is a point around which the shape is symmetrically balanced.
fig, ax = plt.subplots()

# Ellipses
ellipse1 = patches.Ellipse((0, 0), 3, 2, edgecolor='brown', facecolor='yellow', alpha=0.1)
ellipse2 = patches.Ellipse((0, 0), 2, 4, angle=60, edgecolor='gold', facecolor='none')

ax.add_patch(ellipse1)
ax.add_patch(ellipse2)

plt.title('Ellipse Circles')
plt.axis('equal') 
plt.show()