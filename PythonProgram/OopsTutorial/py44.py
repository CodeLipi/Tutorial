# method overloading 
# with variable no of args

class Test:
    def sum(self,*n):
        print('var no args')
        total = 0
        for i in n:
            total = total + i
        print('sum :', total)

t = Test()
t.sum()
t.sum(1)
t.sum(1,2)
t.sum(1,2,3)
t.sum(1,2,3,4)