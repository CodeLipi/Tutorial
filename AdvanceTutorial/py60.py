# bounded semaphore

from threading import *

# s = Semaphore(2)  # it used lock concept 2--> no of release because no acquire is 2
s = BoundedSemaphore()  # not required any no of released
print('main thread aquired..')
s.acquire()
print('main thread aquired.. again')
s.release()
print('released...')