# join()

from threading import *
from time import *

def display():
    for i in range(10):
        print('name:',current_thread().name)
        sleep(3)

# t = Thread(target=display,name='child thread')
t1 = Thread(target=display,name='child thread 1')
t2 = Thread(target=display,name='child thread 2')
# t.start()
t1.start()
t2.start()
# t.join() # here main thread waits until child thread completes
# t.join(10) # here main thread waits min 10 sec until child thread completes
t1.join()
t2.join()
for i in range(10):
    print('main thread')