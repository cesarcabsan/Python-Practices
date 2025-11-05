import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 20, 100)
y = np.sin(x)

plt.plot(x,y)

plt.title("A Graph with grids")
plt.xlabel("Horizontal axis")
plt.ylabel("Vertical axis")

plt.grid()   

plt.show()