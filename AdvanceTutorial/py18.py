# reading zipping file

from zipfile import *

f = ZipFile("zipped.zip",'r',ZIP_STORED)
names = f.namelist()
for name in names:
    print('file name : ', name)
    