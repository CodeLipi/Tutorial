from functools import reduce


l = [10,20,30,0,50,60,70,77]
add = reduce(lambda x,y : x+y, l)

print(add)