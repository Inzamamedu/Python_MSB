"""
# Checking name is title
name = "inzamam haque"

print("Initial Name:", name)

if not name.istitle():
    name = name.title()
print("After Capitalized:", name)
"""

"""
#Odd even number check
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
"""

"""
# positive negitive number check
number = int(input("Enter the number: "))

if number >= 0:
    print("Positive")
else:
    print("Negative")
"""

"""
# Vowel consonent check
character = input("Enter a character to check vowel: ")
vowel = "AaEeIiOoUu"

if character >= "A" and character <= "Z" or character >= "a" and character <= "z":
    if character in vowel:
        print("vowel")
    else:
        print("Consonant")
else:
    print("Invalid character")
"""

# Find out the largest number among three
number1 = 17
number2 = 78
number3 = 41

#number1 = float(input("Enter first number: "))
#number2 = float(input("Enter second number: "))
#number3 = float(input("Enter third number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

print("The largest number is", largest)
