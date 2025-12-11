import pandas as pd
import numpy as np

# Interpolation is a powerful technique in Pandas that used for handling missing values (NaN) in a dataset. It estimates the missing values based on other data points of the dataset.

# Basic conceptual example
df = pd.DataFrame({"A": [1.1, np.nan, 3.5, np.nan, np.nan, np.nan, 6.2, 7.9],
                   "B": [0.25, np.nan, np.nan, 4.7, 10, 14.7, 1.3, 9.2],
})
print("Before interopolation:\n", df)

result = df.interpolate() # there are many methods for interpolation. The linear method is the default one
print("\nAfter interpolation:\n", result) 

# Note: To use the other methods, first you must have installed the scipy library (pip install scipy)
other_method = df.interpolate(method="spline", order=2, limit=1)  
print("\nUsing other method (spline):\n", other_method)


 