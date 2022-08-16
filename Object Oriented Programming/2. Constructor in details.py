"""
class MakingWater:
    # constructor
    def __init__(self, company, quantity, price):
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price




fresh = MakingWater("MGI", "2 Ltr", "38 tk")
kinle = MakingWater("Cocakola", "500 ml", "15 tk")
# Mum = MakingWater("")


print(fresh.company)
print(kinle.company)

"""

"""
class MakingWater:
    # constructor
    def __init__(self, company, quantity, price):
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price
        self.type = "Water"  # ai instance ta sob gular jonna same output deba .




fresh = MakingWater("MGI", "2 Ltr", "38 tk")
kinle = MakingWater("Cocakola", "500 ml", "15 tk")
# Mum = MakingWater("")


print(fresh.type)
print(kinle.type)
"""

class MakingWater:
    # constructor
    def __init__(self, company, quantity, price):
        # instance variable
        self.company = company
        self.quantity = quantity
        self.price = price




fresh = MakingWater("MGI", "2 Ltr", "38 tk")
kinle = MakingWater("Cocakola", "500 ml", "15 tk")  # ai bar amra jode kono data ka update korta chai ta hola 57 ai line ar baira thaka updata kora pare ai tai akhana dakhano hoba
# Mum = MakingWater("")


# print(fresh.company)
# print(kinle.company)

print(fresh.price)

fresh.price = "35 tk"

print(fresh.price)

"""
# making object / instance
fresh = MakingWater()
kinle = MakingWater()
Mum = MakingWater()

# print(fresh)
# print(MakingWater)

# instance variable
fresh.company = "I"
fresh.company = "2 HGltr"
fresh.price = "30 tk"

print(fresh.company)
print(fresh.price)
"""