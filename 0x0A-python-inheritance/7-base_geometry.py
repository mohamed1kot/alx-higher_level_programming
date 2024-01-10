#!/usr/bin/python3
"""a class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry:
    """
    a class BaseGeometry (based on 5-base_geometry.py).
    """
    def area(self):
        """
        instance method: def area(self): that raises an
        Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method.

        raises:
            if value is not an integer: raise a TypeError
            exception,with the message <name> must be an integer.
            if value is less or equal to 0: raise a ValueError
            exception with the message <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
