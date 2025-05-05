# What is Encapsulation 
# Wrapping up data and methodes workingo on data together in single unit(i-eclass) is called as encapsulation 

class Finance:
    def __init__(self):
        self.__revanue = '100000' # public variable
        self.__number_of_sales = 114 # private variable becouse of __
        
    def display(self): #you can access varibale and using inside of class mehtods
        print(f"Revanu of Company:{self.__revanue}\nNumber of Sales:{self.__number_of_sales}")
f1 = Finance()        
print(f1.__dict__)
f1.display()