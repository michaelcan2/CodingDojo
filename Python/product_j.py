class Product:
  
    
    def __init__(self,price,name,weight,brand,status="for sale"):
        self.price=price
        self.name=name
        self.weight=weight
        self.brand=brand
        self.status=status

    def sell(self):
        self.status = "SOLD"
        return self

    def add_tax(self,tax):
        self.price = self.price*tax
        return self 

    def returnItem(self,reason_for_return):
        self.status=reason_for_return
        if(reason_for_return=="defective"):
            self.status=reason_for_return
            self.price=0
        if(reason_for_return=="like new"):
            self.status="for sale"
        if(reason_for_return=="opened"):
            self.status="used"
            self.price=self.price*0.8
        return self
    def displayInfo(self):
        print("The price of the product is ${}".format(self.price))
        print("The Item Name is {}".format(self.name))
        print("The item weight is {} pounds".format(self.weight))
        print("The Brand of the {} is {}".format(self.name,self.brand))
        print("The status of the {} is {}".format(self.name,self.status))
        return self
# laptop=Product(200,"laptop",2.2,"Lenovo")
# laptop.displayInfo()
car= Product(20000,"car",1800,"Nissan")
car.sell().returnItem("like new").displayInfo()

        