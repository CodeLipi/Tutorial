# Variable length arguments

def sum(*n):
    result = 0
    for x in n :
        result = result + x
    print('Sum : ', result)


sum()
sum(1)
sum(1,2)
sum(1,2,3)