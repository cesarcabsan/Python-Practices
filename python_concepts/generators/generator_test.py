# Generators are functions that can pause and resume their execution.
"""""
def my_generator():
    yield 1
    yield 2
    yield 3
# A generator mainly works with the yield keyword.

for val in my_generator():
    print(val)
"""

"""""
# Generators are useful for saving memory in large datasets
def large_sequence(n):
    for i in range(n):
        yield i

# With yield, this won't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen)) 
print(next(gen))
print(next(gen)) 
"""""

## Number yielding generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)


