#while loop with input
'''
choice = input("You're in a loop, Do you want to leave?")

def loopLeave(choice):
    while True:
        if choice == 'y' or choice == 'Y':
            print("You broke the loop sucessfully")
            break
        elif choice == 'n' or choice == 'N':
            another_choice = input("Still on loop, please press y or Y to leave the loop ")
            if another_choice == 'y' or another_choice == 'Y':
                print("You broke the loop sucessfully")
                break
            else:
                print(another_choice)               
loopLeave(choice)
'''
#Looping over a list
felines = ['Cat', 'Lion', 'Leopard', 'Tiger', 'Panther']
for feline in felines:
    print(f"{feline} has {len(feline)} letters!")

#Looping over dictionaries
states_in_mexico = {
    'Jalisco': 'Guadalajara',
    'Tabasco': 'Villahermosa',
    'Nuevo Leon': 'Monterrey',
    'Yucatan': 'Merida' 
}
print("Lists of capitals of Mexico's given states: ")
for capital in states_in_mexico.values():
    print(capital)

#mulplication table
'''
n = int(input("Insert a number: "))
for i in range(1, 11):
    print(f"{n} x {i} =", n*i)
'''
#fibonacci sequence
'''
n_fib = int(input("How many terms do you wanna insert?: "))
n1, n2 = 0, 1
count = 0
if n_fib < 0:
    print("Please insert positive numbers")
else:
    print("Fibonacci sequence:")
    while count < n_fib:
        print(n1, end=' ')
        nth = n1 + n2
        n1 = n2 
        n2 = nth
        count += 1
'''
#Check if the number is odd or even
while True:
    num = int(input("Insert number to evalute: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    
    another_num = input("Want to value another number?")
    if another_num == 'y' or another_num == 'Y':
        print("Good, lets value if its odd or even")
    else:
        break