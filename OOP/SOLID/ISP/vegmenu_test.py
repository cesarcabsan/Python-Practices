from abc import ABC, abstractmethod

class IVegetarianMenu(ABC):
    @abstractmethod
    def get_veg_items(self):
        pass
    
class INonVegetarianMenu(ABC):
    @abstractmethod
    def get_nonveg_items(self):
        pass
    
class IDrinkMenu(ABC):
    @abstractmethod
    def get_drink_items(self):
        pass
    
class VegetarianMenu(IVegetarianMenu):
    def get_veg_items(self):
        return ["Vegetable Curry", "Paneer Tikka", "Salad"]
        
class NonVegetarianMenu(INonVegetarianMenu):
    def get_nonveg_items(self):
        return ["Chicken Curry", "Fish Fry", "Mutton Biryani"]

class DrinkMenu(IDrinkMenu):
    def get_drink_items(self):
        return ["Water", "Soda", "Juice"]
        
def display_veg_menu(menu: IVegetarianMenu):
    print("Vegetarian Menu:")
    for item in menu.get_veg_items():
        print(f"- {item}")
   
def display_nonveg_menu(menu: INonVegetarianMenu):
    print("Non-Vegetarian Menu:")
    for item in menu.get_nonveg_items():
        print(f"- {item}")

def display_drink_menu(menu: IDrinkMenu):
    print("Drink Menu:")
    for item in menu.get_drink_items():
        print(f"- {item}")
        
veg_menu = VegetarianMenu()
nonveg_menu = NonVegetarianMenu()
drink_menu = DrinkMenu()

display_veg_menu(veg_menu)
display_nonveg_menu(nonveg_menu)
display_drink_menu(drink_menu)
