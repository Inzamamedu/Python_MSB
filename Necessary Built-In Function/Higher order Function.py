# Higher order function
# function -> (function) / ferurn another function

"""
def square(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5, 6]
square = map(square, numbers)  # function, iterable
print(set(square))
"""

"""
def my_map(any_function, items):
    final_result = []
    for i in items:
        x = any_function(i)
        final_result.append(x)
        final_result.append(x)
    return final_result


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5, 6]
print(my_map(square, numbers))

"""

def my_map(any_function, items):
    final_result = []
    for i in items:
        #x = any_function(i)
        #final_result.append(x)
        final_result.append(any_function(i))
    return final_result


numbers = [1, 2, 3, 4, 5, 6]
print(my_map(lambda num: num ** 2, numbers))








