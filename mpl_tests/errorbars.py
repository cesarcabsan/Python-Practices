import matplotlib.pyplot as plt

# Imagine you are measuring the height of a plant every week for a month. Each time you measure, there might be a little bit of variation due to factors like changes in weather. 
# The error bar on your graph will show this range of possible values for each height measurement, giving you an idea of how confident you can be in the accuracy of your data.

# Example: plant measurement over time
x = [1, 2, 3, 4]
y = [10, 12, 11, 13]
y_error = [0.5, 0.3, 0.4, 0.6]

plt.errorbar(x, y, yerr=y_error, fmt='o', label='Plant Height', capsize=5, color='green')

plt.title("Plant Height measurement over time")
plt.xlabel("Weeks")
plt.ylabel("Height(cm)")
plt.legend(loc='upper left')
plt.show()