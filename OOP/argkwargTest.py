# Args example
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3))
print(sum_numbers(1,2,3,4,5))

# kwargs example
def greet(**kwargs):
    greeting = kwargs.get("greeting", "Hello!")
    name = kwargs.get("name", "there")
    return f"{greeting}, {name}!"

print(greet(name="Cesar", greeting="Hi"))
print(greet())

# Combining args and kwargs
def create_profile(name, email, *args, **kwargs):
    profile = {
    'name': name,
    'email': email,
    'skills': args,
    'details': kwargs
    }
    return profile  

profile = create_profile(
    "Cesar Cab", "ccab@gmail.com",
    "English", "Programming",
    age=23, status="Active"
)

print(profile)