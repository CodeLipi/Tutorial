# Inheritance
# Is a Relationship

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
    # pass 
    def __init__(self):
        print('Child class constructor')

    def __del__(self):
        print('Child class destructor')

    def m1(self):
        print('Child class, instance method')

    @classmethod
    def m2(cls):
        print('Child class, class method')

    @staticmethod
    def m3():
        print('Child class, static method')

ch = Child()
print(ch.a)
# print(ch.b)
ch.m1()
ch.m2()
ch.m3()


# class X:
#     def m1():
#         pass
#     def m2():
#         pass
#     def m3():
#         pass
#     def m4():
#         pass

# class Y(X):   # class childClass(parentClass)
#     pass

# y = Y()

# y.m1()
# y.m2()
# y.m3()
# y.m4()

# class Y is a relationship with class Y