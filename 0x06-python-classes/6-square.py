#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """
    a class Square that defines a square by: (based on 3-square.py)

    Attributes:
        size: Private instance attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        new instance form class

        Args:
            size: size of the square
            position:  must be a tuple of 2 positive integers
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        public instance method that returns the current square area

        args:
            size: size of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        return the size of the square
        """
        return (self.__size)

    @property
    def position(self):
        """
        Private instance attribute: position
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """
        size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer

        if size is less than 0, raise a ValueError
        exception with the message size must be >= 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        """
        if (type(value) != tuple or len(value) != 2
                or not all(True if num == int else False for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                [print(" ", end="") for i in range(self.__position[0])]
                [print("#", end="")for i in range(self.__size)]
                print("")
