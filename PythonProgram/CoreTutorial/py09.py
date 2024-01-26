# command line argument

from sys import argv 

print(argv) # print the value what we enter in cmd, first value is always current file.
print(argv[1:])

print(type(argv))  # list type
print(len(argv))

print(argv[0])
print(argv[1])
print(argv[2])