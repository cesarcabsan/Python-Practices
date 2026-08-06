import pandas as pd


data = {'A': [1, 2, 3],
        'B': ['X', 'Y', 'Z'],
        'C': ["ray", None, None],
        'D': [2.0, None, 5.1]
        }
df = pd.DataFrame(data)

# Standard
df.info()  

# Verbose = False (less detailed)
#df.info(verbose=False)

# memory usage and non null count 
#df.info(memory_usage='deep', show_counts=False)

# Max cols
df.info(max_cols=3)
df.info(max_cols=4)  # If the number of columns exceeds the max_cols value, a concise summary is provided instead of a detailed description.

