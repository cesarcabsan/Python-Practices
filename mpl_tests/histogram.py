import matplotlib.pyplot as plt
import numpy as np 

x_data = np.random.randn(1000)

plt.hist(x_data, bins=30, color='green', edgecolor='black')

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram Test')
plt.show()