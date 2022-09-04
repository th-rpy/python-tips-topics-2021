import numpy as np 
import timeit # for timing 
import random 
import matplotlib.pyplot as plt
arr_num = [2000, 2500, 3000, 4000, 5000, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 
           11000, 11500, 15000]
arr_time, arr_time2 = [], []
loop_num = 1500

def normal_func():
    for _ in range(loop_num): # loop_num times
        random.random() # Referencing the module every time to find the random() method
        
#print("Normal function: ", timeit.timeit(normal_func, number=loop_num))
for i in arr_num:
    arr_time.append(timeit.timeit(normal_func, number=i))
    
# Optimized function by cache=ing the method call
def optimized_func():
    rnd  = random.random # caching the method call on an object to avoid the method call every time. 
    for _ in range(loop_num):
        rnd() 
        
      
for i in arr_num:
    arr_time2.append(timeit.timeit(optimized_func, number=i))  
#print("Optimized function: ", timeit.timeit(optimized_func, number=loop_num))

plt.plot(arr_num, arr_time, label = "Normal function")
plt.plot(arr_num, arr_time2, label = "Optimized function")
plt.xlabel("Number of calls the function") 
plt.ylabel("Time(s)")
plt.legend()
plt.show()