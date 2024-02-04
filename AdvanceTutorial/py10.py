# seek() method

data = 'All students are sincere'

f = open('py10.txt', 'w')
f.write(data)

with open('py10.txt', 'r+') as f:
    text = f.read()
    print(text)
    print('current cursor position : ', f.tell())
    f.seek(17)
    print('current cursor position : ', f.tell())
    f.write('gems !!!')
    f.seek(0)
    text= f.read()
    print('data after modification ...')
    print(text)
    
 