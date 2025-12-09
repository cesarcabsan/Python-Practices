import pandas as pd

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\nba.csv")
print(df.head())

# stack
stacked = df.stack()
print("\nStacked DF:\n", stacked.head(26))

# unstack
unstacked = stacked.unstack()
print("\nUnstacked DF:\n", unstacked.head(10))

