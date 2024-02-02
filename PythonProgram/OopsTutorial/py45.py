# Constructor overloading is not possible just like method overloading
# but we make possible with like method overloading

class Test:
    def __init__(self):
        print('No args')

    def __init__(self,a):
        print('one args')

    def __init__(self,a,b):
        print('two args')

# t = Test()    # raise error
# t = Test(1)   # raise error  
t = Test(1,2)    