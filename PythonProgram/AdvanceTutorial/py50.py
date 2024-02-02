# ident()
# active_count()

from threading import *
from time import *

def display():
    # print('child thread', current_thread().ident)
    print('started....', current_thread().name)
    sleep(3)
    print('ended....', current_thread().name)
print('no of active thread', active_count())
# print('no of active thread', active_count())

t1 = Thread(target=display, name='childThread 1')
t2 = Thread(target=display, name='childThread 2')
t3 = Thread(target=display, name='childThread 3')
t1.start()
t2.start()
t3.start()

print('Main thread id number ', current_thread().ident)
print('no of active thread', active_count())
sleep(3)
print('no of active thread', active_count())
# print('Child thread id number ', t.ident)

