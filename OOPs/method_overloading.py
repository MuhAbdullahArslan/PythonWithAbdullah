# class Addition:
#     def add(self,num1,num2):
#         return num1 + num2
#     def add(self,num1,num2,num3):
#         return num1 + num2 + num3
    
    
# add1 = Addition()
# add1.add(3,4) # here throught error
#     add1.add(3,4) # here throught error
#     ~~~~~~~~^^^^^
# TypeError: Addition.add() missing 1 required positional argument: 'num3'
# PS C:\Users\Abdullah_Abdul-Rehma\Desktop\Python\oops> 
# add1.add(3,4,5)

class Addition:
    def add(self,num1=None,num2=None,num3=None):
        if num1 != None and num2 != None and num3 != None:
            return num1 + num2 + num3
        elif num1 != None and num2 != None:
            return num1 + num2
        else:
            print("invalid operation")
    
    
add1 = Addition()
print(add1.add(3,4))