#inheritance classes in Python

# Printing text
class Student:
    def __init__(self, name, subject):
        self.name = name 
        self.subject = subject

    def study(self):
        pass

class Course(Student):
    def study(self):
        return f'Student {self.name} is coursing the subject {self.subject}'

student_course = Course("Matt", "Math")
print(student_course.study())

# Method overwriting
class Student:
    def work(self):
        print("Sending homework")
        
class Teacher(Student):
    def work(self):
        print("Grading homework")
        
take_homework = Teacher()
take_homework.work()

# Area of shapes
class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Trapezium(Shape):
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        return 1/2 * (self.base_a + self.base_b) * self.height 


shapes = [Rectangle(2, 3), Circle(5), Trapezium(9, 10, 8)]
for shape in shapes:
    print(f"Area: {shape.area()}")
 

#super() function
class Emp:
    def __init__(self, id, name, add):
        self.id = id
        self.name = name
        self.add = add 

class Freelance(Emp):
    def __init__(self, id, name, add, emails):
        super().__init__(id, name, add)
        self.emails = emails 

an_emp = Freelance(231, "Edgar", "Noida", "edg14@hotmail.com")
print("ID: ", an_emp.id)
print("Name: ", an_emp.name)
print("Add: ", an_emp.add)
print("Email: ", an_emp.emails)

## Multiple inheritance        
class Prey:
    def flee(self):
        print("This animal is running away")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Moose(Prey):
    pass

class Bear(Predator):
    pass 

class Fish(Moose, Bear): 
    pass

moose = Moose()
bear = Bear()
fish = Fish()
#moose.run()
#bear.hunt()
fish.flee()
fish.hunt()


# Method resolution order (MRO)
class A:
    def room(self):
        print("This is the class A room")

class B:
    def room(self):
        print("This is the class B room")

class DerivedClass(A, B):
    pass

r = DerivedClass()
r.room()

#multilevel inheritance
class SuperCl:
    def super_method(self):
        print("This is the main super class")

class DerivedCl1(SuperCl):
    def derived_method(self):
        print("This is a derived class")

class DerivedCl2(DerivedCl1):
    def sec_derived_method(self):
        print("This is another derived class")

derivate = DerivedCl2() 
#Since DerivedCl2 inherits from DerivedCl1, which is derived from SuperCl, it means that DerivedCl2 will inherit all the atributes of both classes.
derivate.super_method()  #SuperCl
derivate.derived_method() #DerivedCl1
derivate.sec_derived_method() #DerivedCl2  
 