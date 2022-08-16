"""
my_tuple = (10, 20, 30, 20, 25)

print("summation of tuple items:", sum(my_tuple))
print("Length of Tuple:", len(my_tuple))

print("Average:", sum(my_tuple) / len(my_tuple))

print("Reversed Tuple:", my_tuple[::-1])

print(my_tuple.count(20))
"""

"""
my_tuple = (10, 20, 30, 20, 25)
new_list = list(my_tuple)

print(type(my_tuple))
print(type(new_list))
print(new_list)
print(my_tuple)
"""

# list to touple
my_list = [10, 20, 30, 20, 20]
print(type(my_list))
new_tuple = tuple(my_list)

print(new_tuple)
print(type(new_tuple))