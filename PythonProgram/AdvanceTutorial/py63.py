# Inter thread communication
# condition

from threading import *
from time import *

def consumer(c):
    c.acquire()
    print('consumer is waiting for update...')
    c.wait() # now thread will entered into waiting state
    print('consumer got nofication & consuming item...')
    c.release()

def producer(c):
    c.acquire()
    print('producer producing items...')
    sleep(5)
    print('producer giving the notification...')
    c.notify()
    print('producer releasing')
    c.release()


c = Condition()
t1 = Thread(target=consumer, args=(c,))
t2 = Thread(target=producer, args=(c,))
t1.start()
t2.start()