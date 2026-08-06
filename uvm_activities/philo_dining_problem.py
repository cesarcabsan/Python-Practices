import threading
import time
import random

NUM_PHILOSOPHERS = 5

forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

def philosopher(index):
    left_fork = index
    right_fork = (index + 1) % NUM_PHILOSOPHERS

    # To prevent deadlock, the last philosopher picks up forks in reverse order
    if index == NUM_PHILOSOPHERS - 1:
        first, second =  right_fork, left_fork
    else:
        first, second = left_fork, right_fork

    while True:
        print(f"Philosopher {index} is thinking.")
        time.sleep(random.uniform(1, 3))

        print(f"Philosopher {index} is hungry.")

    # Pick up forks
        with forks[first]:
            with forks[second]:
                print(f"Philosopher {index} is eating.")
                time.sleep(random.uniform(1, 3))

        print(f"Philosopher {index} has finished his eating his meal.")
        break

# Create and start threads
threads = []
for i in range(NUM_PHILOSOPHERS):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
 

# This code was originally done in c (along with java, its the language that's usually used for solving this problem) 
# This is just an adaptation in python.