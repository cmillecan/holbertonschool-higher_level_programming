#!/usr/bin/python3
"""
Adds all arguments to a Python list
Saves them to a file
"""
import json
from sys import argv
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

new_list = []
if os.path.exists(filename):
    new_list = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

save_to_json_file(new_list, filename)
