# Dunder Method => Double Under (Underscore)
# Magic Method
# Function

# Print(sum([2, 3, 4, 5, 6, 7, 8]))
# x = sum([2, 3, 4, 5, 6, 7, 8])
# print(x)

def add(num1, num2):
    """This is add Function. It took 2 parameter and returns their summation"""
    return num1 + num2


x = add
print(x)
print(add)
print(x.__name__)
print(add.__name__)
print(sum.__doc__)
print(add.__doc__)
print(len.__doc__)
