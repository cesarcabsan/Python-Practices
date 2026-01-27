from dataclasses import dataclass

@dataclass
class Website:
    name: str
    type_of_website: str
    no_of_characters: str


@dataclass
class Programming_Website(Website):
    name: str
    languages_covered: list[str]

new_instance = Programming_Website("DataCamp", "Technical", 24, ['Python', 'C', 'C++'])
    
print(new_instance)