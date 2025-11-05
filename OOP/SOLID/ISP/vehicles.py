from abc import ABC, abstractmethod

#Split vehicle class into smaller interfaces to follow the ISP principle
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Plane(Flyable):
    def go(self):
        print("Moving up")

    def fly(self):
        print("Flying in the air")

class Truck(Movable):
    def go(self):
        print("Big wheels moving")


plane = Plane()
truck = Truck()

plane.go()
plane.fly()

truck.go()

