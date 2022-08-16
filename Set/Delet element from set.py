"""
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Initial Set:",my_set)

my_set.remove(7)
# my_set.remove("Apple")  # ai khana remove function ar modda apple valut use kora hoi ca ja set ar modda nai vai ai khana error dakhaba  kintu discard function use korla error dakhai to na
my_set.discard("Apple")  # discard ar shubhedha holo set ar modda item thakla remove korba nar jode nau thaka  tar poro error dakhaba na
print("After Updating Set:", my_set)
"""

"""
my_set = {"Python", "banana", "apple", "guva", "mango"}
print("Initial set:", my_set)

print(my_set.pop())
print(my_set)

print(my_set.pop())
print(my_set)

print(my_set.pop())
print(my_set)
"""

my_set = {"Python", "banana", "apple", "guva", "mango"}

my_set.clear()
print(my_set)