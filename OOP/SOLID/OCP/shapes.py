from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Hexagon(Shape):
    def __init__(self, sidelen):
        self.sidelen = sidelen 

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.sidelen ** 2

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()

 
rectangle = Rectangle(14, 16)
circle = Circle(2)
triangle = Triangle(6, 6)
hexagon = Hexagon(3)

area_calculator = AreaCalculator()

shapes = [rectangle, circle, triangle, hexagon]
for shape in shapes:
    print(area_calculator.calculate_area(shape))

 
