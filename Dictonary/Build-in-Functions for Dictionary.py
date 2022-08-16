"""
my_dict = {'Name': 'Inzamam', 'Country': 'Bangladesh', 1: 'python', 2: 'java'}
print(len(my_dict))

new = my_dict.copy()
del new["Country"]
print(new)

print(my_dict)
"""

"""
info = {"name": "unknown", "age": "unkonwn", "address": "unknown"}
print(info)

keys = {"name", "age", "address"}
value = "unkonwn"
person = dict.fromkeys(keys,value)  # ai khana .fromkeys ai function ar kaj holo bar bar ake value asla ai function use korla ak barai kaj sesh hoi ja.
print(person)
"""

"""
my_dict = {'Name': 'Inzamam', 'Country': 'Bangladesh', 1: 'python', 2: 'java'}

print(my_dict.keys())
print(type(my_dict.keys()))

print(my_dict.values())
print(type(my_dict.values()))
"""

"""
# pair akara dakhbo
my_dict = {'Name': 'Inzamam', 'Country': 'Bangladesh', 1: 'python', 2: 'java'}
print(my_dict.items())
print(type(my_dict.items()))
"""

"""
my_dict = {'Name': 'Inzamam', 'Country': 'Bangladesh', 1: 'python', 2: 'java'}
print(my_dict)

my_dict.popitem()
print(my_dict)

"""

int_dict =  {1: "a", 7: "c", 2: "Python", 12: "Java"}
print(sorted(int_dict))

string_dict = {"a": 3.1416, "v": "python", "c": "java", "b": "nothing"}

print(sorted(string_dict))
print(sorted(string_dict, reverse=True))