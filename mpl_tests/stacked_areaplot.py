import matplotlib.pyplot as plt

# Imagine you have data that changes over time, like sales for different products. 
# An area plot is a way to show how much each product contributes to the total sales at each point in time. It uses shaded areas to represent each product, 
# and when you stack them together, you get a visual picture of how they add up over time.
product_sales_over_time = [1, 2, 3, 4, 5]

product_A = [10, 12, 7, 14, 10]
product_B = [5, 8, 7, 10, 9]
product_C = [7, 5, 12, 10, 12]

plt.stackplot(product_sales_over_time, product_A, product_B, product_C,
              labels=['Product A', 'Product B', 'Product C'],
              colors=['skyblue', 'orange', 'limegreen'],
              alpha=0.7, baseline='zero'
            )

plt.title("Product Sales Over Time")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.legend(loc='upper right')
plt.show()