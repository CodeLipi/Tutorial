# abstract class implementation by child class

from abc import *

class Vehicle(ABC):
    @abstractmethod
    def no_of_vehicle(self):
        pass

class Bus(Vehicle):
    def no_of_vehicle(self):
        return 6
    
class Auto(Vehicle):
    def no_of_vehicle(self):
        return 3
    
class Motorcycle(Vehicle):
    def no_of_vehicle(self):
        return 2

b = Bus()
a = Auto()
m = Motorcycle()

print(a.no_of_vehicle())
print(b.no_of_vehicle())
print(m.no_of_vehicle())