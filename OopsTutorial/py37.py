# Multiple Inheritance


class P1:
    def m1(self):
        print('Parent 1 class')

class P2:
    def m2(self):
        print('Parent 2 class')

class C(P1,P2):
    def m3(self):
        print('child class')


c = C()
c.m1()
c.m2()
c.m3()