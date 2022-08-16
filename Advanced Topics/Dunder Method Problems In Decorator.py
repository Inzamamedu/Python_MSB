"""
from functools import wraps

def decor_function(any_func):
    @wraps(any_func)
    def wraps_function(*args, **kwargs):
# This is a wrap function
        print("This function is awesome")
        return any_func(*args, **kwargs)

    return wraps_function


@decor_function
def add(a, b):
#This add function takes 2 parameter and returns summation
    return a + b


print(add.__doc__)
print(add.__name__)
"""

from functools import wraps

def decor_function(any_func):
    @wraps(any_func)
    def wraps_function(*args, **kwargs):
        """ This is a wrap function """
        print(f"You are calling {any_func.__name__} function")
        print(any_func.__doc__)
        return any_func(*args, **kwargs)

    return wraps_function


@decor_function
def add(a, b):
    """This add function takes 2 parameter and returns summation"""
    return a + b


print(add(7, 8))