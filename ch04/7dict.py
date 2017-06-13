#!/usr/bin/python3.5

# myDict = {"Peter":23, "John":25, "Jane":21, "Arthur":30}
# userNameAndAge = dict(Peter = 24, John = 26, Jane = 22, Authur = 35)

# declaring the dictionary, dictionary keys and data can be of different data types
myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2}

# print the entire dictionary
print(myDict)       # Items may be displayed in a different order. Items in a dictionary are not necessarily stored in the same order as the way you declared them.

# print the item with key = "One"
print(myDict["One"])

# print the item with key = 7.9
print(myDict[7.9])

# modify the item with key = 2.5 and print the updated dictionary
myDict[2.5] = "Two and a Half"
print(myDict)

# add a new item and print the updated dictionary
myDict["New Item"] = "I'm new here!"
print(myDict)

# remove the item with the key = "One" and print the updated dictionary
del myDict["One"]
print(myDict)
