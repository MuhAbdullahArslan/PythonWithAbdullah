#Non-parameterized cunstructor class
class Employee:
    def __init__(self): # Constructor automatic call than create an objects
        self.salary = 23000 # starting value of salary wth attribute salary
        self.age = 21

e1 = Employee() # create first employee obj
e2 = Employee() # create Second employee obj

# __dict__ to return the dict of all attributes
print(e1.__dict__) # for display all the class attributes 

# parameterized cunstructor class
class Employee:
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.salary = sal

e1 = Employee("Arslan",26,80000)
e1 = Employee("Ali",25,75000)

print(e1.__dict__)

# default cunstructor class
class Employee:
    pass # if you write nothing call python build In Constructor

e1 = Employee()
e2 = Employee()

print(e1.__dict__) # return empty dict becouse builtIn constructor is empty
