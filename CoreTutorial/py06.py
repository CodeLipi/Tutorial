x = 10
print(id(x))  # 140709768252120

y = 10
print(id(y))  # 140709768252120

print(x is y)

x  = 11
print(id(x)) # 140709768252152

print(x is y)

x = 257
y = 257

print(x is y)

x = 10.0
y = 10.0
print(x is y)

x = 3+4j
y = 3+4j
print(x is y)