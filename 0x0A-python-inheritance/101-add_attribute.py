#!/usr/bin/python3
""" a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, atter, V):
    """
     a function that adds a new attribute to an object if it’s possible

     Raise:
        TypeError exception, with the message can't add new attribute
        if the object can’t have new attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, atter, V)
        return
    raise TypeError("can't add new attribute")
