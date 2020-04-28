#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number > 5:
    print("The Last digit of {:d} is {:d} and is greater \
than 5".format(number, last_digit))
elif number == 0:
    print("The Last digit of {:d} is {:d} and \
is 0".format(number, last_digit))
else:
    print("The Last digit of {:d} is {:d} and is \
less than 6 and not 0".format(number, last_digit))
