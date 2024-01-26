from sys import argv

# working with number
# when we enter value on cmd it takes as string
# ex: 10 20 treated as '10','20'

print('Your input on cmd : ', argv)

# so while adding the number type conversion is must
# here we can also use eval() function for type conversion

print('Sum of argument : ', int(argv[1]) + int(argv[2]))
# print('Sum of argument : ', eval(argv[1]) + eval(argv[2]))