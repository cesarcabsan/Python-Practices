import pandas as pd

# Melting in Pandas is the process of converting a DataFrame from a wide format to a long format.
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},'B': {0: 1, 1: 3, 2: 5},'C': {0: 2, 1: 4, 2: 6}})
print("DF Before melting:\n", df)

melted = pd.melt(df, id_vars=['A'], value_vars=['B'])

print("\nMelted dataframe:\n", melted)

print("---------------------------------")

# wide_to_long() function
df2 = pd.DataFrame({'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
                    'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
                    'ht1': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
                    'ht2': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]})
print('\nInput DataFrame:\n', df2)

# the wide_to_long() method provides more control over the transformation. It's useful when the columns have a structured naming pattern that includes a suffix.
long_df = pd.wide_to_long(df2, stubnames='ht', i=['famid', 'birth'], j='age')
print('\nLong Melted DataFrame:\n', long_df)