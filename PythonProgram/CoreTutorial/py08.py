# Read multiple value in single line 

# a,b = [int(x) for x in input('Enter 2 value: ').split()]
# print('Your input : ',a,b)
# print('product of your input : ', a*b)



a,b = [float(x) for x in input('Enter 2 value: ').split(',')]
print('Your input : ',a,b)
print('product of your input : ', a*b)