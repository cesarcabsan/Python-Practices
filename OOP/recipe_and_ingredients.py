from dataclasses import dataclass, field
from typing import List

@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str

@dataclass
class Recipe:
    title: str
    ingredients: List[Ingredient] = field(default_factory=list)

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def show_recipe(self):
        print(f"Recipe: {self.title}")
        for ing in self.ingredients:
            print(f"- {ing.quantity} {ing.unit} of {ing.name}")

# Usage
recipe = Recipe(title="Pasta Primavera")

recipe.add_ingredient(Ingredient("Pasta", 200, "Gram"))
recipe.add_ingredient(Ingredient("Tomato", 2, "pieces"))
recipe.add_ingredient(Ingredient("Olive Oil", 3, "tablespoons"))
recipe.add_ingredient(Ingredient("Garlic", 1, "clove"))

recipe.show_recipe()