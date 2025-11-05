# Imagine you’re managing a global car manufacturing company
# You want to design a system to create cars with specific configurations for different regions, such as North America and Europe. 
# Each region may have unique requirements and regulations, and you want to ensure that cars produced for each region meet those standards.

from abc import ABC, abstractmethod

# Abstract car factory interface
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass 

    @abstractmethod
    def create_specification(self):
        pass

# Concrete car factories
class NorthAmericaCarFactory(CarFactory):
    def create_car(self):
        return Sedan()
    
    def create_specification(self):
        return NorthAmericaSpecification()

class EuropeCarFactory(CarFactory):
    def create_car(self):
        return Hatchback()
    
    def create_specification(self):
        return EuropeSpecification()


# Abstract Product Interface for Cars
class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass

# Abstract Product Interface for Car Specifications
class CarSpecification(ABC):
    @abstractmethod
    def display(self):
        pass 
 
# Concrete products for Cars
class Sedan(Car):
    def assemble(self):
        print("Assembling Sedan car")

class Hatchback(Car):
    def assemble(self):
        print("\nAssembling Hatchback car")

# Concrete products for Car Specifications
class NorthAmericaSpecification(CarSpecification):
    def display(self):
        print("North America Car Specification: Safety features compliant with local regulations.")

class EuropeSpecification(CarSpecification):
    def display(self):
        print("Europe Car Specification: Fuel efficiency and emissions compliant with EU standards.")

# Client code

# North america car creation
north_america_factory = NorthAmericaCarFactory()
north_america_car = north_america_factory.create_car()
north_america_spec = north_america_factory.create_specification()

north_america_car.assemble()
north_america_spec.display()

# Europe car creation
europe_factory = EuropeCarFactory()
europe_car = europe_factory.create_car()
europe_spec = europe_factory.create_specification()

europe_car.assemble()
europe_spec.display()