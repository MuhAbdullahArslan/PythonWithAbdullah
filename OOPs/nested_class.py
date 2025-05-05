class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    class Dob:
        def __init__(self,dd,mm,yy):
            self.day = dd
            self.month = mm
            self.year = yy
        def display(self):
            print(f"Your Date of birth is {self.day}/{self.month}/{self.year}")
            
s1 = Student("Arslan",21)
dob = s1.Dob(12,8,2009)
dob.display()