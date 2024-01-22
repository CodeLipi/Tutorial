# factorial program
# using ternary method

def fact(n):
    return 1 if n==0 or n==1 else n*fact(n-1)

n = int(input('Enter a number: '))
factorial = fact(n)
print('factorial : ',factorial)
