#!/usr/bin/python3.5
#
# Inline IF statement example below:
# num1 = 12 if userInput == "1" else 13

userInput = input("Enter 1 or 2: ")

if userInput == "1":
    print("Hello World")
    print("How are you?")
elif userInput == "2":
    print("Python Rocks!")
    print("I love Python")
else:
    print("You entered an invalid number.")