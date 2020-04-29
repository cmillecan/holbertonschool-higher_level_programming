#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if b > a and a < 8:
            print("{:d}{:d},".format(a, b), end=' ')
    if a == 8 and b == 9:
        print("{:d}{:d}".format(a, b))
