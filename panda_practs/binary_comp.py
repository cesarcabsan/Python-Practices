import pandas as pd

# Example: Reservation System Audit (Room Prices)

# Imagine you’re auditing room prices between:
# 	DataFrame A: df_prod (production) → Current prices in the live system.
# 	DataFrame B: df_compliance (reference) → Approved baseline prices from compliance.
# You want to check if the production prices deviate (higher, lower, equal, not equal).
# To do that, you're gonna to compare the prices of both dataframes by using the Pandas series's binary comparison operators.


# Production system room prices
df_prod = pd.DataFrame({
    "room_type": ["standard", "deluxe", "suite"],
    "price": [100, 180, 300]
})

# Compliance-approved baseline prices
df_compliance = pd.DataFrame({
    "room_type": ["standard", "deluxe", "suite"],
    "price": [100, 200, 280]
})

# normal way
""""
# binary comparisons
eq_check = df_prod["price"].eq(df_compliance["price"]).rename(None) # equal
gt_check = df_prod["price"].gt(df_compliance["price"]).rename(None) # lower than baseline
lt_check = df_prod["price"].lt(df_compliance["price"]).rename(None) # greater than baseline
ne_check = df_prod["price"].ne(df_compliance["price"]).rename(None) # not equal

# Output
print("Equal:\n", eq_check)
print("\nGreater than:\n", gt_check)
print("\nLower than:\n", lt_check)
print("\nNot Equal:\n", ne_check)
"""""

# Alternate option
comparison_df = pd.DataFrame({
    "room_type": df_prod["room_type"],
    "prod_price": df_prod["price"],
    "baseline_price": df_compliance["price"],
    "equal": df_prod["price"].eq(df_compliance["price"]),
    "greater_than": df_prod["price"].gt(df_compliance["price"]),
    "lower_than": df_prod["price"].lt(df_compliance["price"]),
    "not_equal": df_prod["price"].ne(df_compliance["price"]),
})

print(comparison_df)



