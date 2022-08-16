# list comprehension
# iterator, iterator object

# sequence -> iterator : list , set, dictionary
# process: comprehension

# 1 -10  1. range() 2. loop(for, while)

# ak ta list Comprehension ar 3 ta jinish : output, collection (for loop data), conditional logic

"""
my_list = list(list(range(1, 11)))
print(my_list)

new_list = []
for i in range(1, 11):
    new_list.append(i)
print(new_list)
"""

"""
my_list = [i for i in range(1, 11)]
print(my_list)
"""

"""
my_list = [i for i in range(-1, -11, -1)]
print(my_list)
"""
"""
name = ["Aditta", "Rock", "John"]
new_name = []
for i in name:
    new_name.append(i[0])
print(new_name)
"""

"""
name2 = ["Aditta", "Rock", "John"]  # list comprehension
my_name = [i[0] for i in name2]

print(my_name)
"""

"""
name1 = ["Aditta", "Rock", "John"]
rev_name = []
for i in name1:
    rev_name.append(i[::-1])
print(rev_name)
"""

"""
name2 = ["Aditta", "Rock", "John"]  # using list comprehension
rev_name2 = [i[::-1]for i in name2]
print(rev_name2)

"""

"""
name2 = ["Aditta", "Rock", "John"]  # using list comprehension
rev_name2 = [i[::-1]for i in name2][::-1]
print(rev_name2)

"""

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr = []
for i in numbers:
    sqr.append(i**2)
print(sqr)
"""

"""
# list comprehension ar maddoma
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr = [i**2 for i in numbers]
print(sqr)
"""

"""
# conditional logic : if , if else
even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
"""
"""
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)
"""

"""
even_numbers = []
odd_nubbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_nubbers.append(i)

print(even_numbers)
print(odd_nubbers)

"""

# jode if else 2 ta ak shata chola asa ta hola formula change haia jaba
# ak ta list Comprehension ar 3 ta jinish : output, conditional logic, collection (for loop data)

even_numbers = []
odd_nubbers = []

numbers = [even_numbers.append((i) if i % 2 == 0 else odd_nubbers.append(i) for i in range(1, 11)]

print(even_numbers)
print(odd_nubbers)