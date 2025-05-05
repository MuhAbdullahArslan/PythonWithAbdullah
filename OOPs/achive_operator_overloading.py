class Book:
    def __init__(self,book_name,num_of_page):
        self.name = book_name
        self.pages = num_of_page
        
b1 = Book("Think and Grow Rich",455)
b2 = Book("Rich Dad Poor Dad",349)

print("Total num of pages books",b1.pages + b2.pages)
# Before overloading opertor +
# print("Total num of pages books",b1 + b2) # through error
#     print("Total num of pages books",b1 + b2)
#                                      ~~~^~~~
# TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

class Book:
    def __init__(self,book_name,num_of_page):
        self.name = book_name
        self.pages = num_of_page
    
    # using operator overloading remove the error
    def __add__(self,other): # (b1+b2)
        total = self.pages + other.pages
        return total
b1 = Book("Think and Grow Rich",455)
b2 = Book("Rich Dad Poor Dad",349)

print("Total num of pages books",b1 + b2)  #b1.__add__(b2) ----> Book.__add__(b1,b2)