from abc import ABC, abstractmethod

# Shape prototype interface
class Shape(ABC):
    @abstractmethod
    def clone(self):    
        pass

    @abstractmethod
    def draw(self):
        pass

# Concrete shape prototype
class Circle(Shape):
    # When you create a circle, you give it a color.
    def __init__(self, color: str):
        self.color = color

    # This creates a copy of the circle.
    def clone(self):
        return Circle(self.color)
    
    def draw(self):
        print(f"Drawing a {self.color} circle.")

# Client code
class ShapeClient:
    # When you create a client, you give it a prototype (a shape).
    def __init__(self, shape_protoype: Shape):
        self.shape_prototype = shape_protoype

    # This method creates a new shape using the prototype.
    def create_shape(self):
        return self.shape_prototype.clone()
    
# Usage

# Create a concrete shape prototype  
circle_prototype = Circle("blue")

# Create a client and give it the prototype.
client = ShapeClient(circle_prototype)

# Use the prototype to create a new shape
colored_circle = client.create_shape()

# Draw the newly created red circle.
colored_circle.draw()