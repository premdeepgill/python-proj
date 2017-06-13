#!/usr/bin/python3.5

inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg + '\n')
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()
