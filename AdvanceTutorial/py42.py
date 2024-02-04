# Creating a thread without using any class

from threading import *

def display():
    # print('hello')
    print('This code (display) executed by thread : ', current_thread().name)

# print('This code executed by thread : ', current_thread().name)
t = Thread(target=display)   # MainThread create child thread object
# print('hi')
# print('This code executed by thread : ', current_thread().name)

t.start()  # Thread-1 (display)
print('This code executed by thread : ', current_thread().name)

