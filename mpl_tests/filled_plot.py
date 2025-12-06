import matplotlib.pyplot as plt
import numpy as np

# sine wave
plt.figure()
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)
plt.plot(x,y, color="blue")
plt.title('Sine Wave')
plt.fill(x, y, "lightblue")


# Conditionals (using the where parameter)
plt.figure()
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x,y, label='sin(x)')
plt.fill_between(x,y, where=(y > 0), color='green', alpha=0.3, label='y > 0')
plt.fill_between(x,y, where=(y < 0), color='red', alpha=0.3, label='y < 0')

plt.title("Conditional (where parameter)")
plt.legend()


# Two lines 
plt.figure()
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')  
plt.plot(x, y2, label='cos(x)')

plt.fill_between(x, y1, y2, where=(y1 >= y2), facecolor='yellow', alpha=0.3, hatch='/', label='sin(x) >= cos(x)')
plt.fill_between(x, y1, y2, where=(y1 < y2), facecolor='orange', alpha=0.3, hatch='\\', label='sin(x) < cos(x)')

plt.title('Filled Plot between Two Lines')
plt.legend()


# Confidence interval
plt.figure()
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_upper = y + 0.2
y_lower = y - 0.2

plt.plot(x,y, label='Mean (sin(x))', color='purple')
plt.fill_between(x,y, y_upper, y_lower, color='purple', alpha=0.3, label="Confidence interval")

plt.title("Confidence Interval Visualization with plt.fill_between()")
plt.legend()


# Display the plots
plt.show()