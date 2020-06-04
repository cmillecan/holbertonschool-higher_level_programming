#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """
    Reads a file and prints it to stdout
    """
    with open(filename) as f:
        print(f.read(), end='')
