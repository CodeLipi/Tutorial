class Test:
    a = 10

    def __init__(self):
        Test.b = 20
        del Test.a

    def m1(self):
        Test.c = 30
        del Test.b

    @classmethod
    def m2(cls):
        cls.d = 40
        del Test.c

    @staticmethod
    def m3():
        Test.e = 50
        del Test.d

print(Test.__dict__)

t = Test()
print(Test.__dict__)

t.m1()
print(Test.__dict__)

Test.m2()
print(Test.__dict__)

Test.m3()
print(Test.__dict__)

Test.f = 60
print(Test.__dict__)
