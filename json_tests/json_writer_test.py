import json

# Example: Saving student records

students = [
    {"name": "Nathan", "grade": 90},
    {"name": "Luke", "grade": 85},
    {"name": "Anna", "grade": 92}
]

json_str = json.dumps(students, indent=4)

with open("student_records.json", "w") as f:
    f.write(json_str)

print("Data written to json file: student_records.json")
