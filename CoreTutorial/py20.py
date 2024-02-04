d = {}

word = input('enter :')
for x in word:
    d[x] = d.get(x,0) + 1
print(d)

words = dict ()