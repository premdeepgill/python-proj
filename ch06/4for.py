#!/usr/bin/python3.5

message = "Hello"
pets = ["cats", "dogs", "turtles", "hamsters"]
age = {"Peter":5, "John":7}

for i, p in enumerate(pets):
    print(i, p)

for i in age:
    print("Name = %s, Age = %d" %(i, age[i]))

for i, j in age.items():
    print("Name = %s, Age = %d" %(i, j))

for i in message:
    print(i)
