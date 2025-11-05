from abc import ABC, abstractmethod

class PizzaMaker(ABC):
    def make_pizza(self):
        self.prepare_pizza_dough()
        self.prebake_crust()
        self.prepare_ingredients()
        self.add_toppings()
        self.bake_pizza()
        if self.customer_wants_packed_pizza(): # Optional step based on hook method
            self.pack_pizza()
            
    def prepare_pizza_dough(self):
        print("Preparing pizza dough with plain flour, dried yeast, caster sugar, salt, olive oil, and warm water.")
            
    def prebake_crust(self):
        print("Pre baking crust at 325 F for 3 minutes.")

    @abstractmethod
    def prepare_ingredients(self): # Abstract method to be implemented by each subclass
        pass
        
    @abstractmethod
    def add_toppings(self): # Another abstract method to be implemented by each subclass
        pass
        
    def bake_pizza(self):
        print("Baking pizza at 400 F for 12 minutes.")
            
    def pack_pizza(self):
        print("Packing pizza in pizza delivery box.")
            
    # Hook method with default behavior; can be overridden by subclasses
    def customer_wants_packed_pizza(self):
        return True
            
# Subclasses
class VegPizzaMaker(PizzaMaker):
    def prepare_ingredients(self):
        print("Preparing mushroom, tomato slices, onions, and fresh basil leaves.")
        
    def add_toppings(self):
        print("Adding mozzerella cheese and tomato sauce along with ingredients to crust.")
        
    
class NonVegPizzaMaker(PizzaMaker):
    def prepare_ingredients(self):
        print("Preparing chicken ham, onion, chicken sausages, and smoked chicken")
        
    def add_toppings(self):
        print("Adding cheese, pepper jelly, and BBQ sauce along with ingredients to crust.")
        

class InHouseAssortedPizzaMaker(PizzaMaker):
    def prepare_ingredients(self):
        print("Preparing sweet corns, chicken sausage, green chillies, and onions.")
        
    def add_toppings(self):
        print("Adding cheddar cheese and bechamel sauce along with ingredients to crust.")
        
    def customer_wants_packed_pizza(self): # Override the hook method to skip packing 
        return False
        

# Code usage 
print("-----Making Veg Pizza-----")
veg_pizza = VegPizzaMaker()
veg_pizza.make_pizza()

print("-----Making Non Veg Pizza-----")
non_veg_pizza = NonVegPizzaMaker()
non_veg_pizza.make_pizza()

print("-----Making In-House Assorted Pizza-----")
in_house_pizza = InHouseAssortedPizzaMaker()
in_house_pizza.make_pizza()