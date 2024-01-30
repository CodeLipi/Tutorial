# handling binary data

f1 = open('tree.jpg', 'rb')   # it works for input.mp4, input.png ...
f2 = open('newpic.jpg', 'wb')

bytes = f1.read()
f2.write(bytes)

print('new image created !!')
# print(bytes)

f1.close()
f2.close()