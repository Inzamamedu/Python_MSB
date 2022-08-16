"""
# program - 1: get full dictionary
result = {"Bangla": 87,"English": 75,"Mathematics": 81, "Physics": 78}
result_dict = dict()
for k, v in result.items():
    result_dict[k] = v
print(result_dict)


result = {"Bangla": 87,"English": 75,"Mathematics": 81, "Physics": 78}
result_dict = {k:v for k, v in result.items()}
print(result_dict)
"""

"""
# program - 2: square the key
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num**2
print(square_dict)

sqr = {num: num**2 for num in range(1, 11)}
print(sqr)

"""

"""
# program - 3: get only even even values pair (if condition)
class_roll = {"Abir": 26, "Rudra": 11, "Mithu": 81,"Mimi": 78}
class_roll_dict = dict()
for k, v in class_roll.items():
    if v % 2 == 0:
        class_roll_dict[k] = v
print(class_roll_dict)

class_roll2 = {"Abir": 26, "Rudra": 11, "Mithu": 81,"Mimi": 78}
class_roll_compress = {k: v for k,v in class_roll2.items() if v % 2 == 0}
print(class_roll_compress)

"""

"""
# program - 4: nested if conditional logic
age = {"Peter": 38,"Siyam": 48, "Rida": 27, "Jason": 33, "Coper":57}
age_dict = {}
for k,v in age.items():
    if v % 2 != 0:
        if v < 40:
            age_dict[k] = v
print(age_dict)

age2 = {"Peter": 38,"Siyam": 48, "Rida": 27, "Jason": 33, "Coper":57}
age_dict = {k: v for k,v in age2.items() if v % 2 != 0 if v < 40}
print(age_dict)

"""

# program - 5: if else conditional logic
age = {"Peter": 38,"Siyam": 48, "Rida": 27, "Jason": 33, "Coper":57}
age_dict = dict()
for k, v in age.items():
    if v > 40:
        age_dict[k] ="Old"
    else:
        age_dict[k] = "Young"
print(age_dict)

# conditional logic (output), collection

age2 = {"Peter": 38,"Siyam": 48, "Rida": 27, "Jason": 33, "Coper":57}
age_dict_com = {k: "Old" if v > 40 else "Young" for k, v in age2.items()}
print(age_dict_com)