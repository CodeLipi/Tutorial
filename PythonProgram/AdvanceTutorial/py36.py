# subn()

import re

t = re.subn("\\d",'xxxxx','a7b5e4d9')
print(t)
print(type(t))
print('The result string : ', t[0])
print('The no of replacement : ', t[1])