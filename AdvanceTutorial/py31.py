# regular expresion

import re

# matcher = re.finditer('[abc]','abdfabdfbadccsbcsabd')
# matcher = re.finditer('[^abc]','abdfabdfbadccsbcsabd')
# matcher = re.finditer('[a-z]','abdfabdfbadccsbcsabd')
# matcher = re.finditer('[A-Z]','HASACSAVSDGSD2394U2Y34Y2')
# matcher = re.finditer('[0-9]','HASACSAVSDGSD2394U2Y34Y2')
# matcher = re.finditer('[0-9A-Za-z]','xcnsfsdfHASACSAVSDGSD2394U2Y34Y2')
# matcher = re.finditer('[^0-9A-Za-z]','vdf@#$@#kxvjk#4Y2')
# matcher = re.finditer('a','abababaaaababaaaabb')
# matcher = re.finditer('a+','abababaaaababaaaabb')
# matcher = re.finditer('a*','abababaaaababaaaabb')
# matcher = re.finditer('a?','abababaaaababaaaabb')
# matcher = re.finditer('a{3}','abababaaaababaaaabb')
# matcher = re.finditer('a{1,4}','abaabaaabaaaababaaaabb')
# matcher = re.finditer('[^a]','abaabaaabaaaababaaaabb')
matcher = re.finditer('^a','abaabaaabaaaababaaaabb')

for m in matcher:
    print(m.start(),'......',m.group())