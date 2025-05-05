class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
        
class Changes:
    @staticmethod
    def increment_salary(obj,incre):
        obj.salary = incre + obj.salary

e1 = Employee("Arslan",55000)

c1 = Changes()

c1.increment_salary(e1,5000)
e1.display()