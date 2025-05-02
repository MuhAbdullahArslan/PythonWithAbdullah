# class variables
#1) variable made for entire class(all object same variable)
# only one copy crated and distributed to all objects
# modification in class variable impact on all objects

class Student:
    # Collage Name same for all object so it is class variable
    collage_name = "SoA"
    def __init__(self,name,degree):
        self.name = name
        self.degree = degree
        
    # class method is use to modifiy class variable
    @classmethod #python built in decorator to make class name first agrument of method
    def update_collage_name(cls,name): # first argument class name
        cls.collage_name = name
        
std1 = Student("Hassan","DAE(Diploma of associate engineering)")
std2 = Student("Husnain","CS(computer science)")

# all object same value | one copy for all 
# Accessing the class variable with obj only can see not change 
print(std1.collage_name)
print(std2.collage_name)

# Accessing the class variable with class_name
print(f"Acessing the collage name with the help of class_name: {Student.collage_name}")
# update the collage_name which is class_variable

Student.collage_name = "GSTC"
# modificatrion in class varaibale impact on all obj
print(f"Acessing the collage name with the help of class_name: {std1.collage_name}")
print(f"Acessing the collage name with the help of class_name: {std2.collage_name}")

Student.update_collage_name("NFC")
print(Student.collage_name)






