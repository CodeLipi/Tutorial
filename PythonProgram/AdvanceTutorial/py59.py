# Bounded Semaphore
# method to call release() multiple time


from threading import *

s = Semaphore()  # it used lock concept
s.acquire()
print('main thread aquired..')
s.acquire()
print('main thread aquired.. again')
s.release()   # it solved by bounded semaphore