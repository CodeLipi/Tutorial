# composition
# has a relationship

class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    def getinfo(self):
        print('Car name : {}, Model : {}, Color : {}'.format(self.name,self.model,self.color))

class Employee:
    def __init__(self, id, name, car):
        self.id = id
        self.name = name
        self.car = car
    def empinfo(self):
        print('Emp id : ', self.id)
        print('Emp Name : ', self.name)
        print('Emp car info : ', self.car.getinfo())

c = Car('Ferari', 'SuperSonic', 'LightBlue')
emp = Employee(1435, 'Kush', c)
# so emp has a relationship with c

emp.empinfo()



# class X:
#     def m1():
#         pass
#     def m2():
#         pass
#     def m3():
#         pass
#     def m4():
#         pass

# class Y:
#     pass

# x = X()

# x.m1()
# x.m2()
# x.m3()
# x.m4()

# class Y has a X reference