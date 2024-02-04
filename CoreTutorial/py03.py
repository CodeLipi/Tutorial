
f = 10  # 10.0
f = 10.2    # 10.2

# f = 0b10.2  # doesn't support binary
# f = 0o10.2  # doesn't support octal
# f = 0x10.2  # doesn't support hexa decimal

f = 1.2e4   # 12000.0
f = 1.2e100     # 1.2e+100
f = 1.2e100000   # inf (infinite)


n = 1.2e-3      # 0.0012
n = 1.2e-10     # 1.2e-10
n = 1.2e-10000000     # 0


print(f)
print(n)
