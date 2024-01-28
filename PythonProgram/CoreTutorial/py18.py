# dictionay


# d = dict()
d = {'name1' : 'jenny', 'name2' : 'john', 'name3' : 'david'}

# print(d['name3'])  # prints value of 1 key
# print(d.keys())  # prints all the keys

# update
d['name4'] = 'lavrov'

# prints whole dictionary
# print(d)

# del
# del d['name1']

# clear
# d.clear()

d[1024] = 'even number'

l = [1,2,3,4,5,6,7,8,9,10]
t = (10,)
s = {12,34}
d['list']  = l
d['tuple']  = t
d['set']  = s

# print(d)

# print(len(d))

# d.get(key, default value)
# print(d.get(100))
# print(d.get(100, 'kush'))

# print(d.pop('set'))

# print(d.popitem())  # remove random key-value
# print(d.popitem())  # remove random key-value
# print(d.popitem())  # remove random key-value

# print(d.popitem())  # remove random key-value, when dict is empty raise error

# # whole access
# for x in d:
#     print(x, '\t', d[x])

print('keys.....................')
for key in d.keys():
    print(key)
print('values.......................')
for value in d.values():
    print(value)
print('items..................')
for item in d.items():
    print(item)
print('keys............value.................')
for key,value in d.items():
    print(key, '\t', value)

