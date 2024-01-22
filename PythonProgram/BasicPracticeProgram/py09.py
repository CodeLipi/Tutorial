# factorial progam
# using iterative method


def fact(n):
    if n<0:
        return 0
    elif n==1 or n==0:
        return 1
    else: 
        fact = 1
        while(n>1):
            fact = fact*n
            n = n-1
        return fact

n = int(input('Enter a number : '))

factorial = fact(n)
print("factorial: ", factorial)
