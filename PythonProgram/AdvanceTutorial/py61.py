# interthread communication

# Producer and consumer problem

from threading import *
from time import *

e = Event()
def consumer():
    print('consumer thread waiting for update...')
    e.wait()
    print('consumer thread got notification and start consuming items...')

def producer():
    sleep(10)
    print('producer thread producing item..')
    print('producer thread giving notification by settng event')
    e.set()

t1 = Thread(target=producer)
t2 = Thread(target=consumer)

t1.start()
t2.start()
