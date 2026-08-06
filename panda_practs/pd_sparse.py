import pandas as pd
import numpy as np 

# Sparse structures store data in a compressed format. Useful for large databases that have lots of repeated values (like NaN)
arr = np.random.randn(21)
arr[2:-2] = np.nan

# Convert to sparse series
sparse_series = pd.Series(pd.arrays.SparseArray(arr))

print("Output sparse Series:\n",sparse_series)
print("DataType of the Series:",sparse_series.dtype)


print("--------------------------------------------------------------")
# Converting sparse array to dense
# Create sparse array
df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
df.iloc[:5] = np.nan
#print(df)

# Sparse object
sparse_df = df.astype(pd.SparseDtype("float", np.nan))
print("Sparse Object:\n",sparse_df.dtypes)

# Dense output (corverting to dense form)
dense_result = sparse_df.sparse.to_dense()
print("\nOutput Dense:\n", dense_result.dtypes)


# Memory usage check
#df.info(memory_usage="deep") # Detailed summary of the dataframe. It shows the true memory usage at the bottom (memory usage: 288.0 bytes)

#print(df.memory_usage(deep=True)) # shows the exact byte count for each individual column and the index

 