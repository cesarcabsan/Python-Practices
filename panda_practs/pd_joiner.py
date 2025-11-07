import pandas as pd

# Cooking class attendees
attendees = {
    'Name':['Lucy', 'Thomas', 'Renata', 'Isaac'],
    'Age':[34, 29, 41, 36]
}

# Dietary preferences
dietary_prefers = {
    'Preference':['Vegetarian', 'Gluten-Free', 'Vegan', 'No Dairy'],
    'Allergy':['None', 'Peanuts', 'Soy', 'None']
}

# create dataframes and set indexes
df1 = pd.DataFrame(attendees, index=['C0', 'C1', 'C2', 'C3'])
df2 = pd.DataFrame(dietary_prefers, index=['C0', 'C2', 'C3', 'C4'])

# Apply the join() function 
joined_df = df1.join(df2, how='outer') 
print(joined_df) # The join() function combines DataFrames primarily based on their indices, while the merge() function focuses on common columns
 
