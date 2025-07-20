#Multithreading
#When to use it
#I/O bound tasks
#Concurrent execution

import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcdefgh":
        time.sleep(2)
        print(f"Letter:{letter}")


t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_letter)


t=time.time()

#Starting the thread
t1.start()
t2.start()

#Waiting for thread to complete
t1.join()#This is multithreading
t2.join()

# print_num()#This is simple threading
# print_letter()
finished_time=time.time()-t
print(finished_time)