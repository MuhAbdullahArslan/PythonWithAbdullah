# staticmethod
# perfome operation on external data(not belog to class and object)
# static data = class data
# it can also perform operation on class data 
# no need to pass object or class referance 
# created using decorator '@staticmethod'


class SimpleIntrest:
    bankName = "HBL"
    rate_of_intrest = 12.25 #class attribute
    @staticmethod
    def simple_intrest(prin,n_y): #not need to pass obj or class
        si = (prin*n_y*SimpleIntrest.rate_of_intrest)/100
        print(f"Simple Intrest = {si}")
        
si = SimpleIntrest()

si.simple_intrest(10000,3)