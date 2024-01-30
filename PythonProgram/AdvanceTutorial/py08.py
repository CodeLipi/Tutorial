# with statement 


with open('py08.txt','w') as f:
    f.write('This is line 1 \n')
    f.write('This is line 2 \n')
    f.write('This is line 3 \n')
    print('file closed ? : ', f.closed)
print('file closed ? : ', f.closed)