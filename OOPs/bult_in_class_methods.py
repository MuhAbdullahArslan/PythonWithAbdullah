# Built in Class funtion
# Creating a Employee class with attributes (name,age,salary)
class Employee:
    # assign the data of employee 
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.salary = sal
        
e1 = Employee("Hassan",34,80000)

# 1) get the value of perticular variable
# syntax:- getattr(object_name,attribute_name)

print(f"Age of Employee is: {getattr(e1,"age")}")

# 2) set the value of perticular variable
# syntax:- setattr(object_name,attribute_name,new_value)

print(f"Before the set value Salary is: {e1.salary}")
setattr(e1,'salary',85000) # update the salary attribute
print(f"After setattr function Salary is : {e1.salary}")

# 3) delete the value of perticular variable
# syntax:- delattr(object_name,attribute_name)

print(f"Before Deleting the Attribute {e1.__dict__}")
delattr(e1,'age') # delete the age attribute
print(f"After Deleting the Attribute {e1.__dict__}")

# 4) class has a given attribute check if has return True not has return False
# syntax:- hasattr(object_name,attribute_name)

print(hasattr(e1,'age')) # False Becouse you delete it above

