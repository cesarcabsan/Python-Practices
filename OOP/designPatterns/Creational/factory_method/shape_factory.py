from abc import ABC, abstractmethod

# Shape interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass 

# Concrete shape classes
class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")        

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")  

class Triangle(Shape):
    def draw(self):
        print("Inside Triangle::draw() method.")        
        
class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")        
        
        
# Shape factory for generating object of concrete shape classes  
class ShapeFactory:
    # use getShape method to get object of type shape 
    def get_shape(self, shape_type) -> Shape:
        if shape_type is None:
            return None     
        
        elif shape_type == "Rectangle":
            return Rectangle()
        
        elif shape_type == "Square":
            return Square()
        
        elif shape_type == "Triangle":
            return Triangle()

        elif shape_type == "Circle":
            return Circle()
        
        return None 
        
# Usage
shape_factory = ShapeFactory()

# Creating shape variables (the standard way) 

#shape1 = shape_factory.get_shape("Rectangle")
#shape1.draw()

#shape2 = shape_factory.get_shape("Square")
#shape2.draw()

#shape3 = shape_factory.get_shape("Triangle")
#shape3.draw()

#shape4 = shape_factory.get_shape("Circle")
#shape4.draw()


# With for loop list
shape_types = ["Rectangle", "Square", "Triangle", "Circle"]
for shape in shape_types:
    shape = shape_factory.get_shape(shape)
    shape.draw()
