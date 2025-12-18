import pandas as pd

df = pd.read_json("C:\\Users\\cesar\\OneDrive\\Documents\\json_files\\employee_performance.json")
print(df)

# json files can be printed in a variety of orientations
print("\nColumnn orientation (Standard):\n", df.to_json()) # orient='column': Coverts each column into a key in the JSON object. It is the standard orientation for JSON files.
print("\nSplit orientation:\n", df.to_json(orient='split')) # orient='split': separates columns, index and data clearly.
print("\nIndex orientation:\n", df.to_json(orient='index')) # orient='index': shows each row as a key-value pair with its index.
print("\nValues orientation:\n", df.to_json(orient='values')) # orient='values': outputs a list of lists, where each inner list represents a row of values without any column names or index information.
print("\nRecords orientation:\n", df.to_json(orient='records')) # orient='records': Represents each row of the DataFrame as a separate JSON object within a list.
print("\nTable orientation:\n", df.to_json(orient='table')) # orient='table': Data is formmated as a table, including a 'schema' that describes the columns and their data types, along with the 'data' itself
