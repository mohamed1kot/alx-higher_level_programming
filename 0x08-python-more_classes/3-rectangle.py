#!/usr/bin/python3
"""defines a rectangle class"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle

    Attributes:
        width: width of rectangle.
        height: height of rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        create a new instance of rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        function is retraive the width

        return:
            th width of rectangle
        """
        return self.__width

    @property
    def height(self):

        """
        function is retraive the height

        return:
            th height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):

        """
        setter height of rectangle
        Args:
            vlaue: int value of height value
        Raise:
            TypeError: if height is not int
            ValueError: if height is less then Zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):

        """
        setter width of rectangle
        Args:
            vlaue: int value of width value
        Raise:
            TypeError: if width is not int
            ValueError: if width is less then Zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("widht must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Public instance method return the area of Rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Public instance method that returns the perimeter of rectangle
        """
        if ((self.__width or self.__height) == 0):
            return (0)
        return ((2 * (self.__width + self.__height)))

    def __str__(self):
        """
        print the rectangle with the character #
        Returns:
             rectangle with the character #
        """
        rectangle = ""
        if ((self.__width or self.__height) == 0):
            return ("")
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle += "#"
            if (h != (self.__height - 1)):
                rectangle += "\n"
        return (rectangle)
