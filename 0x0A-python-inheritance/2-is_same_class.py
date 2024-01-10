#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is exactly an instance
    of the specified class ; otherwise alse.
    """
    if (type(obj) == a_class):
        return True
    return False
