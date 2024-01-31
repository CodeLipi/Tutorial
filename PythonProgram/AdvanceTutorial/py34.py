# search()

import re

s = input('Enter pattern : ')
m = re.search(s,'abaabaaab')

if m!= None:
    print('Match is available')
    print('First occurrence with start index : {} and end index : {}'.format(m.start(),m.end()))
else:
    print('Match is not available')