import matplotlib.pyplot as plt
import numpy as np

# Step plot: Type of graph that shows how values change abruptly at specific points, rather than changing continuously.

# Temperature changes throughout the day (with step plot)
plt.figure()
hours = np.array([0, 4, 9, 18, 21, 23])
temperatures = np.array([20.0, 21.0, 22.0, 21.0, 20.0, 20.0]) 
plt.step(hours, temperatures, where='post', linewidth=2, color="red")

plt.xlabel("Hour of the Day")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Changes throughout the day")
plt.grid(True)

# Time plot: graph that represents the change of a variable over a certain time period
# Measuring the temperature every hour for a day in the US (with time plot) 
plt.figure()
time_hours = np.arange(24)
temperature_f = np.array([65, 62, 95, 62, 83, 64, 63, 92, 60, 97, 68, 81, 68, 70, 80, 83, 91, 82, 66, 60, 98, 65, 89, 91])

# Creating time plot (Matplotlib does not have a separate function specifically for creating time plots, so we have to use the plot() function to generate these plots.
plt.plot(time_hours, temperature_f, marker='o')
plt.xlabel("Time(hours)")
plt.ylabel("Temperature (°F)") # For temperatures, Fahrenheit is primarly used on the US, while other countries tend to use Celsius instead.
plt.title("Temperature measurements over a day")
plt.grid(True)
plt.show()

 
