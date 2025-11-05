import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection='polar')
r = 2
rads = np.arange(0, (2 * np.pi), 0.01)
for rad in rads:
    plt.polar(rad, r, 'c.')
plt.show()
