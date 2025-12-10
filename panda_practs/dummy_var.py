import pandas as pd 

# Dummy variables, also known as indicator variables, are binary (0 or 1) variables created to represent categorical data numerically.

df = pd.DataFrame({"keys": list("aeeioou"), "values": range(7)})
print(df) # Input Dataframe

# Create dummy variables for the keys column
dummies = pd.get_dummies(df["keys"], prefix="Col_")
print("\nDatabase's Dummy Variables:\n", dummies)

print("----------------------------------------------------")
# Creating Categorical Variables from Dummies
df2 = pd.DataFrame({"Col_A": [1,0,1], "Col_B":[0,1,0]})
print(df2) # Input Dataframe

# # Convert the dummy variables back to categorical (use the from_dummies() function)
turn_to_categorical_series = pd.from_dummies(df2, sep="_")
print('\nResultant Categorical Variables:\n', turn_to_categorical_series)