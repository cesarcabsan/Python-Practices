import json

# Example: Employee Access Control System: Imagine you’re designing a system to manage employee access rights.

# Step 1: Define a class for employees
class Employee:
    def __init__(self, emp_id, name, role, access_level):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.access_level = access_level

    def __repr__(self):
        return f"{self.name} ({self.role}) - Access: {self.access_level}"
    
     # Compliance check: interns should never have high access
    def is_compliant(self):
        if self.role.lower() == "intern" and self.access_level == "high":
            return False
        return True
    
# Step 2: Load JSON data
with open("employees_status.json") as f:
    data = json.load(f)

# Step 3: Convert JSON into employees objects
employees = [Employee(emp["id"], emp["name"], emp["role"], emp["access_level"]) for emp in data]

# Step 4: Run compliance checks
for emp in employees:
    print(emp, "✓" if emp.is_compliant() else "X (Non-compliant)")


 