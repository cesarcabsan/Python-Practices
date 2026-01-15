import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [2000, 2200, 2500, 1800, 2900, 5000]

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='blue', label='Monthly Sales')

# Create arrow pointer and text label near it
plt.annotate(
    'Sales Boost',
    xy=('Jun', 5000), xytext=('May', 4500),
    arrowprops=dict(facecolor='green', edgecolor='green', linewidth=2, shrink=0.05, headwidth=10),
    fontsize=12, color='green', weight='bold'
)

# Title and labels
plt.title('Arrow Demo - Sales Increase Highlight', fontsize=14)
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

