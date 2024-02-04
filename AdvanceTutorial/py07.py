# r mode only read the data
# does not create file if not exist 
# if file is not exist then raise FileNotFoundError


# f = open('py07new.txt', 'r')   # FileNotFoundError
f = open('py07.txt', 'r')   # FileNotFoundError

# data = f.read()
# data_10 = f.read(10)
# data_1_line = f.readline()
# data_1_line = f.readline()
data_list = f.readlines()

# print(type(data))   # string type



# print(data)  # read whole data
# print(data_10)  # read 10 character --> This is fi
# print(data_1_line)  # read 1 line --> This is first line

# always add a new line character print which
# print(data_1_line)  # read 1 line --> This is first line
# print(data_1_line)  # read 1 line --> This is first line
# print(data_1_line)  # read 1 line --> This is first line

# not added new line
# print(data_1_line, end='')  # read 1 line --> This is first line
# print(data_1_line, end='')  # read 1 line --> This is first line

# print(f.readlines())  # this return list

for line in data_list:
    print(line, end='')
f.close()
