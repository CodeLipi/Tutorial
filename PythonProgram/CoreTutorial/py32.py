# Generators

def countdown(num):
    print("Start coundown")
    while(num>0):
        yield num
        num -= 1

values = countdown(5)
for x in values :
    print(x)