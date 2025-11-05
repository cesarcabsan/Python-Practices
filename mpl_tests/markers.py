import matplotlib.pyplot as plt

x = [3,8,2,6,3,10]
 
plt.plot(x, marker = '*', ms = 20, mec = 'k', mfc = 'c', linestyle = '--', linewidth=2.0, label="Markers for plot")

plt.title("Graph line with markers")
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.show()

