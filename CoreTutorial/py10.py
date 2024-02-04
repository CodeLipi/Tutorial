# working with command line argument

from sys import argv
print('The number of argument : ', len(argv))
print('The list of argument : ', argv)

print('Command line argument one by one : ')
for x in argv :
    print(x)
