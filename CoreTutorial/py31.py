# why we use tuple over list


# list = [x*x for x in range(10000000000000000000000000000000)]  # this gives MemoryError
tuple = (x*x for x in range(10000000000000000000000000000000))  # this doesn't raise any error

# for x in list:
#     print(x)   # raise MemoryError

print(type(tuple))  # <class 'generator'>
# not the tuple because comprehension is not applied on tuple when we apply its become generator

# for x in tuple:
#     print(x)  # this doesn't raise any error