# global variable
# global keyword
x = "This is global variable"

def my_function():
    x = 10
    return print("Inside of the function:",x)


my_function()
print("outside of the function:", x)

my_function()
print("outside of the function:", x)