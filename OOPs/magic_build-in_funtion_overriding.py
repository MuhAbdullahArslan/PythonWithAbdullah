
class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.fruits = basket1
        self.electronics = basket2
        self.other = basket3
    # here over-ride the __str__ funtion
    def __str__(self):
        return f"{self.fruits},\n{self.electronics},\n{self.other}"
    
c1 = Cart(['apple','banana','mangoes'],['resistance','transister','diode'],['Alphi','knife','soild'])

print(c1)



class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.fruits = basket1
        self.electronics = basket2
        self.other = basket3
    
    def __len__(self):
        print(f"This is len overriding")
        return len(self.fruits) + len(self.electronics) + len(self.other)
    
c1 = Cart(['apple','banana','mangoes'],['resistance','transister','diode'],['Alphi','knife','soild'])

print(len(c1))
