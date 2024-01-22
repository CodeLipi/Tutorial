class Test:
    def __init__(self):
        print('no-arg constructor')

    def __init__(self,x):
        print('one-arg constructor')

# t = Test()
t = Test(10)

# it always providing the preference to the last constructor
# constructor overloading is not possible.
