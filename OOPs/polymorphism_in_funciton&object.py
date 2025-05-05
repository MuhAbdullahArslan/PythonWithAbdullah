class BMW:
    def fule_type(self):
        print("Deasil")
        
    def max_speed(self):
        print("Maximum Speed of BMW is 180")

class Fararri:
    def fule_type(self):
        print("petrol")
        
    def max_speed(self):
        print("Maximum Speed of BMW is 220")
        
def car_info(obj):
    obj.max_speed()
    obj.fule_type()

fararri = Fararri()
bmw = BMW()

car_info(fararri)
print("---------")
car_info(bmw)
