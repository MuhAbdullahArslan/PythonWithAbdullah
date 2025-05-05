# In oop ,we have two terms 
# constructor
# Destruction
# A special  method destroys objets and releases reasources tied to onj
# Destructor is called automatically whan object is destoryed
import time
class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.salary = sal
        
    def display(self):
        print(f"Employee Name:{self.name}\nEmployee Salaray:{self.salary}")
        
    def __del__(self):
        print("del method called")
        
e1 = Employee("Arslan",38000)
e2 = e1
del e1

time.sleep(5)


