## Law of demeter (Principle of least knowledge) is a design guideline that states that an object should only communicate with its immediate neighbors, and not with objects further away in the hierarchy. 
## In other words, an object should not have knowledge of the internal structure of other objects. 
# Its goal is to achieve loose coupling and high maintenability.

# Example 1
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        return self.engine.start() # Internal logic encapsulated within Car

class Driver:
    def __init__(self):
        self.car = Car()

    def drive(self):
        # Here, the Driver interacts only with Car, not with Engine directly
        return self.car.start_car() # Accessing through Car's public method

driver = Driver()
print(driver.drive())

# Example 2 (method parameters)
class Library:
    def borrow_book(self, title):
        book = Book(title)
        book.issue()
        return book

class Book:
    def __init__(self, title):
        self.title = title
    
    def issue(self):
        print("Book issued:", self.title)

book = Book("GeeksForGeeks")
book.issue()

# Example 3 (Objects passed as arguments)
class Printer:
    def print(self, document):
        document.send_to_printer()

class Document:
    def send_to_printer(self):
        print("Document is being printed...")

document = Document()
document.send_to_printer()


# In Summary, a method should only call methods of: 
# Itself, Its parameters, Its instance variables (but only the ones that are objects of classes it directly owns)
# and Objects that are directly associated with it (friends)

