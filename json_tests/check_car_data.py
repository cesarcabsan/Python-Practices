import json

with open("car_data.json", "r") as f:
    car_data = json.load(f)

print(car_data.items())
