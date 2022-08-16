"""
def summation(number1, number2):
    return number1 + number2


print(summation(50, 60))
"""
"""
summation = lambda number1, number2, number3, number4: number1 + number2 + number4 + number4

print(summation(20, 30, 10, 10))
"""
"""
def is_even(number):
    return number % 2 == 0


print(is_even(5))
print(is_even(4))
"""
"""
# ai bar amra uporar program lambda dea korbo

is_even = lambda number: number % 2 == 0


print(is_even(7))
print(is_even(10))
"""

"""
def password_digit_checker(password):
    if len(password) >= 6:
        return True
    else:
        return False


my_pass = "India"  # ai khana bangladesh use korla true hoba
print(password_digit_checker(my_pass))

"""

"""
password_digit_checker = lambda password: len(password) >= 6


my_pass = "Bangladesh"
print(password_digit_checker(my_pass))
"""

# ai bar amra uotput a true false ar poreborta text print korbo

password_digit_checker = lambda password: "Password is accepted" if len(password) >= 6 else "Password less than 6 digit"


my_pass = "Bangladesh"
print(password_digit_checker(my_pass))