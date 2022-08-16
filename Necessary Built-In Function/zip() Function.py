# zip(list, list)
"""
l1 = ["user1", "user2", "user3", "user4"]
l2 = ["Aditta", "Niyamul", "Rudra"]

pair = dict(zip(l1, l2))
print(pair)
"""

"""
# user = ["user1", "user2", "user3", "user4"]
f_name = ["Inzamam", "Abdul", "Alim"]
l_name = ["Ul", "Alim", "Mondol"]

pair = tuple(zip(f_name, l_name))
print(pair)
print(type(pair))

"""

"""
l1 = [(1, 2, 7), (3, 6, 4), (5, 9, 6), (7, 0, 8)]
unpacking_my_list = list(zip(*l1))
print(unpacking_my_list)

"""

"""
my_list = [(1, 2, 7), (3, 6, 4), (5, 9, 6), (7, 0, 8)]
l1, l2, l3 = list(zip(*my_list))

print(l1)
print(l2)
print(l3)
"""

l1 = [1, 3, 5]
l2 = [2, 4, 6]

max_pair_list = []
min_pair_list = []

for i in zip(l1, l2):
    max_pair_list.append(max(i))

for i in zip(l1, l2):
    min_pair_list.append(min(i))


print("Max pair list:", max_pair_list)
print("Min pair list:", min_pair_list)