import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\cesar\\OneDrive\\Documents\\csv_tests\\employee_data.csv")

plt.figure(figsize=(10, 4))
# Good correlation (Experience vs Salary)
plt.subplot(1,2,1)
plt.scatter(df["YearsExperience"], df["MonthlySalary"], color="lawngreen")

plt.title("Experience vs Salary")
plt.xlabel("Years of experience")
plt.ylabel("Monthly Salary")
plt.grid(True)

# Bad correlation (Employee ID vs Salary)
plt.subplot(1,2,2)
plt.scatter(df["EmployeeID"], df["MonthlySalary"], color="firebrick")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Monthly Salary")
plt.grid(True)

plt.tight_layout()
plt.show()