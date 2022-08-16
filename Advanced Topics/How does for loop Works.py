"""
my_list = [1, 2, 3, 4]  # iterable

for number in my_list:
    print(number)
"""

"""
my_list = [1, 2, 3, 4]  # iterable
number = iter(my_list)

print(next(number))
print(next(number))
print(next(number))
print(next(number))
# print(next(number))  # stopIteration
"""

"""
my_list = [1, 2, 3, 4]  # iterable
number = iter(my_list)


while True:
    try:
        print(next(number))
    except StopIteration:
        break
"""

my_list = [1, 2, 3, 4]  # iterable

for number in my_list:
    print(number)

my_list = [1, 2, 3, 4]  # iterable
number = iter(my_list)


while True:
    try:
        print(next(number))
    except StopIteration:
        break
