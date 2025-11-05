from abc import ABC, abstractmethod

# Product interface
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass 

    @abstractmethod
    def bake(self):
        pass 

    @abstractmethod
    def cut(self):
        pass 

    @abstractmethod
    def box(self):
        pass 

# Concrete product implementations
class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")

    def bake(self):
        print("Baking Margherita Pizza")

    def cut(self):
        print("Cutting Margherita Pizza")

    def box(self):
        print("Boxing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

    def bake(self):
        print("Baking Pepperoni Pizza")

    def cut(self):
        print("Cutting Pepperoni Pizza")

    def box(self):
        print("Boxing Pepperoni Pizza")

# Creator interface
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass 

# Concrete creator implementations
class MargheritaPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return MargheritaPizza()
    
class PepperoniPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return PepperoniPizza()
    
    
# Client code

# Create a Margherita through its factory
#pizza_factory = MargheritaPizzaFactory()
#pizza = pizza_factory.create_pizza()

# Create a Pepperoni pizza through its factory
pizza_factory = PepperoniPizzaFactory()
pizza = pizza_factory.create_pizza()

pizza.prepare()
pizza.bake()
pizza.cut()
pizza.box()


 