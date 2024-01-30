# pickling : process of saving (writing) state of object in a file
# unpickling : process of reading state of object in a file

class Employee:
    def __init__(self,id,name,salary,address):
        self.name = name
        self.id = id
        self.salary = salary
        self.address = address

        # vertical are instance variable

emp = Employee(100,'jenny',1200,'ohio')
print(emp.id)
print(emp.name)
print(emp.salary)
print(emp.address)