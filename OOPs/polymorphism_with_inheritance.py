# Polymorphism With Inheritance

class Veh:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
        
    def get_details(self):
        print("Name is:",self.name)
        print("Color is:",self.color)
        print("Price is:",self.price)
    
    def max_speed(self):
        print("Maximum Speed limit is 80")
    
    
class Car:
    def max_speed(self):
        print("Maximum Speed limit is 120")
        
v1 = Veh("Truck",'Black',20000000)

c1 = Car()

v1.max_speed()
c1.max_speed()