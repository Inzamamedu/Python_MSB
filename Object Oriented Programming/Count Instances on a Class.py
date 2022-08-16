class MakingWater:
    # class variable / instance variable
    count_instances = 0
    def __init__(self, company, quantity, price):
        MakingWater.count_instances += 1
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"


fresh = MakingWater("MGI", "2 Ltr", "38 tk")
kinle1 = MakingWater("Cocakola", "500 ml", "15 tk")
kinle2 = MakingWater("Cocakola", "500 ml", "15 tk")
kinle3 = MakingWater("Cocakola", "500 ml", "15 tk")



print(MakingWater.count_instances)