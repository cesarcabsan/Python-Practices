from datetime import date
#Person class with age calculation
class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate
        
    def __str__(self):
        return f"Name: {self.name}, \nCountry: {self.country}, \nBirth Date: {self.birthdate}"
        
    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if today < date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1 
        return age
   
person1 = Person('Tyson', 'UK', date(1999, 7, 6))
person2 = Person('Cassandra', 'Spain', date(2000, 4, 6))
person3 = Person('Miguel', 'Chile', date(1989, 11, 10))

print(f"Person1\n{person1},\nAge: {person1.calculate_age()}\n")
print(f"Person2:\n{person2},\nAge: {person2.calculate_age()}\n")
print(f"Person3:\n{person3},\nAge: {person3.calculate_age()}")