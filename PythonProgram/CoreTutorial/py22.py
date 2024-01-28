def display (**n):   # **n works as dict (**kwargs)
    print("record info")
    for key, value in n.items():
        print(key,"\t",value)

display(name = 'kush', marks = 100, age = 23, day = 'sumday')
display(name = 'jenny', marks = 140, age = 53, day = 'mmonday', job = 'cs')
display(name = 'kolfher', marks = 123, day = 'mmonday', job = 'service')