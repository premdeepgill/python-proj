#!/usr/bin/python3.5

f = open('textfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline, end= '')
print(secondline)

f.close()
