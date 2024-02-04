# trafic single program

from threading import *
from time import *

e = Event()
def trafficpolice():
    while True:
        sleep(10)
        print('traffic police giving green signal')
        e.set()
        sleep(20)
        print('traffic police giving red signal')
        e.clear()

def driver():
    num = 0
    while True:
        print('driver is waiting for green signal')
        e.wait()
        print('traffic signal is green..vehicles can move')
        while e.is_set():
            num += 1
            print('vehicle number :', num, 'crossing the signal')
            sleep(2)
        print('traffic signal is red ... driver have to wait')

t1 = Thread(target=trafficpolice)
t2 = Thread(target=driver)

t1.start()
t2.start()