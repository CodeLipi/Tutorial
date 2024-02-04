class Test:
    def __init__(self):
        #  print('Address of object refered by self : ', id(self))
        print('constructor')

    def m1 (self, x):
        print('method')



t = Test()
# print('Address of object refered by t : ', id(t))
t.m1(10)