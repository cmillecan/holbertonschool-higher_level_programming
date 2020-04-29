#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz", end=' ')
            continue
        elif num % 3 == 0:
            print("Fizz", end=' ')
            continue
        elif num % 5 == 0:
            print("Buzz", end=' ')
            continue
        else:
            print("{:d}".format(num), end=' ')
    print("Buzz", end=' ')
