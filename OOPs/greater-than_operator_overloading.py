class Hotel:
    def __init__(self,name,fare):
        self.name = name
        self.fare = fare
    # overloading the > operator
    def __gt__(self,other):# (h1,h2)
        return self.fare > other.fare
    
h1 = Hotel("Taj Hotal",320000)
h2 = Hotel("Raja Hotal",4300000)

print(h2 > h1) # True