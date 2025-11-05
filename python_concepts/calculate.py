def calculation(first_num, second_num, operator):
    if operator == "+":
        return first_num + second_num
    elif operator == "-":
        return first_num - second_num
    elif operator == "*":
        return first_num * second_num 
    elif operator == "/":
        return first_num / second_num 
    elif operator == "%":
        return first_num % second_num 
    else:
        print("Sorry, I can't comprehend your operation")
        
def init():
    first_num = int(input("Enter a number"))
    operator = input("Add a math operator [+, - , *, /, %]")
    second_num = int(input("Enter another number")) 
    
    print(first_num, operator, second_num, "=", calculation(first_num, second_num, operator))

init()