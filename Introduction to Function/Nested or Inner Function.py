# Nested Function / Inner Function
"""
def outer_function():
    print("1st line of outer function")

    def inner_function():
        print("This is inner function")

    inner_function()
    print("2nd line of outer function")


outer_function()


"""

def outer_function(rcv):
    print("1st line of outer function")

    def inner_function():
        print(f"Hello {rcv}")

    inner_function()
    print("2nd line of outer function")


msg = "World!"
outer_function(msg)

# closure