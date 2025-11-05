import pandas as pd

# Series (one-dimensional arrays, basically a column in a table)
panda1 = [5, 3, 4, 6]
my_pdvar = pd.Series(panda1, index = ["a", "b", "c", "d"])  # use index to create labels
print(my_pdvar["c"])

print("----------------------------------------------------")
# Dataframes (two-dimensional data structures, its like a table with rows and columns)
strays_data = {
    "Stray animals": ["Cats", "Dogs"], 
    "Encountered": [32, 50]
}

df = pd.DataFrame(strays_data, index=['-', '-'])
print(df)