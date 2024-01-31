# fullmatch()

import re

s = input('Enter pattern : ')
m = re.fullmatch(s,'abcdefgh')

if m!= None:
    print('Full string matched')
else:
    print('Full string not matched')