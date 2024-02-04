# Method Overriding

class P:
    def marry(self):
        print('with one girl...')

class C(P):
    def marry(self):  # method overriding
        super().marry()
        print('with two girl...')

c = C()
c.marry()