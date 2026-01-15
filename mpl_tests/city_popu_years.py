import matplotlib.pyplot as plt

# Line plot example from tutorialspoint: Population data of a city over several years (or this case, the recent decade)
x = [2020, 2021, 2022, 2023, 2024, 2025] 
y = [800, 820, 844, 900, 920, 970]

plt.plot(x, y, marker='o', color='green')

plt.title("City Population over years")
plt.xlabel("Years")
plt.ylabel("Population (in thousands)")

plt.show()