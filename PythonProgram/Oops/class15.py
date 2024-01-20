class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
print(t.__dict__)  # {'a': 10, 'b': 20}

t.m1()
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30}

# instance variable here too, outside of the class, only for t object
t.d = 40
t.e = 50
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

t1 = Test()
t1.m1()
t1.f = 60   # instance variable for t1 object only
print(t1.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'f': 60}

