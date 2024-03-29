#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        method must be implemented
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        should print, and str() should return, the following rectangle
        description: [Rectangle] <width>/<height>
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
