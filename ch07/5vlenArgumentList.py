#!/usr/bin/python3.5

# Non-keyworded variable length argument list
def addNumbers(*num):
    sum = 0
    for i in num:
        sum += i
    print(sum)

addNumbers(23, 324, 43535, 6654)

# Keyworded variable length argument list
def printMemberAge(**age):
    for i, j in age.items():
        print("Name = %s, Age = %s" %(i, j))

printMemberAge(Peter = 5, John = 7)
