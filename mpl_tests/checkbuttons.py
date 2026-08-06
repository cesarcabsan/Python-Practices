import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

fig, ax = plt.subplots()

visibility_status = [True, True, True]

line1, = ax.plot([1,2,3], [4,5,6], label='Line 1', visible=visibility_status[0])

line2, = ax.plot([5,4,1], [2,1,3], label='Line 2', visible=visibility_status[1])

line3, = ax.plot([6,5,2], [1,4,5], label='Line 3', visible=visibility_status[2])

check_ax = plt.axes([0.7, 0.05, 0.2, 0.1])
check_buttons = CheckButtons(check_ax, ['Line 1', 'Line 2', 'Line 3'], visibility_status)

# Update visibility based on checkbox state
def update_visibility(label):
    if label == 'Line 1':
        line1.set_visible(not line1.get_visible())
    elif label == 'Line 2':
        line2.set_visible(not line2.get_visible())
    elif label == 'Line 3':
        line3.set_visible(not line3.get_visible())
    plt.draw()

check_buttons.on_clicked(update_visibility)
plt.show()
