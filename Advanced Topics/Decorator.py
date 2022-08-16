"""
def common_function(any_function):
    def wrap_function():
        print("This function is awesome")
        any_function()
    return wrap_function


def msg1():
    print("This is function 1")


def msg2():
    print("This is function 2")

# old way
x = common_function(msg1)
x()

print()
# old way
y = common_function(msg2)
y()
"""

def common_function(any_function):
    def wrap_function():
        print("This function is awesome")
        any_function()
    return wrap_function


def msg1():
    print("This is function 1")


def msg2():
    print("This is function 2")


def msg3():
    print("This is function 3")


@common_function
def msg3():
    print("This is function 3")

# old way
x = common_function(msg1)
x()

print()
# old way
y = common_function(msg2)
y()

msg3()