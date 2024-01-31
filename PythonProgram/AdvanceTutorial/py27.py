# Destructor
import time
class Test:
    def __init__(self):
        print('object initialization....')

    def __del__(self):
        # print('fulfiling last wish and performing cleanup activities...')
        print('Destructor execution..')

# t1 = Test()

# t1 = None   # t1 exists and reusable but unlinked with obj
# del t1    # t1 got delete not reusable

# t2 = t1
# t3 = t2
# del t1

# time.sleep(10)
# print('object not yet destroyed after deleting t1')

# del t2
# time.sleep(10)
# print('object not yet destroyed after deleting t2')

# print('I am trying to delete t3 also')
# del t3 

# print('end of app....')
        



l = [Test(), Test(), Test()]
time.sleep(5)
del l
time.sleep(4)
print('end of app....')