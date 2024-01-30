# a mode does not override the data
# create file if not exist
# append/write data from the end..

f = open('py06.txt', 'a')

f.write('This is first line \n')
f.write('This is second line \n')
f.write('This is third line \n')
f.close()
print('writing successful to the file... \n')

