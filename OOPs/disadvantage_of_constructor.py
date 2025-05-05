# 1.Circular Referencing 
# when two obj refer to each other
import time
class Employee:
    def __init__(self,obj2):
        self.obj2 = obj2
    def __del__(self):
        print("Employee class destructor called")
    
class Account:
    def __init__(self,num):
        self.number = num
        self.obj1 = Employee(self)

    def __del__(self):
        print("Account class destructor called")

ac = Account(12345)

del ac

time.sleep(5)

