#!/usr/bin/python3
"""function that returns the list of available attributes"""


def lookup(obj):
    """
     a function that returns the list of available attributes
     and methods of an object

     Returns:
        a list object
    """
    return dir(obj)
