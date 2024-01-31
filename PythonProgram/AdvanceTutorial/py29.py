# regular expression

import re

# search = re.compile('kush')
search = re.compile('ab')
# print(type(search))

# matcher = search.finditer('kush is learnig regular expression and kush is anonymous !!')
matcher = search.finditer('ajabababdfjsdfsdfsabababaaabbbjfsjadfjasdfasdfaaabababababsdfjioasfsdfassdababababjsdfsjdfjsabbbbsjkfsaaabababbabaaaabbabb')

count = 0
for match in matcher:
    count += 1
    print('Match at index : ', match.start())
print("Match find no of times : ", count)