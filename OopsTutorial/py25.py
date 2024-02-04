# accessing member of a class to another class


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print('id : ', self.id)
        print('name : ', self.name)
        print('salary : ', self.salary)


class UpdateEmp:
    def update(emp):
        emp.salary = emp.salary + 1000
        emp.display()

e = Employee(100,'jenny', 10000)
UpdateEmp.update(e)