# a small exercise from one of the uvm activities
total = 0.0
item_n = int(input("Enter the number of items you want to store: "))

for i in range(1, item_n + 1):
    quantity = int(input(f"Item {i} quantity:"))
    price = int(input(f"Item {i} price:"))
    
    total += quantity * price
    
    
print(f"Total pay: ${total:.2f}")

