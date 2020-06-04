#!/usr/bin/python3
""" Task 3 """


def write_file(filename="", text=""):
    """
    Writes a string to a text file.
    Returns the number of characters written.
    """
    with open(filename, 'w') as f:
        return f.write(text)
