# Synchronization by using lock concept

# l = Lock()
# l.acquire()
#     performing synchronized operation (critical code)
# l.release()


from threading import *
from time import *
l = Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print('good morning ', end='')
        sleep(1)
        print(name)
    # l.release()

t1 = Thread(target=wish, args=('Kush',))
t2 = Thread(target=wish, args=('Jenny',))
t3 = Thread(target=wish, args=('John',))
t4 = Thread(target=wish, args=('Peter',))
t5 = Thread(target=wish, args=('Ken',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

sleep(12)
print(t1.is_alive())
print(current_thread().is_alive())

# program got hanged because lock is