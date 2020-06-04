#!/usr/bin/python3
""" Task 1 """


def number_of_lines(filename=""):
    """
    Returns the number of lines in a text file
    """
    count = 0
    with open(filename) as f:
        for i in f:
            count += 1
    return count
