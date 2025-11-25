import matplotlib.pyplot as plt
import numpy as np

# basic stem plot
plt.figure()
x = [1,2,3,4,5]
y = [4,6,9,12,17]

plt.stem(x, y, linefmt='c--', markerfmt='^b', basefmt='r-', orientation='horizontal')
plt.title("Basic Stem Plot")

# sinusoidal stem plot
plt.figure()
sinusoidal_varX = np.linspace(0, 2 * np.pi, 45)
sinusoidal_varY = np.sin(sinusoidal_varX)

plt.stem(sinusoidal_varX, sinusoidal_varY, linefmt='b-', markerfmt='D', basefmt='r-')
plt.title("Sinusoidal Stem Plot")


# Example: Number of cars passing through a particular road intersection each hour of the day
plt.figure()
hours = np.arange(24)
num_of_cars = [5,10,15,25,22,20,18,23,30,35,40,45,50,55,60,65,70,75,80,85,80,75,65,55]

plt.stem(hours, num_of_cars, basefmt='r-')
plt.title("Traffic volume over 24 hours")
plt.xlabel("Hour of the day")
plt.ylabel("Number of cars passing through")
plt.show()