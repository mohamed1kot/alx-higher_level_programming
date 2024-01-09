#!/usr/bin/python3
"""a function return the dictionary description with simple data structure"""


def class_to_json(obj):
    """
     a function that returns the dictionary description with
     simple data structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object

     Args:
        obj:  is an instance of a Class
    Return:
        dictinary
    """
    return obj.__dict__
