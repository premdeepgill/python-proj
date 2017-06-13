#!/usr/bin/python3.5

message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
    # Global  variables are accessible inside a function
    print(message1)
    # Declaring a local variable
    message2 = "Local variable"
    print(message2)

"""
Calling the function
Note that myFunction() has no parameters.
Hence, when we call this function,
we use a pair of empty parentheses.
"""
myFunction()

print("\nOUTSIDE THE FUNCTION")

# Global variables are accessible outside
print(message1)

# Local variables are NOT accessible outside the function
#print(message2)
