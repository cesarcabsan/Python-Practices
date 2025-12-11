import pandas as pd
import numpy as np

indx = pd.date_range("2026-01-01", periods=10, freq="D")
data = np.random.default_rng(2).integers(0, 10, 10).astype(np.float64)
s = pd.Series(data, index=indx)
s.iloc[[1, 2, 5, 6, 9]] = np.nan

print("Original Series:")
print(s)

result = s.interpolate(method="time")

print("\nResultant Time Series after applying the interpolation:")
print(result)