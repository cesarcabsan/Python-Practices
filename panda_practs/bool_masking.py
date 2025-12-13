import pandas as pd

# Scenario example: Imagine you’re managing a dataset of products in a warehouse. You want to filter for restocking needs and specific categories

product_data = {
    "product_id": [201, 202, 203, 204, 205],
    "category": ["Electronics", "Furniture", "Clothing", "Electronics", "Groceries"],
    "stock": [50, 17, 16, 25, 100],
    "supplier": ["A", "B", "C", "A", "D"]
}

df = pd.DataFrame(product_data)
print("Warehouse product data:\n", df)

# find products that are low in stock (fewer than 20 units at least).
low_stock = df[df["stock"] < 20]
print("Low on stock:\n", low_stock)

# Now suppose you want to filter for priority categories (like Electronics and Groceries) 
priority = df[df["category"].isin(["Electronics", "Groceries"])]
print("Priority categories:\n", priority)