# enumerate() list of thread

from threading import *
from time import *

def display():
    print('started....', current_thread().name)
    sleep(3)
    print('ended....', current_thread().name)

t1 = Thread(target=display, name='childThread 1')
t2 = Thread(target=display, name='childThread 2')
t3 = Thread(target=display, name='childThread 3')
t1.start()
t2.start()
t3.start()

l = enumerate()  # l = [t1,t2,t3]
for t in l:
    print('name:',t.name)
    print('alive?:',t.is_alive())

sleep(10)
print('after 10 seconds of sleeping...')
print(t1.name,'alive?:',t1.is_alive())
print(t2.name,'alive?:',t2.is_alive())
print(t3.name,'alive?:',t3.is_alive())
l = enumerate()  # l = [mainthread]
for t in l:
    print('name:',t.name)
    print('alive?:',t.is_alive())