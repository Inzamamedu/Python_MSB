"""
# program 1

x = None
print(x)
"""

"""
# program - 2
x = None

if x is None:   # Checking if the variable is None
    print("x is None")
else:
    print("Not None")

"""

"""
# program - 3
print(None is None)
"""

"""
# program - 4
print(None is False)

"""

"""
# program - 5
text = ""   # empty string

print(text is None)
"""

"""
# program - 6
a = None
b = None
print(id(None))
print(id(a))
print(id(b))

"""

"""
#program - 7
def fun():
    print("Hello World")


a = fun()
print(a)
print(id(a))
print(type(a))
"""
"""
# default value
def add(a, b, c=None):  # None means c is optional and it must in the last parameter
    return a + b + c


print(add(4, 5, 7))
"""

"""
# a = 1
# args = 2, 3, 4 (start,end)
# c = 4
def add(a, *args, c=None):  # variable first position, args and None as usual
    # a will not add because we didn't use it
    # c will not work
    total = 0
    for i in args:
        total += i
    return total

print(add(1, 2, 3, 4))
"""

# a = 1
# c = 2
# args = 3, 4
def add(a, c=None, *args, **kwargs):   # variable first position,args and none as usual
    # a, c will not add because we didn't use them
    total = 0
    for i in args:
        total += i
    # total += c
    return total


print(add(1, 2, 3, 4, {k:v}))
