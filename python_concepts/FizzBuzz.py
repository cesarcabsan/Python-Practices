#FizzBuzz 

def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    
    elif n % 3 == 0:
        print("Fizz")

    elif n % 5 == 0:
        print("Buzz")

n = int(input("Enter a number:"))
fizzBuzz(n)

