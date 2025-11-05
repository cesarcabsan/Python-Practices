import threading 
import time 
import datetime
import logging 
# Configure the logging module to display messages with DEBUG level or higher.
# The format specifies how the log messages will appear.
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')

# Consult function to simulates a consultation process
def consult(id_person):
    logging.info("Consulting ID " + str(id_person))
    time.sleep(2)
    return

# Save function to simulates a process of saving data
def save(id_person, data):
    logging.info("Consulting ID " + str(id_person) + " data " + data)
    time.sleep(5)
    return

start_time = datetime.datetime.now()

t1 = threading.Thread(name="thread_1", target=consult, args=(1, )) # Create a thread for the consult function with ID 1
t2 = threading.Thread(name="thread_2", target=save, args=(1, "Testing threads")) # Create a thread for the save function with ID 1 and some data

t1.start()
t2.start()

t1.join()
t2.join()

end_time = datetime.datetime.now()

print("Concurred time: " + str(end_time.second - start_time.second))