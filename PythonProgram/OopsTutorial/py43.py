# method overloading 
# with default args

class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        elif a!=None:
            print(a)
        else:
            print('no args')
t = Test()
t.sum()
t.sum(1)
t.sum(1,2)
t.sum(1,2,3)
# t.sum(1,2,3,4)  # raise error

