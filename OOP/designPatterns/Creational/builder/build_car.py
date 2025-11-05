class Car:
    # Constructor to initialize car attributes
    def __init__(self, make, model, year, color, num_doors, engine_type, transmission_type, sunroof=False, gps=False):
        self.make = make
        self.model = model
        self.year = year 
        self.color = color
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.transmission_type = transmission_type
        self.sunroof = sunroof 
        self.gps = gps

# Method to display the car attributes
    def __str__(self):
        return (f"Car Details:\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}\n"
                f"Color: {self.color}\n"
                f"Number of Doors: {self.num_doors}\n"
                f"Engine Type: {self.engine_type}\n"
                f"Transmission: {self.transmission_type}\n"
                f"Sunroof: {True if self.sunroof else False}\n"
                f"GPS: {True if self.gps else False}")
 
class CarBuilder:
    # Constructor initializes default values for the car's attributes
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None 
        self.color = None
        self.num_doors = None
        self.engine_type = None
        self.transmission_type = None
        self.sunroof = False 
        self.gps = False

    # Setter methods for each car attribute
    def set_make(self, make):
        self.make = make 
        return self
    
    def set_model(self, model):
        self.model = model 
        return self
    
    def set_year(self, year):
        self.year = year 
        return self
    
    def set_color(self, color):
        self.color = color 
        return self
    
    def set_num_doors(self, num_doors):
        self.num_doors = num_doors 
        return self
    
    def set_engine_type(self, engine_type):
        self.engine_type = engine_type 
        return self
    
    def set_transmission_type(self, transmission_type):
        self.transmission_type = transmission_type 
        return self
    
    def set_sunroof(self, sunroof):
        self.sunroof = sunroof 
        return self
    
    def set_gps(self, gps):
        self.gps = gps 
        return self

    # Method to build and return the final Car object with all the set attributes
    def build(self):
        return Car(self.make, self.model, self.year, self.color, self.num_doors, self.engine_type, self.transmission_type, 
                   sunroof=self.sunroof, gps=self.gps)
    
# Usage
builder = CarBuilder()
# Chaining setter methods to set all car attributes, then build the car object
my_car = builder.set_make("Toyota") \
                .set_model("Camry") \
                .set_color("Red") \
                .set_year(2024) \
                .set_num_doors(4) \
                .set_engine_type("Gasoline") \
                .set_transmission_type("Automatic") \
                .set_sunroof(False) \
                .set_gps(True) \
                .build()
 
print(my_car)