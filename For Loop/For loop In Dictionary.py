"""

my_dectionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
# keys -> Manual
for i in my_dectionary:
    print(i)

"""

"""
my_dictionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
# built in function -> keys()
for i in my_dictionary.keys():
    print(i)
"""

"""
my_dictionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
# manual
for i in my_dictionary:
    print(my_dictionary[i])
"""

"""
my_dictionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
# built in function -> values()
for i in my_dictionary.values():
    print(i)
"""

"""
my_dictionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
# manual
for i in my_dictionary:
    print(f"{i} : {my_dictionary[i]}")
"""

"""
my_dictionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
# build in function item(). ai khana i ar bodola 2 ta variable use kora hoi ca jata 2 ta item ka access korta para
for k, v in my_dictionary.items():
    print(f"{k} : {v}")
    
    
"""

# ai bar ak line a dict dea kora fala hoi ca.
my_dictionary = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
new_dict = {}
for k, v in my_dictionary.items():
    new_dict[k] = v

print(new_dict)

