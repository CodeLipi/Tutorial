# adding number when user input

a = input('Enter first number : ')
b = input('Enter second number : ')

sum = float(a) + float(b)
print(f'The sum of {a} and {b} : {sum}')   # f-string method

print('The sum of {0} and {1} is {2}'.format(a,b,sum)) # format method