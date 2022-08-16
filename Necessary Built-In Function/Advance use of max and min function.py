"""
numbers = [1, 3, 2, 6, 5, 4, 7, 9, 8]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
"""


"""
names = ["Niyab", "Rock", "Ali"]

print(min(names, key=len))
print(max(names, key=len))
"""

"""
std = {
    "Niyan":{"score": 98, "serial": 30},
    "Aditya": {"score": 10, "serial": 25},
    "Peter": {"score": 50, "serial": 22}
}

print(type(std))

print(max(std, key=lambda x: std[x]["score"]))
print(min(std, key=lambda  item: std[item]["score"]))

"""

std = {
    "Niyan":{"score": 98, "serial": 30},
    "Aditya": {"score": 10, "serial": 25},
    "Peter": {"score": 50, "serial": 22}
}
                                                     # run hoi na error dakhai
print(type(std))

print("Maximum Score Data:", max(std, key=lambda item: item.get("Score")))
print("Maximum Score Person Name:", max(std, key=lambda item: item.get("Score"))["Name"])


print("Minimum Score Data:", min(std, key=lambda item: item.get("Score")))
print("Minimum Score Person Name:", min(std, key=lambda item: item.get("Score"))["Name"])
