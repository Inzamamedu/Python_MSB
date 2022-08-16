"""
numbe = 0
if numbe % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

"""

number = 0
while number <= 5:
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number,"is odd")
    number +=  1
"""

"""

#   amra jane ja while loop a increment and decrement use na korla  infinite loop cholta thaka tai ai
# proble solve korar jonna amra break keyword use kora hoica. brake use na korla 10 cross korla infinite loop hoia jato.

target = 10
number = int(input("Enter the number: "))

while number > target:
    print(number, "is grater than", target)
    break
else:
    print(number, "is less than", target)

"""


# input a number
# check the number - int/string (else -> invalid input)
# int -> less than 10 -> (odd / enen ). else -> enter a number which is less than 10

target = 10
number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    while number <= target:
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
        break
    else:
        print("enter a number which is less than 10")
else:
    print("Invalid Input")