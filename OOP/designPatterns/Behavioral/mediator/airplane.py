# Several airplanes in an airport must coordinate their movements and communicate with one another in order to prevent collisions and guarantee safe takeoffs and landings. 
# Direct communication between aircraft without a centralized mechanism could result in chaos and higher risk.
from abc import ABC, abstractmethod 

# Colleage interface
class Airplane(ABC):
    @abstractmethod
    def request_takeoff(self):
        pass

    @abstractmethod
    def request_landing(self):
        pass

    @abstractmethod
    def notify_air_traffic_control(self, message: str):
        pass

# Concrete colleage
class CommercialAirplane(Airplane):
    def __init__(self, mediator: "AirTrafficControlTower"):
        self.mediator = mediator

    def request_takeoff(self):
        self.mediator.request_takeoff(self)

    def request_landing(self):
        self.mediator.request_landing(self)

    def notify_air_traffic_control(self, message: str):
        print(f"Commercial airplane: {message}")

# Mediator interface
class AirTrafficControlTower(ABC):
    @abstractmethod
    def request_takeoff(self, airplane: Airplane):
        pass 

    @abstractmethod
    def request_landing(self, airplane: Airplane):
        pass

# Concrete mediator
class AirportControlTower(AirTrafficControlTower):
    def request_takeoff(self, airplane: Airplane):
        print("Processing takeoff request...")
        airplane.notify_air_traffic_control("Takeoff clearance granted")

    def request_landing(self, airplane: Airplane):
        print("Processing landing request...")
        airplane.notify_air_traffic_control("Landing clearance granted")

# Usage

# Instanciate the mediator 
control_tower = AirportControlTower()

# Instanciate concrete colleages
airplane1 = CommercialAirplane(control_tower)
airplane2 = CommercialAirplane(control_tower)

# Set up the association between concrete colleagues and the mediator
airplane1.request_takeoff()
airplane2.request_landing()

