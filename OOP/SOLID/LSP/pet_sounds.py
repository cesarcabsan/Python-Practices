class Pet:
    def make_sound(self):
        pass

class Dog(Pet):
    def make_sound(self):
        return "Woof!"

class Cat(Pet):
    def make_sound(self):
        return "Meow!"

def pet_sound(pets: list[Pet]):
    for pet in pets:
        print(pet.make_sound())

pet = Pet()
pet_sound([pet])

dog = Dog()
cat = Cat()
pet_sound([dog, cat])