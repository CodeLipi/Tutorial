# d[key] = value
# if key is present then old value is replace with new value
    
# d.setdefault(key,value)
# in this case if key is present then previous value holds not replace with new one.
 
d = {1:10,2:20,3:30,4:40}
# d[1]='str'
print(d[1])

d.setdefault(1,'notstring')
print(d[1])


d1 = {111:'34'}

d1.update(d)
print(d)
print(d1)

