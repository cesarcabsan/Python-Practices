from abc import ABC, abstractmethod
# Abstraction simplifies the code's complexity by hiding all of the unnecesary details.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")

class Bike(Vehicle):
    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")

move = Bike()
move.start()
move.stop()

# Data processing example with polymorphism
class DataProcessor(ABC):    
    @abstractmethod
    def process_data(self, data):
        pass 

class NumericDataProcessor(DataProcessor):
    def process_data(self, data):
        return [x * 2 for x in data]

class TextDataProcessor(DataProcessor):
    def process_data(self, data):
        return [s.upper() for s in data]

    
def process_all(data_processor: DataProcessor, data) -> list:
    return data_processor.process_data(data)

num_processor = NumericDataProcessor()
text_processor = TextDataProcessor()

numeric_data = [1,2,3,4,5]
text_data = ["Learning", "Things"]

print(process_all(num_processor, numeric_data))
print(process_all(text_processor, text_data))


#Abstract properties (using the property decorator)
class Owner(ABC):
    @property
    @abstractmethod
    def feed(self):
        pass

class Pet(Owner):
    def feed(self):
        return "Feeding pet"
    
pet = Pet()
print(pet.feed())


# Concrete methods 
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def move(self):   # Concrete method with implementation
        return "Moving"

class Cow(Animal):
    def sound(self):
        return "Moooooo!"
    
cow = Cow()
print(cow.sound())
print(cow.move())

  