import matplotlib.pyplot as plt

# Interactive cursor  
def my_cursor(event):
    if event.inaxes:                    # Checks if the cursor is within the plot area
        x, y = event.xdata, event.ydata          # Get cursor position
        print(f"Cursor at x={x:.2f}, y={y:.2f}")    # Display coordinates

plt.figure()
plt.plot([1,2,3], [4,5,6])

plt.connect('motion_notify_event', my_cursor)
plt.show()

