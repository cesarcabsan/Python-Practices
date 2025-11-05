from abc import ABC, abstractmethod

class IColor(ABC):
    @abstractmethod
    def get_color(self):
        pass

class Green(IColor):
    def get_color(self):
        print("Green")

class Blue(IColor):
    def get_color(self):
        print("Blue")

class Yellow(IColor):
    def get_color(self):
        print("Yellow")

color = Yellow()
color.get_color()

 

