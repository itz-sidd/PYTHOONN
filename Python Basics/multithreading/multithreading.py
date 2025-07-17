#Multithreading
#When to use it
#I/O bound tasks
#Concurrent execution

import threading
import time

def print_num():
    for i in range(5):
        print(f"Number:{i}")

def print_letter():
    for letter in "abcdefgh":
        print(f"Letter:{letter}")


t=time.time()
print_num()
print_letter()
finished_time=time.time()-t
print(finished_time)