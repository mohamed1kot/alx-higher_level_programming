#!/usr/bin/python3
"""a script that adds all arguments to a Python list"""
import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

try:
    file = load("add_item.json")
except (FileNotFoundError):
    file = []

for i in sys.argv[1:]:
    file.append(i)
save(file, "add_item.json")
