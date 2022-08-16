
from functools import wraps


def int_data_type_allow(any_function):
    @wraps(any_function)
    def wrap_function(*args):
        data_type = []
        for item in args:
            data_type.append(type(item) == int)
        if all(data_type):
            return any_function(*args)
        else:
            return "Invalid items"
    return wrap_function


@int_data_type_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1, 2, 3, 4, 5, 6))



"""
from functools import wraps



def int_data_type_allow2(any_function):
    @wraps(any_function)
    def wrap_function(*args):
        if all(type(item) == int for item in args):
            return any_function(*args)
        return "Invalid Arguments"
    return wrap_function


@int_data_type_allow2
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1, 2, 3, 4, 5, 6))
"""