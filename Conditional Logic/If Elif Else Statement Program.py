# if , elif , else
# grade
"""
markes = int(input("Enter Marks: "))

if markes > 100:
    print("Invalid Input")
elif markes >= 80:
    print("A+")
elif markes >= 70:
    print("A")
elif markes >= 60:
    print("A-")
elif markes >= 50:
    print("B")
elif markes >= 40:
    print("C")
elif markes >= 33:
    print("D")
elif markes >= 0:
    print("F")
else:
    print("Invalid Input")

"""

markes = int(input("Enter Marks: "))

if 100 >= markes >= 80:
    print("A+")
elif 79 >= markes >= 70:
    print("A")
elif 69 >= markes >= 60:
    print("A-")
elif 59 >= markes >= 50:
    print("B")
elif 49 >= markes >= 40:
    print("C")
elif 39 >= markes >= 33:
    print("D")
elif 32 >= markes >= 0:
    print("F")
else:
    print("Invalid input")



