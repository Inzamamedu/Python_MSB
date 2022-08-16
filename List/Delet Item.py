# index: _delitem_(), del
# item: remove(), pop()
# list: clear()

"""
# index: _delitem_() use hoia ca

my_list = [10, "Sun", "Water", 65.87, "Biriyani", 354, "abc", "xyz", "rice"]
print("Initial list:",my_list)

my_list.__delitem__(4)
my_list.__delitem__(2)  #akhon jode amra 7 number index ka remove korta chai ta hola hoba na karon ar aga amra 2 ta hemove kora dea ce tai 7 num index ka remove korta hola 7 thak 2 minus korta hoba orthakt bracket ar modda 5 deta hoba
my_list.__delitem__(5)  # abar ai rokom na lekha sobar aga likhla tokhon index 7 deali xyz remove hoi jai to

print("Updated list:",my_list)
"""

"""
# del key word use korbo

my_list = [10, "Sun", "Water", 65.87, "Biriyani", 354, "abc", "xyz", "rice"]
print("Initial list:",my_list)

del my_list[3]
del my_list[4]

print("Updated list:",my_list)
"""

"""
# item: remove()

my_list = [10, "Sun", "Water", 65.87, "Biriyani", 354, "abc", "xyz", "rice"]
print("Initial list:",my_list)

my_list.remove("Sun")
print("Updated list:",my_list)
"""

"""
# pop()

my_list = [10, "Sun", "Water", 65.87, "Biriyani", 354, "abc", "xyz", "rice"]
print("Initial list:",my_list)

my_list.pop()  # pop function ak bara last thaka ak ta ak ta kora delete kora
my_list.pop()
my_list.pop()

print("Updated list:",my_list)
"""

"""
# del


my_list = [10, "Sun", "Water", 65.87, "Biriyani", 354, "abc", "xyz", "rice"]
print("Initial list:",my_list)

del my_list[1:5]  #sun to biriynii porjonto nai kora deba  [ n-1]

print("Updated list:",my_list)
"""

#

my_list = [10, "Sun", "Water", 65.87, "Biriyani", 354, "abc", "xyz", "rice"]
print("Initial list:",my_list)

my_list.clear()

print("Updated list:",my_list)