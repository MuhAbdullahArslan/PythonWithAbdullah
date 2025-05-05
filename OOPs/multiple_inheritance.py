# Multiple_inheritance
# class is deriverd from multipal base class
# syntax:- 
# class Parent1:
#     attribute,methods
# class Parent2:
#     attribute,methods
# class Chlid(Parent1,Parent2):
#     attribute,methods

class Country:
    def __init__(self):
        print("This is country class constructor")
        self.office = "Punjab"
class District:
    # def __init__(self):
    #     print("This is District class constructor")
    #     self.office = "Faisalabad"
    pass
class State(District,Country):
    # def __init__(self):
    #     print("This is State class constructor")
    #     self.office = "jarawalaroad"
    pass
              
s1 = State()
print(s1.__dict__)
print(type(s1))