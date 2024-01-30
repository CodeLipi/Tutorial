# working with directories

# walk()

import os

for dirpath, dirnames, filenames in os.walk('.'):
    print('cwd : ', dirpath)
    print('directories : ', dirnames)
    print('filenames : ', filenames)
    print('...........................................')