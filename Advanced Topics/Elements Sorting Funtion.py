# sort() => list

# sorted() => tuple,set,dictionary

x = ["Guva", "Banana", "Mango", "Apple"]
print(type(x))
x.sort()  # only for list
print(x)

y = ("Guva", "Banana", "Mango", "Apple")
print(type(y))
print(sorted(y))  # sorted() => for tuple

z = [
    {"Name": "Napa", "Price": 10},
    {"Name": "Ace+", "Price": 30},
    {"Name": "Omidon", "Price": 20},
    {"Name": "Napa Rapid", "Price": 15},
]

print(sorted(z, key=lambda p: p.get("Name")))
print(sorted(z, key=lambda p: p.get("Name"), reverse=True))

s = {"Guva", "Banana", "Mango", "Apple"}
print(type(s))
print(sorted(s))