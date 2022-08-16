# 3 element : output, collection, conditional logic
# if else: output(conditional logic), collection

"""
# progam - 1
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
blank_set = set()
for i in my_set:
    blank_set.add(i*3)
print("Initial set:", my_set)
print("New Set:", blank_set)

my_set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_set = {i * 3 for i in my_set2}
print(new_set)

"""

"""
# Program - 2
my_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100 }
blank_set = set()
for i in my_set:
    if i >= 50:
        blank_set.add(i)

print("Initial Set:",my_set)
print("New Set:",blank_set)

my_set2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100 }
new_set = {i for i in my_set if i >= 50}
print(new_set)

"""

"""
# Program - 3
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
blank_set = set()
for i in my_set:
    if i % 2 == 0:
        blank_set.add(i*3)

print("Initial Set:",my_set)
print("New set:", blank_set)

my_set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_set = {i * 3 for i in my_set2 if i % 2 == 0}
print(new_set)

"""

# Program - 4
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = set()
odd_set = set()
for i in my_set:
    if i % 2 == 0:
        even_set.add(i)
    else:
        odd_set.add(i)

print("Even set:", even_set)
print("Odd_Set", odd_set)


my_set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set2 = set()
odd_set2 = set()

new_set = {even_set2.add(i) if i % 2 == 0 else odd_set2.add(i) for i in my_set2}
print(even_set2)
print(odd_set2)