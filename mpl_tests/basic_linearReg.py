import matplotlib.pyplot as plt 
import numpy as np 

# Linear regression is a type of regression where a straight line is drawn through the data points. Its used for predicting future values. 

# Data
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

m, b = np.polyfit(x,y,1)  # m = slope, b = intercept

# Fit a straight line: y = mx + b
regression_line = m * x + b  

#plotting
plt.scatter(x,y, color="blue", label="Data Points")
plt.plot(x, regression_line, color="red", label=f"Regression line: y = {m:.2f}x + {b:.2f}")

plt.title("Basic linear regression test")
plt.xlabel("x")
plt.ylabel("y")

plt.legend(loc='lower left', bbox_to_anchor=(0.90, 1))
plt.grid(linewidth=0.3)
plt.show()
