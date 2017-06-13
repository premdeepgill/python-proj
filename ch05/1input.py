#!/usr/bin/python3.5
#
# Note that the input() function differs slightly in Python 2 and Python 3.
# In Python 2, if you want to accept user input as a string, you have to
# use the raw_input() function, which works similar to
# the input() function in Python 3.

myName = input("Please enter your name: ")
myAge = input("Hi %s, what about your age: " %(myName))

print("Hi {}, you turned {} years old today.".format(myName, myAge))
print("Hello World, my name is", myName, "and I am", myAge, "years old.")