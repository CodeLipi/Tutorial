# Synchronization with RLock(Re-entrant lock/again and agin lock==> recursive lock) concept 

from threading import *
from time import *

l = RLock()
print('main thread acquire the lock')
l.acquire()
print('main thread acquire the lock again')
l.acquire()
print('main thread acquire the lock again once')
l.acquire()
print('main thread release the lock')
l.release()   # 1 baar hi kafi hai release ke liye
# l.release()
# l.release()

# this works with rlock
# best for recursive lock