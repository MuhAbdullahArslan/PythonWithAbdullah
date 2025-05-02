# by default constructor of parent class available to  child class

class Parent:
    def __init__(self):
        print("parent class constructor")
        self.vehical = "bike"

class Child(Parent):
    pass

c1 = Child() # if child not have constructor it can use parent class constructor

print(c1.__dict__)

# constructor overriding
class Parent:
    def __init__(self):
        print("parent class constructor")
        self.vehical = "bike"

class Child(Parent):
    def __init__(self):
        print("Child class constructor")
        self.vehical = "BMW"

c1 = Child()

print(c1.__dict__)

