import pandas as pd
import json

# The json_normalize() is mainly used when we are working with nested JSON structues.  

# reading json dataframe
data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}

json_data = json.dumps(data)
df_normalize = pd.json_normalize(json.loads(json_data))
print(df_normalize)

# max_level parameter
candidate_data = [
    {
        "id": 1,
        "candidate": "Roberto mathews",
        "health_index": {"bmi": 22, "blood_pressure": 130},
    },
    {"candidate": "Shane wade", "health_index": {"bmi": 28, "blood_pressure": 160}},
    {
        "id": 2,
        "candidate": "Bruce tommy",
        "health_index": {"bmi": 31, "blood_pressure": 190},
    },
]
mlevel0 = pd.json_normalize(candidate_data, max_level=0) # flattens only the first level of the JSON object (second level is retained as a key value pair)
mlevel1 = pd.json_normalize(candidate_data, max_level=1) # flatters first two levels of the JSON dataframe (shows flat table)

print(f"\nDataframe with JSON max level normalize:\nmax_level 0:\n{mlevel0}\nmax level 1:\n{mlevel1}")