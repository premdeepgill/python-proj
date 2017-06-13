#!/usr/bin/python3.5

inputFile = open('in.png', 'rb')
outputFile = open('out.png', 'wb')

imageBuffer = inputFile.read(10)

while len(imageBuffer):
    outputFile.write(imageBuffer)
    imageBuffer = inputFile.read(10)

inputFile.close()
outputFile.close()
