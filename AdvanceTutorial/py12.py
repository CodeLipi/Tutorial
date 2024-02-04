# WAP to print the number of lines, words and  characters present in the given file.

import os, sys

fname = input('Enter file name : ')
if os.path.isfile(fname):
    print('file exists : ', fname)
    f = open(fname, 'r')
    print(type(f))
    print(f)
else:
    print('file not exists : ', fname)
    sys.exit(0)    # 0 --> normal termination, nonzero --> abnormal termination

line_count = word_count = char_count = 0

for line in f:
    line_count += 1
    char_count = char_count + len(line)
    words = line.split()
    word_count = word_count + len(words)

print('number of lines : ', line_count)
print('number of words : ', word_count)
print('number of char : ', char_count)
f.close()