class Demo:
    pass

d1 = Demo()

class Employee:
    # assign the data of employee 
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.salary = sal
        
e1 = Employee("Hassan",34,80000)

# isinstance check the object belong to the class 
# return True if belong else not belong
# syntax:- isinstance(object,class_name)
print(isinstance(e1,Employee)) # True

print(isinstance(e1,Demo)) # False

# use with if-else

# if isinstance(object,class_name):
#     pass