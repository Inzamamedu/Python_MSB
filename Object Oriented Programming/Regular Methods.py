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


fresh = MakingWater("MGI", "2 Ltr", "38 tk")
kinle = MakingWater("Cocakola", "500 ml", "15 tk")


fresh.get_product_info()
fresh.get_product_type()


