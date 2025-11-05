import pandas as pd

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\data_badcal.csv")
print(df)

df.loc[5, "Duration"] = 45  # the original duration in that index was 450, which is inconsistent with the csv's duration ranges from 30 to 60. 

df.dropna(subset=['Date'], inplace=True) # remove rows with empty values

# values can also be modified by looping through them, this is mostly recommended for bigger data sets
for x in df.index:
    if df.loc[x, "Pulse"] < 100:
        df.drop(x, inplace=True)

print("\nUpdated Dataframe:\n", df)
  
 