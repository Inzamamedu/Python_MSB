def square():
    number = int(input("Enter a number to square: "))
    print("Squre of", number, "is", number ** 2)


square()     # function call korar somoy khaial rakhta hoba ja 2 line gap rakhta hoba

"""
process:
1. data
2. function -> process
3. return output

"""

def square(num):  # parameter | paremeter and argument  ar nam kokhonoi same houa jaba na
    print("Squre of", number, "is", number ** 2)


number = int(input("Enter a number to square: "))
square(number)  # Arguments | argument and parameter ar difference holo:
                 # Arguments : holo jokhon kono function ka call kora variable/data ka pass korahoy tokhon ta argument
                 # parameter : ar jokhon oi variable ta function ar modda recived hoi tokhon ta parameter