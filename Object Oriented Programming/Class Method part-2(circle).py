"""
class Circle:

    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def calculate_circle_circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(4, 3.1416)
c2 = Circle(5, 3.1416)


print(c1.calculate_circle_circumference())
print(c2.calculate_circle_circumference())

"""

# ai bar amra oop ar madhomma dakhbo

class Circle:

    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius


    def calculate_circle_circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(4)
c2 = Circle(5)


print(c1.calculate_circle_circumference())
print(c2.calculate_circle_circumference())