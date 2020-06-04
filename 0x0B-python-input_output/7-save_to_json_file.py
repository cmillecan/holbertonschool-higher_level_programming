#!/usr/bin/python3
""" Task 7 """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Opject to a text file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
