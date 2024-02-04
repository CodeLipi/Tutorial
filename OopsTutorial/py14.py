class Test:
    @classmethod
    def m1(cls):
        print(id(cls))

    @classmethod
    def m2(cls):
        print(id(cls))

print(id(Test))
Test.m1()
Test.m2()
