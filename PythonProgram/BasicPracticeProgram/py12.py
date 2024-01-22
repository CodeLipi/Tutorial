# factorial program
# when number is negative too

def fact (n):
    if n<0:
        return nfact(n)
    else:
        return 1 if n==0 or n==1 else n*fact(n-1)

def nfact (n):
    return -1 if n==-1 else n*nfact(n+1)

n = int(input('Enter a number (-ve or +ve): '))
result = fact(n)
print('factorial : ',result)
