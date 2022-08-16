"""
# control statement
# break

i = 1
while i <= 10:
    print(i)
    if i == 6:
        break
    i += 1
print("Out of loop")
"""

"""
for i in range(1, 11):
    print(i)
    if i == 6:
        break

print("Out of loop")
"""

"""
language_name = "Python"
while True:
    name = input("Enter language name: ")
    if name == language_name:
        print("Correct")
        break
    print("Invalid language name")
"""

my_list = [9, 4, 6, 34, 78]
number = int(input("Enter a number that you wanna search: "))

for i in my_list:
    if i == number:
        print(number, "found")
        break
else:
    print(number, "not found")