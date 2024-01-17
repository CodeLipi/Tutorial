# maximum of two number

def maximum(x,y):
    if x>y:
        return x
    else:
        return y
    
a,b = 99,4
# result = maximum(a,b)
# print('Maximum : ', result)

print(maximum(a,b))

# using inbuild max()

print(max(a,b))


# using ternary operator

print(a if a>b else b)