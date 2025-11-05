#square list comprehension   
def square_numbers(nums):
    square_lst = []
    for num in nums:
        square_lst.append(num**2)
    return square_lst 

nums = [1,2,3,4,5,6]
result = square_numbers(nums)
print(f"Square list: {result}")

#cube list comprehension
cubes = [i**3 for i in range(5)]
print(f"Cube list: {cubes}")

#number of letters a string 
phrase = "Today its very rainy"
ys = [i for i in phrase if i == 'y']
print(len(ys))

#remove even numbers
numbers = [3,5,45,97,32,22,10,19,39,43]
result = [number for number in numbers if number % 2 != 0]
print(result)