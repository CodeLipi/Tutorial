# Reading all the mobile no from a website  


import re
from urllib import request as req

u = req.urlopen('https://www.redbus.in/info/contactus')

text  = u.read()
numbers = re.findall('[0-9]{12}',str(text))

for n in numbers:
    print(n)