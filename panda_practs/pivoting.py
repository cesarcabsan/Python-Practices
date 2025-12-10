import pandas as pd

# Pivoting is a data transformation technique that reshapes data from a "long" to a "wide" format, similar to pivot tables in Excel. It is primarly done with Pandas library

df = pd.DataFrame({"Col1": range(12),"Col2": ["A", "A", "A", "B", "B","B", "C", "C", "C", "D", "D", "D"],
                   "date": pd.to_datetime(["2024-01-03", "2024-01-04", "2024-01-05"] * 4)})
# Display the Input DataFrame
print('Original DataFrame:\n', df)
# Reshape data from the dataframe with pivot(). Values must be unique.
pivoted = df.pivot(index="date", columns="Col2", values="Col1")
print("\nPivoted dataframe:\n", pivoted)

# Pivot_table() for aggregating duplicated values.
df2 = pd.DataFrame({
    'A': ['John', 'Cody', 'Emily', 'Steven', 'Nicky'],
    'B': ['Masters', 'Graduate', 'Graduate', 'Masters', 'Graduate'],
    'C': [27, 23, 21, 23, 24]
})

table = pd.pivot_table(df2, index=['A', 'B'])
print("\nPivot table:\n", table)


 