#!/usr/bin/python3
""" a function that returns True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """
     a function that returns True if the object is an instance of a class
     that inherited(directly or indirectly)
     from the specified class ; otherwise False.
     Return:
        True if the object is an instance of a class.
        otherwise False.
    """
    if (type(obj) == a_class):
        return False
    return (isinstance(obj, a_class))
