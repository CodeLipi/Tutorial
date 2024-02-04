# zipping file

from zipfile import *

f = ZipFile("zipped.zip",'w',ZIP_DEFLATED)

# added file to be zipped into single zip file
f.write('zip1.txt')
f.write('zip2.txt')
f.write('zip3.txt')
f.close()
print('zip file created...')