def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False

l = [0,2,5,8,10,12,15,19,20]
evenList = list(filter(isEven,l))
print(evenList)   # filtered output of even number

# filter function takes value and when the function return True, filter works on True and False (boolean value)

# by filter and lambda fn

l = [0,2,5,8,10,12,15,19,20]
eList = list(filter(lambda x : x%2==0, l))
print(eList)
