#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
     class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation Class
        size must be private. No getter or setter.
        size must be a positive integer, validated by integer_validator.
        """
        if self.integer_validator("size", size) == None:
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area method nust be print the area of squre
        """
        return (self.__size * self.__size)
