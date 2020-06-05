#!/usr/bin/python3
""" Task 9 """
from sys import argv
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    new_list = load_from_json_file(filename)
else:
    new_list = []

for i in sys.argv[1:]:
    new_list.append(i)

save_to_json_file(new_list, filename)
