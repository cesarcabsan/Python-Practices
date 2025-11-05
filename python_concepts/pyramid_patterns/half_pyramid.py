# half pyramid
rows = 5
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("----------*")

# inverted half pyramid
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()

print('____________________________')

#Left half pyramid
N = 5

for i in range(1, N + 1):
    for j in range(1, N - i + 1):
        print(" ", end=" ")
        
    for k in range(1, i + 1):
        print("*", end=" ")
        
    print()

print("----------*")
# Inverted left half pyramid
for i in range(N):
    for j in range(i):
        print(" ", end=" ")

    for k in range(N-i):
        print("*", end=" ")
    print()


print('_________________________')
# No nested loop (using int input this time)
n_rows = int(input("Enter a number of rows: "))

def half_pyramid(n_rows):
    for i in range(1, n_rows + 1):
        print("* " * i)

def inverted_half_pyramid(n_rows):
    for i in range(n_rows, 0, -1):
        print("* " * i)

 
half_pyramid(n_rows)
inverted_half_pyramid(n_rows)