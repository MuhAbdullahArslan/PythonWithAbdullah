# Creating a Employee class with attributes (name,age,salary)
class Employee:
    # assign the data of employee 
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.salary = sal
    # inside of class function call method 
    def display(self):
        print(f"\t-:Emplyee Data:-\nName: {self.name}\nAge: {self.age}\nSalary: {self.salary}")
# create an object of Employee class
e1 = Employee("Arslan",26,80000)
e2 = Employee("Ali",25,75000)

# Accesinging Attribute and Methods of Emplyee class
# Acessing current class attributes
print(e1.age)
print(e1.name)
print(e1.salary)
# Acessing current class method 
e1.display()

# you can update attribute value
e1.salary = 85000
# now display the changed value
e1.display()