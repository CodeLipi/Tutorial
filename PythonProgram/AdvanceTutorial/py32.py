# match()

import re

s = input('Enter pattern : ')
m = re.match(s,'abcdefgh')

if m!= None:
    print('Match is available at beginning')
    print('start index : {} and end index : {}'.format(m.start(), m.end()))
else:
    print('Not find at beginning')