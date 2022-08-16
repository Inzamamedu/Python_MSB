my_dict = {1: "Python", "Bangla": "A+", 4: 96, "English": 78}
print(my_dict[1])
print(my_dict["Bangla"])


my_dict = {1: "welcome", 2: "to", 3:{"a": "Python", "b": "programming"}}
print(my_dict[3]["a"])
print(my_dict[3]["b"])

print(my_dict.get(24))  # ai khana .get() function use korar mana hoilo ai khana key 24 nai but kono error dakhassa na .ai error thaka bachar jonna ger function use kora hoi
print(my_dict.get(24, "Not found"))   # ar get function ar moda multi-dimensional  suppert korana
                                      #like: print(my_dict.get[3]["a"]))

print("Hello")