#!/usr/bin/python3
"""function that writes an Object to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file
    using a JSON representation.

    Args:
        my_obj: the dict will be converted to josn file.
        filename: the name of file will be created.
    """
    with open(filename, "w") as file:
        obj = json.dumps(my_obj)
        file.write(obj)
