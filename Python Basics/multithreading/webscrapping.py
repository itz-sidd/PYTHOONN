

# import threading
# import requests
# from bs4 import BeautifulSoup

# urls=[
# 'https://www.langchain.com/langgraph',

# 'https://blog.langchain.com/',

# 'https://python.langchain.com/docs/introduction/',
# ]


# def fetch_content(url):
#     response=requests.get(url)
#     soup=BeautifulSoup(response.content,'html.parser')
#     print(f'fetch {(len(soup.text))} charcters from {url}')

# threads=[]

# for url in urls:
#     thread=threading.Thread(target=fetch_content,args=(url,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("All web-pages fetched")


###Real World example

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

#Function to compute factorial of s given number

def computer_factorial(number):
    print(f"Computing fsctorial of {number}")
    result=math.factorial(number)
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000,8000]

    start_time=time.time()

    #Creating a pool of work process
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time Takem: {end_time - start_time} seconds")