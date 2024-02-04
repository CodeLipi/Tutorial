# pickling : process of saving (writing) state of object in a file
# unpickling : process of reading state of object in a file

import pickle
class Employee:
    def __init__(self,id,name,salary,address):
        self.name = name
        self.id = id
        self.salary = salary
        self.address = address

        # vertical are instance variable
    def display(self):
        print(self.name, self.id, self.salary, self.address)

# emp = Employee(100,'jenny',1200,'ohio')
# print(emp.id)
# print(emp.name)
# print(emp.salary)
# print(emp.address)

# emp.display()
        
with open('emp.dat','wb') as f:
    e1 = Employee(100,'jenny', 1200, 'ohio')
    # e2 = Employee(102, 'john', 1000,'petersburg')
    # perform pickling
    pickle.dump(e1,f)
    # pickle.dump(e2,f)
    print('Pickling of Employee object completed...')

with open('emp.dat','rb') as f:
    # perform unpickling
    obj = pickle.load(f)
    print('Employee Information after unpickling....')
    obj.display()


