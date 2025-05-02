# new class can access old class method+attribute 
# Parent class , Base class , Exiting class ,Super Class
# Child class ,Sub class, deriverd class

# object class:-
# all class in python  are deriverd from the buildin "object" class
# syntax:- 
# class Parent(object):
#     attribute+methods
# class Child(Parent):
#     attribute+mehtods

class Employee:
    bouns = 2000
    def display(self):
        print(f"Employee have bonus : {self.bouns}")
    
class Manager(Employee):
    bouns = 2500
    def show(self):
        print(f"Manager have bouns: {Manager.bouns1}")
        
e1 = Employee()
m1 = Manager()

print(e1.bouns)
print(m1.bouns)

e1.display()
m1.display()