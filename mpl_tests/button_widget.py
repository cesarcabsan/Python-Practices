import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def button_click(event):
    print("Button Clicked!")

plt.figure()
plt.plot([3,5,7], [2,8,5])

button_ax = plt.axes([0.7, 0.05, 0.2, 0.075]) # [left, bottom, width, height]
button = Button(button_ax, 'Click Me') # Display the button's function
button.on_clicked(button_click)
plt.show()
