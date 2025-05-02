class Student:
    """
    Student class create for store the data of student like(name,age,gender)
    """
    def __init__(self,name,age,gender):
        self.name = name
        self.age  = age
        self.gender = gender
    
# s1 = Student("Arslan",25,"Male")

print(Student.__dict__) #Dictionary containing class's namespace

print(Student.__doc__) # Class doucmantion string

print(Student.__name__) # Return the name of class

print(Student.__module__) # Module Name in which class is define # return __main__ becouse class define in current file

print(Student.__base__) # list of base classes