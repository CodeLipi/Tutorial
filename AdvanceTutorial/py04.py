# file handling

# r mode only reads the data


# f = open('py04.txt','w')
# f = open('py04.txt','r')
# f = open('py04new.txt','r') # FileNotFoundError
# f = open('py04.txt','x') # FileExistsError
f = open('py04new.txt','x')

print('file name : ', f.name)
print('file mode : ', f.mode)
print('readable ? : ', f.readable())
print('writeable ? : ', f.writable())

f.close()
print('file closed ? : ', f.closed)

# file handling with existing ?

