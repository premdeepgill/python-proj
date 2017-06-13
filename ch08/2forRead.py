#!/usr/bin/python3.5

f = open('textfile.txt', 'r')

for line in f:
    print(line, end= '')

f.close()
