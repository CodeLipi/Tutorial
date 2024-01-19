# Prime No Program
# Half Method
# This program is fast because it checks half the value

n = int(input('enter a no : '))

flag = False

if n==1:
    print('Not Prime')

for i in range(2,n//2+1):
    if n%i == 0:
        flag = True

if flag:
    print('Not Prime')
else:
    print('Prime')
