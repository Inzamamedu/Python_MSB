# append(), insert(), extend()
# manual
"""
# append ar use
my_list = [10, "Python", "Biryani", 45.22]
print("Initial List:",my_list)

my_list.append("hello")  # append function ar kaj holo pasha pashe bosha mana last thaka add hoia  pasha pashe bosha
my_list.append(100)

print("updated list:",my_list)
"""

"""
# insert use
my_list = [10, "Python", "Biryani", 45.22]
print("Initial List:",my_list)

my_list.insert(1,"Sea")  #index, item  (insert ak ta ak ta kora item insert kora )
my_list.insert(4,100)

print("Updated List:",my_list)
"""

""" 
# extend ar ak ta neom
my_list_1 = [10, "Python", "Biryani", 45.22]
my_list_2 = ["Sea", "Hello", 3.1416, 90]

my_list_1.extend(my_list_2)

print("updated list:",my_list_1)
"""

"""
# extend ar aro ak ta neom
my_list_1 = [10, "Python", "Biryani", 45.22]

my_list_1.extend(["Sea", "Hello", 3.1416, 90])  # ai khana varible use na koa extend function use kora hoi ca.

print(my_list_1)
"""


#extend manual use

my_list_1 = [10, "Python", "Biryani", 45.22]
my_list_2 = ["Sea", "Hello", 3.1416, 90]

print(my_list_1 + my_list_2)


