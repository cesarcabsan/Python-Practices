import matplotlib.pyplot as plt 

# An event plot is used to display the occurrences of events over a specific period of time.

# Example: Bus arrival times (in hours of the day)
bus_line_A = [6.5, 7.0, 8.25, 9.5, 11.0, 13.0, 15.25, 17.0]
bus_line_B = [6.0, 7.5, 9.0, 10.5, 12.0, 14.0, 16.0, 18.0]

# Put the together
bus_data = [bus_line_A, bus_line_B]

# create event plot
plt.eventplot(bus_data, lineoffsets=[1,2], linelengths=0.8, colors=['yellow', 'orange'])
plt.yticks([1,2], ['Line A', 'Line B'])
plt.xlabel("Hour of day")
plt.title("Bus Arrival Times at Central Station")
plt.show()
