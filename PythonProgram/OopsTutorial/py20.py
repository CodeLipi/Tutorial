class Test:
    a = 10
    def m1 (self):
        self.a = 222    # declaring not the updating static var

print(Test.a)
t = Test()   # 10
t.m1()
print(t.a)   # 222
print(Test.a)   # 10
