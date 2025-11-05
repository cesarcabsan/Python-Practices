import pandas as pd

data = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\employees.csv")
print(data)
# replacing blank spaces with '_'
# Note: The Dataframe.query() method only works if the column name doesn't have any empty spaces.
data.columns = [column.replace(" ", "_") for column in data.columns]

## filtering with query method
# filtering one column
data.query("Senior_Management == True", inplace=True)
print("Single column filtering:\n", data)
 
# filtering multiple columns
data.query('Senior_Management == True '
           'and Gender == "Male" '
           'and Team == "Marketing" '
           'and First_Name == "Johnny"', inplace=True)
print("Multiple column filtering:\n", data)

 