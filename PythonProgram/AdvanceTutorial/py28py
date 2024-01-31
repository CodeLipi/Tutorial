# How to find number of references of an object ?

import sys

class Test:
    pass

t1 = Test()

t2 = t1
t3 = t1
t4 = t1

# print(sys.getrefcount(t1))  # 5 because python internal maintain one reference object


del t1
print(sys.getrefcount(t2))  # 4