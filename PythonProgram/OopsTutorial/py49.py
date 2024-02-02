# Interface vs Abstract vs Concrete

from abc import *

class DBInterface(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def disconnect(self): pass
    
class Oracle(DBInterface):
    def connect(self):
        print('connecting...Oracle')
    def disconnect(self):
        print('disconnecting...Oracle')

class Mysql(DBInterface):
    def connect(self):
        print('connecting...Mysql')
    def disconnect(self):
        print('disconnecting...Mysql')

class Sybase(DBInterface):
    def connect(self):
        print('connecting...Sybase')
    def disconnect(self):
        print('disconnecting...Sybase')

dbname = input('enter db name :')
classname = globals()[dbname]

# print(type(classname))   # this return abc type class

x = classname()
x.connect()
x.disconnect()

# print(globals())
