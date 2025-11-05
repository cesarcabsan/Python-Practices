from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def get_area(self):
        return self.side * self.side
        
def calculate_area(shape: Shape):
    return shape.get_area()
    
rectangle = Rectangle(4, 5)
square = Square(5)

## Normal execution
# print(calculate_area(rectangle))
# print(calculate_area(square))

## Execution with list and for loop
shapes = [rectangle, square]
for shape in shapes:
    print(calculate_area(shape))

