# Inner classes

class Person:
    def __init__(self):
        print('Person class constructor ...')
        self.name = 'kush'
        self.dob = self.Dob()   # notice here for Dob initialization
    def display(self):
        print('name : ', self.name)
    class Dob:
        def __init__(self):
            print('Date of birth constructor ....')
            self.dd = 23
            self.mm = 4
            self.yy = 2023
        def display(self):
            print('Date of birth : {}/{}/{} '.format(self.dd, self.mm, self.yy))

p = Person()
p.display()
# p.Dob().display()
p.dob.display()