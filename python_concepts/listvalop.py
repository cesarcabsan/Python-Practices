
#Operating values from every number in a list (Code here is same but different operators)

#sum
numbers = [13, 26, 9, 40, 38]
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 5
print("Sum:", numbers)

#substract 
numbers = [13, 26, 9, 40, 38]
for i in range(len(numbers)):
    numbers[i] = numbers[i] - 5
print("Substraction:", numbers)

#multiply
numbers = [13, 26, 9, 40, 38]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print("Multiplication:", numbers)

#divide 
numbers = [13, 26, 9, 40, 38]
for i in range(len(numbers)):
    numbers[i] = numbers[i] / 2
print("Division:", numbers)

#Find remainder
numbers = [13, 26, 9, 40, 38]
for i in range(len(numbers)):
    numbers[i] = numbers[i] % 3
print("Remainder:", numbers)


