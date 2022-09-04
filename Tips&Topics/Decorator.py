import time # import time module

# Timer Decorator for measuring the time taken by a function to execute. 
def timer (func):
    def wrap_func(*args, **kwargs): # wrap_func is the wrapper function
        start = time.time() # start is the start time of the function
        res = func(*args, **kwargs) # res is the result of the function
        end = time.time() # end is the end time of the function
        wrap_func.time = end-start # wrap_func.time is the time taken by the function to execute
        return res # return the result of the function
    wrap_func.time = 0 
    return wrap_func  # return the wrapper function

# Using the above decorators, write a function that computes the Fibonacci number of a given number. 
l = [] 
@timer
def fib(n):
    assert n >= 0, "n must be >= 0"
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

# Call the function fib . 
print(fib(25)) # 75025
print("Fibonacci Function took %f seconds" % fib.time) # Fibonacci Function took 0.568558 seconds

#################################################################################################

from collections import Counter

# Count Calls Decorator for counting the number of times a function is called.
def count_calls(func):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return func(*args, **kwargs)
    wrapped.calls = 0
    return wrapped 

# Count the number of times fib is called without using the count_calls decorator.
def fib(n):
    global counted
    assert n >= 0, "n must be >= 0"
    if n in [0, 1]:
        return n
    counted+=1
    return fib(n - 1) + fib(n - 2)

counted = 0
print(fib(25)) # 75025
print("Fibonacci Function is called %i times" % counted) # Fibonacci Function is called 121392 times.

# Count the number of times fib is called without using the count_calls decorator.
@count_calls
def fib(n):
    assert n >= 0, "n must be >= 0"
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(25)) # 75025
print("Fibonacci Function is called %i times" % fib.calls) # Fibonacci Function is called 121392 times.