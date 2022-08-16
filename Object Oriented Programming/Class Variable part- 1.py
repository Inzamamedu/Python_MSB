"""
class MakingWater:
    # class variable / instance variable
    count_instances = 0
    # constructor
    def __init__(self, company, quantity, price):
        MakingWater.count_instances += 1
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"


     # Function -> Method
     # Regular method - 1
    def get_product_info(self):
        print(f"{self.company} company{self.type} price is {self.price} and quantity is {self.quantity}")

    # regular method - 2
    def get_product_type(self):
        print(f"This factory produces {self.type}")


fresh = MakingWater("MGI", "2 Ltr", "600")
kinle = MakingWater("Cocakola", "500 ml", "300")

print(fresh.__dict__)

"""

"""
class MakingWater:
    # class variable / instance variable
    count_instances = 0
    # constructor
    def __init__(self, company, quantity, price):
        MakingWater.count_instances += 1
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"


     # Function -> Method
     # Regular method - 1
    def get_product_info(self):
        print(f"{self.company} company{self.type} price is {self.price} and quantity is {self.quantity}")

    # regular method - 2
    def get_product_type(self):
        print(f"This factory produces {self.type}")


    def give_discount(self, discount_percent):
        off_price = (discount_percent / 100) * self.price
        return self.price - off_price


fresh = MakingWater("MGI", "2 Ltr", 600)
kinle = MakingWater("Cocakola", "500 ml", 300)

print(fresh.give_discount(50))  # discount percent

"""


"""
#  float_discount

class MakingWater:
    # class variable / instance variable
    count_instances = 0
    flat_discount = 50

    # constructor
    def __init__(self, company, quantity, price):
        MakingWater.count_instances += 1
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"


     # Function -> Method
     # Regular method - 1
    def get_product_info(self):
        print(f"{self.company} company{self.type} price is {self.price} and quantity is {self.quantity}")

    # regular method - 2
    def get_product_type(self):
        print(f"This factory produces {self.type}")


    def give_discount(self, discount_percent):
        off_price = (discount_percent / 100) * self.price
        return self.price - off_price

    def flat_discount1(self):
        off_price = (self.float_discount / 100) * self.price
        return self.price - off_price


fresh = MakingWater("MGI", "2 Ltr", 600)
kinle = MakingWater("Cocakola", "500 ml", 300)

print(fresh.give_discount(90))  # discount percent
print(kinle.flat_discount1())


"""

"""
   # ai bar amra baira thaka discount call korbo

class MakingWater:
    # class variable / instance variable
    count_instances = 0
    flat_discount = 50

    # constructor
    def __init__(self, company, quantity, price):
        MakingWater.count_instances += 1
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"


     # Function -> Method
     # Regular method - 1
    def get_product_info(self):
        print(f"{self.company} company{self.type} price is {self.price} and quantity is {self.quantity}")

    # regular method - 2
    def get_product_type(self):
        print(f"This factory produces {self.type}")


    def give_discount(self, discount_percent):
        off_price = (discount_percent / 100) * self.price
        return self.price - off_price

    def flat_discount1(self):
        off_price = (self.flat_discount / 100) * self.price
        return self.price - off_price


fresh = MakingWater("MGI", "2 Ltr", 600)
kinle = MakingWater("Cocakola", "500 ml", 300)

print(fresh.give_discount(90))  # discount percent
print(kinle.flat_discount1())

MakingWater.flat_discount = 30  # percent
print(kinle.flat_discount1())

"""

 # ai bar amra dakhbo vajal ta kothai

class MakingWater:
    # class variable / instance variable
    count_instances = 0
    flat_discount = 50

    # constructor
    def __init__(self, company, quantity, price):
        MakingWater.count_instances += 1
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"


     # Function -> Method
     # Regular method - 1
    def get_product_info(self):
        print(f"{self.company} company{self.type} price is {self.price} and quantity is {self.quantity}")

    # regular method - 2
    def get_product_type(self):
        print(f"This factory produces {self.type}")


    def give_discount(self, discount_percent):
        off_price = (discount_percent / 100) * self.price
        return self.price - off_price

    def flat_discount1(self):
        off_price = (self.flat_discount / 100) * self.price
        return self.price - off_price


    def flat_discount2(self):
        off_price = (MakingWater.flat_discount / 100) * self.price
        return self.price - off_price


fresh = MakingWater("MGI", "2 Ltr", 600)
kinle = MakingWater("Cocakola", "500 ml", 300)


# print(fresh.give_discount(90))  # discount percent
# print(kinle.flat_discount1())

# working
MakingWater.flat_discount = 30  # percent
print(kinle.flat_discount1())

# not working
fresh.flat_discount = 90  # percent
print(fresh.flat_discount2())