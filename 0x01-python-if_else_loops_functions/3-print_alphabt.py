#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if letter in [101, 113]:
        continue
    print("{:c}".format(letter), end="")
