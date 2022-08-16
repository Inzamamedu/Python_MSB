"""
names = ["Peter", "Rock", "Milli"]
position = 0
for name in names:
    print(f"{position}---------->{name}")
    position += 1
"""

"""

names = ["Peter", "Rock", "Milli"]


for position, name in enumerate(names):  # position, item
   #print(f"{position}---------->{name}")
    print(f"{name}---------->{position}")
"""

names = ["Peter", "Rock", "Milli"]


def position_finder(name, targer):
    for position, name in enumerate(name):
        if targer == name:
            return position
    return "Not found"


print("The position of Milli:", position_finder(names, "Milli"))
print("The position of Python:", position_finder(names, "Python"))
