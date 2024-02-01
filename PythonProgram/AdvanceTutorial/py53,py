from threading import *
from time import *

def job():
    for i in range(10):
        print('child thread')
        sleep(3)

t = Thread(target=job)
t.daemon = True   # but here we can the nature because its not active
t.start()
# t.daemon = True   # we can not nature of active thread
# sleep(5)
print('end of main thread..')