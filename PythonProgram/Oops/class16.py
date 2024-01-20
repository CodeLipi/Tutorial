class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):      # deleting inside the class
        del self.a

t = Test()
print(t.__dict__)

print('After deleting...')
t.m1()
print(t.__dict__)

del t.b   # deleting outside the class
print(t.__dict__)
