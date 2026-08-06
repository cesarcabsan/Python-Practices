# Similar to list comprehensions, generator expressions with parentheses () can be used to create generators

# List comprehension (Eager evaluation - Loads everything into memory)
list_comp = [x * x for x in range(8)]
print(list_comp)

# Generator expression (Lazy evaluation - Yields elements on demand)
gen_exp = (x * x for x in range(8))
print(gen_exp)
print(list(gen_exp))

