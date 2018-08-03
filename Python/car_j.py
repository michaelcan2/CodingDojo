# class Car:
#     def __init__(self,price,speed,fuel,mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage

#     def display_all(self):
#         print("price:",self.price,"speed:",self.speed,"fuel:",self.fuel,"mileage:",self.mileage)


# car1 = Car(300,30,2,10)


# car1.display_all()

class car:
    def __init__(self,price,speed,fuel,mileage):
        self.price=price
        if(self.price>10000):
            tax=0.15
        else:
            tax=0.12
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.tax=tax
    def display_all(self):
        # print("Price:{}".format(self.price))
        # print("Speed:{}".format(self.speed))
        # print("fuel:{}".format(self.fuel))
        # print("mileage:{}".format(self.mileage)
        # print("tax:{}".format(self.tax))
        print("Price: {}".format(self.price))
        print("Speed: {}mph".format(self.speed))
        print("Fuel: {}".format(self.fuel))
        print("Mileage: {}mpg".format(self.mileage))
        print("Tax: {}".format(self.tax))

one=car(2000,35,'Full',15)
one.display_all()


  # def __init__(self,price,name,weight,brand,status):
    #     self.price = price
    #     self.name = name
    #     self.weight = weight
    #     self.brand = brand
    #     self.status = "for sale"

    # def return_item(self,reason_for_return):
    #     if (self.reason_for_return = "defective"):
    #         self.status = "defective"
    #         self.price = 0
    #     elif(self.reason_for_return = "like new"):
    #         self.status = "for sale"
    #     elif(self.reason_for_return = "opened"):
    #         self.status = "used"
    #         return self