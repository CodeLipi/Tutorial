class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):      # deleting inside the class
        del self.a

t1 = Test()
t2 = Test()

t1.a = 222   # replaced privious value if a,b is not present then its created
t1.b = 555

print(t1.__dict__)
print(t2.__dict__)

# del t1.a
# print(t1.__dict__)  # {'b': 20, 'c': 30}
# print(t2.__dict__)  # {'a': 10, 'b': 20, 'c': 30}

