# #Processing that runs parallely

# import multiprocessing
# import time


# def sq():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Square:{i*i}")

# def cube():
#     for i in range(5):
#         time.sleep(1.5)
#         print(f"Cube:{i**3}")

# if __name__=="__main__"

# #Creating 2 processes
# p1=multiprocessing.Process(target=sq)
# p2=multiprocessing.Process(target=cube)
# t=time.time()

# #Starting the process
# p1.start()
# p2.start()

# #Waiting for it to complete
# p1.join()
# p2.join()

# finished_time=time.time()-t
# print(finished_time)



#ThreafdPOol Executor
# from concurrent.futures import ThreadPoolExecutor
# import time

# def print_number(number):
#     time.sleep(1)
#     return f"Number : {number}"

# numbers=[1,2,3,4,5]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(print_number,numbers)

# for result in results:
#     print(result)

from concurrent.futures import ProcessPoolExecutor
import time

def sq_num(number):
    time.sleep(1)
    return f"Square : {number*number}"

numbers=[1,2,3,4,5,6,7,8,9]

if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(sq_num,numbers)

    for result in results:
        print(result)