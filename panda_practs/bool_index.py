import pandas as pd

# example:  filtering suspicious reservations
# Imagine you’re auditing a hotel reservation system and want to flag bookings that violate compliance rules:
# 	Rule 1: Reservations longer than 30 days (possible misuse or fraud).
#	Rule 2: Reservations with unusually low daily rates (below compliance threshold).

df = pd.DataFrame({
    "reservation_id": [1001, 1002, 1003, 1004],
    "guest_name": ["Alicia", "Jake", "Carlos", "Diana"],
    "nights": [5, 36, 10, 35],
    "daily_rate": [120, 80, 200, 50]
})

# Rule 1: Reservations longer than 30 nights
long_stays = df.loc[df["nights"] > 30]

# Rule 2: Reservations with daily rate below 30
underpriced = df.loc[df["daily_rate"] < 100]

print("Long stays:\n", long_stays)
print("\nUnderpriced revervations:\n", underpriced)