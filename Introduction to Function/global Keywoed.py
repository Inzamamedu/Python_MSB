x = 10 # global variable

def my_function():
    global x
    x += 5 # local variable
    return print("After incrementing", x)

print("Initial value:", x)
my_function()
print("After incrementing global variable value:", x)