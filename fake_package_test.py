from faker import Faker
import json 
from random import randint

fake = Faker()
n1 = 5
students = {}

# creating JSON
for i in range(n1):
    students[i] = {
        'id': randint(1, 10),
        'name': fake.name(),
        'address': fake.address(),
        'latitude': float(fake.latitude()),
        'longitude': float(fake.longitude())
    }

print(json.dumps(students, indent=4))
with open('fake_student_data.json', 'w') as fp:
    json.dump(students, fp, indent=4)

print(f"JSON file created with {n1} student records")
