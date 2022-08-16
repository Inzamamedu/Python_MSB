"""
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

    # class method using as a constructor
    @classmethod
    def class_method_as_a_constructor(cls, information):
        company, quantity, price = information.split(",")
        return cls(company, quantity, price)




fresh = MakingWater("MGI", "2 Ltr", 600)

kinle = MakingWater.class_method_as_a_constructor("Cocakola, 500 ml,300")
print(kinle.price)

"""

# regular method use kora ki vaba kora ai ta dakhbo

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

    # class method using as a constructor
    @classmethod
    def class_method_as_a_constructor(cls, information):
        company, quantity, price = information.split(",")
        return cls(company, quantity, price)


    # regular method
    def custom_info(self):
        return print(f"{self.company}, {self.price}")



fresh = MakingWater("MGI", "2 Ltr", 600)

kinle = MakingWater.class_method_as_a_constructor("Cocakola, 500 ml,300")
kinle.custom_info()
