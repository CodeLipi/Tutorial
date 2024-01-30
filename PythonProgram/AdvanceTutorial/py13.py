# reading line by line data

# f = open('py11.txt', 'r')
# for line in f :
#     print(line, end = '')
# f.close()



# reading char by char data

f = open('py11.txt', 'rb')
for char in f.read():
    # print(char)    # returns unicode of char
    print(chr(char), end=' ')
f.close()