"""
# map(function, iterables)
def square(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5, 6]
square = map(square, numbers)  # function, iterable
print(set(square))
"""

"""
numbers = [1, 2, 3, 4, 5, 6]


squares = map(lambda num: num ** 2, numbers)
print(set(squares))
"""

country = ["Bangladesh", "Bhutan", "Nepal"]
country_name_length = map(len, country)   # map onak fast loop ar thaka tai amra map use korbo
print(list(country_name_length))