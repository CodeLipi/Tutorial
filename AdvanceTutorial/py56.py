from threading import *


l = Lock()
print('main thread acquire the lock')
l.acquire()
print('main thread acquire the lock again')
l.acquire()
print('main thread acquire the lock again once')
l.acquire()
print('main thread release the lock')
l.release()
# recursive lock hang the program, works on second lock only


# in recursion theread is lock again and again
# def f1(n):
#     l = acquire()
#     result = f1(n-1)*n