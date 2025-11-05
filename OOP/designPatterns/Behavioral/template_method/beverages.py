from abc import ABC, abstractmethod

# Abstract class defining the template method
class BeverageMaker(ABC):
    # Template method defining the overall process
    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

# Abstract methods to be implemented by subclasses
    @abstractmethod
    def brew(self):
        pass
    @abstractmethod
    def add_condiments(self):
        pass

# Common methods
    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

# Concrete subclasses for implementing the abstract methods
class TeaMaker(BeverageMaker):
    def brew(self):
        print("Steeping on tea")
    def add_condiments(self):
        print("Adding lemon")

class CoffeeMaker(BeverageMaker):
    def brew(self):
        print("Dripping coffee through filter")
    def add_condiments(self):
        print("Adding sugar and milk")

# Usage 
print("Making tea")
tea_maker = TeaMaker()
tea_maker.make_beverage()

print("\nMaking coffee")
coffee_maker = CoffeeMaker()
coffee_maker.make_beverage()


# The template method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets
# subclasses override specific steps of the algorithm without changing its structure.
 