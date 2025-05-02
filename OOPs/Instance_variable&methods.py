# instance variable
# 1) variable made for particular instance
# 2) separate copy is created for every object
# 3) value of variable diff from obj to obj
# 4) modifiction in one object won't effect other object

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
s1 = Student("Arslan",49)
s2 = Student("Hassan",50)
s3 = Student("Ali",88)

print(f"Data for Student1: {s1.__dict__}")
print(f"Data for Student2: {s2.__dict__}")
print(f"Data for Student3: {s3.__dict__}")

# crating instance variable outside of class
s1.age = 32 # adding the new variable (age) 
print(f"After adding age var:{s1.__dict__}") # after adding showing namespace

s2.marks = 65
print(f"After update the marks:{s2.__dict__}")

# deleting the instance of variable
del s1.age
print(s1.__dict__)
# instance method
# 1) instance method belog to instance variable can you change remove modify with that

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    # instance method 
    def display(self):
        print(f"\t-:(Student Report):-\nName: {self.name}\nMarks: {self.marks}")
    
    def update_data(self):
        self.name = input("Enter the name:")
        self.marks = int(input("Enter the marks:"))
        
s1 = Student("Arslan",49)
s2 = Student("Hassan",50)
s3 = Student("Ali",88)

s1.display() #instance method

s1.update_data()
s1.display()

