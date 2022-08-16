# add()

"""
my_set = {1, 2, 3}
print("Initial set:",my_set)

my_set.add(5)
my_set.add(7)
my_set.add(8)
print("Updated set:",my_set)
"""

"""
my_set = {1, 2, 3}
print("Initial set:",my_set)

my_set.add((5, 6, 7))
print("Updated set:", my_set)
"""

my_set = set()

for i in range(1, 6):  # end: n-1 (6-1)
    my_set.add(i)
print(my_set)