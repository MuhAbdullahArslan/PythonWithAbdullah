# super()
# we can access parent class properties
# This function returns a temporary object which contains reference to parent class
# it makes inheritance more manageable and extesible

class Computer:
    def __init__(self):
        self.ram = "4gb"
        self.storage = '512gb'
        print("This is computer class(parent class)")
class Phone(Computer):
    def __init__(self):
        super().__init__()
        self.name = "Iphone X"
        print("This is phone class(child class)")
    
p1 = Phone()

# paramiterized constructor
class Computer:
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        print("This is computer class(parent class)")
class Phone(Computer):
    def __init__(self,ram,storage):
        super().__init__(ram,storage)
        self.name = "Iphone X"
        print("This is phone class(child class)")
    
p1 = Phone("5gb","125gb")

print(p1.__dict__)

