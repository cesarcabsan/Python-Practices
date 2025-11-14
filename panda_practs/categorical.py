import pandas as pd 

size_list = ['small', 'medium', 'large', 'medium', 'large']
## Creating categorical data type column
categorical_data = pd.Categorical(size_list)
print(categorical_data, "\n")

## Converting regular panda series to categorical series (use either astype or dtype)
# with dtype parameter inside Series
cat_series = pd.Series(size_list, dtype='category') 
print(cat_series)

"""""
# with astype
series_to_categorical = data_series.astype('category')
print(series_to_categorical)
"""""

## access categories and codes
"""""
print(data_series.cat.categories) # returns the unique categories present in the categorical variable
print(data_series.cat.codes) # returns the integer codes representing the categories for each element in the categorical variable
"""""
# Check if a categorical variable is ordered or not
ordered_categories = pd.Categorical(cat_series, categories=['small', 'medium', 'large'], ordered=True)
is_ordered = ordered_categories.ordered
print("Is it ordered? ", is_ordered, "\n")

## add new categories
new_categories = ['tiny', 'gigantic']
update_cat_series = cat_series.cat.add_categories(new_categories)
print(update_cat_series, "\n")

## Renaming categories
category_mapping = {'tiny': 'tiny size', 'small': 'small size', 'medium': 'medium size', 'large': 'large size', 'gigantic': 'gigantic size'}
rename_categories = update_cat_series.cat.rename_categories(category_mapping)
print(rename_categories, "\n")

# Remove categories
categories_to_remove = ['small', 'large']
category_series_removed = update_cat_series.cat.remove_categories(categories_to_remove)
print(category_series_removed)