#!/usr/bin/python3
""" Task 1 """


def number_of_lines(filename=""):
    """
    Returns the number of lines in a text file
    """
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
