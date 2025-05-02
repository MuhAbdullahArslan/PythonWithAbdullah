class Person:
    # setter method use to set value of variable
    def set_name(self,name): 
        self.name = name
    # getter method use to get and display the value of variable
    def get_name(self):
        print("This is:-",self.name)
        
p1 = Person()
p1.set_name(input("Enter the person name:"))

p1.get_name()
