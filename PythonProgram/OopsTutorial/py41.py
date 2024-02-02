# operater overloading

class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):    # operator overloading
        return self.pages+other.pages
    
    def __lt__(self,other):    # operator overloading
        return self.pages<other.pages
    
    def __gt__(self,other):    # operator overloading
        return self.pages>other.pages

b1 = Book(100)
b2 = Book(200)

# print('total pages :', b1+b2)  # doesn't add obj
print('total pages :', b1+b2)