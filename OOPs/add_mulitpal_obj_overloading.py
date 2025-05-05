class Num:
    def __init__(self,value):
        self.value = value
    
    def __add__(self,other):
        return Num(self.value + other.value)
    
    def __str__(self):
        return str(self.value)
    
n1 = Num(34)
n2 = Num(43)
n3 = Num(84)
n4 = Num(84)
n5 = Num(84)
n6 = Num(84)
n7 = Num(84)

print("The addition of all Numbers is:",n1 + n2 + n3 + n4 + n5 +n6 + n7)