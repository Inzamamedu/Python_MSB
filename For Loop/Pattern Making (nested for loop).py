# pattern making using python
"""
1
22
333
4444
55555
"""
"""
*
**
***
****

"""


for i in range(0, 6):
    for j in range(i):
        print(i, end="")
    print()

for i in range(0, 6):
    for j in range(i):
        print("*", end="")
    print()