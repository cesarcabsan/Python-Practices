# Consider a software application that needs to handle the creation of various types of vehicles, such as 
# Two Wheelers, Three Wheelers, and Four Wheelers. Each type of vehicle has its own specific properties and behaviors.

from abc import ABC, abstractmethod

# Product interface for vehicles
class Vehicle(ABC):
    @abstractmethod
    def print_vehicle(self):
        pass
    
# Concrete product classes representing different types of vehicles
class TwoWheeler(Vehicle):
    def print_vehicle(self):
        print("Im a two wheeler")

class FourWheeler(Vehicle):
    def print_vehicle(self):
        print("Im a four wheeler")    


# Factory Interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

# Concrete creators for each concrete product
class TwoWheelerFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return TwoWheeler()
 
class FourWheelerFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return FourWheeler()
        

# client class
class Client:
    def __init__(self, factory: VehicleFactory):
        self.p_vehicle = factory.create_vehicle()
        
    def get_vehicle(self) -> Vehicle:
        return self.p_vehicle

# Usage
two_wheeler_factory = TwoWheelerFactory()
two_wheeler_client = Client(two_wheeler_factory)
two_wheeler = two_wheeler_client.get_vehicle()
two_wheeler.print_vehicle()

four_wheeler_factory = FourWheelerFactory()
four_wheeler_client = Client(four_wheeler_factory)
four_wheeler = four_wheeler_client.get_vehicle()
four_wheeler.print_vehicle()
    
