# w mode override the data
# create file if not exists


f = open('py05.txt', 'w')

# f.write('This is first line \n')
# f.write('This is second line \n')
# f.write('This is third line \n')

list = ['line 1 \n', 'line 2 \n', 'line 3 \n', 'line 4 \n' ,'line 5 \n' ,'line 6 \n' ,'line 7 \n' ,'line 8 \n' ,'line 9 \n']

f.writelines(list)
f.close()

print('writing successful to the file... \n')
