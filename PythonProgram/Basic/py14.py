# Check a number is prime or not ?

def prime(n):
    count = 0
    for i in range (1,n+1):
        if n%i == 0:
            count = count +1

    if count == 2:
        print('prime')
    else:
        print('not prime')

user_input = int(input('Enter a number : '))
prime(user_input)
