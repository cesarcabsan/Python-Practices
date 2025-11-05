# Example: Consider building a custom meal for a restaurant order, 
# which includes a taco, a drink, and a side.

# Product class that represents the complex object to be built
class Meal:
    def __init__(self):
        self.taco = None
        self.drink = None
        self.side = None

# Abstract Builder class defining the building steps for a meal
class MealBuilder:
    def __init__(self):
        self.meal = Meal()  # Builder maintains an instance of the product

    def build_taco(self):
        pass  # To be implemented by concrete builder

    def build_drink(self):
        pass  # To be implemented by concrete builder

    def build_side(self):
        pass  # To be implemented by concrete builder

    def get_meal(self):
        return self.meal  # Final assembled product


# Concrete Builder that creates a specific type of meal 
class VegetarianMealBuilder(MealBuilder):
    def build_taco(self):
        self.meal.taco = "Grilled Veggie Taco"   

    def build_drink(self):
        self.meal.drink = "Fresh Lime Juice"   

    def build_side(self):
        self.meal.side = "Quinoa Salad"   

# Director class that defines the construction sequence
class Director:
    def construct_meal(self, builder):
        builder.build_taco()
        builder.build_drink()
        builder.build_side()
        return builder.get_meal()
    
# Usage
vegetarian_builder = VegetarianMealBuilder()
director = Director()
meal = director.construct_meal(vegetarian_builder)

print(f"Taco: {meal.taco}, \nDrink: {meal.drink}, \nSide: {meal.side}")
