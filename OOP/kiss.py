#KISS (Keep it simple, stupid)

#Calculator (Instead of creating a complex structure with sophisticated classes and interfaces, we can opt for a simple solution using direct functions or methods to perform basic operations)
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        print("Cannot divide by zero")

#calculate the results
print(add(34, 21))
print(sub(141, 131))
print(mul(5, 3))
print(div(81, 9))

 




