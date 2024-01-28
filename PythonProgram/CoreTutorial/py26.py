def double(x):
    return x*2

l = [0,2,5,8,10,12,15,19,20]
doubleList = list(map(double,l))
print(doubleList)   # filtered output of even number

# map function takes value and the function return calculated value

# by map and lambda fn

l = [0,2,5,8,10,12,15,19,20]
dList = list(map(lambda x : x*2, l))
print(dList)
