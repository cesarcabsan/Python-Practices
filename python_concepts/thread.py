from time import sleep
from threading import Thread
import threading
#Running function in a thread with arguments 
def task(sleeping, message):
    sleep(sleeping)
    print(message)

thread = Thread(target=task, args=(1.5, "Here's a Message from another thread"))
thread.start()
print("Waiting... ")
thread.join()


#Calculare square and cube of a number concurrently
def square(num):
    print("Square: {}".format(num*num))

def cube(num):
    print("Cube: {}".format(num*num*num)) 

t1 = threading.Thread(target=square, args=(10, ))
t2 = threading.Thread(target=cube, args=(10, ))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")

