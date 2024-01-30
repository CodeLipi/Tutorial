# tell() method

f = open('py09.txt', 'r')
print(f.tell())   # 0
print(f.read(4))    # This
print(f.tell())     # 4
print(f.read(10))   #  is first
print(f.tell())     # 14
f.close()
