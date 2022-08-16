
from functools import wraps

def filter_data_type_allow(data_type):
    def data_type_allow(any_function):
        @wraps(any_function)
        def wrap_function(*args):
            if all(type(item) == data_type for item in args):
                return any_function(*args)
            return "Invalid Arguments"
        return wrap_function
    return data_type_allow



@filter_data_type_allow(int)
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1, 2, 3, 4, 5, 6))


@filter_data_type_allow(float)
def float_add_all(*args):
    total = 0.0
    for i in args:
        total += i
    return total


print(float_add_all(3.3, 5.26, 3.755))



@filter_data_type_allow(str)
def string_join(*args):
    joined = ""
    for i in args:
        joined += i
    return joined


print(string_join("I", "love", "Python","programming"))