import pandas as pd

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\salary.csv")
new_df = df.dropna()
print("New dataframe:\n", new_df) # Dropna returns a new dataframe that removes all empty values.   
print("\nOriginal dataframe:\n", df) # the dropna() function won't modify the original dataframe.

#To actually modify the dataframe, you have to use the inplace=True argument.
""""
df.dropna(inplace=True)
print(df.to_string())
"""

# You can fill up empty values with the fillna() function
df.fillna({"Salary": 43000}, inplace=True)
df.loc[5, "Salary"] = 46000 # but if you want an specific cell to have a different value instead
print("\nDataframe with new added values:\n", df)

# To remove duplicates, use the drop_duplicates() function. 
df.drop_duplicates(subset=["Salary"], inplace=True) # To delete from specific column, use the subset=["column_name"] argument
print("\nRemoved duplicate values:\n", df)