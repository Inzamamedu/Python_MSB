
# alla()
# list, tuple, set, dictionary
"""
print(all([True, True, True, True]))
print(all([True, True, False, True]))
print(all([False, False, False, False]))
"""

"""
even_list = []
numbers = [2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)


print(even_list)
"""

"""
even_list = []
numbers = [2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    if i % 2 == 0:
        even_list.append(True)


print(even_list)

"""
def sum(*args):
    if all([type(args) == int or type(args) == float for args in args]):
        total = 0
        for i in args:
            total += i
        return total
    return "Invalid Input"


print(sum(5, 7, 8, 9))
print(sum(5, 7, 8, 9, "Python", "ABC"))