a = 10

def f1():
    a = 20
    print(a)  # 20 : local variable
    # print(globals())  # this prints whole dictionary of global variables
    print(globals()['a'])  # 10 : global variable

f1()