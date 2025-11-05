from abc import ABC, abstractmethod
import math 
from typing import List

# Visitor interface
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle") :
        pass

    @abstractmethod
    def visit_square(self, square: "Square"):
        pass

    @abstractmethod
    def visit_triangle(self, triangle: "Triangle"):
        pass

# Element interface
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        pass 


# Concrete elements
class Circle(Shape):
    def accept(self, visitor: ShapeVisitor):
        visitor.visit_circle(self)

class Square(Shape):
    def accept(self, visitor: ShapeVisitor):
        visitor.visit_square(self)

class Triangle(Shape):
    def accept(self, visitor: ShapeVisitor):
        visitor.visit_triangle(self)

# Concrete visitor
class AreaCalculator(ShapeVisitor):
    def __init__(self):
        # Initialize total area  
        self.total_area = 0.0
        # Hardcoded dimentions, not extracted from shape objects
        self.circle_radius = 5
        self.side_of_square = 4
        self.triangle_base = 3
        self.triangle_height = 6

    def visit_circle(self, circle: Circle):
        # Calculate area of circle and update total_area
        self.total_area += math.pi * self.circle_radius ** 2

    def visit_square(self, square: Square):
        # Calculate area of square and update total_area
        self.total_area += self.side_of_square ** 2

    def visit_triangle(self, triangle: Triangle):
        # Calculate area of triangle and update total_area
        self.total_area += (self.triangle_base * self.triangle_height) / 2

    def get_total_area(self):
        return self.total_area


# Usage

# List of shapes to be processed
shapes: List[Shape] = [Circle(), Square(), Triangle()]

# Create the area calculator visitor
area_calculator = AreaCalculator()

# Let each shape accept the visitor (calculating areas)
for shape in shapes:
    shape.accept(area_calculator)

print(f"Total area: {area_calculator.get_total_area():.2f}")
   
 


 