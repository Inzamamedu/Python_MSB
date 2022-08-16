# filter() -> function, iterable
"""
def is_even(num):
    return num % 2 == 0


numbers = [5, 4, 7, 3, 9, 1, 2, 8]
evens = filter(is_even,numbers)
print(set(evens))
"""

"""
numbers = [5, 4, 7, 3, 9, 1, 2, 8]
evens = filter(lambda num: num % 2 == 0, numbers)
print(list(evens))
"""

numbers = [5, 4, 7, 3, 9, 1, 2, 8]
evens = [i for i in numbers if i % 2 == 0]
print(tuple(evens))