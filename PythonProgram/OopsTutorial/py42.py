# method overloading (with same no of arguments method is not possible)

class Test:
    def m1(self):
        print('no args')
    def m1(self,a):
        print('one args')
    def m1(self,a,b):
        print('two args')

t = Test()
# t.m1()   # raise error 0 args given
# t.m1(10)  # raise error 1 args given
t.m1(10,20)  # this is possible (acceptable last or recent method)
# t.m1(10,2,3,4)  # raise error 4 args given