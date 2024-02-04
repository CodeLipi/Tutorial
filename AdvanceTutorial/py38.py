# Write a program to extract the mobile no from a text file 

import re

f1 = open('in.txt', 'r')
f2 = open('out.txt', 'w')

for line in f1:
    list = re.findall('[6-9]\\d{9}', line)
    for number in list:
        f2.write(number+'\n')

print("All the number extracted in out.txt file")

f1.close()
f2.close()