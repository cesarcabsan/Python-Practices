from abc import ABC, abstractmethod
# Abstraction and encapsulation mix example.

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self._name

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def show_animals(self):
        for animal in self._animals:
            print(f"{animal.get_name()} says: ", end="")
            animal.make_sound()

# Usage 
zoo = Zoo()
dog = Dog("Buddy")
cat = Cat("Whiskers")

zoo.add_animal(dog)
zoo.add_animal(cat)

zoo.show_animals()

