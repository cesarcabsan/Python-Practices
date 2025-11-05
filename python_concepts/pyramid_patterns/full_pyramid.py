# No functions (normal way with nested for loops i, j and k)
rows = 5 
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("*", end=" ")
    print()


# with functions (no nested loops)
def print_full_pyramid(rows):
    for i in range(1, rows + 1):
        # Calculate spaces needed for centering
        spaces = "  " * (rows - i)
        # Calculate stars needed for the current row
        stars = "* " * (2 * i - 1)
        # Print the row
        print(spaces + stars)

print_full_pyramid(rows)