# Hybrid inheritance
# it contain multipal tyope of inheritance
# MRO represent how properties (method + attribute0) are searched in inheritance
# Roule -1)
# First search in child class and then goes to parent class
# Rule -2)
# Depth first left to right approach

# You can user mor() method for knowing mro of the object

class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B,C):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass

print(P.mro()) #knowing the search of inheritance with the help of mro() mehtod
# output
# [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]