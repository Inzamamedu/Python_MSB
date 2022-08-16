"""
# closures

# Nested Function

def outer_func():
    print("Hello, I'm inner function.")

    inner_func()


outer_func()
"""

"""
# way -1
def outer_func():
    print("Hello, I'm inner function.")

    def inner_func():
        print("Hello, I'm inner function.")


        return inner_func


outer_func()()

"""

"""

# way -2
def outer_func():
    print("Hello, I'm outer function.")

    def inner_func():
        print("Hello, I'm inner function.")


        return inner_func

x = outer_func()
outer_func()

"""
# Rules of clusures
# 1. must carry an inner/Nested function
# 2. return => Inner function
# 3. No parenthesis in return

"""
def outer_func(msg):
    # print("Hello, I'm outer function.")

    def inner_func():
        print(f"Hello, I'm {msg}")


    return inner_func


x = outer_func("Inzamam")
x()
"""


"""
# x ^ n, 2 ^ 4 = 2 x 2 x 2 x 2
def to_power(number):

    def calc_power(power):
        return number ** power

    return calc_power


num = to_power(2)
print(num(4))

queeb = to_power(3)
print(queeb(3))

square = to_power(5)
print(square(2))

"""

"""
# x ^ n, 2 ^ 4 = 2 x 2 x 2 x 2
def to_power(number1):

    def calc_power(power):
        return number1 ** power

   # return calc_power


   def multiplication(number2):
       return number1 * number2

   return multiplication


x = to_power(5)
print(x(6))

num = to_power(2)
# print(queeb(3))

queeb = to_power(3)
# print(queeb(3))

square = to_power(5)
# print(square(2))

"""