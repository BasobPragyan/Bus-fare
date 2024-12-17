class vehicle:
    def __init__(self,price):
        self.price=price
    def fare(self,seats):
        totalfare=seats*self.price
        print("Fare of vehicle is : ",totalfare)
class bus(vehicle):
    def __init__(self, price):
        super().__init__(price)
    def fare(self,seats):
        totalfare=seats*self.price
        print("The fare of the bus is : ",totalfare+(0.1*totalfare))

bus1=bus(45)
bus1.fare(89)