from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def walk(self):
        pass

class SwimAbility(ABC):
    @abstractmethod
    def swim(self):
        pass

class FlyAbility(ABC):
    @abstractmethod
    def fly(self):
        pass

class Hamster(Animal):
    def eat(self):
        return True
    def walk(self):
        return True

class Duck(Animal, SwimAbility):
    def eat(self):
        return True
    def walk(self):
        return True
    def swim(self):
        return True

class Pigeon(Animal, FlyAbility):
    def eat(self):
        return True
    def walk(self):
        return True
    def fly(self):
        return True


hamster = Hamster()
print(f"Hamster:\nEat? {hamster.eat()}\nWalk? {hamster.walk()}")

duck = Duck()
print(f"\nDuck:\nEat? {duck.eat()}\nWalk? {duck.walk()}\nSwim? {duck.swim()}")

pigeon = Pigeon()
print(f"\nPigeon:\nEat? {pigeon.eat()}\nWalk? {pigeon.walk()}\nFly? {pigeon.fly()}")


