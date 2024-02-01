from time import *
from threading import *

def doubles(numbers):
    for i in numbers:
        sleep(1)
        print('doubles : ', i*2)

def squares(numbers):
    for i in numbers:
        sleep(1)
        print('squares : ', i*i)   

# begintime = time.time()
numbers = [1,2,3,4,5,6]
begintime = time()

# doubles(numbers)
# squares(numbers)

t1 = Thread(target=doubles, args=(numbers,))
t2 = Thread(target=squares, args=(numbers,))

t1.start()
t2.start()

# using this main thread wait to complete both
if t1.is_alive():
    t1.join()
else : 
    print('t1 not alive')

if t2.is_alive():
    t2.join()
else : 
    print('t2 not alive')
# t1.join()
# t2.join()

# main thread starts
endtime = time()
print('total time taken : ', endtime-begintime)