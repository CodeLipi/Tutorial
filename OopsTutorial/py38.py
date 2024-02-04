# Hybrid Inheritance

class GrandFather:
    def m1(self):
        print('grand father class')

class Father(GrandFather):
    def m2(self):
        print('father class')

class Uncle(GrandFather):
    def m3(self):
        print('uncle class')

class Child(Father,Uncle):
    def m4(self):
        print('child class')

c = Child()

c.m1()
c.m2()
c.m3()
c.m4()