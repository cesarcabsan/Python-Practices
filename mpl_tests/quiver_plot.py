import matplotlib.pyplot as plt
import numpy as np
# type of graph used to visualize vector fields, which represent both direction and magnitude. 
# In simple terms, it shows arrows on a grid, where each arrow represents a vector pointing in a specific direction with a certain length.

# Basic quiver plot 
plt.figure()
x = [0,0]
y = [0,0]
x_direct = [1,0]
y_direct = [1,-1]

plt.quiver(x, y, x_direct, y_direct, scale=5, color='blue')
plt.title("Basic Quiver Plot with Two Arrows")

 
# Meshgrid (visually represents evenly spaced vectors as distinct arrows.)
fig, ax = plt.subplots()
x_mgrid = np.arange(0, 2.2, 0.2)
y_mgrid = np.arange(0, 2.2, 0.2)

X, Y = np.meshgrid(x_mgrid, y_mgrid)
u = np.cos(X)*Y
v = np.sin(Y)*Y

ax.quiver(X,Y,u,v)
ax.axis([-0.3, 2.3, -0.3, 2.3])
ax.set_aspect('equal')
ax.set_title("Meshgrive Quiver Plot")


# Gradient (represents a visualization of a vector field with a changing gradient in a 2D space.)
plt.figure()
x_grad = np.arange(-2, 2, 0.1)
y_grad = np.arange(-2, 2, 0.1)
 
X, Y = np.meshgrid(x_grad, y_grad)
z = np.sin(X) * np.cos(Y)
dx, dy = np.gradient(z)

plt.quiver(X, Y, dx, dy)

plt.title("Gradient Quiver Plot")


# Colored (Arrows are represented in different colors. The color of the arrows depends on specific parameters such as distance from origin, strength, or direction.)
plt.figure()
x_colored = np.arange(0, 2 * np.pi + 2 * np.pi / 20, 2 * np.pi / 20)
y_colored = np.arange(0, 2 * np.pi + 2 * np.pi / 20, 2 * np.pi / 20)
X, Y = np.meshgrid(x_colored, y_colored)
u_colored = np.cos(X) * np.sin(Y)
v_colored = np.sin(X) * np.cos(Y) 

color = np.sqrt(u_colored**2 * v_colored**2)

plt.quiver(X,Y, u_colored, v_colored, color, alpha=1, cmap='viridis')
plt.title("Colored Quiver Plot")


plt.show()
