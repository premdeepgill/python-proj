#!/usr/bin/python3.5

j = 0
for i in range(5):
    j += 2
    print('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print("I will be skipped over if j=6!")
