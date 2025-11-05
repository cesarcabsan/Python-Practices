from abc import ABC, abstractmethod

class Sushi(ABC):
    def make(self):
        self.cook_rice()
        self.add_filling()
        self.wrap()
        self.cook()
        self.serve()
        
    def cook_rice(self):
        print('Rice is boiled.')
        
    def serve(self):
        print('Served with wasabi and marinated ginger root.')

# The method add_filling() should always be present in all recipes, so its defined as an abstract method:        
    @abstractmethod
    def add_filling(self):
        pass
    
# The methods wrap() and cook() are not mandatory, so let’s define them in the core class without the necessity to implement them in the inherited classes:
    def wrap(self):
        pass

    def cook(self):
        pass
    
class UnagiMaki(Sushi):
    def add_filling(self):
        print('Smoked eel added.')

    def wrap(self):
        print('Wrapped in nori.')
        
        
class BakedShrimpRoll(Sushi):
    def add_filling(self):
        print('Cleaned shrimp added.')

    def wrap(self):
        print('Tempura sprinkled.')

    def cook(self):
        print('Baked in oven.')
        
        
my_sushi = UnagiMaki()
my_sushi.make()

my_sushi_2 = BakedShrimpRoll()
my_sushi_2.make()