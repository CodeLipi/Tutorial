# import time


# import py03 as module2
# print("Sleeping start")
# time.sleep(10)
# import py03 as module2
# print("End of program")




import time
from importlib import reload

import py03 as module2
print("Sleeping start")
time.sleep(10)
reload(module2)
print("End of program")

# print(dir(module2))