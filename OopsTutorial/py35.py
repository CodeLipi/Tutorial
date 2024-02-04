# Multi level inheritance

class GrandFather:
    def m1(self):
        print('Grandfather class')

class Father(GrandFather):
    def m2(self):
        print('Father class')

class Myself(Father):
    def m3(self):
        print('Myself class')

c = Myself()
c.m1()      
c.m2()      
c.m3()      