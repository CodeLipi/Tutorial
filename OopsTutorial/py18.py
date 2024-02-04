class Test:
    a = 10  # static variable

    def __init__(self):
        self.a = 5
        self.b = 15
        # static variable inside constructor
        Test.b = 20

    def m1(self):
        # static variable inside instance method
        Test.c = 30

    @classmethod
    def m2(cls):
        Test.d = 40
        cls.e = 50

    @staticmethod
    def m3():
        var = 'hello' # local var
        Test.f = 60     # static var

t = Test()
t.m1()
Test.m2()
Test.m3()

# outside of the class static variable
Test.g = 70
print(Test.__dict__)

