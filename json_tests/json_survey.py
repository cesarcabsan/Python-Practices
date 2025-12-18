import pandas as pd

# Scenario:
# The json file (survey.json) processes survey responses collected from employees during a compliance readiness assessment.
# Each participant answered a set of questions (Q1, Q2, Q3, etc.), but not all questions were mandatory.
# The goal is to flatten the nested JSON structure, handle missing answers, and add audit columns to track how many questions each person answered and whether any responses are missing.



# Step 1: Read JSON file
df = pd.read_json("C:\\Users\\cesar\\OneDrive\\Documents\\json_files\\survey.json")

# Step 2: Flatten nested 'answers'
answers_df = pd.json_normalize(df["answers"])

# Step 3: Combine user with answers
final_df = df[["user"]].join(answers_df)

# Step 4: Handle missing values
final_df = final_df.fillna("N/A")

# Step 5: Add audit columns
final_df["answered_count"] = (final_df != "N/A").sum(axis=1) - 1
final_df["has_missing"] = final_df.eq("N/A").any(axis=1)

# Step 6: Display results
print(final_df) 