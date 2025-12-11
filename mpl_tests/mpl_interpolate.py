import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Interpolation real life implementation example: Airline Passenger Dataset 

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, index_col="Month", parse_dates=["Month"])

# Introduce missing values
np.random.seed(0)
missing_idx = np.random.choice(df.index, size=15, replace=False)
df.loc[missing_idx, "Passengers"] = np.nan

# Plot the data with missing values
plt.figure()
plt.plot(df.index, df["Passengers"], label="Original data", linestyle="-", marker='o')
plt.title("Airline passengers with missing values")
plt.legend()
plt.xlabel("Month")
plt.ylabel("Passengers")

# apply interpolation 
plt.figure()
df_interpolation = df.interpolate(method="spline", order=3)

# Create plot with interpolation
plt.plot(df_interpolation.index, df_interpolation["Passengers"], label="Spline interpolation")
plt.plot(df.index, df["Passengers"], label="Original data", alpha=0.5)
plt.scatter(missing_idx, df_interpolation.loc[missing_idx, "Passengers"], label="Interpolated values", color="purple")
plt.title("Airline passengers with spline interpolation")
plt.legend()
plt.xlabel("Month")
plt.ylabel("Passengers")


plt.show()

