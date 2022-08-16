"""
def square(num):
    return "Squre of", number, "is", number ** 2


number = int(input("Enter a number to square: "))
print(square(number))   # ai khana print use korar fola tuple akara print hoi ca ai priblem solve korar jonna amra 3
                         # 3 num line a return ar pora print use korbo
"""
"""
def square(num):
    return print("Squre of", number, "is", number ** 2)


number = int(input("Enter a number to square: "))
square(number)
"""

# ai tar aro 1 ta vaba kora jai oi ta holo:
"""
def square(num):
    return print("Squre of", number, "is", number ** 2)


number = int(input("Enter a number to square: "))
final_output = square(number)

print(final_output)
"""
"""
# aro ak vaba kora jai

def square(num):
    return number ** 2


number = int(input("Enter a number to square: "))
final_output = square(number)

print("Squre of", number, "is", final_output)
"""


# ai bar amra dakhbo ak ta function ka ki vaba bar bar reuse kora jai mana ak ta operation dea bar bar use kora

def square(num):
    return number ** 2


number = int(input("Enter a number to square: "))
print("Squre of", number, "is", square(number))

number = int(input("Enter a number to square: "))
print("Squre of", number, "is", square(number))

number = int(input("Enter a number to square: "))
print("Squre of", number, "is", square(number))


