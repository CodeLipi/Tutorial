class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def eatanddrink():
        print('eating and drinking...')
    # def eatanddrink(self):
    #     print('eating and drinking...')

class SoftwareEngineer(Person):
    def __init__(self,name, age, id, salary):   # taking 4 argument
        super().__init__(name, age)  # sending 2 argument to parent class
        self.id = id
        self.salary = salary
    def info(self):
        print('Details...')
        print(self.name, self.age, self.id, self.salary)

se = SoftwareEngineer('kush',23,1004,15000)
se.info()
se.eatanddrink()