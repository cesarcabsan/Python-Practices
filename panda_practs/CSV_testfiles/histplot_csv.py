import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\data.csv")

df["Duration"].plot(kind="hist", color="orange")
plt.title("Pandas histogram plot")
plt.xlabel("Frequency")
 
plt.show()