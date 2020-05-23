#!/usr/bin/python3
"""
text_indentation module

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for char in ['.', '?', ':']:
        text = text.replace(char, char + '\n\n')

    print('\n'.join(x.strip() for x in text.split('\n')), end='')
