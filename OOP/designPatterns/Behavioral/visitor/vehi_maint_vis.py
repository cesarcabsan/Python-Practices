from abc import ABC, abstractmethod

# Visitor interface 
class VehicleVisitor(ABC):
    @abstractmethod
    def car_cost(self, car): 
        pass

    @abstractmethod
    def motorcycle_cost(self, motorcycle): 
        pass

    @abstractmethod
    def truck_cost(self, truck): 
        pass

# Visitable interface 
class VisitableVehicle(ABC):
    @abstractmethod
    def accept(self, visitor: VehicleVisitor): 
        pass

# Concrete Visitor 
class MaintenanceEstimator(VehicleVisitor):
    def car_cost(self, car):
        return car.base_cost * 1.2  # 20% maintenance markup for cars

    def motorcycle_cost(self, motorcycle):
        return motorcycle.base_cost * 0.8  # Lower cost for motorcycles

    def truck_cost(self, truck):
        return truck.base_cost * 1.5  # Higher cost for trucks

# Concrete Elements 
class Car(VisitableVehicle):
    def __init__(self, base_cost):
        self.base_cost = base_cost

    def accept(self, visitor: VehicleVisitor):
        return visitor.car_cost(self)  # Delegates to visitor's car_cost method

class Motorcycle(VisitableVehicle):
    def __init__(self, base_cost):
        self.base_cost = base_cost

    def accept(self, visitor: VehicleVisitor):
        return visitor.motorcycle_cost(self)  # Delegates to visitor's motorcycle_cost method

class Truck(VisitableVehicle):
    def __init__(self, base_cost):
        self.base_cost = base_cost

    def accept(self, visitor: VehicleVisitor):
        return visitor.truck_cost(self)  # Delegates to visitor's truck_cost method


# Client code 
estimator = MaintenanceEstimator()
vehicles = [Car(500), Motorcycle(300), Truck(800)]

for v in vehicles:
    cost = v.accept(estimator)  # Double dispatch: vehicle accepts visitor, visitor processes vehicle
    print(f"{v.__class__.__name__} maintenance cost: ${cost:.2f}")