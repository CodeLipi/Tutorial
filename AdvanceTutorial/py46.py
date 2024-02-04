# Creating a thread without extending Thread class

from threading import *

class Test:
    def display(self):  # overriding run method
        for i in range(10):
            print('Child thread ', current_thread().name)

obj = Test()
t1 = Thread(target=obj.display).start()
t2 = Thread(target=obj.display).start()
t3 = Thread(target=obj.display).start()
t4 = Thread(target=obj.display).start()

# for i in range(10):
#     print('Main thread ', current_thread().name)