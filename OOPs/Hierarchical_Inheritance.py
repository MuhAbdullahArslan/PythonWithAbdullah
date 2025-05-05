# hierarchical inheritance
# one parent and multipal child class

class Person:
    def __init__(self,name):
        print("This is parent class constructor")
        self.name = name
        
class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
        
p1 = Person("Arslan")
print(p1.__dict__)

s1 = Student("Arslan",85)
print(s1.__dict__)

e1 = Employee("Arslan",98000)
print(e1.__dict__)