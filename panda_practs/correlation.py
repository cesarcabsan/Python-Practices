import pandas as pd
import numpy as np 

# Basic
data = {"Array 1": [40, 80, 110],
      "Array 2": [62.1, 48.50, 28.7],
      "Array 3": [60, 20.2, 32.10]
}

df = pd.DataFrame(data)
print(df.corr())

# correlation between two columns
two_col_corr = df["Array 1"].corr(df["Array 2"])
print(two_col_corr)

print("---------------------------------------")
# Missing values (import numpy module for this)
temp_and_sales = {"Temperature": [22, 25, 32, 28, 30],
                  "Coffee Sales": [158, 145, np.nan, np.nan, 140]
            }

df2 = pd.DataFrame(temp_and_sales)
print("With NaN Values:\n", df2)
correlation1 = df2["Temperature"].corr(df2["Coffee Sales"])
print(f"correlation: {correlation1}") # Correlation ignores empty values

# To remove NaN Values use dropna(inplace=True) argument
df2.dropna(inplace=True)
correlation2 = df2["Temperature"].corr(df2["Coffee Sales"])  
print("\nWithout NaN Values:\n", df2)
print(f"Correlation: {correlation2}") # Correlation 2 is the same as the first one, giving more proof that corr() ignores NaN values

 

 