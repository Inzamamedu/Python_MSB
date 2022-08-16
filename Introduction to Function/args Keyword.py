# *args
# print()
"""
def summation(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(summation(1, 2, 3, 4, 5, 6))

"""

"""
def summation(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


my_list = [1, 2, 3, 4, 5, 6]
print(summation(*my_list))   # * means unpacking

"""
def summation(*args):
    print(type(args))


summation()