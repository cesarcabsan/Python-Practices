import pandas as pd

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\salary.csv")

# Inspect number of missing values
print(df.isna())
print(df.isna().sum())

# Remove all empty values from list
nan_free_df = df.dropna()
print("\n Dataframe without empty values:\n", nan_free_df)

# Note: The original dataframe doesnt get modified with just df.dropna() alone. 
# To do that, you need to use the inplace = True argument inside it.
print("\nOriginal dataframe:\n", df) 

print("---------------------------------------")

# Alternative: add values to the empty cells
df['Salary'] = df['Salary'].fillna(df['Salary'].median())   
print("Empty values filled (through median calculation):\n", df)