import matplotlib.pyplot as plt

vegetables = ["Carrot", "Broccoli", "Tomato", "Onion", "Lettuce", "Cucumber"]
sizes = [35, 27, 41, 12, 23, 29]
veg_colors = ("orange", "green", "red", "violet", "lime", "darkgreen")

fig1, ax = plt.subplots()
ax.pie(sizes, labels=vegetables, autopct="%1.1f%%", colors=veg_colors)

plt.title("Vegetables")
plt.show()