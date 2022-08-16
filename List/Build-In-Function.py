"""
my_list = ["Bangladesh", "Sun", 28, 40, "Sun"]

print(my_list.count(20))
print(my_list.count("Sun"))
print(my_list.count("Bangladesh"))

print("Initial list:", my_list)

my_list.reverse()
print("Reversed list:", my_list)  # ai khana .reverse() function prit and variable ar modda use kora jai na tai aga function call kora hoi ca
"""

"""
# ar ak ta upai asa reverse kora jai
my_list = ["Bangladesh", "Sun", 28, 40, "Sun"]
print("Initial list:", my_list)

print(my_list[::-1])
"""
"""
# ai bara amra maximum ,minimum,sum ber korbo

int_list = [50, 60, 3, 10, 13]

print("Minimum value:", min(int_list))
print("Maximum value:", max(int_list))

print("Summation of list item:", sum(int_list))
"""

"""
# sort()

int_list = [10, 60, 3, 85, 45]
print("Initial list:", int_list)

int_list.sort()
print("integer sorted list:", int_list)  #ai function o print or variable ar modda use kora jai na
"""

"""
float_list = [50.36, 69.54, 74.458, 3.1416, 5.278]
print("Initial list:", float_list)

float_list.sort()
print("sorted float list:", float_list)
"""

"""
mixed_list = [3.1416, 2, 5.78, 26.35, 7, 1.25, 8]
print("initial list:", mixed_list)

mixed_list.sort()
print("Sorted mixed list:",mixed_list)

"""

"""
capital_string = ["India", "Bangladesh", "Water", "Sea", "Red"]
print("Initial list:", capital_string)

capital_string.sort()
print("Sorted capital strign:", capital_string)
"""

"""
lower_string = ["red", "india", "bhutan", "sea"]
print("Initial list:",lower_string)

lower_string.sort()
print("Sorted lower string:", lower_string)

"""

"""
mixed_string = ["red", "India", "bhutan", "Sea", "water"]
print("Initial list:", mixed_string)

mixed_string.sort()
print("sorted mixed list:",mixed_string)
"""

"""
mixed_string = ["red", "India", "bhutan", "Sea", "water"]
print("Initial list:", mixed_string)

mixed_string.sort(key=str.lower)
print("sorted mixed list:",mixed_string)
"""

"""
mixed_string = ["red", "India", "bhutan", "Sea", "water"]
print("Initial list:", mixed_string)

mixed_string.sort(key=len)
print("sorted mixed list:",mixed_string)
"""

"""
mixed_string = ["red", "India", "bhutan", "xy", "Sea", "water"]
print("Initial list:", mixed_string)

mixed_string.sort(key=str.lower,reverse=True)  #ai khana reverse use korta hola aga condition dea tar por use korta hoba
print("Reversed list:",mixed_string)
"""


# index(item, start range, end range)


my_list = [5, 8, "red", "rice", "red", "water", "red", 8]

print(my_list.index("red"))
print(my_list.index("red",3))
print(my_list.index("red", 5, 7))