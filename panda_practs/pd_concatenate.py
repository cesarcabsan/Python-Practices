import pandas as pd

branch_a = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April'],
    'Branch': ['A', 'A', 'A', 'A'],
    'Sales': [25000, 27000, 29000, 21000]
})


branch_b = pd.DataFrame({
    'Month': ['May', 'June', 'July', 'August'],
    'Branch': ['B', 'B', 'B',' B'],
    'Sales': [22000, 26000, 28000, 20000]
})

branch_c = pd.DataFrame({
    'Month': ['September', 'October', 'November', 'December'],
    'Branch': ['C', 'C', 'C',' C'],
    'Sales': [24000, 23000, 30000, 23000]
})

concatenate_branches = pd.concat([branch_a, branch_b, branch_c], ignore_index=True)
print(concatenate_branches)


# axes logic
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]
}

data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]
}

df0 = pd.DataFrame(data1, index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

data_concat = pd.concat([df0, df1], axis=1, join="inner", ignore_index=True) # outer keeps all columns and inner keeps the colums with the most common values
print("\nConcatenated DataFrame by Setting Logic on Axes\n", data_concat)

# group keys
index_keys = pd.concat([df0,df1], keys=['x', 'y'])
print("\nWith hierarchical index keys\n", index_keys)