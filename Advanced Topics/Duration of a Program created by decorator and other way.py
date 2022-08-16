"""
import time
from functools import wraps

# 0.18555259704589844 -> decor with list comprehension

def decor_function(any_function):
    @wraps(any_function)
    def wrap_function(*args, **kwargs):
        print(f"Executing ------> {any_function.__name__} function")
        start = time.time()
        result = any_function(*args, **kwargs)
        end = time.time()
        total_time = end-start
        print(f"This function took {total_time} seconds")
        return result
    return wrap_function


@decor_function
def square(n):
    return [x ** 2 for x in range(1, n+1)]


square(1000000)

"""
"""
import time
from functools import wraps

n = 1000000
start = time.time()
n = [x ** 2 for x in range(1, n+1)]
end = time.time()
total_time = end - start
print(f"This function took {total_time} seconds")
"""
import time
from functools import wraps

start = time.time()
for x in range(1, 1000001):
    r = x ** 2
end = time.time()
total_time = end - start
print(f"This function took {total_time} seconds")