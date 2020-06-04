#!/usr/bin/python3
""" Task 4 """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.
    Returns the number of characters added.
    """
    with open(filename, 'a') as f:
        return f.write(text)
