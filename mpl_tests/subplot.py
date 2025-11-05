import matplotlib.pyplot as plt
import numpy as np

#Plot 1
sub_x1 = np.array([1,2,3,4])
sub_y1 = np.array([10,20,25,30])
plt.subplot(2,2,1) #the figure has 2 rows, 2 columns, and this plot is the first plot.
plt.plot(sub_x1, sub_y1, 'b')

#plot 2
sub_x2 = np.array([1,2,3,4])
sub_y2 = np.array([30,25,20,10])
plt.subplot(2,2,2) #the figure has 2 rows, 2 columns, and this plot is the second plot.
plt.plot(sub_x2, sub_y2, 'r')

#plot3
sub_x3 = np.array([1,2,3,4])
sub_y3 = np.array([30,20,15,10])
plt.subplot(2,2,3)   #the figure has 2 rows, 2 columns, and this plot is the third plot.
plt.plot(sub_x3, sub_y3, 'y')

#plot4
sub_x4 = np.array([1,2,3,4])
sub_y4 = np.array([10,15,20,30])
plt.subplot(2,2,4) # the figure has 2 rows, 2 columns, and this plot is the fourth plot.
plt.plot(sub_x4, sub_y4, 'g')

plt.tight_layout() # avoid overlapping
plt.show()

