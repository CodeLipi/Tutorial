# abstraction

# abstract method
# only declaration, not the proper implematation

# abstract class
# partial implementation of a class

from abc import *

class Vehicle:
    @abstractmethod
    def no_of_vehicle(self):  # abstract method
        pass

# class Fruit(ABC):  # abstract class (can't instantiate abstract class without an implementation for abstract method)
#     @abstractmethod
#     def taste(self):  # abstract method
#         pass
#    
       
class Fruit(ABC):  # abstract class (can't instantiate abstract class without an implementation for abstract method)
    def taste(self):  # abstract method
        print('hello fruit abstract method')

v = Vehicle()
f = Fruit()
f.taste()
