height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))
height = height/100 
BMI = weight/(height*height)
print("Body mass:", BMI)

if BMI > 0:
    if BMI <= 16:
        print("You're pretty underweight")
    elif BMI <= 18.5:
        print("You're underweight")
    elif BMI <= 24.9:
        print("You're Healthy")
    elif BMI <= 30:
        print("You're overweight")
    else:
        print("You're obese")
else:
    print("Please share your details")
