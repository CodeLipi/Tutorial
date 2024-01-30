# reading csv file

import csv

f = open('emp.csv','r')
r = csv.reader(f)    # return csv reader object pointing to f
data = list(r)
# print(type(data), type(r))

for line in data:
    for word in line:
        print(word, '\t', end='')
    print()
f.close()