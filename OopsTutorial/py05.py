class Test:
    def __init__(x):       # x --> self
        print('constructor')

t = Test()
# this works fine


# t1 = Test(x)  # because x is var parameter
# NameError: name 'x' is not defined

# t2 = Test(10)
# TypeError: Test.__init__() takes 1 positional argument but 2 were given

# t2 = Test(x=10)
# TypeError: Test.__init__() got multiple values for argument 'x'