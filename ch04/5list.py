#!/usr/bin/python3.5

# declaring the list, list elements can be of different data types
myList = [1, 2, 3, 4, 5, "Hello"]

# print the entire list
print(myList)

# print the third item
print(myList[2])

# print the last item
print(myList[-1])

# assign myList (from index 1 to 4) to myList2 and print myList2
myList2 = myList[1:5]
print(myList2)

# modify the second item in myList and print the updated list
myList[1] = 20
print(myList)

# append a new item to myList and print the updated list
myList.append("How are you")
print(myList)

# remove the sixth item from myList and print the updated list
del myList[5]
print(myList)
