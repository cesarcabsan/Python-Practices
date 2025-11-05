class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

class BirthdayCelebrator:
    def celebrate_birthday(self, person):
        person.age += 1
        print(f"{person.name} is now {person.age} years old!")


person = Person("Shawn", 27)
celebrator = BirthdayCelebrator()

person.greet()
celebrator.celebrate_birthday(person)
person.greet()


 
 