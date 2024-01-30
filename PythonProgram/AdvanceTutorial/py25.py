# unpickling multiple data

import pickle

f = open('emp1.dat', 'rb')
print('employee details....')

while(True):
    try:
        obj = pickle.load(f)
        # obj.display()
        if obj.id == 100:
            obj.display()
    except EOFError :
        print('all employee completed...')
        break
# obj1 = pickle.load(f)
# obj2 = pickle.load(f)
# obj3 = pickle.load(f)
# obj4 = pickle.load(f)  # EOFError, because we input only 3 data
# obj.display()
f.close()
