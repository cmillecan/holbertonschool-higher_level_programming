#!/usr/bin/python3
""" Task 15 """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string.
    """
    with open(filename) as f:
        contents = f.readlines()

    with open(filename, 'w') as f:
        string = ''
        for line in contents:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)
