"""
my_dictionary = {"Name": "john", "age": 20, "address": "new york,usa", 2: 34}

# membership operator: in,not in

print("Name" in my_dictionary)
print("age" in my_dictionary)   #  ai gula keys dhora kaj kora

print("john" not in my_dictionary)
print("Name") not in my_dictionary
"""


# ai basr values dhora kaj korbo
my_dictionary = {"Name": "john", "age": 20, "address": "new york,usa", 2: 34}

print("john" in my_dictionary.values())
print(20 not in my_dictionary.values())
print("new york,usa" in my_dictionary.values())