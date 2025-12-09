import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\car_data.csv")

# Scatter Plot
fig1, ax1 = plt.subplots()
df.plot(kind="scatter", x="Weight", y="CO2", color="slategrey", ax=ax1)
ax1.set_title("CO2 emissions vs Car Weight", fontweight="bold")
ax1.set_xlabel("Weight (kg)")
ax1.set_ylabel("CO2 emissions (g/km)")

# Line Plot
fig2, ax2 = plt.subplots()
df.plot(kind="line", x="Volume", y="CO2", marker="o", linestyle="-", color="teal", ax=ax2)
ax2.set_title("CO2 emissions by Engine Volume", fontweight="bold")
ax2.set_xlabel("Engine Volume (cc)")
ax2.set_ylabel("CO2 emissions (g/km)")
ax2.legend().remove()


# Bar Plot
fig3, ax3 = plt.subplots()
avg_co2 = df.groupby("Car")["CO2"].mean().sort_values()
avg_co2.plot(kind="bar", color="cornflowerblue", ax=ax3)
ax3.set_title("Average CO2 emissions by Car Brand", fontweight="bold")
ax3.set_ylabel("Average CO2 emissions (g/km)")
ax3.grid(axis='y')

plt.show()