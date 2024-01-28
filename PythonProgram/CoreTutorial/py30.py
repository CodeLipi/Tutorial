# function decorators

def decorator(func):
    def inner(name):
        if name == "Sunny":
            print("go fuck yourself !!")
        else:
            func(name)
    return inner

def decorator2(func):
    def inner(name):
        if name == 'Donold':
            print("what the fuck you are doing?")
        else:
            func(name)
    return inner

# @decorator    # pahle ye execute hoga
# @decorator2    # then ye execute hoga
# def wish(name):
#     print('Hello',name, "Good Morning !")

# wish("kush")
# wish('jenny')
# wish('Sunny')
# wish('Donold')

# explicitly link

def wish(name):
    print('Hello',name, "Good Morning !")

# we can link decorator explicitly
decorFunction = decorator(wish)
decorFunction2 = decorator2(wish)

# wish("kush")
# wish('Sunny')
# wish('Donold')

decorFunction('kush')
decorFunction('Sunny')
decorFunction('Donold')

