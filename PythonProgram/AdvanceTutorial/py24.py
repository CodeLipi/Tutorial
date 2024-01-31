# pickling multple data object

import pickle, py23 as p


f = open('emp1.dat', 'wb')
n = int(input('Enter no of employee : '))
for i in range(n):
    eno = int(input('Enter id : '))
    ename = input('Enter name : ')
    esal = int(input('Enter salary : '))
    eaddr = input('Enter city : ')

    e = p.Employee(eno, ename, esal, eaddr)
    pickle.dump(e,f)
    print('data stored in file....')

f.close()