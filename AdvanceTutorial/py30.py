# regular expression

import re

# search = re.compile('bab')
# matcher = search.finditer('abbabababababababababbabababaababab')

matcher = re.finditer('ab','abbabababababababababbabababaababab')

count = 0
for m in matcher:
    count += 1
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
print("Match find no of times : ",count)