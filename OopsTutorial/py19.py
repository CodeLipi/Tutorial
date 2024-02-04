class Test:
    a = 10

    @classmethod
    def m1(cls):
        cls.a = 20

    @staticmethod
    def m2():
        Test.a = 30

t = Test()
print(t.a)

Test.m1()
print(Test.a)

Test.m2()
print(Test.a)