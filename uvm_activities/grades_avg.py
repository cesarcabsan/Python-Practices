def fill_arr(n):
    grades = []
    for i in range(n):
        grade = float(input(f"Grade {i+1}: "))
        grades.append(grade)
    return grades
    
def average_cal(grades):
    return sum(grades) / len(grades)
    
# Main program
n = int(input("How many grades do you want to add for checking? "))
if n <= 0:
    print("Error")
else:
    grades = fill_arr(n)
    average = average_cal(grades)
    print(f"Average total: {average}")