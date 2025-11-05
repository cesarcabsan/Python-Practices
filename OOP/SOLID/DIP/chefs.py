from abc import ABC, abstractmethod
# Abstract Chef class (interface)
class IChef(ABC):
    @abstractmethod
    def make_pizza(self):
        pass

# Concrete classes
class ItalianChef(IChef):
    def make_pizza(self):
        print("The italian chef is making a pizza!")

class RobotChef(IChef):
    def make_pizza(self):
        print("The robot chef is making pizza with automation!")

# Waiter class that depends on the IChef abstraction class.
class Waiter:
    def __init__(self, chef: IChef):
        self._chef = chef # The waiter does not depend on concrete chef classes, only the abstraction class
        
    def take_order(self):
        self._chef.make_pizza() # Calls the make_pizza method, works with any IChef implementation
        
# Usage Main
chef = ItalianChef()  # Choosing a chef (ItalianChef or RobotChef)
     
waiter = Waiter(chef) # Dependency injection: Pass the chef into the Waiter.

waiter.take_order()  # Waiter takes the order and delegates pizza making to its chosen chef.