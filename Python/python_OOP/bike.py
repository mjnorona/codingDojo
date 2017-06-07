class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Max Speed: " + self.max_speed
        print "Miles: " + str(self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()