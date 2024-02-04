# inner classes

class Outer:
    def m1(self):
        print('outer class method')
    class Inner:
        def m2(self):
            print('inner class method')

# out = Outer()
# out.m1()

# iner = out.Inner()   # first way
# iner = Outer().Inner()        # second way
# iner.m2()
            
Outer().Inner().m2()  # third way