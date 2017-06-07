class Product(object):
    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price += tax * self.price
        return self

    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in the box":
            self.status = "for sale"
        elif reason == "open box":
            self.status = "used"
            self.price = self.price * .8
        return self

    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Item Name: " + self.itemName
        print "Weight: " + self.weight
        print "Brand: " + self.brand
        print "Cost: " + str(self.cost)
        print "Status: " + self.status
        print ""
        return self

product1 = Product(200, "TV", "30lb", "Samsung", 1000)
product1.displayInfo()
product1.returnItem("open box")
product1.displayInfo()

