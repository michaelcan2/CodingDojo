class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    
    def display_all(self):
        info = "Price: {}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
        print info