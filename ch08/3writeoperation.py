#!/usr/bin/python3.5

f = open('textfile.txt', 'a')

f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!')

f.close()
