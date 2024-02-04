class Test :
    x = 10

    def __init__(self):
        self.y = 20

    @classmethod
    def m1(cls):
        cls.x = 888
        cls.y = 999

    # def m1(self):
    #     self.x = 888
    #     self.y = 999

t1 = Test()
t2 = Test()
Test.m1()
print('t1 : ', t1.x, t1.y) # 888 20
print('t2 : ', t2.x, t2.y) # 888 20


# t1 = Test()
# t2 = Test()
# t1.m1()
# print('t1 : ', t1.x, t1.y) # 888 999
# print('t2 : ', t2.x, t2.y)  # 10 20
