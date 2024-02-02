# multi-threading

from threading import *

print('curren thread : ', current_thread().name)   # MainThread
# current_thread().setName('kush')
current_thread().name = 'kush'
print('curren thread : ', current_thread().name)   # kush