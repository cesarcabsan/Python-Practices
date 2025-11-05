import matplotlib.pyplot as plt
import numpy as np

#Basic plot (lines)
x = np.array([1, 4, 6, 6])
y = np.array([3, 8, 2, 10])

plt.plot(x, y, marker='o')   ## if you want to show points and not lines, use the 'o' parameter (if you want to show both, use marker = 'o' or any symbol like *)

plt.title("Basic plot (with line)")
plt.xlabel("Horizontal axis")
plt.ylabel("Vertical axis")

plt.show()