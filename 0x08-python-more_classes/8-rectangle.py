#!/usr/bin/python3
"""defines a rectangle class"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle

    Attributes:
        width: width of rectangle.
        height: height of rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        create a new instance of rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                rectangle += str(self.print_symbol)
            if (h != (self.__height - 1)):
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """
        Print the message Bye rectangle...
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        raise:
            raise a TypeError exception with the message
            rect_1 must be an instance of Rectangle
            raise a TypeError exception with the message
            rect_2 must be an instance of Rectangle
        Return:
            returns the biggest rectangle based on the area
            rect_1 if both have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if (area1 >= area2):
            return (rect_1)
        return (rect_2)
