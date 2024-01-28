# this is module

a = 10   # global variable

def f1():
    # global a = 1000  # this type of global declaration is possible

    global a  # to make global variable inside the fn
    a = 1000  # overwrite the global variable inside the function
    b = 20  # local variable
    print('f1 function :',a)
    print('f1 function :',b)

def f2():
    global a  # to make change in here of global(update)
    a = 2000
    print('f2 function :',a)   # here global var is not overwitten
    # print('f2 function :',b)  # local variable is not accessed here


f1()
f2()


# if we change order global variable changes
# f2()
# f1()