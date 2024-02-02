# join()

from threading import *
from time import *

def display():
    for i in range(10):
        print('child thread')
        sleep(3)

t = Thread(target=display)
t.start()
# t.join() # here main thread waits until child thread completes
t.join(10) # here main thread waits min 10 sec until child thread completes
for i in range(10):
    print('main thread')