# factorial program
# using for loop

def fact(n):
    fact = 1
    for i in range(2, n+1):
        fact = fact*i
    return fact

n = int(input('Enter a number : '))
result = fact(n)
print('factorial : ',result)
