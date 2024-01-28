# function aliasing or duplicating



def wish(name):
    print('Good Morning', name)

wish('jenny')  #  function call
greet= wish  # function aliasing
greet('kush')  # alias call

print(id(wish))   # 2258750442048
print(id(greet))  # 2258750442048
