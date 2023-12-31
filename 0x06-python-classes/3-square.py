#!/usr/bin/python3
""" class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """
    class Square that defines a square by: (based on 1-square.py)

    Attributes:
            size :must be an integer.
    """
    def __init__(self, size=0):
        """
        new instance in the square

        args:
            size: size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            pass

    def area(self):
        """
         that returns the current square area.

         args:
            size: Private instance attribute.
        """
        return self.__size ** 2
