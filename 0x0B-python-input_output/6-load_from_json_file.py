#!/usr/bin/python3
""" a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”.

    Args:
        filename: the name of the file will be crete the object from it.
    """
    with open(filename, "r") as f:
        obj = json.load(f)
        return (obj)
