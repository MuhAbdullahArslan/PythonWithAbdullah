# "+" ----> 1) 10 + 20 = 30
          # 2) "hello" + "World" = helloWorld
          # 4) [1,2,3] + [4,5,6] = [1,2,3,4,5,6]
          
# integer datatype  
num1 = 10
num2 = 20

print(num1 + num2) #30
print(num1.__add__(num2)) #30
print(int.__add__(num1,num2)) #30
# step 1) check datatype of left operand # int
# step 2) go in that class
# step 3) cll __add__() funtion

# string datatype  
str1 = "hello"
str2 = "hy"

print(str1 + str2) #hellohy
print(str1.__add__(str2)) #hellohy
print(str.__add__(str1,str2)) #hellohy
# step 1) check datatype of left operand # int
# step 2) go in that class
# step 3) cll __add__() funtion
