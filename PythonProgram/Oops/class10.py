class Test :
    def __init__(self, name):
        self.name = name

t = Test('Kush')
print(t.name)

t.__init__('Rohit')     # here re-initialization happens
print(t.name)

