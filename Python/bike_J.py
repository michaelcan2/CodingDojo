# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.logged = True


#     def login(self):
#         self.logged = True
#         print(self.name + "is logged in.")
#         return self

#     def logout(self):
#         self.logout = False
#         print(self.name + "is logged out")
#         return self

#     def show(self):
#         print("name is {self.name}, email me{self.email}.")

#     moment = User("michael", mcg.com,true)

class Bike:
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 
    
    def display_Info(self):
        print({self.price}, {self.max_speed}, {self.miles})
        return self

    def ride(self):
        self.miles += 10
        print("Riding")
        return self


red_bike = Bike(4,55)
red_bike.ride().display_Info()

   def reverse(self):
        self.miles +=- 5
        print("Reversing")
        return self

blue_bike = Bike(5,33)
green_bike = Bike(2,44)
    # WHY WONT MY INSTANCES PRINT!

# class bike:
#     def __init__(self,price,max_speed):
#         self.price=price
#         self.max_speed=max_speed
#         self.miles=0
#     def displayInfo(self):
#         print("The price is ${} for this bike".format(self.price))
#         print("The maximum speed is {} miles per hour".format(self.max_speed))
#         print(self.miles)
#     def ride(self):
#         self.miles+=10
#         print("Riding")
#         return self
#     def reverse(self):
#         self.miles+=-5
#         if (self.miles<0):
#             self.miles=0
#         print("Reversing")
#         return self



# bike1=bike(500,25)
# bike1.ride().displayInfo()