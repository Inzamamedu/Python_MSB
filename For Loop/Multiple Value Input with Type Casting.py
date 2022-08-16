"""
# taking three inputs at a time
students, boys, girls = input("Enter three values: ").split()
print("Total number of students:", students)
print("Number of boys is : ", boys)
print("Number of girls is : ", girls)
"""
students, boys, girls = [int(i) for i in input("Enter three values: ").split()]

print("Total number of students:", students)
print("Number of boys is : ", boys)
print("Number of girls is : ", girls)

print(type(students))
print(type(boys))
print(type(girls))

