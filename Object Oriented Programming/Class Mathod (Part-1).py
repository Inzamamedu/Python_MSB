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

    # class method
    @classmethod
    def set_discount(cls,new_discount):
        cls.flat_discount = new_discount


    # regular method
    def apply_discount(self):
        off_price = (MakingWater.flat_discount / 100) * self.price
        self.price = self.price - off_price


fresh = MakingWater("MGI", "2 Ltr", 600)
kinle = MakingWater("Cocakola", "500 ml", 300)


print(fresh.price)
MakingWater.set_discount(90)
fresh.apply_discount()
print(fresh.price)