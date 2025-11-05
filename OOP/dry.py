#D.R.Y (Dont Repeat Yourself)

# Code Without DRY.
'''
length1 = 5
width1 = 10
area1 = length1 * width1
length2 = 7
width2 = 3
area2 = length2 * width2
print(f"Area1: {area1}")
print(f"Area2: {area2}")
'''
# Feels repetitive?, Here's where we apply DRY.
def calculate_rec_area(length, width):
    return length * width

area1 = calculate_rec_area(5, 10)
area2 = calculate_rec_area(7, 3)
print(f"Area1: {area1}")
print(f"Area2: {area2}")
# Both codes have the same output, but the one with the function follows the DRY principle by decreasing code repetition.


# Printing name example
def greet(name):
    print(f"Hello {name}!, nice to meet you")

greet("John")
greet("Emily")
greet("Mike")

