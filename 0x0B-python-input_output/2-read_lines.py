#!/usr/bin/python3
""" Task 2 """


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file and prints to stdout
    """
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        counter = 0
        for line in f:
            if counter < nb_lines:
                print(line, end='')
            counter += 1
