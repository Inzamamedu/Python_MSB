def decor_function(any_func):
    def wrap_function(*args, **kwargs):
        print("This function is awesome")
        return any_func(*args, **kwargs)

    return wrap_function


@decor_function
def add(a, b):
    return a + b


print(add(5, 6))