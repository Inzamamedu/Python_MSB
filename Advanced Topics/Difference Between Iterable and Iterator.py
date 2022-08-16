"""
my_list = [1, 2, 3, 4]  # iterable

x = map(lambda i: i ** 2,my_list)  # iterator
                                    # iterator 1 bar e loop hoy ar ak bare result dai . ata 1 bar ar bashe kaj kora na
print(next(x))
print(next(x))
print(next(x))
print(next(x))


for i in x:
    print("for loop output")
    print(i)
"""

my_list = [1, 2, 3, 4]  # iterable


x = map(lambda i: i ** 2,my_list)  # iterator

print(next(x))
print(next(x))
print(next(x))
print(next(x))


for i in map(lambda i: i ** 2, my_list):
    print(i)

