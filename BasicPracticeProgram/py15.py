# Prime number : checking...

n = int(input('Enter a num : '))
flag = False

if n == 1:
    print('Not Prime No : ', n)

for i in range(2,n):
    if n%i == 0:
        flag = True

if flag:
    print('Not Prime No : ', n)
else:
    print('Prime No : ', n)