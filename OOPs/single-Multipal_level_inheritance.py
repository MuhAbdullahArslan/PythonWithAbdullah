# Types of inheritance
# Depending on numbers of child class invvolved 
# 1)Single-level inheritance
# 2)Multi-level inheritance
# 3)Hierarchical level inheritance
# 4)Multipal level inheritance
# 5)Hybird level inheritance
# 6)cyclic level inheritance

# Single-level inheritance
# one parent and one child class
# class Human:
#     def __init__(self): # not exicute because child class has constructor
#         print("This is Human class constructor")
#         self.name = input("Enter your name:")
        
# class Employee(Human): # not exicute because child class has constructor
#     def __init__(self):
#         super().__init__()
#         print("This is Empoyee class constructor")
#         self.salary = float(input("Enter the salary:"))

# e1 = Employee()



# multi-level inheritance
# parent class and child class further inherited into new class forming multipal level
class Human:
    def __init__(self):
        print("This is Human class constructor")
        self.name = input("Enter your name:")
        
class Employee(Human):
    def __init__(self):
        super().__init__()
        print("This is Empoyee class constructor")
        self.salary = float(input("Enter the salary:"))

class Manager(Employee):
    def __init__(self):
        super().__init__()
        print("This is parent class constructor")
        self.bouns = float(input("Enter the bouns"))
        
# m1 = Manager()
# e1 = Employee()
h1 = Human()

# Note:- lower class can access upper class all attribute and methods but the other hand upper class can not access lower class attribute and method