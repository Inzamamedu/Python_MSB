"""
my_dict = {"Name": "Inzamam", "Country": "Bangladesh", 1: "Python", "Programming":{"a": "Java", "b": "Python"}}

print("Initial Dictionary:", my_dict)

del my_dict[1]
print(my_dict)

del my_dict["Programming"]["a"]
print("Updated Dictionary:", my_dict)

"""

my_dict = {"Name": "Inzamam", "Country": "Bangladesh", 1: "Python", "Programming":{"a": "Java", "b": "Python"}}

print("Initial Dictionary:", my_dict)

my_dict.clear()
print(my_dict)  # ai khana dictonary ar sob item ka delete kora deba but dictonary thakba

del my_dict
print("Updated Dictionary:", my_dict)  # ar ai khana full dictonary kai delet kora deba ai error a dakhaba ja ai "my_dict" nama kono dict nai