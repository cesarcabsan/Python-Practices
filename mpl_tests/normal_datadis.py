import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(5.0, 1.0, 10000)

plt.hist(x, 100, color="purple")
plt.show()