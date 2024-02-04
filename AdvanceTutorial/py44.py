# Creating a thread by extending Thread class

from threading import *

class Mythread(Thread):
    def run(self):  # overriding run method
        for i in range(10):
            print('Child thread')

t = Mythread().start()

for i in range(10):
    print('Main thread')