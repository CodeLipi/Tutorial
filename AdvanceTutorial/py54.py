from threading import *
from time import *

def job1():
    print('job 1 execution ...')
    print(current_thread().name, 'is daemon :', current_thread().daemon)
    ct = Thread(target=job2, name='SubChildThread')
    print(ct.name, 'is daemon :',ct.daemon)
    ct.start()

def job2():
    print('job 2 execution ....')

t = Thread(target=job1,name='ChildThread')
t.daemon = True
t.start()
sleep(5)
print(current_thread().name,'is daemon :',current_thread().daemon)