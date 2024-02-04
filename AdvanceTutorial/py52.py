# Daemon thread

from threading import *

def job():
    print('child thread')

t = Thread(target=job)  # main is parent and t is child
print(t.daemon)   # False
# t.setDaemon(True)  # depricated
t.daemon = True
print(t.daemon)   # True



# print(current_thread().isDaemon())
# print(current_thread().name)
# print(current_thread().daemon)
# print(current_thread().setDaemon(True))  # mainthread is not changable to daemon