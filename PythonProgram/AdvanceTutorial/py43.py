from threading import *

def display():
    for i in range(1,11):
        print('child thread')

t = Thread(target=display).start()
for i in range(10):
    print('Main thread ')


# thread overlap each other