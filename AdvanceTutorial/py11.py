# os and sys module

# checking the file is exist or not?

import os, sys

fname = input('Enter file name : ')

if os.path.isfile(fname):
    print("file exists")
    f = open(fname, 'r')
    print('contents of file : ')
    data = f.read()
    print(data)
    f.close()
else:
    print('file {} not exist !'.format(fname))
    sys.exit(0)

