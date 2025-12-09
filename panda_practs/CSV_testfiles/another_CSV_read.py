import pandas as pd

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\people_data.csv", usecols=["First Name", "Email", "Job Title"])
print(df)


 