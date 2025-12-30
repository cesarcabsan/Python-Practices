import json 
from dataclasses import dataclass, asdict

# to_dict()
class Animal:
    def __init__(self, species, breed):
        self.species = species
        self.breed = breed

    def to_dict(self):
        return {'species': self.species, 'breed': self.breed}
    
animal = Animal("Tiger", "Bengal")
serialize = json.dumps(animal.to_dict())
print(serialize)

# asdict()
@dataclass
class Person:
    name: str
    age: int

person = Person("Abel", 22)
res = json.dumps(asdict(person))
print(res)

