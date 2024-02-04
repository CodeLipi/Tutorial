# super() method

class Parent:
    a = 10  # static variable

    def __init__(self):
        print('Parent class constructor')
        # self.b = 20  # instance variable

    def m1(self):
        print('Parent class, instance method')

    @classmethod
    def m2(cls):
        print('Parent class, class method')

    @staticmethod
    def m3():
        print('Parent class, static method')

    def __del__(self):
        print('Parent Destructor')

class Child(Parent):
    a = 50
    def __init__(self):
        super().__init__()  # this is method call, not required self
        print('Child class constructor')
        print(super().a)
        super().__del__()
        super().m1()
        super().m2()
        super().m3()

    def __del__(self):
        # super().__del__()
        print('Child class destructor')

    def m1(self):
        print('Child class, instance method')
        # super().m1()

    @classmethod
    def m2(cls):
        print('Child class, class method')
        super().m2()

    @staticmethod
    def m3():
        # super().m3()   # in static method super() is not possible
        print('Child class, static method')

ch = Child()
print(ch.a)
# print(ch.b)
ch.m1()
ch.m2()
ch.m3()