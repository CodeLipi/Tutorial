# Synchronization with semaphor 

# l = lock/rlock
# s = semaphor(counter),  default counter=1
# counter defined how many thread acquried at a time

# s.acquire()   count + 1
# s.release()   count - 1

from threading import *
from time import *

s = Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print('good morning ',end='')
        sleep(1)
        print(name)
    s.release()

t1 = Thread(target=wish, args=('Kush',))
t2 = Thread(target=wish, args=('Jenny',))
t3 = Thread(target=wish, args=('Thompson',))
t4 = Thread(target=wish, args=('Kenedy',))
t5 = Thread(target=wish, args=('Noor',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()