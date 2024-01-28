# simple way to calling inner function directly

def outer():
    print("outer function started")
    def inner():
        print('inner function execution')
    print('outer function returning to inner function')
    return inner    # returning whole function
    # return inner()     # returning  the function what is inside of this return

f1 = outer()
print(f1())  # None
f1()    # this holds the inner function
f1()
f1()
f1()
f1()

# f1 = outer  # assign a new name for outer function
