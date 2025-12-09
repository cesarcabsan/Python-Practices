import pandas as pd

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\data.csv")
# When a dataframe has many rows, pandas will always return only the first and last 5 rows.
print(df) # The print the full dataframe, use the to_string() function

# The default display setting for the maximum number of rows shown in a Pandas DataFrame when printed is 60 
print("Default max row number:", pd.options.display.max_rows) # if a DataFrame has more than 60 rows, Pandas will truncate the display and will return only the headers and the first and last 5 rows.

# To adjust this setting and display more or fewer rows, you can use the pd.set_option(n)
pd.set_option("display.max_rows", None) # setting None allows us to return all rows from the dataframe without truncation
print("\nFull dataframe:\n", df)