# nonlocal variable
# nonlocal keyword

x = "Global"  # global variable

def outer_function():
    x = "Local"  # local variable

    def inner_function():
        nonlocal x # x is declaring a nonlocal variable
        x = "Nonlocal" # nonlocal
        print("From outer function:", x)


    print("From outer Function:", x)
    inner_function()
    print("From outer function:", x)


outer_function()